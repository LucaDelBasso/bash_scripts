import requests

url = "https://numbersapi.p.rapidapi.com/random/trivia"

querystring = {"json":"true","fragment":"true","max":"1000","min":"0"}

headers = {
    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    'x-rapidapi-key': "2389ef68f4mshb47f2b8165e8bbfp107ca0jsn95349ab1c019"
    }

r = requests.request("GET", url, headers=headers, params=querystring).json()

if r["found"]:
    print(f'{r["number"]} is {r["text"]}.')
else:
    print("No number fact :(")
