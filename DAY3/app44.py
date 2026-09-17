# Task:
# -------

import pprint
import json

def f1():
    '''return Config list'''
    Config = ['Type=ethernet','Interface=eth0','Onboot=yes','bootproto=static'] # local variable
    return Config


def f2(Config):
    '''Iterate Config list and returns Config dict'''
    for var in Config:
        K,V = var.split("=") # split single line into multiple values
        config_dict.setdefault(K,V) # adding new data to an existing dict
    return config_dict

def f3(config_dict):
    '''Display dict structure'''
    pprint.pprint(config_dict)

def f4(config_dict):
    '''Dict operation'''
    config_dict['Interface'] = 'eth1' # modification
    config_dict['bootproto'] = 'dhcp' # modification
    config_dict['IP'] = '10.20.40.50' # adding new data config_dict('IP','10.20.40.5')
    config_dict['subnet'] = 24        # adding new data 
    print('\nUpdated dict details:-')
    f3(config_dict) # nested call with args
    return config_dict

def f5(config_dict):
    '''Convert from Python data -> JSON Data'''
    json_obj = json.dumps(config_dict,indent=4)
    if(json_obj):
        print("JSON Object is created")
        
config_dict = {}  # empty dict
rv1 = f1() # 1st Call
rv2 = f2(rv1) # 2nd - function call with arg
f3(rv2) # 3rd - function call with dict arg

rv4 = f4(rv2) # 4th - function call with dict arg
f5(rv4) # 5th - function call with updated dict
print('Exit from main code')