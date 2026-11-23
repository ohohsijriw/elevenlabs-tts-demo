import os
import sys
import requests

API_KEY = os.getenv('ELEVENLABS_API_KEY')
if not API_KEY:
    print('Set ELEVENLABS_API_KEY first.')
    sys.exit(1)

VOICE_ID = os.getenv('ELEVENLABS_VOICE_ID', '21m00Tcm4TlvDq8ikWAM')
TEXT = os.getenv('ELEVENLABS_TEXT', 'Hello from a minimal ElevenLabs text-to-speech demo.')
OUTPUT = os.getenv('ELEVENLABS_OUTPUT', 'output.mp3')

url = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}'

headers = {
    'xi-api-key': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'audio/mpeg',
}

payload = {
    'text': TEXT,
    'model_id': 'eleven_multilingual_v2',
    'voice_settings': {
        'stability': 0.5,
        'similarity_boost': 0.75,
    },
}

try:
    response = requests.post(url, json=payload, headers=headers, timeout=60)
    response.raise_for_status()
except requests.RequestException as exc:
    print(f'Request failed: {exc}')
    sys.exit(1)

with open(OUTPUT, 'wb') as audio_file:
    audio_file.write(response.content)

print(f'Saved audio to {OUTPUT}')
