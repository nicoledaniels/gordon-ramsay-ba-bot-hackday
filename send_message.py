import os
import sys
import json
import requests

params = {
    "access_token": os.environ["PAGE_ACCESS_TOKEN"]
}

headers = {
    "Content-Type": "application/json"
}

def send_image_message(recipient_id, url):
    log("Sending message to {recipient}: {text}".format(recipient=recipient_id, text=url))

    image = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url,
                    "is_reusable": True
                }
            }
        }
    })

    request = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=image)

    if request.status_code != 200:
        log_error_responses(request)
      

def send_text_message(recipient_id, text):
    log("Sending message to {recipient}: {text}".format(recipient=recipient_id, text=text))

    payload = json.dumps({
      "recipient": {
        "id": recipient_id
      },
      "message": {
        "text": text
      }  
    })

    request = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, json=payload)

    if request.status_code != 200:
        log_error_responses(request)

def log_error_responses(request):
    log(request.status_code)
    log(request.text)

def log(message):  
  # simple wrapper for logging to stdout on the console

  print str(message)
  sys.stdout.flush()
