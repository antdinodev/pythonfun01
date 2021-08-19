import requests

#https://httpbin.org/

payload = {'page': 2, 'count': 25}

payload2 = {'username': 'Meliisa','password': 'testing'}


r = requests.get('https://cdn.pixabay.com/photo/2013/07/13/01/24/bunny-155674_960_720.png' ,params = payload)
#to post data use requests.post
r2 = requests.post('https://httpbin.org/post' ,params = payload2)

print(r.headers)
print(r.url)

print(r2.headers)
print(r2.url)
print(r2.text)

r_dict = r2.json()
print(r_dict['form'])
#print(r2.json())