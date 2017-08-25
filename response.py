import os
import sys

drink = ["drink","beverage","liquid"]
catch_all_images = ["http://bit.ly/2w50PPl", "http://bit.ly/2wvacZz", "http://bit.ly/2xzkm8u", "http://bit.ly/2wF5Hfr", "http://bit.ly/2xzpGZn",
					"http://bit.ly/2msXj9x", "http://bit.ly/2w4OHxW", "http://bit.ly/2xjPNEs", "http://bit.ly/2wNIreM", "http://bit.ly/2wbo7l2", 
					"http://bit.ly/2iwMg2a", "http://bit.ly/2xzqGg5", "http://bit.ly/2ixG4qL", "http://bit.ly/2wFak9C", "http://bit.ly/2vdMCka", 
					"http://bit.ly/2wbGlTm", "http://bit.ly/2w503SD", "http://bit.ly/2xzldGh", "http://bit.ly/2gc001A", "http://bit.ly/2wv5OKa", 
					"http://gph.is/2xzJj3G"]

def classify(msg):
    msg = msg.strip()
    msg = msg.lower()
    
    for word in drink:
      if word in msg:
        return "https://media.giphy.com/media/ZXW1OXBCTRF2o/giphy.gif"
      else: 
      	return catch_all_images[random.randint(0, len(catch_all_images) - 1)]