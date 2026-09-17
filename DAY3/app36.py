# Tuple of list
network_configs = (['ethernet','eth0','10.20.30.40','host01'],
                   ['ethernet','eth1','10.20.30.33','host02'])
print(len(network_configs))
print(network_configs)
print(network_configs[0])
print(network_configs[0][2])
network_configs[0][2] = "192.168.1.33"
print(network_configs)

# Tuple of Tuple
#-----------------
network_configs = (('ethernet','eth0','10.20.30.40','host01'),
                   ('ethernet','eth1','10.20.30.33','host02'))

# Tuple of dict
#--------------------
network_configs = (
    {'type': 'ethernet', 'interface': 'eth0', 'ip': '10.20.30.40', 'hostname': 'host01'},
    {'type': 'ethernet', 'interface': 'eth1', 'ip': '10.20.30.33', 'hostname': 'host02'}
)
print(len(network_configs))
print(network_configs)
print(network_configs[0])
print(network_configs[0]['ip'])
network_configs[0]['ip'] = '192.168.1.33'
print(network_configs)
