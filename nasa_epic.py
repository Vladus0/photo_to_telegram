import requests
import os
import os.path
from dotenv import load_dotenv
from download_img import download_img


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    url = "https://api.nasa.gov/EPIC/api/natural/all"
    payload = {
        "api_key": api_key,
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
    
    response = requests.get(url, params=payload, headers=headers, proxies=proxies_dict)
    response.raise_for_status()
    dates_epic_nasa_images = (response.json())


    for date_epic_nasa_image in dates_epic_nasa_images:
        link = f"https://api.nasa.gov/EPIC/api/natural/date/{date_epic_nasa_image['date']}"
        filename = f"epic_nasa_image_{date_epic_nasa_image['date']}"
        download_img(link, filename, api_key)


if __name__=="__main__":
    main()