from operator import itemgetter
import requests
import plotly.express as px

# Fetch the top submission IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url=url)
print(f"Status Code: {r.status_code}")
get_submission_Ids = r.json()

make_submission_Dicts = []
for take_sub in get_submission_Ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{take_sub}.json"
    r = requests.get(url)
    print(f"id: {take_sub} \t status: {r.status_code}")
    get_response_dict = r.json()

    # Try-except block to handle potential KeyErrors
    try:
        # Build a dictionary for each article
        build_submission_dict = {
            "title": get_response_dict['title'],
            "hn_link": f"https://news.ycombinator.com/item?id={take_sub}",
            "comments": get_response_dict['descendants']
        }
        make_submission_Dicts.append(build_submission_dict)
    except KeyError:
        print("The comment box is empty or the post is promotional\n")

# Sort the submissions by the number of comments
make_submission_Dicts = sorted(make_submission_Dicts, key=itemgetter('comments'), reverse=True)

hn_links, comments, hovers = [], [], []
print("\nSelected info on Hacker News Submissions\n")
for sub in make_submission_Dicts:
    sub_title = sub['title']
    sub_link = sub['hn_link']
    sub_comments = sub['comments']
    print(f"\nTitle: {sub_title}")
    print(f"\nDiscussion Link: {sub_link}")
    print(f"\nComments: {sub_comments}")
    hn_links.append(sub_link)
    comments.append(sub_comments)
    hovers.append(sub_title)

title = "Hacker News Most Active Discussions"
labels = {"x": "Submission Title", "y": "Number of Comments"}
fig = px.bar(x=hovers, y=comments, title=title, labels=labels, hover_name=hn_links)
fig.show()
