# Conditional statement 
# ------------------------
# Code block that executes only one time
#                          =============
# expression ->bool 
# function() ->bool
# obj.method() ->bool
# ---------------------
#   |-> Use conditional statements
#
# if(condition):
#    ....
#    ....
#
# if(condition):
#    True block
# else:
#    False block
#
# read a device name from <STDIN>
# check if the device name is router or not 
#                              |->OK     |->Not a router
# --------------------------------------------
device_name = input("Enter device name: ")
if device_name == "router":
    print("OK")
else:
    print(f"Sorry your input device name is:{device_name} not a router")
    
# prompt:
# read a device name as input from user test device vendor is cisco or not 
# ---------------------------
device_vendor = input("Enter device vendor: ")
if device_vendor == "cisco":
    print("OK")
else:
    print(f"Sorry your input device vendor is: {device_vendor} not cisco")
    
# Task:
# read an app name from <STDIN>
# check if the app name is "myapp"  - initialize port number is 5000
# check if the app name is "demoapp" - initialize port number is 6000
# check if the app name is testapp - initialize port number is 8080
# |
# default app name is: webTest port 8000
#
# display app name and running portnumber.
# ---------------------------

app_name = input("Enter app name: ")
if app_name == "myapp":
    port = 5000
elif app_name == "demoapp":
    port = 6000
elif app_name == "testapp":
    port = 8080
else:
    app_name = "webTest"
    port = 8000

print(f"App Name: {app_name}, Running Port: {port}")
