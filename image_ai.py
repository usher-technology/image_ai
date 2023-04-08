
import datetime
import urllib.request
from PIL import Image

# How to use image_ai:
# Use the functions below to generate AI images via OpenAI API. 
# OpenAI API Key is Required. To find your key/signup to OpenAI follow this link --> Find Key: https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key SignUp: https://platform.openai.com/signup
# Argument Options: 
# image_size: 256x256, 512x512, or 1024x1024 pixels.
# path: Example "C:\\Users\\politimax\\theaihub\\hub\\Media\\" 

OPENAI_KEY = "Place Key Here"
SAVE_PATH = "C:\\example\\example\\example\\folder\\Media\\"

def create_image(prompt_text,image_size):
    now = datetime.datetime.now()
    filename = 'ai_image_' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
    openai.api_key = OPENAI_KEY
    try: 
        response = openai.Image.create(
            prompt= prompt_text,
            n=1,
            size=image_size
        )
        print(response)
        image_url = response['data'][0]['url']
        print("Generating A.i. Image")
        url = image_url
        print(url)
        urllib.request.urlretrieve(url, filename)
        img = Image.open(filename)
        img.show()
        return(filename)
    
    except openai.error.OpenAIError as e:
        print(e.error)
       
def create_image_path(prompt_text,image_size,path ):
    now = datetime.datetime.now()
    filename = 'ai_image' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
    openai.api_key = OPENAI_KEY
    try: 
        response = openai.Image.create(
            prompt= prompt_text,
            n=1,
            size= image_size
        )
        print(response)
        image_url = response['data'][0]['url']
        print("Generating A.i. Image")
        url = image_url
        print(url)
        urllib.request.urlretrieve(url, path + filename)
        img = Image.open(path + filename)
        img.show()
        return(path + filename)
    
    except openai.error.OpenAIError as e:
        print(e.error)

def create_variation(data,image_size):
  now = datetime.datetime.now()
  filename = 'ai_image_variation_' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
  openai.api_key = OPENAI_KEY
  response = openai.Image.create_variation(
    image=open(data, "rb"),
    n=1,
    size=image_size
  )
  image_url = response['data'][0]['url']
  url = image_url
  urllib.request.urlretrieve(url, filename)
  img = Image.open(filename)
  img.show()

def create_variation_path(data,image_size,path):
  now = datetime.datetime.now()
  filename = 'ai_image_variation_' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
  openai.api_key = OPENAI_KEY
  try:
    response = openai.Image.create_variation(
      image=open(data, "rb"),
      n=1,
      size=image_size
    )
    image_url = response['data'][0]['url']
    url = image_url
    urllib.request.urlretrieve(url, path + filename)
    img = Image.open(path + filename)
    img.show()
    return(path + filename)
  
  except openai.error.OpenAIError as e:
    print(e.error)

#Example 1: Create an image a dog
#create_image("picture of a dog", "256x256")

#Example 2: Create 5 images of a tiger
#for i in range(5):
    #create_image("picture of a tiger", "256x256")
   
#Example 3: Create image variation
#image = create_image("picture of a dragon", "256x256")
#create_variation(image,"256x256")
