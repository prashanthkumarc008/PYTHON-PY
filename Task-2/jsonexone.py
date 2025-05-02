import json
user = '''
       {
       "userName":"Rahul",
       "avail":true,
       "loc":null
       }
       '''

user_data = json.loads(user)
print(user_data)
print(user)