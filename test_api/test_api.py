import requests
HOST = 'http://192.168.56.101:7070'
res = requests.post(HOST + '/api-token-auth/', {
    'username':'username',
    'password':'password',
})

res.raise_for_status()
token = res.json()['token']
print(token)

# 인증이 필요한 요청에 아래의 headers를 붙임
headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}

# Post Create
data = {
    'title' : 'test_api.py test', 
    'text' : 'API내용 by code', 
    'created_date' : '2023-06-11T18:34:00+09:00', 
    'published_date' : '2023-06-11T18:34:00+09:00'
}

file = {'image' : open('/home/sksmschl/Desktop/sidebar2.jpg', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())