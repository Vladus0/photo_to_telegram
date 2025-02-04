import requests
import os
import os.path
from dotenv import load_dotenv
from download_img import download_img


def main():
    load_dotenv()
    api_key = os.environ['API_KEY']
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


if __name__=="__main__":
    main()