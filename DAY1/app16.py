s = 'python'
print(type(s))
print(s[0])
print(s[1])
print(s[-3:]) # last 3 chars
print('') # empty line

var = b'python'
print(type(var))
print(var[0])
print(var[1])
print(var[-3:]) # last 3 chars
print('') # empty line

msg = "This is my payload information about cisco router"
###
payload = msg.encode() 
print(type(payload))
result = payload.decode()
print("result=",result)
#-------------------------------------------
# prompt1: python bytes type 
# bytes is an immutable sequence of integers from 0 to 255. It stores raw
# binary data, such as file contents or network packets.
# Text can be converted to bytes with encode() and converted back with decode().
text = "café"
data = text.encode("utf-8")
print("encoded:", data)
print("first byte:", data[0])       # indexing returns an integer
print("decoded:", data.decode("utf-8"))

# Use bytearray when the binary data needs to be modified.
mutable_data = bytearray(b"abc")
mutable_data[0] = ord("A")
print("bytearray:", mutable_data)

# prompt2: bytes type example
# prompt3: str Vs bytes

