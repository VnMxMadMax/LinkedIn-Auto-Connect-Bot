# LinkedIn Auto Connect Bot

## 📌 Overview
This Python script automates sending connection requests on LinkedIn using Selenium. It searches for a specified job role and sends connection requests to people on multiple pages.

## 🚀 Features
- **Automated Login**: Logs into LinkedIn using provided credentials.
- **Search People by Role**: Searches for LinkedIn users based on a specified job title.
- **Auto-Connect Requests**: Sends connection requests without a note.
- **Human-like Behavior**: Uses random delays, scrolling, and cursor movements to avoid detection.

## 🛠️ Installation
### 1️⃣ Prerequisites
- Python 3.x
- Google Chrome (latest version)
- ChromeDriver (managed automatically)

### 2️⃣ Install Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

## 🔑 Setup
### 1️⃣ Configure Environment Variables
To keep credentials secure, store them as environment variables:
```bash
export LINKEDIN_EMAIL="your_email@example.com"
export LINKEDIN_PASSWORD="your_password"
```

On Windows (Command Prompt):
```cmd
set LINKEDIN_EMAIL=your_email@example.com
set LINKEDIN_PASSWORD=your_password
```

### 2️⃣ Run the Script
```bash
python linkedin_auto_connect.py
```

## ⚠️ Disclaimer
- This script is for educational purposes only.
- Use responsibly to avoid violating LinkedIn’s policies.
- Please don't run this code more than 2 times in a week as linkedin has 100-200 connection request per week

## 📜 License
This project is licensed under the MIT License.

