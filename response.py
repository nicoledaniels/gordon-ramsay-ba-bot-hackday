import os
import sys

drink = ["drink","beverage","liquid"]
chicken = ["chicken","wings","poultry","drumsticks","thigh","nugget","tenders","breast"]
pasta = ["noodle","spaghetti","alfredo","penne","rigatoni","al dente","pasta","cannelloni","fettunccine","linguine","macaroni","noodle","ravioli","rigatoni","tagliatelle","vermicelli"]
meat = ["meat","steak","ribeye","chops","lamb","venison","beef","pork","belly","rump","bison","bacon","goat","liver","hot dog","jamon","sausage","mutton","turkey","duck","wild boar"]
pizza = ["pizza","peperoni","margherita"]

def classify(msg):
    msg = msg.strip()
    msg = msg.lower()
    msg = msg.split()
    
    for word in msg:
      if word in drink:
        return "https://media.giphy.com/media/ZXW1OXBCTRF2o/giphy.gif"
      if word in chicken:
        return "https://media3.giphy.com/media/kzidPabWvU6pG/giphy.gif"
      if word in pasta:
        return "http://i0.kym-cdn.com/photos/images/original/000/732/862/9b0.png"
      if word in meat:
        return "https://media3.giphy.com/media/we4Hp4J3n7riw/giphy.gif"
      if word in pizza:
        return "https://media.giphy.com/media/2FaztatdwiCRrkPCg/giphy.gif"