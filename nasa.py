import requests
import os
from dotenv import load_dotenv
from download_img import download_img
from urllib.parse import urlparse



def get_extension_url(nasa_image):
    url = urlparse(nasa_image)
    path = os.path.splitext(url.path)[1]
    return path

def main():
    load_dotenv()    
    api_key = os.environ['NASA_API_KEY']
    number_of_photos = 30
    payload = {
        "api_key": api_key,
        "count": number_of_photos
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://google.com"
    }
    proxy = os.environ['PROXY_URL']
    proxies_dict = {
        "http": proxy,
        "https": proxy
    }
    url = "https://api.nasa.gov/planetary/apod" 
    response = requests.get(url, params=payload, headers=headers, proxies=proxies_dict)
    response.raise_for_status()

    nasa_images = response.json()
    for image_num, image in enumerate(nasa_images):
        nasa_image = image["url"]
        path = get_extension_url(nasa_image)
        if path == "":
            continue
        else:
            filename = f"nasa_image{image_num}{path}"
            download_img(nasa_image, filename)


if __name__=="__main__":
    main()
    