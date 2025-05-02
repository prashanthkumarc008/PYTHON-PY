import requests

resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
""" print(type(resp_data))
print(type(resp_data.json())) """
users=resp_data.json()
print(type(users))