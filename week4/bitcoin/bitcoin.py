#!/usr/bin/env python3
import requests
import sys

API_KEY =  ecd96072043d77cc2fe0bfa80636b639ff2e2795a62c49cf4f1d1931b2d139b3 # Replace with your real CoinCap API key
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

def main():
    bitcoin_amount = get_arguments()
    price = get_current_price()
    cost = bitcoin_amount * price
    print(f"${cost:,.4f}")  

def arguments_check():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    
    try:
        # Try to convert to float
        bitcoin_amount = float(sys.argv[1])
        return bitcoin_amount
        
    except ValueError: #if it cannot convert to float
        sys.exit("Command-line argument is not a number")

def get_current_price():
    try:
    
        response = requests.get(url)
        response.raise_for_status()  # catch HTTP errors
        res = response.json() 
        return float(res["data"]["priceUsd"])
        
    except requests.RequestException:
        return None



if __name__=="__main__":
    main()
