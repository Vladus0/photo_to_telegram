import requests
import os
from urllib.parse import urlparse
import os.path
from dotenv import load_dotenv
load_dotenv()


os.makedirs('imgs', exist_ok=True)
api_key = os.environ['API_KEY']


def download_img(url, filename, api_key = ""):
    filepath = f'imgs/{filename}'
    payload = {
        "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)

url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"


def fetch_spacex_last_launch():
    response = requests.get(url)
    response.raise_for_status()
    images_space_x = response.json()["links"]["flickr"]["original"]
    for image_num, image in enumerate(images_space_x):
        filename = f'spacex{image_num}.jpg'
        download_img(image, filename)


def extension_url(nasa_image):
    url = urlparse(nasa_image)
    return os.path.splitext(url.path)[1]


fetch_spacex_last_launch()


def nasa_images(api_key):
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
        filename = f"nasa_image{image_num}{extension_url(nasa_image)}"
        download_img(nasa_image, filename)

nasa_images(api_key)


url = "https://api.nasa.gov/EPIC/api/natural/images"
payload = {
        "api_key": api_key,
    }
response = requests.get(url, params=payload)
response.raise_for_status()
epic_nasa_images = (response.json())
for images_num, image in enumerate(epic_nasa_images):
    epic_nasa_image = image["image"]
    epic_nasa_image_date = image["date"]
    epic_nasa_image_date = epic_nasa_image_date.split(' ')[0]
    year = epic_nasa_image_date.split('-')[0]
    mounth = epic_nasa_image_date.split('-')[1]
    day = epic_nasa_image_date.split('-')[2]
    link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{mounth}/{day}/png/{epic_nasa_image}.png"
    filename = f"epic_nasa_image_{images_num}.png"
    download_img(link, filename, api_key)