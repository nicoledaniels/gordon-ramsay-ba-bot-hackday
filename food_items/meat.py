from sustenance import Sustenance

class Meat(Sustenance):
  name = "meat"
  aliases = {"meat","steak","ribeye","chops","lamb","venison","beef","pork","belly","rump","bison","bacon",
	         "goat","liver","hot dog","jamon","sausage","mutton","turkey","duck","wild boar"}
  urls = ["https://media3.giphy.com/media/we4Hp4J3n7riw/giphy.gif"]

  def __init__(self, name=name, urls=urls, alias=aliases):
    Sustenance.__init__(self, name, urls, alias)
