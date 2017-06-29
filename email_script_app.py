# import smtplib
# gmailserver="smtp.gmail.com"
# sender="bgarna@gmail.com"
# receiver="Kankamsolomon@gmail.com"
# password='mypassword'


# server = smtplib.SMTP(gmailserver, 587)
# server.ehlo()
# server.starttls()
# server.login(sender, password)
# msg = "HI"
# server.sendmail(sender, receiver, msg)
# server.quit()
# print "done"


import smtplib

def welcome():
	print '-----------------------'
	print '     EMAIL APP'
	print '-----------------------'


def info():
	print 'To send an email, please provide the information below'
	sender=raw_input('Your email please:   ')
	receiver=raw_input('Your recepient email please:   ')
	password=raw_input('Your email password:   ')
	msg=raw_input('Your message to the sender:   ')
	data(sender,receiver,password,msg)
	

def data(sender,receiver,password,msg):
	gmailserver="smtp.gmail.com"
	server = smtplib.SMTP(gmailserver, 587)
	server.ehlo()
	server.starttls()
	server.login(sender, password)
	server.sendmail(sender, receiver, msg)
	server.quit()

welcome()
info()





