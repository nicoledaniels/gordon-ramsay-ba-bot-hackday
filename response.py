import os
import sys
import random
import re

drink = ["drink","beverage","liquid"]
chicken = ["chicken","wings","poultry","drumsticks","thigh","nugget","tenders","breast"]
pasta = ["noodle","spaghetti","alfredo","penne","rigatoni","al dente","pasta","cannelloni","fettunccine","linguine","macaroni","noodle","ravioli","rigatoni","tagliatelle","vermicelli"]
meat = ["meat","steak","ribeye","chops","lamb","venison","beef","pork","belly","rump","bison","bacon","goat","liver","hot dog","jamon","sausage","mutton","turkey","duck","wild boar"]
pizza = ["pizza","peperoni","margherita"]
catch_all_images = ["http://bit.ly/2w50PPl", "http://bit.ly/2wvacZz", "http://bit.ly/2xzkm8u", "http://bit.ly/2wF5Hfr", "http://bit.ly/2xzpGZn",
					"http://bit.ly/2msXj9x", "http://bit.ly/2w4OHxW", "http://bit.ly/2xjPNEs", "http://bit.ly/2wNIreM", "http://bit.ly/2wbo7l2", 
					"http://bit.ly/2iwMg2a", "http://bit.ly/2xzqGg5", "http://bit.ly/2ixG4qL", "http://bit.ly/2wFak9C", "http://bit.ly/2vdMCka", 
					"http://bit.ly/2wbGlTm", "http://bit.ly/2w503SD", "http://bit.ly/2xzldGh", "http://bit.ly/2gc001A", "http://bit.ly/2wv5OKa", 
					"http://gph.is/2xzJj3G"]

def classify(msg):
    msg = msg.strip()
    msg = re.sub(r'[^\w\s]','',msg)
    msg = msg.lower()
    msg = msg.split()
    
    print(msg)

    for word in msg:
      print(word)
      if word in drink:
        print(word in drink)
        return "https://media.giphy.com/media/ZXW1OXBCTRF2o/giphy.gif"
      elif word in chicken:
        return "https://media3.giphy.com/media/kzidPabWvU6pG/giphy.gif"
      elif word in pasta:
        return "http://i0.kym-cdn.com/photos/images/original/000/732/862/9b0.png"
      elif word in meat:
        return "https://media3.giphy.com/media/we4Hp4J3n7riw/giphy.gif"
      elif word in pizza:
        return "https://media.giphy.com/media/2FaztatdwiCRrkPCg/giphy.gif" 
      
    return catch_all_images[random.randint(0, len(catch_all_images) - 1)]
