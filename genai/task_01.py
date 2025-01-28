import argparse

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from vertexai.generative_models import GenerativeModel, Part, Image

project_id ='qwiklabs-gcp-01-398fd625f871'
location = 'us-west1'


def generate_bouquet_image(prompt:str):
    vertexai.init(project=project_id, location=location)

    model = ImageGenerationModel.from_pretrained('imagegeneration@002')

    images = model.generate_images(prompt=prompt,number_of_images=1,
        seed=1,add_watermark=False)

    images[0].save('bouquet.jpg')

    return images

def analyze_bouquet_image(image_path):
    vertexai.init(project=project_id, location=location)

    # Create the multimodal generative model
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

    # Load the image and generate the content
    response = multimodal_model.generate_content([
        Part.from_image(Image.load_from_file(image_path)),  # Read the image in binary mode
        "Generate birthday wishes based on image"
    ])

    return response.text

# generate_bouquet_image('Create an image containing a bouquet of 2 sunflowers and 3 roses')

analysis = analyze_bouquet_image('bouquet.jpg')
print('Analysis:', analysis)
# bouquet.png