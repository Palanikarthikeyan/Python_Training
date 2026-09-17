'''
list - index based access + mutable + append() pop() ... 
tuple - index based access + immutable - record / fixed row 
dict - key:value based + mutable + get() pop(key) setdefault() keys()

list of list
list of tuple
list of dict
=====   ______
|          |-> unnamed 
named
'''
import pprint

# List of List
network_configs = [['ethernet','eth0','10.20.30.40','host01'],
                   ['ethernet','eth1','10.20.30.33','host02']]
network_configs.append(['ethernet','eth2','10.23.44.32','host03'])
print(network_configs)
# To update eth1 interface IP => 10.50.60.66
# ==========================================
network_configs[1][2]="10.50.60.66"

print(network_configs)

print('') # empty line
# List of Tuple
network_configs = [('ethernet','eth0','10.20.30.40','host01'),
                   ('ethernet','eth1','10.20.30.33','host02')]
network_configs.append(('ethernet','eth2','10.23.44.32','host03')) 
print(network_configs)

# List of dict
# -----------------
network_configs = [{'type':'ethernet','interface':'eth0','IPADDR':'10.20.30.40','host':'host01'},
                   {'type':'ethernet','interface':'eth1','IPADDR':'10.20.30.33','host':'host02'}]
network_configs.append({'type':'ethernet','interface':'eth2','IPADDR':'10.23.44.32','host':'host03'}) 

# print(network_configs)

pprint.pprint(network_configs)