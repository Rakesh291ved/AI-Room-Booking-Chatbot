from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(phone, date, time):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()

    sender_email = "vedanthrakesh2910@gmail.com"
    sender_password = "gmomoyfxugvivtsk"  # App password
    receiver_email = "nccreation934@gmail.com"

    s.login(sender_email, sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Booking request"

    message = f"""Hello team,

This is your AI Chatbot. We received a room booking request for {date} at {time}.
Phone number: {phone}

Thanks and Regards,
Your AI Chatbot."""

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
    s.quit()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        phone = request.form["phone"]
        date = request.form["date"]
        time = request.form["time"]
        send_email(phone, date, time)
        return render_template("index.html", message="Booking email sent successfully!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
