from sustenance import Sustenance

class Pizza(Sustenance):
  name = "pizza"
  aliases = ["pizza","pepperoni","margherita"]
  urls = ["https://media.giphy.com/media/2FaztatdwiCRrkPCg/giphy.gif"]

  def __init__(self, name=name, urls=urls, alias=aliases):
    Sustenance.__init__(self, name, urls, alias)