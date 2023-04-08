# image_ai
Created by Bertran Usher

Use image_ai to generate or manipulate AI images with OpenAI's DALL-E Image Generation API. OpenAI API KEY REQUIRED.


**Summary**: The aim of image_ai is to make OpenAI's image generation API accessible through simple and customizable functions.Usei to generate or manipulate ai images with openai’s DALL·E Image generation api. 

**image_ai creates an image using OpenAI's API**. Each function takes two or three parameters, prompt_text, image_size, and/or path. It then creates a filename based on the current date and time. It then uses the OpenAI API to create an image based on the prompt_text and image_size parameters. It then prints the response from the API, generates the A.I. image, prints the URL, and downloads the image to the filename. Finally, it opens the image and returns the filename.


---------------------------------------------------------------------------------------


**Functions:**

**create_image**(prompt_text,image_size): Will create a single ai generated image based on parameter input. In order to create multiple images, add the function into a loop. 

**create_image_path(prompt_text,image_size,path)**: Will send created image to selected path folder.

**create_variation(data,image_size):**

**create_variation_path(data,image_size,path)**


---------------------------------------------------------------------------------------


**Function Parameters:**

*prompt_text*: Input image prompt into this parameter. 
Example: create_image(“4k image of a lion”, “256x256) 

*image_size*: Input image size into this parameter. 
Accepted image sizes: 256x256, 512x512, or 1024x1024 pixels

*path*: Input path folder into this parameter. 
SAVE_PATH = "C:\\Users\\Home\\Documents\\theaihub\\media\\"
Example: create_image_path(“4k image of a lion”, “256x256, SAVE_PATH) 

*data*: Image file for create_variation, must be in png. For example; “my_pic.png”.


---------------------------------------------------------------------------------------


**Required API:**

Openai API secret Key: Learn how to get your own openai api key  by clicking the link provided:https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key

Required Modules: 
1. Openai - pip install openai or pip3 install openai, official documentation: https://platform.openai.com/docs/api-reference?lang=python
2. Pillow - This module should be pre-installed, if not, official documentation should be consulted in the event of any errors: https://pillow.readthedocs.io/en/stable/installation.html
3. Datetime - This module should be pre-installed, if not, official documentation should be consulted in the event of any errors: https://docs.python.org/3/library/datetime.html
4. Urllib - This module should be pre-installed, if not, official documentation should be consulted in the event of any errors: https://docs.python.org/3/library/urllib.request.html
