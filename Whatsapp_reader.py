import config
import requests

# API configuration from config.py
apiUrl = config.API_URL
idInstance = config.ID_INSTANCE
apiTokenInstance = config.API_TOKEN_INSTANCE

chat_id = config.CHAT_ID

def set_account_settings():
    url = f"{apiUrl}/waInstance{idInstance}/setSettings/{apiTokenInstance}"
    payload = {
        "webhookUrl": "",  # Your webhook URL if needed
        "webhookUrlToken": "",
        "delaySendMessagesMilliseconds": 5000,  # Example delay value, adjust as needed
        "markIncomingMessagesReaded": "no",   # Ensure incoming messages are marked as read
        "markIncomingMessagesReadedOnReply": "no",
        "outgoingWebhook": "no",
        "outgoingMessageWebhook": "yes",
        "outgoingAPIMessageWebhook": "no",
        "incomingWebhook": "yes",  # Enable incoming message notifications
        "deviceWebhook": "no",
        "stateWebhook": "no",
        "keepOnlineStatus": "no",
        "pollMessageWebhook": "no",
        "incomingBlockWebhook": "no",
        "incomingCallWebhook": "no"
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            if result.get("saveSettings"):
                print("Account settings updated successfully.")
            else:
                print(f"Failed to update account settings: {result}")
        else:
            print(f"Error updating account settings: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request error: {e}")


def fetch_latest_message(chat_id, count):
    url = f"{apiUrl}/waInstance{idInstance}/getChatHistory/{apiTokenInstance}"
    payload = {
        "chatId": chat_id,
        "count": count
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            messages = response.json()
            if messages:
                return messages
            else:
                print(f"No messages found in chat {chat_id}")
        else:
            print(f"Error fetching messages: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request error: {e}")

def mark_message_as_read(chat_id, message_id):
    url = f"{apiUrl}/waInstance{idInstance}/readChat/{apiTokenInstance}"
    if not message_id: # mark all as read
        payload = {
            "chatId": chat_id,
        }
    else: # mark only this message as read
        payload = {
            "chatId": chat_id,
            "idMessage": message_id
        }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            if result.get("setRead"):
                print(f"Marked message {message_id} in chat {chat_id} as read.")
            else:
                print(f"Failed to mark message {message_id} in chat {chat_id} as read: {result}")
        else:
            print(f"Error marking message {message_id} in chat {chat_id} as read: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Request error: {e}")

# Example usage:
if __name__ == '__main__':
    set_account_settings()  # Enable necessary settings

    fetch_latest_message(chat_id)
