import random

class Sustenance:
  def __init__(self, name, urls, alias = None):
    self.name = name
    self.alias = alias
    self.image_urls = urls

  def random_image_url(self):
    return self.image_urls[random.randint(0, len(self.image_urls) - 1)]
