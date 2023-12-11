import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for motor control
motor_pin1 = 17  
motor_pin2 = 18 

# Setup motor pins as output
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)

def activate_motor(direction):
    # Activate the motor for 0.01 seconds
    GPIO.output(motor_pin1, direction)
    GPIO.output(motor_pin2, not direction)
    time.sleep(0.01)
    GPIO.output(motor_pin1, GPIO.LOW)
    GPIO.output(motor_pin2, GPIO.LOW)

try:
    while True:
        # Activate motor in one direction
        activate_motor(True)

        # Pause for 2 seconds
        time.sleep(2)

        # Activate motor in the opposite direction
        activate_motor(False)

        # Pause for 2 seconds
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
