import secret
import time
import os
import requests
from picamera import PiCamera
import telegram

#bot_message = "Bleep bloop I'm a bot c:"
#send_text = 'https://api.telegram.org/bot' + secret.tgBotKey() + '/sendMessage?chat_id=' + secret.tgChatID() + '&parse_mode=Markdown&text=' + bot_message
#response = requests.get(send_text)

bot = telegram.Bot(secret.tgBotKey)

picturePath = '/home/pi/image.jpg'

camera = PiCamera()
camera.start_preview()
time.sleep(1)
camera.capture(picturePath)
camera.stop_preview()
picture = open(picturePath, 'rb')
camera.close()

#Wait for 2 seconds
time.sleep(2)
#Close the photo
camera.close()

#send_picture = 'https://api.telegram.org/bot' + secret.tgBotKey() + '/sendPhoto?chat_id=' + secret.tgChatID()# + 'attach://' + picture
#response = requests.get(send_picture, picture)

bot.send_photo(chat_id=secret.tgChatID(), photo=open(picturePath, 'rb'))

print (response.json())