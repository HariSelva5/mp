import random as r
# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    return ("Your OTP :",otp)
    #print (otp)
a=otpgen()
print(a)