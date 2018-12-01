from sustenance import Sustenance

class Drink(Sustenance):
  name = "drink"
  aliases = ["drink","beverage","liquid"]
  urls = ["https://media.giphy.com/media/ZXW1OXBCTRF2o/giphy.gif"]

  def __init__(self, name=name, urls=urls, alias=aliases):
    Sustenance.__init__(self, name, urls, alias)
