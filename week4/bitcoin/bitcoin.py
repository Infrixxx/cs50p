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
        url="https://api.coinbase.com/v2/prices/BTC-USD/spot"
    
        response = requests.get(url)
        
    except requests.RequestException:
        continue
