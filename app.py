from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv  # Import dotenv package

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Function to send email
def send_email(subject, body, recipient_email):
    sender_email = os.getenv("EMAIL_USER")  # Get email from environment variable
    sender_password = os.getenv("EMAIL_PASSWORD")  # Get password from environment variable

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the Gmail server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        server.quit()

# Route for the homepage
@app.route("/")
def hello_world():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Compose the email content
    subject = f"New Message from {name}"
    body = f"From: {name}\nEmail: {email}\nMessage:\n{message}"

    # Send the email to your email address
    send_email(subject, body, "sk2579784@gmail.com") 

    return "Message sent successfully! Thank you for contacting me."

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
  
