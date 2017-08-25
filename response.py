import os
import sys

drink = (["drink","beverage","liquid"])

def classify(msg):
    msg = msg.strip()
    msg = msg.lower()
    
    if(msg in drink):
       return "https://media.giphy.com/media/ZXW1OXBCTRF2o/giphy.gif"