import os
from twilio.rest import Client
from dotenv import load_dotenv
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def send_message(number, message):
    number = '+1{}'.format(number)
    """
    message = client.messages.create(
        body='Hi there!',
        from_='+12158762820',
        to='+15198976215'
    )
    print(message.sid)
    """
    print('sending message {} to {}'.format(number, message))
