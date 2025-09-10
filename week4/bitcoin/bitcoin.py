#!/usr/bin/env python3
"""
request user bitcoin ammount from command line
check if it can be converted to float
if not sys.exit("Command-line argument is not a number")
if no argument sys.exit("Missing command-line argument")
"""
import requests
import sys

def main():
    arguments_check()
    
def arguments_check():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    
    if not bitcoin_amount.isnumeric():
            sys.exit("Command-line argument is not a number")
    return bitcoin_amount=sys.argv[1]

def get_current_price():
    try:
        url="https://api.coinbase.com/v2/prices/BTC-USD/spot"
    
        response = requests.get(url)
        
    except requests.RequestException:
        continue
