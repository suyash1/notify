import json
import random
import string
import uuid
import requests

import sounddevice as sd
from scipy.io.wavfile import write


fs = 44100  # Sample rate
seconds = 3  # Duration of recording

my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
file_name = ''.join([''.join(random.choices(string.ascii_lowercase + string.digits, k=10)), '.wav'])
write(file_name, fs, my_recording)  # Save as WAV file
pilot_id = str(uuid.uuid4())

# sending file name and pilot id to a topic in a POST call to notify service
response = requests.post('http://localhost:8010/publish_note',
                         json={'pilot_id': pilot_id, 'file_path': file_name, 'exchange': 'test', 'topic': 'test.#'})
print(json.loads(response.content))
