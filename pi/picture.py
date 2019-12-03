from datetime import datetime
from picamera import PiCamera

#Get file path for pictures
def getPicturePath():
    time = datetime.now()
    return '/home/pi/Git/iot-doorbell-pi/webControl/DoorbellPics/'+ time.strftime("%Y-%m-%d %H-%M-%S") +'.jpg'

picturePath = getPicturePath()
camera = PiCamera()
#camera.start_preview()
#time.sleep(1)
camera.capture(picturePath)
#camera.stop_preview()
#Close the camera
camera.close()