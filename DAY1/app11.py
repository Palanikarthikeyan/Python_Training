# Conditional statement - Code block will execute only one time
#  Vs
# Looping statement - Code block will execute multiple times
# 
# Conditional statement - if, if-else, if-elif-else
# Looping statement - for, while
#                     ===  =====
#
# for loop - executes a code block for a fixed number of times

# while loop - executes a code block for an unknown number of times
#                                        ---------------------------
# Rule1: Initialization 
# Rule2: Condition
# Rule3: Increment/Decrement

# Demonstration of while loop
# while loop executes a code block as long as the condition is true

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("Loop finished")

while(False):
    print("This will not be printed")

# break ; continue  - looping keywords
#
# Task:
# -------
# Write a python program:
# initialize a pin number (pin = 1234)
# use while loop
#      -> read a pin number from <STDIN>
#      -> check if the pin number is correct or not
#      -> display Success if the pin number is correct - <count>
# -> maximum 3 attempts are allowed 
# ===================================
# if all 3 inputs are failed - pin is blocked
# ==============================================

pin = 1234
attempts = 0
while attempts < 3:
    u = int(input("Enter pin number: "))
    if u == pin: print(f"Success! Pin is correct. Attempts: {attempts + 1}"); break
    print("Incorrect pin. Try again.")
    attempts += 1
if attempts == 3 and u != pin:
    print("Pin is blocked after 3 failed attempts.")