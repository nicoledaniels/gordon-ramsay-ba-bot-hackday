from sustenance import Sustenance

class Chicken(Sustenance):
  name = "chicken"
  aliases = ["chicken","wings","poultry","drumsticks","thigh","nugget","tenders","breast"]
  urls = ["https://media3.giphy.com/media/kzidPabWvU6pG/giphy.gif"]
	
  def __init__(self, name=name, urls=urls, alias=aliases):
    Sustenance.__init__(self, name, urls, alias)
