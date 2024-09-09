import cv2
import sys

# to figure out which camera to use;
# sudo apt install v4l-utils
# v4l2-ctl --list-devices
# which should give something like:
# USB 2.0 Camera: USB Camera (usb-0000:00:14.0-1):
	# /dev/video2
	# /dev/video3
# 
# Integrated Camera: Integrated C (usb-0000:00:14.0-6):
	# /dev/video0
	# /dev/video1

# when I have connected my usb 2.0 camera.
# Then to access the builtin camera, use index 0
# and to use the usb camera, use index 2

s = 0  # cam id;
if len(sys.argv) > 1:
    s = int(sys.argv[1])

source = cv2.VideoCapture(s)

window_name = f'Camera device: {s}'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

try:
    while cv2.waitKey(1) != 27:  # while not Escape
        has_frame, frame = source.read()
        if not has_frame:
            break
        cv2.imshow(window_name, frame)
except Exception as e:
    print(e)
    raise
finally:
    source.release()
    cv2.destroyWindow(window_name)
