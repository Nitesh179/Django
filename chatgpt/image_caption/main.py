import openai
import clip
import requests
import numpy as np
from PIL import Image
import torch, os
from dotenv import load_dotenv


# load_dotenv()
openai.api_key="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"
# Load the CLIP model:
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Define a function to generate captions for images:
def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    image_input = preprocess(image).unsqueeze(0).to(device)

    # Generate image features using CLIP
    with torch.no_grad():
        image_features = model.encode_image(image_input)

    # Set the prompt text for caption generation
    prompt = "Generate a caption for this image:"

    # Generate caption using GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.5,
        logit_bias={},
    )

    # Extract the generated caption
    generated_caption = response.choices[0].text.strip()

    return generated_caption

# Provide the path to the image you want to generate a caption for:
image_path = "./image.jpeg"


# Call the generate_caption() function to generate a caption for the image:
caption = generate_caption(image_path)
print("Generated caption:", caption)



