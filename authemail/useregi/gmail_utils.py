import os.path
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import base64
import os
import json


SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def gmail_send_message(recipient_email, subject, message_body):
    print("where")
    """Send an email message.

    Args:
        recipient_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        message_body (str): Body of the email.

    Returns:
        Message object, including message id, if successful. None otherwise.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        print("what")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("123")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=5000)
            print("appFLow")
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            print("1000")

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(message_body)
        message['to'] = recipient_email
        message['from'] = 'me'
        message['subject'] = subject
        print("body prepared")

        # Encode the message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message_body = {'raw': raw_message}
        send_message = service.users().messages().send(
            userId='me', body=message_body).execute()
        print(f'Message Id: {send_message["id"]}')
        print("message body sent")
        return send_message
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    recipient_email = "recipient@example.com"
    subject = "Test Subject"
    message_body = "This is the body of the email."
    gmail_send_message(recipient_email, subject, message_body)
