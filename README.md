# AI-Room-Booking-Chatbot
AI Room Booking Chatbot
🤖 AI Room Booking Chatbot 📅
A smart and simple Flask-based chatbot system for booking rooms via a web interface and receiving confirmation via email.

🌟 Project Overview
The AI Room Booking Chatbot is a lightweight web application built with Flask that allows users to book a room by simply filling out a form. Once submitted, the app sends an automated email notification to the admin team with the booking details using the Gmail SMTP server.

🎯 Objective: Automate the room booking request process using an intelligent chatbot interface that seamlessly integrates with email notifications.

🚀 Features
🧠 AI-driven interaction (simulated via a friendly UI)

📩 Sends booking details via email to the admin

🔐 Secure email handling using app-specific password

💡 Minimal and intuitive interface

🔁 Real-time booking requests through the web

🛠️ Tech Stack
Component	Technology
Backend	Python, Flask
Frontend	HTML, CSS (via Flask Templates)
Email Service	SMTP (Gmail)

🧪 How It Works
User visits the chatbot interface.

Fills in their phone number, booking date, and preferred time.

On form submission, the app:

Sends an email to the admin with the booking details.

Displays a success message to the user.

📁 Project Structure
bash
Copy code
AI-Room-Booking-Chatbot/
│
├── templates/
│   └── index.html            # Main UI template
│
├── app.py                    # Flask app with email logic
└── README.md                 # This file
📧 Email Integration
The system uses Gmail's SMTP server to send booking requests securely.

Make sure to enable "Less secure app access" or use an App Password if 2FA is enabled.

Replace these credentials in app.py:

python
Copy code
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
⚙️ How to Run the Project
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/AI-Room-Booking-Chatbot.git
cd AI-Room-Booking-Chatbot
Install Dependencies:

bash
Copy code
pip install Flask
Run the App:

bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000

📸 Screenshot

👨‍💻 Developer
Made with ❤️ by Vedanth Rakesh
Email: vedanthrakesh2910@gmail.com

📃 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute with credit.

