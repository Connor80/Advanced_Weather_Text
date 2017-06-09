from WeatherText import *
from Wunder import *
from flask import Flask, request as REQUEST, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

def WeatherText():
    """Respond to weather inquiries via text message.
    Initialize with any text."""
    body = REQUEST.values.get('Body', None)
    resp = MessagingResponse()

    if body.lower() == 'sunset':
        resp.message(sunsetText)
    elif body.lower() == 'moon':
        resp.message(moonText)
    elif body.lower() == 'humidity':
        resp.message(humidityText)
    elif body.lower() == 'wind':
        resp.message(windText)
    elif body.lower() == 'rain':
        resp.message(rainText)
    elif body.lower() == 'all':
        resp.message(allText)
    else:
        resp.message(Welcome)
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
