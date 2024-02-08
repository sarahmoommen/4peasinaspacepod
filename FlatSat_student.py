"""
The Python code you will write for this module should read
acceleration data from the IMU. When a reading comes in that surpasses
an acceleration threshold (indicating a shake), your Pi should pause,
trigger the camera to take a picture, then save the image with a
descriptive filename. You may use GitHub to upload your images automatically,
but for this activity it is not required.

The provided functions are only for reference, you do not need to use them. 
You will need to complete the take_photo() function and configure the VARIABLES section
"""

#AUTHOR: 4peasinaspacepod
#DATE: 2/6/2023

#import libraries
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
from adafruit_lis3mdl import LIS3MDL
#from git import Repo
from picamera2 import Picamera2

#VARIABLES
THRESHOLD = 1      #Any desired value from the accelerometer
REPO_PATH = "/home/pi/4peasinaspacepod"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "/Images"   #Your image folder path in your GitHub repo: ex. /Images

#imu and camera initialization
i2c = board.I2C()
accel_gyro = LSM6DS(i2c)
mag = LIS3MDL(i2c)
picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

def img_gen(name):
    """
    This function is complete. Generates a new image name.

    Parameters:
        name (str): your name ex. MasonM
    """
    t = time.strftime("_%H%M%S")
    imgname = (f'{REPO_PATH}/{FOLDER_PATH}/{name}{t}.jpg')
    return imgname


def take_photo():
    """
    This function is NOT complete. Takes a photo when the FlatSat is shaken.
    Replace psuedocode with your own code.
    """
    picam2.start()
    while True:
        accelx, accely, accelz = accel_gyro.acceleration #Queries for accelerometer values.
        #CHECKS IF READINGS ARE ABOVE THRESHOLD
        accelx=round(accelx, 0)
        accely=round(accely, 0)
        accelz=round(accelz, 0)
        if accelx > THRESHOLD :
            #PAUSE
            time.sleep(3) 
            #NAME
            name = "SarahO"     #First Name, Last Initial  ex. MasonM
            #TAKE PHOTO
            #picam2.capture("/home/pi/4peasinaspacepod/Images/4peasinapodimg.jpg") #capture the image
            picam2.capture_file("/home/pi/4peasinaspacepod/Images/4peasinapodimg.jpg")
            print("Done.")
            picam2.stop()
            #PUSH PHOTO TO GITHUB
           #git_push()
        #PAUSE


def main():
    take_photo()


if __name__ == '__main__':
    main()
