
from config import key
import json

response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
	size="1024x1024")
print(response)
image_url = response['data'][0]['url']
print(image_url)
