import requests
import plotly.express as px
from c import get_GitHub_repo_info

url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"
headers ={
    "Accept" : "application/vnd.github.v3+json"
}
repo_name = "JavaScript"
get_GitHub_repo_info(url,headers,repo_name)