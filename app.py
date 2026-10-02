from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()


def send_email(subject, body, recipient_email):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("ERROR: EMAIL_USER or EMAIL_PASSWORD is not configured.")
        return False

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server = None

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(
            sender_email,
            recipient_email,
            msg.as_string()
        )

        print("Email sent successfully!")
        return True

    except Exception as e:
        print(f"Email error: {e}")
        return False

    finally:
        if server is not None:
            try:
                server.quit()
            except Exception:
                pass


# Homepage
@app.route("/")
def hello_world():
    return render_template("index.html")


# Contact form
@app.route("/send_message", methods=["POST"])
def send_message():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    subject = f"New Message from {name}"

    body = f"""From: {name}
Email: {email}

Message:
{message}
"""

    success = send_email(
        subject,
        body,
        "sk2579784@gmail.com"
    )

    if success:
        return "Message sent successfully! Thank you for contacting me."

    return "Sorry, your message could not be sent. Please try again later.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
