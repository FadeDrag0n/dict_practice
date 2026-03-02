user_dict = {}

for i in range(1, 4):
    flow_key = input(f"Enter key {i}: ")
    flow_value = input(f"Enter value for {flow_key}: ")
    user_dict[flow_key] = flow_value
user_dict['test'] = 'test'
user_dict['test2'] = 'test2'
print(user_dict)
del user_dict['test']
print(user_dict)