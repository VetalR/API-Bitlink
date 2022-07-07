# API Bitlink


# Project description
* API Bitlink provides the creation of a "Bitlink" or needs to know,
how many times the user clicked on the link

## Installing
* To install it, make sure you have Python 3.8 or greater installed
* Copy application from repo: 
`git clone https://github.com/VetalR/API-Bitlink.git`

## Get Bitly token key
* Registry on the service "Bitly", follow link https://app.bitly.com/Bm5jgApGBTn/bitlinks/3b1a5uR
* Generate token type `GENERIC ACCESS TOKEN` (It is needed to interact with `API Bitly`), \
follow link https://bitly.com/a/oauth_apps
* Create file into project directory `.env`
  * Set into `.env` file a variable `TOKEN_BITLY` and use value `generated token key`
    * Variable example: `TOKEN_BITLY=17c09e20ad155405123ac1977542fecf00231da7`

## How to use
* Activate your virtual environment
* Run script to install the required packages `pip3 install -r {path/}API-Bitlink/requirements.txt`
* Run script, instead of argument {link}, Input full link, if you want to get bitlink or input bitlink, if you want to get count of clicks
``python {path/}API-Bitlink/click_counter.py {link}``

## Simple Example
* To execute it: ``python3 click_counter.py https://dvmn.org``
* Example output `Bitlink: https://bit.ly/39BLGLE`
