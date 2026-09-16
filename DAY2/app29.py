# str - collection of chars         - immutable
# bytes - collection of ASCII       - immutable
# list - Collection of ordered items   - mutable  <== (A)
# tuple - - Collection of ordered items - immutable
# --------------------------------------//index based
#
# dict - Collection of unorderd item - mutable <== (B)
#        ---------------------------// key:value based 
# 
#   +-----------------------------+
#   |     Key     |     Value     |
#   +-------------|---------------+
#   |     K1      |      Value1   |
#   +-------------|---------------+
#   |     K2      |      Value2   |
#   +-------------|---------------+
#   |     K3      |      Value3   |
#   +-------------|---------------|
#   |     K4      |      10       |
#   +-----------------------------|
#   |     K5      |      10       |
#   +-----------------------------+
#
#  Usecases:
#  -----------
#  large data sets - dict
#  env variable    - dict
#  webprogramming - html form - dict
#  webparsing - dict
#  json - object -> dict
#  lookup table ->dict
#  network device config -> dict
#  property file/conf file -> dict
#  ...
print(type({}))

d={'K1':'V1','K2':10,'K3':3.5,'K4':True,'K5':'data'} # 1D
print(type(d),len(d))
print(d)

# How to get/fetch nth item from given dict
# dictname['key'] -> Value/KeyError 
#           ---           
print(d['K1'])
print(d['K2'])

# how to modify an existing dict - value
# dictname['oldKey'] = UpdatedValue

d['K1'] = 'Data-1'
d['K3'] = 'C:\\Users\\User\\Project1\\net.cfg'

print(d)

# To add new data to an existing dict
# -------------------------------------
# dictName['newKey'] = value <== adding new data
#  Vs
# dictName['oldKey'] = value <== modification
