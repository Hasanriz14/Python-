import requests
import plotly.express as plt

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url=url,headers= headers)
print(f"Status Code: {r.status_code}")
resp = r.json()
print(resp.keys())
print(f"Total repos : {resp["total_count"]}")
print(f"Complete results:{not resp["incomplete_results"]}")

repo_dicts = resp["items"]
print(f"Repo returned : {len(repo_dicts)}")
repo_links ,stars,hover_text= [],[],[]
repo_dict = repo_dicts[0]
print("\nSelected info on each repository\n")
for repo_dict in repo_dicts:
    repo_names = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href = '{repo_url}'>{repo_names}</a>"
    repo_links.append(repo_link)
    
    stars.append(repo_dict['stargazers_count'])
    owner= repo_dict['owner']['login']
    description = repo_dict['description']
    hovee = f"{owner}<br />{description}"
    hover_text.append(hovee)

title = "Most starred Python Projects on GitHub"
labl = {"x":"Repository","y":"Stars"}
fig = plt.bar(x=repo_links,y = stars,title=title,labels=labl,hover_name=hover_text)
fig.update_traces(marker_color = 'SteelBlue',marker_opacity = 0.6)
fig.update_layout(title_font_size = 24, xaxis_title_font_size =20,yaxis_title_font_size =20)
fig.show()

# Ruby Haskell Perl java GO