
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import certifi   # Add this import

# Email configuration
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "testravikki@gmail.com"
password = "nskv apjq xinl dbsz"
receiver_email = "kishanapply@gmail.com"
#9453 7190
#nskv apjq xinl dbsz



# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Screenshots from Selenium Script"

# Add body to email
body = "Please find the attached screenshots."
message.attach(MIMEText(body, "plain"))

# Attach files
screenshot_files = ["screenshot1.png", "screenshot2.png", "screenshot3.png"]  # Add your screenshot file names here

for filename in screenshot_files:
    if os.path.exists(filename):
        with open(filename, "rb") as attachment:
            # Create a MIMEBase object
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(filename)}",
            )
            message.attach(part)
    else:
        print(f"File {filename} does not exist.")

# Create secure connection with server and send email
context = ssl.create_default_context(cafile=certifi.where())  # Use certifi for the certificate file
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
