from urllib import request
import json

def get():
    response = request.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status==200:
        quote = response.json()

        return qoute

        