import re
from food_items import chicken
from food_items import drink
from food_items import meat
from food_items import pasta
from food_items import pizza
from food_items import other
from image_detection import get_relevant_tags

def classify_text(msg):
    # Classify the message based on what words the user sent
    # If an appropriate image for a Sustenance class is found,
    # return it
    # If not, return a random Gordon Ramsay image

    if type(msg) is str or type(msg) is unicode:
      word_list = message_to_word_list(msg)
    else:
      word_list = msg
    return random_image_url(word_list)

def classify_attachment(attachment):
    # To classify this image, we need to use the Clarifai API to determine
    # the components of the image
    # Send a list of image tags to the classify text method in order to obtain
    # a relevant gif/image

    payload = attachment.get('payload')
    image_url = payload.get('url')
    image_tags = get_relevant_tags(image_url)
    return classify_text(image_tags)

def message_to_word_list(message):
    # Split the message into an array of its words

    message = message.strip()
    message = re.sub(r'[^\w\s]', '', message)
    message = message.lower().split()

    return message

def random_image_url(word_list):
    # Using the words the user has sent,
    # return a random image url in the appropriate class' image store

    image_url = ""
    for word in word_list:
      if word in chicken.Chicken().alias:
        return chicken.Chicken().random_image_url()
      elif word in drink.Drink().alias:
        return drink.Drink().random_image_url()
      elif word in meat.Meat().alias:
        return meat.Meat().random_image_url()
      elif word in pasta.Pasta().alias:
        return pasta.Pasta().random_image_url()
      elif word in pizza.Pizza().alias:
        return pizza.Pizza().random_image_url()
    return other.Other().random_image_url()