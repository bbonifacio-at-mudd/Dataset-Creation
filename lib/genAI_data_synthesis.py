import os
import requests
from PIL import Image

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def generate_image(description, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": description,
        "n": 1,
        "size": "1024x1024",
        "quality": "hd"  # Set to 'hd' for higher detail images
    }

    response = requests.post("https://api.openai.com/v1/images/generations", headers=headers, json=data)
    
    print("API Response:", response.json())
    return response.json()


def save_generated_image(image_data, filename):
    # Extract the image URL from the response
    image_url = image_data['data'][0]['url']
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        # Save the image
        with open(filename, 'wb') as f:
            f.write(image_response.content)

# Usage
folder = "Backgrounds/Blackjack_Topdown"
api_key = 
images = load_images_from_folder(folder)

output_folder = "Backgrounds/Blackjack_genAI"
startvalue = 10

for idx, img in enumerate(images):
    idx+=startvalue
    description = """A top-down view of an empty blackjack table with a vivid green felt. 
    The table has places for seven players with white outlined boxes for bets.
    Text on the table includes 'BLACKJACK PAYS 3 TO 2', 'Dealer must stand on 17 and draw to 16', 
    and 'INSURANCE PAYS 2 TO 1', with card suit symbols. 
    A golden-yellow decorative band runs around the edge. 
    The image should be clean, with no cards, chips, or players."""

    generated_image_data = generate_image(description, api_key)
    output_filename = os.path.join(output_folder, f"gen_blackjack_{idx}.jpg")
    save_generated_image(generated_image_data, output_filename)

