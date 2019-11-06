import secret
import time
import os
import requests
from picamera import PiCamera

#bot_message = "Bleep bloop I'm a bot c:"
#send_text = 'https://api.telegram.org/bot' + secret.tgBotKey() + '/sendMessage?chat_id=' + secret.tgChatID() + '&parse_mode=Markdown&text=' + bot_message
#response = requests.get(send_text)

picturePath = '/home/pi/image.jpg'

camera = PiCamera()
camera.start_preview()
time.sleep(1)
camera.capture(picturePath)
camera.stop_preview()
#picture = open(picturePath, 'rb')
picture = open(picturePath, 'rb')
camera.close()

#Wait for 2 seconds
time.sleep(2)
#Close the photo
camera.close()

url = "https://api.telegram.org/bot" + secret.tgBotKey() + "/sendPhoto"
files = {'photo': open(picturePath, 'rb')}
data = {'chat_id' : secret.tgChatID()}
r= requests.post(url, files=files, data=data)
print(url)
print(files)
print(data)
print(r.status_code, r.reason, r.content)

#send_picture = 'https://api.telegram.org/bot' + secret.tgBotKey() + '/sendPhoto?chat_id=' + secret.tgChatID()# + 'attach://' + picture
#response = requests.post(send_picture, picture=picture)
