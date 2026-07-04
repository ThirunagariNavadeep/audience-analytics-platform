import requests

response = requests.get(
       "https://www.omdbapi.com/",
    params={
        "apikey": "55269e72",
        "i": "tt0114709"
    }
)

print(response.status_code)
print(response.json())
