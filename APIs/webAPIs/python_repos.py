import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

#Store API response in a variable
response_dict = r.json()
print("Total respositories: ", response_dict['total_count'])

#explore info about repo
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

#examine first repo
repo_dicts = repo_dicts[0]
print("\nKeys: ", len(repo_dicts))
for key in sorted(repo_dicts.keys()):
    print(key)


#process results
#print(response_dict.keys())

