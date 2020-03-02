import requests

url = "https://morning-star.p.rapidapi.com/market/auto-complete"

querystring = {"query":"nasdaq"}

headers = {
    'x-rapidapi-host': "morning-star.p.rapidapi.com",
    'x-rapidapi-key': "060113bfa6msh6e845788c6d3adfp12f7a6jsnaf0bc8dcf9c5"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
