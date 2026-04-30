from flask import Flask, request

app = Flask(__name__)
led_status = "OFF"

@app.route('/')
def home():
    return "Server is running"

@app.route('/led', methods=['GET', 'POST'])
def led():
    global led_status

    if request.method == 'POST':
        led_status = request.data.decode()
        print("Received:", led_status)
        return "OK"

    return led_status