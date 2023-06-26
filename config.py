import os
from dotenv import load_dotenv

load_dotenv()

# data for Ukassa
ACCOUNT_ID = os.getenv('ACCOUNT_ID')
SECRET_KEY = os.getenv('SECRET_KEY')

# server domain name
ADDRESS = os.getenv('ADDRESS')

# mailgun data
EMAIL_KEY = os.getenv('EMAIL_KEY')
EMAIL_URL = os.getenv('EMAIL_URL')
EMAIL_FROM = os.getenv('EMAIL_FROM')