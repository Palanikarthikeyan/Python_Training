hosts={} # empty dict
print(f"Total no.of items:{len(hosts)}")
count = 0
while(count < 5):
    K = input('Enter host-Alias name:(ex: host01)')
    V = input(f'Enter {K} IPAddress:') 
    hosts[K] = V # adding new data to an existing dict
    count = count + 1

print(f"Total no.of items:{len(hosts)}")
for var in hosts:
    print(f'{var} - {hosts[var]}')