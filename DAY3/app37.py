# Tuple of list
network_configs = (['ethernet','eth0','10.20.30.40','host01'],
                   ['ethernet','eth1','10.20.30.33','host02'])

# Convert to dict of list
network_dict_of_list = {
    'eth0': ['ethernet', '10.20.30.40', 'host01'],
    'eth1': ['ethernet', '10.20.30.33', 'host02']
}

# Convert to dict of tuple
network_dict_of_tuple = {
    'eth0': ('ethernet', '10.20.30.40', 'host01'),
    'eth1': ('ethernet', '10.20.30.33', 'host02')
}

# Convert to dict of dict
network_dict_of_dict = {
    'eth0': {'type': 'ethernet', 'ip': '10.20.30.40', 'hostname': 'host01'},
    'eth1': {'type': 'ethernet', 'ip': '10.20.30.33', 'hostname': 'host02'}
}
print(network_dict_of_dict['eth0']['type'])
print(network_dict_of_dict['eth0']['ip'])
