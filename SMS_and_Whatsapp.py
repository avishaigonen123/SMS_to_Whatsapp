import time
import config
import SMS_sender
import Whatsapp_reader
from datetime import datetime, timedelta

def convert_unix_timestamp(unix_timestamp):
    # Convert the UNIX timestamp to a datetime object
    dt = datetime.utcfromtimestamp(unix_timestamp)
    # Format the datetime object to a readable string
    formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')
    return dt, formatted_time

count = 10
last_messages = Whatsapp_reader.fetch_latest_message(config.CHAT_ID, count) # get 10 last messages

# Get the current time
current_time = datetime.utcnow()

for message in last_messages[::-1]:
    print("Message:: ----------------------------------------------------------------")
    unix_timestamp = message['timestamp']     
    message_time, readable_time = convert_unix_timestamp(unix_timestamp)
    
    # Calculate the time difference
    time_difference = current_time - message_time
    print(time_difference)
    # Check if the time difference is greater than 2 hours
    # i wanna check every two hours, and if got messages within this timestamp, send it
    if time_difference > timedelta(hours=2):
        print(f"Skipping message received at {readable_time}, older than 2 hours.")
        continue
    
    print(f"Message time is: {readable_time}")
    print(message['textMessage'])
    content_splitted = message['textMessage'].split('\n')
    for paragraph in content_splitted:
        print(paragraph)
        time.sleep(5)
        if paragraph:
            SMS_sender.send_sms(config.RECIPIENT_NUMBER, paragraph)

Whatsapp_reader.mark_message_as_read(config.CHAT_ID, "") # mark all messages as read