from operator import itemgetter
import requests
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code:{r.status_code}")

# Process INfo about each subMission
submission_Ids = r.json()
submission_Dicts = []
for submission_Id in submission_Ids[:5]:
# Make a new call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_Id}.json"
    r = requests.get(url)
    print(f"id:{submission_Id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_Dict = {
        "title" : response_dict['title'],
        "hn_link" : f"https://news.ycombinator.com/item?id={submission_Id}",
        "comments":response_dict['descendants'],

    }
    submission_Dicts.append(submission_Dict)
    try:
        submission_Dicts =sorted(submission_Dicts,key=itemgetter('comments'),reverse = True)
    except KeyError :
        print("Keyvalue error since the comment box is empty") 
    

for subm_dict in submission_Dicts:
    print(f"\nTitle : {subm_dict['title']}")
    print(f"\nDiscussion Link : {subm_dict['hn_link']}")
    print(f"\nComments : {subm_dict['comments']}")