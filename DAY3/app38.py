import json
network = {
    'eth0': {'type': 'ethernet', 'ip': '10.20.30.40', 'hostname': 'host01'},
    'eth1': {'type': 'ethernet', 'ip': '10.20.30.33', 'hostname': 'host02'},
    'eth2': ['ethernet','10.20.33.44','host03'],
    'eth3': ('ethernet','15.25.33.34','host04')
}

# python -> json
json_data = json.dumps(network)

# json ->python
py_data = json.loads(json_data) ### 
print(type(py_data))
print(py_data)