import cv2
import time
import platform
import subprocess
import zxing

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
    # url = "http://your_mobile_device_ip:8080/video"  
    cap = cv2.VideoCapture(0)

    pause_flag = False

    try:
        while True:
            ret, frame = cap.read()
            timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
            filename = f"captured_image.jpg"

            # save frame-by-frame
            cv2.imwrite(filename, frame)
                
            rd = zxing.BarCodeReader()   
            rs = rd.decode(filename)

            if(rs):
                print("QR Code Data:",rs.raw)
                pause_flag = True
                time.sleep(5)
                pause_flag = False
            


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

    finally:
        print("done")


if __name__ == "__main__":
    capture_and_decode_qr()
