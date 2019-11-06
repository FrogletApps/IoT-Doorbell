from pushbullet import Pushbullet
import secret
    
pb = Pushbullet(secret.apiKey)

push = pb.push_link("Cool site", "https://www.google.com")

