import time

pin_history = [] # Empty list
correct_pin = 1234
attempts = 0

while attempts < 3:
    pin = input("Enter your PIN: ")
    attempts += 1
    if pin.isdigit() and int(pin) == correct_pin:
        pin_history.append(f'PIN accepted - {attempts} - entry time:{time.ctime()}')
        print(f"PIN accepted - {attempts}")
        break
    print("Incorrect PIN")
    pin_history.append(f'User input  pin:{pin} is not valid - {time.ctime()}')
else:
    pin_history.append(f'pin is blocked - {time.ctime()}')
    print("pin is blocked")

show_history = input("Would you like to view pin history? (Yes/No): ")
if show_history in ("Yes", "YES"):
    for entry in pin_history:
        print(entry)

