import os
from classification import classify_text, classify_attachment
from heroku_logging import log
from send_message import send_image_message, send_text_message
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify_request():
    # Facebook sends a verification token to guarantee that a malicious
    # actor isn't sending us fake requests
    # Validate the received token with our token

    received_token = request.args.get("hub.verify_token")
    return verify_token(received_token)

@app.route('/', methods=['POST'])
def send_response():
    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)

    for event in data["entry"]:
        for messaging_event in event["messaging"]:
            message = messaging_event.get("message")
            recipient_id = messaging_event["sender"]["id"]
            if message.get("text"):
                message_text = message.get("text")
                response_message = classify_text(message_text)
                send_image_message(recipient_id, str(response_message))
            elif message.get("attachments")[0] and message.get("attachments")[0]["type"] == "image":
                response_message = classify_attachment(message.get("attachments")[0])
                send_image_message(recipient_id, str(response_message))
            else:
                response_message = "I'm sure this food is dreadful, but I only accept text and images"
                send_text_message(recipient_id, str(response_message))

    return "Success", 200

def verify_token(received_token):
    # If tokens match, allow the program to continue execution
    # Otherwise, a malicious actor is sending us requests, return error

    if received_token == os.environ['VERIFY_TOKEN']:
        return request.args.get("hub.challenge")
    return "Verification token mismatch", 403

if __name__ == '__main__':
    app.run(debug=True)
