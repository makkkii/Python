'''*--Important Note--*
Before using this please visit https://myaccount.google.com/lesssecureapps
and turn on the allow secure apps slider there.
Otherwise this will not work.'''

import smtplib
import time
number_of_emails_sent = 0
email_sender = input("What's your email?\n")
password = input("What's your password?\n")
email_goto = input("Who do you want to send it to? (Type in their email)\n")
times_to_send = int(input("How many times do you want to spam it? (Maximum of 100 emails)\n"))
msg = input("What's the message?\n")

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, password)
    server.sendmail(email_sender, email_goto, msg)
    server.quit()
try:
    for i in range(times_to_send):
        send_email()
        number_of_emails_sent += 1
        print("Email #"+ str(number_of_emails_sent),"sent successfully.")
        """time.sleep(.5)"""
        while True:
            if number_of_emails_sent < times_to_send:
                """time.sleep(.5)"""
                print("Attempting next email...")
                break
            elif number_of_emails_sent == times_to_send:
                print("Done!")
                break
            else:
                print("An error has occured...")
                break
except:
    print("Some error occured.")
