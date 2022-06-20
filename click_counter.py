import os
import requests
from dotenv import load_dotenv


def shorten_link(token, url):

    header = {
        'Authorization': f'Bearer {token}'
    }
    body = {
            "long_url": url
        }

    response = requests.post(url='https://api-ssl.bitly.com/v4/bitlinks',
                             headers=header,
                             json=body)
    response.raise_for_status()

    return response.json()['link']


if __name__ == '__main__':

    load_dotenv()
    TOKEN = os.getenv('TOKEN_BITLY')
    link = input('Input URL: ')

    try:
        bit_link = shorten_link(TOKEN, url=link)
    except requests.exceptions.HTTPError:
        SystemExit('Unexpected Link, retry else')
    else:
        print('Bitlink:', bit_link)
