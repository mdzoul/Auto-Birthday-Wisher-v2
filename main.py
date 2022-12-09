import requests
import datetime
from twilio.rest import Client

# Set the current date
current_date = datetime.datetime.now()

# Set the URL of the Google Sheet you want to read
spreadsheet_url = 'https://api.sheety.co/YOUR_SPREADSHEET_ID'

# Read the Google Sheet using the Sheety API
response = requests.get(spreadsheet_url)
clients = response.json()['birthdayData']

# Iterate through the clients in the Google Sheet
for client in clients:
    # Get the client's name, phone number, and birthday
    client_name = client['name']
    client_phone = '+65' + str(client['phone'])
    client_birthday = datetime.datetime.strptime(client['birthday'], '%d/%m/%Y')

    # Check if today is the client's birthday
    if current_date.month == client_birthday.month and current_date.day == client_birthday.day:
        # Send the birthday wish to the client via WhatsApp
        client = Client("ACCOUNT_SID", "AUTH_TOKEN")
        message = client.messages.create(
            body=f'Happy birthday, {client_name}!',
            from_='whatsapp:YOUR_TWILIO_PHONE_NUMBER',
            to=f'whatsapp:{client_phone}'
        )
        print(f'Sent birthday wish to {client_name}')
