from pushbullet.pushbullet import Pushbullet
import secret
    
pb = Pushbullet(secret.apiKey)

pb.bullet_link(title="Hello World", body="https://www.google.com")
