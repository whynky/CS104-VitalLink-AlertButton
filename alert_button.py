import time
import requests
import RPi.GPIO as GPIO

# Telegram settings
BOT_TOKEN = "8847161843:AAFUnUREJZ7eYAHG15CgrQq7N9ZhmCPW9EM"
CHAT_ID = "8679334855"

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:

        # Send Telegram message
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": CHAT_ID,
            "text": "Someone pressed the alert button!"
        }

        response = requests.post(url, json=data)

        print("Alert sent!")
        print(response.text)

        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)
