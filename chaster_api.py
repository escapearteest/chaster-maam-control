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

LOCK_ID = '6a08b0e5fef2827dcda0a97b'  # Your current self-lock


def get_lock_status():
    # Try lock endpoint first
    response = requests.get(f'{BASE_URL}/api/locks/{LOCK_ID}', headers=HEADERS)
    if response.ok:
        return response.json()
    # Fallback to session if needed
    response = requests.get(f'{BASE_URL}/api/extensions/sessions/{LOCK_ID}', headers=HEADERS)
    return response.json()

def add_time(seconds: int):
    payload = {
        "name": "add_time",
        "params": seconds
    }
    response = requests.post(f'{BASE_URL}/api/extensions/sessions/{LOCK_ID}/action', json=payload, headers=HEADERS)
    return response.json()

# Test
if __name__ == "__main__":
    print(get_lock_status())
print('Chaster API ready for Ma\'am control.')