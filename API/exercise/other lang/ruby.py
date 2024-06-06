
from github_repo_info import get_GitHub_repo_info

url = "https://api.github.com/search/repositories"
url += "?q=language:ruby+sort:stars+stars:>10000"
headers ={
    "Accept" : "application/vnd.github.v3+json"
}
repo_name= "Ruby"
get_GitHub_repo_info(url,headers,repo_name)