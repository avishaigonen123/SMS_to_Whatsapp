import config
from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_TOKEN

# Twilio phone number
twilio_number = config.TWILIO_NUMBER

def send_sms(to_number, message):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=to_number
        )
        print(f"SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

# Example usage
def main():
    message = '''מה נשמע הלל? הכל טוב?'''
    send_sms(config.RECIPIENT_NUMBER, message)

# main()
