import subprocess
import os
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Set up credentials for speech to text service
apikey = '' #Set API Key here
url = '' #Set API url here
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url)


#

command = 'ffmpeg -i audio.webm -vn -ar 44100 -ac 2 -b:a 192k audio.mp3'
subprocess.call(command, shell=True)y
command = 'ffmpeg -i audio.mp3 -f segment -segment_time 360 -c copy %03d.mp3'
subprocess.call(command, shell=True)
print ("audio split")

files = []
for filename in os.listdir('.'):
    if filename.endswith(".mp3") and filename !='audio.mp3':
        files.append(filename)
files.sort()
print ("Files sorted")

results = []
for filename in files:
    with open(filename, 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_BroadbandModel', inactivity_timeout=360).get_result()
        results.append(res)
print ("files translated")
        
text = []
for file in results:
    for result in file['results']:
        text.append(result['alternatives'][0]['transcript'].rstrip() + '.\n')
        text.append('Accuracy Score:' + str(result['alternatives'][0]['confidence']) + '.\n')
print ("Text diserned")   


with open('output.txt', 'w') as out:
    out.writelines(text)
print("Written to file")
