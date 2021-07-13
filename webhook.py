from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from discord_webhook import DiscordWebhook
from discord.ext import commands
from twilio.rest import Client
import discord
app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    webhook = DiscordWebhook(url='webhook url', content=("Bir kullanıcı whattsapp dan şöyle bir cevap verdi :    {}".format(msg)))
    response = webhook.execute()
    return str(resp)

if __name__ == "__main__":

    app.run(debug=True)
