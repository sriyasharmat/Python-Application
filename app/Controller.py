from tkinter import *
import Model
import View
from twilio.rest import Client 
import random
from tkinter import messagebox


class Controller:
    def __init__(self):
        self.model = Model.Model()
        self.twilioClient = Client
        self.randInt = random.randint
        # self.view= View.View()


    def registerRider(self,username, password, phoneNumber):
        # print(username, password, phonenumber, extension)
        if not username or not password or not phoneNumber:
            return False
    
        self.model.setRider(username,password, phoneNumber)
        
        return True
    


    def registerPassenger(self,username, password, phoneNumber):
        if not username or not password or not phoneNumber:
            return False
    
        return self.model.setPassenger(username,password, phoneNumber)
        return True

    def register_user(self):
        current_tab = self.view.get_current_tab()  
        if current_tab == "Rider":
            username = self.view.get_rider_username()
            password = self.view.get_rider_password()

            phone_extension = self.view.get_rider_phone_extension()
            phone_number = self.view.get_rider_phone_number()
            table_name = "riders"
        elif current_tab == "Passenger":
            username = self.view.get_passenger_username()
            password = self.view.get_passenger_password()
            phone_extension = self.view.get_passenger_phone_extension()
            phone_number = self.view.get_passenger_phone_number()
            table_name = "passengers"
        else:
            return

        if not username or not password:
            # self.view.show_error_message("Both fields are required!")
            return

        # Call the appropriate method in the Model to insert the user
        if current_tab == "Rider":
            self.model.insert_rider(username, password, phone_number, phone_extension)
        elif current_tab == "Passenger":
            self.model.insert_passenger(username, password, phone_number, phone_extension)

        # self.view.show_success_message(f"Registered Successfully as {current_tab}!")


    def sendOtp(self,phoneNumber):
        
        #twillio Details

        accountSID = "ACd607e2f86a57f692c81867be2f0b351f"
        authToken = "b8c87d72917d74156dedf963d6e4b373"
        twillioPhoneNumber = "+18449584452"

        smsClient =  self.twilioClient( accountSID,authToken)


        otpMessage = f"Your Let's Go, OTP is  {self.generateOTP()}"

        try:
            otpMessage = smsClient.messages.create(
                to = phoneNumber,
                from_= twillioPhoneNumber,
                body = otpMessage
            )
        except Exception as e:
            print(e)
            return False

        




    def generateOTP(self):
        return self.randInt(100000,999999)
    

    def login_user(self):
        pass


    def create_ride(self):
        from_location = self.view.from_entry_create.get()
        to_location = self.view.to_entry_create.get()
        date = self.view.date_entry_create.get()
        time = self.view.time_entry_create.get()

        if from_location and to_location and date and time:
            ride_id = self.model.add_ride(from_location, to_location, date, time)
            messagebox.showinfo("Success", f"Ride created with ID: {ride_id}")
            # You can clear the input fields or perform any other necessary actions here
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    # Add similar methods for retrieving users, handling user interactions, etc.