from WeatherText import *
from flask import Flask, request as REQUEST, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

def WeatherText():
    """Respond to weather inquiries via text message."""
    body = REQUEST.values.get('Body', None)
    resp = MessagingResponse()

    if body.lower() == 's':
        resp.message(sunsetText)
    elif body.lower() == 'm':
        resp.message(moonText)
    elif body.lower() == 'summary':
        resp.message(body)
    else:
        resp.message("Options:\n For Sunset respond 's'\nFor Moon phase and visibility respond 'm'\nFor a full summary respond 'summary'")
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
