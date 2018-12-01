from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

def get_relevant_tags(image_url):
  # Using the Clarifai public models, return the words matching the image with the
  # highest confidence

  model = app.public_models.general_model
  response = model.predict_by_url(url=image_url)
  tag_urls = []
  concepts = response['outputs'][0]['data']['concepts']
  for concept in concepts:
    tag_urls.append(concept.get('name'))

  return tag_urls