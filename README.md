# MessageService

## Overview  
The `MessageService` is a Python-based service designed to manage employee data and send email notifications. It integrates with an external API to fetch employee records and provides features to send personalized birthday wishes via email.  

---

## Features  
- **Employee Data Integration**: Fetches employee details from a remote API.  
- **Active Employee Filtering**: Excludes employees who are no longer working or haven’t started.  
- **Birthday Notifications**: Automatically identifies employees with birthdays today, including leap year handling, and sends personalized wishes.  
- **Email Sending**: Uses Gmail's SMTP server to send HTML-based emails.  

---

## How It Works  
1. Fetch employee data from the API:  
   `https://interview-assessment-1.realmdigital.co.za/employees`.  
2. Filter active employees and check if they wish to receive notifications.  
3. Identify employees whose birthdays fall on the current date.  
4. Send an email with a personalized birthday message to the specified recipient.  

---

## Requirements  
- Python 3.x  
- Libraries: `smtplib`, `ssl`, `email.mime`, `requests`  
- Gmail account for SMTP access  

---

## Usage  
1. Initialize the `MessageService` class with sender email credentials and the recipient's email address.  
2. Call the `send_birthday_wishes` method to send birthday notifications.  

---

## Example  

```python
from message_service import MessageService

service = MessageService(
    sender_email="your_email@gmail.com",
    password="your_password",
    receiver_email="recipient_email@gmail.com"
)

service.send_birthday_wishes()
