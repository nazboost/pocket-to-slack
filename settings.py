import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

consumer_key = os.environ.get('consumer_key')
code = os.environ.get('code')
access_token = os.environ.get('access_token')
webhook_url = os.environ.get('webhook_url')
