import smtplib
from email import encoders
from email.mime.text import MIMEText


server = smtplib.SMTP('smtp.gmail.com' , 25)
server.ehlo()
server.starttls()


with open('password.txt', 'r') as file:
    pwd = file.readline()

server.login("hm464@cornell.edu", pwd)

# msg = MIME.Multipart()

# msg["To"] = "hussainahmadafg@gmail.com"
# msg["From"] = "Hussain"
# msg["Subject"] = "Just a test"

# with open("message.txt" , "r") as file:
#     message = file.readline()


# msg.attach(MIMEText(message,"plain"))

# text = msg.as_string()

# server.sendmail("hm464@cornell.edu" , "hussainahmadafg@gmail.com" , text)

