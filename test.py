import requests

BASE = 'http://127.0.0.1:5000/'

# response = requests.get(BASE + 'helloworld')
# print(response.json())

# response = requests.post(BASE + 'helloworld')
# print(response.json())

# response = requests.get(BASE + 'names/tim')
# print(response.json())

# response = requests.put(BASE + 'video/1', {'likes': 10})
# print(response.json())

data = [
    {'name': 'MyVideo One', 'likes': 375, 'views': 19683 },
    {'name': 'MyVideo Two', 'likes': 2345, 'views': 184 },
    {'name': 'MyVideo Three', 'likes': 84547, 'views': 65465 },
    {'name': 'MyVideo Four', 'likes': 118933, 'views': 16584},
    {'name': 'MyVideo Five', 'likes': 654, 'views': 35 },
    {'name': 'MyVideo Six', 'likes': 24474, 'views': 765 }
]

print('put...')
for i in range(1, len(data)+1):
    response = requests.put(BASE + 'video/' + str(i), data[i-1])
    print(response.json())

print('get...')
for i in range(1, len(data)+1):
    response = requests.get(BASE + 'video/' + str(i))
    print(response.json())

# print('non existent video get test...')
# response = requests.get(BASE + 'video/9999999')
# print(response.json())

# response = requests.delete(BASE + 'video/3')
# print(response)

print('Trying update...')
response = requests.patch(BASE + 'video/1', {'likes': 300, 'views': 3000 })
print(response.json())

