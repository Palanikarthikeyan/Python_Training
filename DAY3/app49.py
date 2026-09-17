# module 
# --------
#  |-->Existing python file 
#  |--> reusability 
#
# import pprint
# import json
# import sys
# import <module>
#
# <module>.member 
#          ------
#
# pip install <module> <== commandline tool
# ---         =========
#--------------------------
# D:\
# ----
#   |--> app.py                                p1.py
#        ----------                           ----------------------------------
#         app_name = "web2.0"                  import app
#         app_port = 4040                      print(app.app_name)
#         app_config = "web.cfg"               if(app.app_port >4000):
#         def display():                              rv  = app.display()
#              return "Welcome"                       print(rv)
#       ==============================       --------------------------------
#       python app.py                             python p1.py
#        Output is Empty                          web2.0
#                                                 Welcome
# -------------------------------------------------------------------------------------------
# D:\Demo\
#      |______ p2.py  ----------------------------->  p2.py
#      ==================                             ========== 
#         import app                                  import sys
#         print(app.app_name)                         sys.path.append("D:\\")
# -------------------------------                     import app
#   python p2.py                                      print(app.app_name) # OK
#   ModuleNotFound <-- Error                         ------------------------------
#                                                     python p2.py 
#                                                     web2.0
#
# Linux / mac os users
# ----------------------
# 1.Go to login path 
# 2. vi .bashrc 
# export PYTHONPATH="/home/users/Demo"
# :wq <== save and exit
# 3. source .bashrc
# ---------------------------------------
#
# E:/Project/
#         |____ app1.py app2.py ... app100.py
#         |____ sub1/
#                 |____app101.py app102.py
#         |____ Sub2/
#                 |___Sub3/
#                       |________app103.py app104.py
#
# ---------------------------------------------------------
# Commandline steps
# ------------------
# 1. Create a project folder
# 2. Keep all the python files under this folder ( and subFolder/directory)
# 3. Create package initialization file (specialfile) ==> __init__.py <==
# 4. Copy the external symbols to __init__.py 
# 5. Test your package -> import <projectDirectory>
# ---------------------------------------------------
#
# --> app.py                                p1.py
#        ----------                           ----------------------------------
#         app_name = "web2.0"                  import app
#         app_port = 4040                      print(app.app_name) # Vs print(app_name) ->NameError
#         app_config = "web.cfg"               if(app.app_port >4000):
#         def display():                              rv  = app.display()
#              return "Welcome"                       print(rv)
#       ==============================       --------------------------------
#  SymbolTable / dict Table
# ----------------------------
#  __main__.app_name | web2.0                   app.app_name | web.20
#  ----------------------------                -------------------------
#  __main__.app_port | 4040                    __main__.rv   | ....
#
# 4. Copy the external symbols to __init__.py 
#  from <module> import <member>
#  ----
# from app import app_name
# print(app_name) # web2.0 
#
# from  Project.Sub1.Sub2.Sub3.app104  import  display,select,myvar 
# 
# display() # OK
#
# file: html_template_code.py
#       ------------------------

# import html_template_code
# html_template_code.header() 
# html_template_code.title()
# 
# Vs
# import html_template_code as ht
# ht.header() # OK
# ht.title()  # OK