if test -f "/tmp/doorbellRunning"; then
    echo "tmp flag file exists, won't run pi.py"
else
    echo "tmp flag file does not exist, running pi.py"
    python3 /home/pi/Git/iot-doorbell-pi/pi/pi.py
fi
