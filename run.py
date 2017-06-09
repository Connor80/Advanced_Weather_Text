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

    y = False
    z = False
    while not y and not z:
        resp.message(initial_Welcome)
        if r.lower() == 'atlanta':
            y = True   
        elif r.lower() == 'dallas':
            z = True        

        while y is True:
            resp.message(atl_Welcome)
            if body.lower() == 'sunset':
                resp.message(atl_sunsetText)
            elif body.lower() == 'moon':
                resp.message(atl_moonText)
            elif body.lower() == 'humidity':
                resp.message(atl_humidityText)
            elif body.lower() == 'wind':
                resp.message(atl_windText)
            elif body.lower() == 'rain':
                resp.message(atl_rainText)
            elif body.lower() == 'all':
                resp.message(atl_allText)
            elif body.lower() == 'back':
                y = False

         while z is True:
             resp.message(dal_Welcome)
            if body.lower() == 'sunset':
                resp.message(dal_sunsetText)
            elif body.lower() == 'moon':
                resp.message(dal_moonText)
            elif body.lower() == 'humidity':
                resp.message(dal_humidityText)
            elif body.lower() == 'wind':
                resp.message(dal_windText)
            elif body.lower() == 'rain':
                resp.message(dal_rainText)
            elif body.lower() == 'all':
                resp.message(dal_allText)
            elif body.lower() == 'back':
                z = False
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
