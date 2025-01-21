import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename) :
  msg = MIMEMultipart()
  from_add = 'fe123123min@gmail.com'
  to_add = 'femin.24ee@licet.ac.in'
  subject = 'Automated mail from Python'

  msg['From'] = from_add
  msg['To'] = to_add
  msg['Subject'] = subject

  body = 'This is a mail from python , generated automatically from scrapper and you can find a attachment of a csv file containing the trading data'
  msg.attach(MIMEText(body , 'plain'))

  my_file = open(filename , "rb")

  part = MIMEBase('application' , 'octet-stream')
  part.set_payload(my_file.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition' , 'attachment; filename= '+ filename)
  msg.attach(part)
  message = msg.as_string()

  server = smtplib.SMTP('smtp.gmail.com' , 587)
  server.starttls() # Start the server with authentication
  server.login(from_add , 'ywevkjutyulphlwc')

  server.sendmail(from_add , to_add , message)
  server.quit()