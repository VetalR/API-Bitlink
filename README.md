# API Bitlink
Tool provide to know, how many times consumer click to the link

# Project description
    Create new bitlink or get info about clicks

## Environmental requirements
You will need to use Python ver not lower than 3

## Installing
* Open bash console
* Choose installation directory
* Copy application from repo 
"git clone https://github.com/VetalR/API_Link_click.git"

## Get Bitly token key
* Registry on the service "Bitly", follow link "https://app.bitly.com/Bm5jgApGBTn/bitlinks/3b1a5uR"
* Generate token type "GENERIC ACCESS TOKEN" (It is needed to interact with "API Bitly"), \
follow link "https://bitly.com/a/oauth_apps"
* Create file ".env"
  * Set a variable "TOKEN_BITLY" with a value "generated token key"
    * Variable example: "TOKEN_BITLY=17c09e20ad155405123ac1977542fecf00231da7"

## How to use
* Activate your virtual environment
* Run script to install the required packages "pip3 install -r {path/}requirements.txt"
* Run script "python {path/}click_counter.py"
* Input full link (if you want to get bit link) or input bitlink (if you want to get count of clicks)

## Simple Example
python click_counter.py 
* Input URL: http://google.com
* Bitlink: https://bit.ly/3yLNE6I
