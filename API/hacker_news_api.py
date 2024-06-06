import requests
import json

# Make an API call and register the response
get_url = "https://hacker-news.firebaseio.com/v0/item/40580456.json"
def get_hackr_news(url):
    r = requests.get(url=url)
    print(f"Status Code: {r.status_code}")

    # Explore the structure of the data
    resp = r.json()
    resp_string = json.dumps(resp,indent =4)
    print(resp_string)

get_hackr_news(get_url)
