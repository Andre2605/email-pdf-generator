import getpass
import smtplib
from email.message import EmailMessage
import os.path
import mimetypes

# this is for the email body
message = EmailMessage()

sender = 'example@gmail.com'
recipient = 'example-2@gmail.com'

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = """Hello!

I'm using python to generate this email for you. :)"""
message.set_content(body)

# this is for the email attachment
attachment_path = 'path/to/your/attachment.jpeg'
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/')
# print(mime_type)
# print(mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

# print(message)

# how to send email via gmail
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

mail_server.set_debuglevel(1)

mail_pass = getpass.getpass('Password? ')

mail_server.login(sender, mail_pass)

mail_server.send_message(message)

mail_server.quit()
