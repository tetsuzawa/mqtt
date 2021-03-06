import RPi.GPIO as GPIO
import time

class Flash:

    def __init__(self, BCM_NUM=19):

        self.bcm_num = BCM_NUM
        GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
        GPIO.setup(self.bcm_num, GPIO.OUT) #BCMの{BCM_NUM}ピンを出力に追加する.j

    def flash(self, COUNT):

        try:
            for _i in range(COUNT):
                GPIO.output(self.bcm_num, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(self.bcm_num, GPIO.LOW)
                time.sleep(0.1)

        except KeyboardInterrupt:
            GPIO.output(self.bcm_num, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup(self.bcm_num)
        

if __name__ == '__main__':
    blue = Flash(BCM_NUM=13)
    blue.flash(15)