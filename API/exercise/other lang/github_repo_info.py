import requests
import plotly.express as px

def get_GitHub_repo_info(get_url,get_header,get_repo_name ):
    try: r =requests.get(url=get_url,headers=get_header)
    except ConnectionError : print("Connection error\ncheck internet status \nor try again later\n")
    if r.status_code == 200 :print(f"Status Code : {r.status_code}")
    elif r.status_code == 404 : print(f"Forbidden Code 404")

    get_resp = r.json()
    print(get_resp.keys())
    print(f"Total repos : {get_resp['total_count']}")
    print(f"Complete results : {not get_resp['incomplete_results']}")
    repo_dicts = get_resp['items']
    print(f"Repo returned : {len(repo_dicts)}")
    repo_links,stars,hovers = [],[],[]
    try:set_dict = repo_dicts[0]
    except IndexError : print("link wrong or blocked \n")
    print("\nSelected info on each repository \n")
    for foo in repo_dicts:
        repoName =foo['name']
        repoURL = foo['html_url']
        repoLink  = f"<a href = '{repoURL}'>{repoName}</a>"
        repo_links.append(repoLink)
        stars.append(foo['stargazers_count'])
        owner = foo['owner']['login']
        desc = foo['description']
        hove = f"{owner}<br />{desc}"
        hovers.append(hove)
    title = f"Most starred {get_repo_name} projects on GitHub"
    labels = {"x": "Repository", "y": "Stars"}
    fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hovers)
    fig.update_layout(title_font_size=24, xaxis_title_font_size=18, yaxis_title_font_size=18)

    fig.show()