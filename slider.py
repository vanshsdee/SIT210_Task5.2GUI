import RPi.GPIO as GPIO
import tkinter as tk

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the LEDs
blue_pin = 14
green_pin = 15


# Set up the GPIO pins as outputs
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)


# Set up PWM for each LED (frequency set to 100 Hz)
blue_pwm = GPIO.PWM(blue_pin, 100)
green_pwm = GPIO.PWM(green_pin, 100)


# Start PWM with 0% duty cycle (LEDs off)
blue_pwm.start(0)
green_pwm.start(0)


# Function to update the brightness of LEDs
def update_leds():
    blue_pwm.ChangeDutyCycle(blue_slider.get())   # Set blue LED brightness
    green_pwm.ChangeDutyCycle(green_slider.get())  # Set Green LED brightness

# Function to exit and clean up
def exit_gui():
    blue_pwm.stop()
    green_pwm.stop()
    GPIO.cleanup()
    root.destroy()

# Set up the GUI window
root = tk.Tk()
root.title("Task5.2 GUI")

# blue LED slider
tk.Label(root, text="blue LED").pack()
blue_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda x: update_leds())
blue_slider.pack()

# Green LED slider
tk.Label(root, text="Green LED").pack()
green_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda x: update_leds())
green_slider.pack()


# Add an Exit button
tk.Button(root, text="Exit", command=exit_gui).pack()

# Start the GUI loop
root.mainloop()
