import requests
import os
from dotenv import load_dotenv
from download_img import download_img
from urllib.parse import urlparse


def get_extension_url(nasa_image):
    url = urlparse(nasa_image)
    return os.path.splitext(url.path)[1]

def main():
    load_dotenv()    
    api_key = os.environ['NASA_API_KEY']
    payload = {
        "api_key": api_key,
        "count": 30
    }
    url = "https://api.nasa.gov/planetary/apod" 
    response = requests.get(url, params=payload)
    response.raise_for_status()

    nasa_images = response.json()
    for image_num, image in enumerate(nasa_images):
        nasa_image = image["url"]
        filename = f"nasa_image{image_num}{get_extension_url(nasa_image)}"
        download_img(nasa_image, filename)


if __name__=="__main__":
    main()
    