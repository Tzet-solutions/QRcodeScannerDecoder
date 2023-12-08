import cv2
import time
import platform
import subprocess
from pyzbar.pyzbar import decode

def play_os_based_beep():
    system = platform.system().lower()

    if system == "windows":
        print('\a')
    elif system == "darwin":
        subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
    elif system == "linux":
        subprocess.run(["echo", -e, "\a"])

def capture_and_decode_qr():
    # 0 is to the default camera, you can change it 
    cap = cv2.VideoCapture(0)

    pause_flag = False

    try:
        while True:
            ret, frame = cap.read()
            timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
            filename = f"captured_image.jpg"

            # save frame-by-frame
            # cv2.imwrite(filename, frame)

            decoded_objects = decode(frame)

            for obj in decoded_objects:
                print("QR Code Data:", obj.data.decode('utf-8'), f"\nTIME:{timestamp}\n")
                pause_flag = True
                play_os_based_beep()
                time.sleep(5)
                pause_flag = False

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

    finally:
        # Release the camera and close all windows on exit
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_decode_qr()
