'''
Write a python program
create an empty list
-> display no.of items from given list => 0
-> use while loop - limit is 5
->    - read a hostname from <STDIN>
->    - push input hostname to an existing list
#  using for loop - display list of items
'''
hosts = [] # empty list
print(f'No of items:{len(hosts)}')

count = 0
while count < 5:
    hostname = input("Enter a hostname: ").strip()
    hosts.append(hostname)
    count += 1

print(f"\nNo. of items: {len(hosts)}")

for hostname in hosts:
    print(f"Host name: {hostname}")

print("End of the line")