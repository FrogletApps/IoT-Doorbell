import secret
import os

os.system('curl -u' + secret.apiKey() + ': https://api.pushbullet.com/v2/pushes -d type=link -d title="There\'s someone at the door" -d url="https://www.google.com"')