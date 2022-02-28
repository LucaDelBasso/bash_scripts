import requests
import os

url = "https://numbersapi.p.rapidapi.com/random/trivia"

querystring = {"json":"true","fragment":"true","max":"1000","min":"0"}

headers = {
    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    'x-rapidapi-key': os.getenv("RAPID_API_KEY")
    }

r = requests.request("GET", url, headers=headers, params=querystring).json()

if r["found"]:
    print(f'{r["number"]} is {r["text"]}.')
else:
    print("No number fact :(")
