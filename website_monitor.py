import requests
import smtplib

def CheckWebsiteStatus(url):
	#load website
	response = requests.get(url)
	statuscode = response.status_code
	print(statuscode)

	if statuscode != 200:
		print ("Send email that Website is down!")

def SendEmail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login("YOUR GMAIL EMAIL ADDRES","GMAIL_PASSWORD")

	msg = "Website is Down!"
	server.sendmail("GMAIL ADDRESS","EMAIL TO SEND TO",msg)
	server.quit()

if __name__ == "__main__":
	url = "https://www.google.com/"
	CheckWebsiteStatus(url)
	CheckWebsiteStatus("http://rainierland.com")