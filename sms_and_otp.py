# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import random as r

# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    return ("Your OTP : {}".format(otp))
    #print (otp)
a=otpgen()




# the following line needs your Twilio Account SID and Auth Token
client = Client("AC6453d31f3bcee029abe3690c1954c32e", "09fc81ff544c86b6e3a6d892591affba")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+91-9043796669", 
                       from_="+19284408533", 
                       body=a)



                       


