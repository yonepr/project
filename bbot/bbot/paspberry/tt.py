from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
tilt = 17
GPIO.setup(tilt, GPIO.OUT)
def setServoAngle(servo, angle):
        assert angle >=30 and angle <=150
        pwm = GPIO.PWM(servo, 40)
        pwm.start(8)
        dutyCycle = angle / 18. + 3.
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(30)
        pwm.stop()
if __name__ == '__main__':
        import sys
        if len(sys.argv) == 1:
                setServoAngle(tilt, 90)
        else:
                setServoAngle(tilt, int(sys.argv[2]))
def setServoAngle(servo, angle):
        assert angle >=30 and angle <=150
        pwm = GPIO.PWM(servo, 22)
        pwm.start(8)
        dutyCycle = angle / 18. - 3.
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(1)
        pwm.stop()
if __name__ == '__main__':
        import sys
        if len(sys.argv) == 1:
                setServoAngle(tilt, 90)
        else:
                setServoAngle(tilt, int(sys.argv[2]))
        GPIO.cleanup()
