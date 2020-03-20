# TrackerBot - check cryptocurrencies prices on telegram

import requests


def get_price(coins): 
    base = "https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=BTC,USD,EUR"
    upper_coins = [coin.upper() for coin in coins]
    string = ",".join(upper_coins)
    response = requests.get(base.format(string)).json()
    return response


def get_rank(limit=10):
    base = "https://api.coinmarketcap.com/v1/ticker/?limit={}"
    response = requests.get(base.format(limit)).json()
    return response


def get_history(coin, interval=None, limit=None, aggregate=3):
    interval_string = 'histominute' if interval == 'minute' else 'histohour' if interval == 'hour' else 'histoday'
    base = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym=USD&limit={}&aggregate={}&e=CCCAGG"
    string = base.format(interval_string, coin.upper(), limit, aggregate)
    response = requests.get(string).json()
    return response

