import requests

# Replace 'YOUR_API_KEY' with your actual Deepgram API key
api_key = 'fad099a737d87a33160459e05263e9791462063f'
audio_file = 'path_to_your_audio_file.wav'

headers = {
    'Authorization': f'Token {api_key}',
    'Content-Type': 'application/json',
}

data = {
    'url': audio_file,
    'punctuate': True,
    'language': 'en-US',
    'diarize': True,
}

response = requests.post('https://api.deepgram.com/v1/listen', headers=headers, json=data)

if response.status_code == 200:
    transcript = response.json().get('results', {}).get('channels', [])[0].get('alternatives', [])[0].get('transcript', '')
    print('Transcript:', transcript)
else:
    print('Failed to transcribe audio:', response.status_code)
