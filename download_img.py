import requests
import os


def download_img(url, filename, api_key = ""):
    os.makedirs('imgs', exist_ok=True)
    filepath = f'imgs/{filename}'
    payload = {
        "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)