import requests

token = requests.get('http://localhost:6878/server/api?method=get_api_access_token').json()['result']['token']
query = requests.get(f'http://localhost:6878/server/api?method=search&token=9d324ef909c50629ca3d23faddaa7358236b0bbe62dfd049416dc4d570b60b57&query=Премьер').json()
query = query['result']['results']
for i in query:
    print(f"{i['items'][0]['name']} : {i['items'][0]['infohash']} \n\n")
