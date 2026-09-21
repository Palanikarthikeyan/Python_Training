import urllib.request

# Demonstrate a GET request using the Python standard library
with urllib.request.urlopen('https://www.google.com') as response:
    status_code = response.getcode()
    headers = dict(response.headers.items())
    response_text = response.read().decode('utf-8', errors='replace')

print('Status Code:', status_code)
print('Headers:')
print(headers)
print('Response Text (first 200 characters):')
print(response_text[:200])

