# Task:
# -------
Config = ['Type=ethernet','Interface=eth0','Onboot=yes','bootproto=static']

# Create Config dict
# { Type : ethernet
#  Interace:eth0
#  Onboot:yes
#  bootproto: static }
# --------------------//dict
#   |
# Dict operations:
#   update bootproto ->dhcp
#   update Interface ->eth1
#   add   IP ->10.20.40.50
#   add   subnet ->24
#
# Using pprint.pprint(Updated_dict) - display
# Convert this dict ->json object
#------------------------------------------------
import pprint
import json

Config = ['Type=ethernet','Interface=eth0','Onboot=yes','bootproto=static']

config_dict = {}  # empty dict

for var in Config:
    K,V = var.split("=") # split single line into multiple values
    config_dict.setdefault(K,V) # adding new data to an existing dict
    
pprint.pprint(config_dict)
config_dict['Interface'] = 'eth1' # modification
config_dict['bootproto'] = 'dhcp' # modification
config_dict['IP'] = '10.20.40.50' # adding new data config_dict('IP','10.20.40.5')
config_dict['subnet'] = 24        # adding new data 
print('Updated dict details:-')
pprint.pprint(config_dict)

json_obj = json.dumps(config_dict,indent=4)
########
pprint.pprint(json.loads(json_obj)) # from json ->python