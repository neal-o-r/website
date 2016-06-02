import random
import smtplib

receivers = ['''names''']

givers    = list(receivers)

emails =   ['''emails''']


received = []
# loop pairs people. 
for person in givers:

    temp = list(receivers)
    if person in temp:
        temp.remove(person) # so you can't get yourself
    
    received.append(random.choice(temp)) 

    receivers.remove(received[-1]) # so no one gets two.

print givers
print received

# loop to do the emailing

for i, address in enumerate(emails):

#     # send that address an email (dear giver - this list is arranged the same way) with the corresponding name from received

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    gmail_user = "email address"
    gmail_pwd = "password"
    server.login(gmail_user,gmail_pwd)
    
    name = givers[emails.index(address)]

    giftee = received[i]

    print address, name, giftee
    FROM = ''
    TO = [address] #must be a list
    SUBJECT = "From Santa"
    TEXT = 	"""Hi """+name+"""!\n\nSanta's digital elves have done their work and paired you up with """+giftee+""".\n\nBe lovely and get them a very nice gift.\n\nNo perishables.\n\nHappy Gift Hunting.\n\nHo ho ho,\n\nSanta"""

        # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    try:
        	#server = smtplib.SMTP(SERVER) 
        server = smtplib.SMTP("smtp.gmail.com", 587) #port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        	#server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
	

