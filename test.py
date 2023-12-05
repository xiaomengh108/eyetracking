from picamera2 import Picamera2
import time
import cv2

picam2 = Picamera2()
config = picam2.create_still_configuration(lores = {"size": (4056, 3040), "format": "YUV420"}, display = "lores", buffer_count = 3, queue = False)
picam2.configure(config)

picam2.set_controls({"ExposureTime": 10000, "AnalogueGain": 5})
picam2.start(show_preview=False)

time.sleep(1)  #enjoy the preview

samples = 100
t_0 = time.monotonic()
for x in range(samples):
    data = picam2.capture_array("lores")
t_1 = time.monotonic()
picam2.close()

img = cv2.cvtColor(data, cv2.COLOR_YUV420p2RGB) #alternatively cv2.COLOR_YUV2RGB_I420
print("fps\t\t:", samples/(t_1-t_0))
print("width height\t:", *img.shape[0:2][::-1])

cv2.imshow("last image", cv2.resize(img, (0,0), fx=0.25, fy=0.25))
cv2.waitKey(0)