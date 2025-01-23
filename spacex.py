import requests
from dotenv import load_dotenv
from download_img import download_img


def main():
    load_dotenv()
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    images_space_x = response.json()["links"]["flickr"]["original"]
    for image_num, image in enumerate(images_space_x):
        filename = f'spacex{image_num}.jpg'
        download_img(image, filename)


if __name__=="__main__":
    main()