import json
emp={'eid': 101, 'ename': 'Rahul', 'loc': True}

emp_str=json.dumps(emp)
print(emp_str)