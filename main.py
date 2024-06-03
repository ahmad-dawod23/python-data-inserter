import requests
import randomname
import json
from tokenauth import TokenAuth

#response = requests.get('https://website.example/id', headers={'Authorization': 'access_token myToken'})


url = 'https://localhost:44327/api/Accounts/Login'
myobj = {
  "name": "hamodaboi",
  "email": "no@thanku.com",
  "password": "hamodaboi"
}
x = requests.post(url, json = myobj,verify='D:\stuff\localhost.pem')
json_response = x.json()
token=json_response["access_token"]



url2 = 'https://localhost:44327/api/Categories'
categories= {
  "name": "food",
  "imageUrl": "string",
  "imageArray": "string"
}
y = requests.post(url2, json = categories,verify='D:\stuff\localhost.pem', auth=TokenAuth(token))
json_response2 = y.json()


print(json_response2)