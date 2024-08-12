import requests

# Replace 'YOUR_API_KEY' with your actual Deepgram API key
api_key = 'fad099a737d87a33160459e05263e9791462063f'
audio_file_path = './harvard.wav'  # Local file path

# Open the audio file in binary mode
with open(audio_file_path, 'rb') as audio_file:
    headers = {
        'Authorization': f'Token {api_key}',
        'Content-Type': 'application/octet-stream',
    }

    # Send the file as a binary stream to the API
    response = requests.post(
        'https://api.deepgram.com/v1/listen',
        headers=headers,
        data=audio_file,
        params={
            'punctuate': True,
            'language': 'en-US',
            'diarize': True,
        },
        verify=False  # Disable SSL verification
    )

# Handle the response
if response.status_code == 200:
    transcript = response.json().get('results', {}).get('channels', [])[0].get('alternatives', [])[0].get('transcript', '')
    print('Transcript:', transcript)
else:
    print('Failed to transcribe audio:', response.status_code, response.json())
