import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv('CHASTER_TOKEN')
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

BASE_URL = 'https://api.chaster.app'

def get_lock_status(lock_id):
    response = requests.get(f'{BASE_URL}/api/extensions/sessions/{lock_id}', headers=HEADERS)
    return response.json()

# Add more functions as needed
print('Chaster API wrapper loaded with token.')