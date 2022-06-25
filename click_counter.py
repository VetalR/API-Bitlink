import os
from urllib.parse import urlparse
import requests
from dotenv import load_dotenv


def shorten_link(headers, url):

    body = {"long_url": url}
    response = requests.post(
        url='https://api-ssl.bitly.com/v4/bitlinks',
        headers=headers,
        json=body
    )
    response.raise_for_status()

    return response.json()['link']


def count_clicks(headers, bitlink):

    parse_bitlink = urlparse(bitlink)
    response = requests.get(
        url=f'https://api-ssl.bitly.com/v4/bitlinks/{parse_bitlink.netloc}'
            f'{parse_bitlink.path}/clicks/summary',
        headers=headers
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(headers, url):

    parse_url = urlparse(url)
    response = requests.get(
        url=f'https://api-ssl.bitly.com/v4/bitlinks/{parse_url.netloc}'
            f'{parse_url.path}',
        headers=headers
    )
    return response.ok


if __name__ == '__main__':

    load_dotenv()
    header = {'Authorization': f'Bearer {os.getenv("TOKEN_BITLY")}'}
    link = input('Input URL: ')

    try:
        if is_bitlink(header, link):
            counter = count_clicks(header, bitlink=link)
            print('Number of clicks:', counter)
        else:
            bit_link = shorten_link(header, url=link)
            print('Bitlink:', bit_link)
    except requests.exceptions.HTTPError:
        print('Unexpected link, retry with another link')
