import re
from food_items import chicken
from food_items import drink
from food_items import meat
from food_items import pasta
from food_items import pizza
from food_items import other

def classify(msg):
    # Classify the message based on what words the user sent
    # If an appropriate image for a Sustenance class is found,
    # return it
    # If not, return a random Gordon Ramsay image

    word_list = message_to_word_list(msg)
    return random_image_url(word_list)

def message_to_word_list(message):
    # Split the string into its individual words

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