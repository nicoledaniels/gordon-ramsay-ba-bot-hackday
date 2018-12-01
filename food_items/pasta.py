from sustenance import Sustenance

class Pasta(Sustenance):
  name = "pasta"
  aliases = ["pasta","noodle","spaghetti","alfredo","penne","rigatoni","al dente","pasta","cannelloni","fettunccine",
			 "linguine","macaroni","noodle","ravioli","rigatoni","tagliatelle","vermicelli"]
  urls = ["http://i0.kym-cdn.com/photos/images/original/000/732/862/9b0.png"]
	
  def __init__(self, name=name, urls=urls, alias=aliases):
    Sustenance.__init__(self, name, urls, alias)
