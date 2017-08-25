import os
import sys

drink = ["drink","beverage","liquid"]

def classify(msg):
    msg = msg.strip()
    msg = msg.lower()
    
    for word in drink:
      if word in msg:
        return "https://media.giphy.com/media/ZXW1OXBCTRF2o/giphy.gif"