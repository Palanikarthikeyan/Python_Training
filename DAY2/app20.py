"""The list.pop() method removes and returns an item from a list.

With no index, it removes the last item. You can provide an index to remove
that specific item.
"""

tasks = ["email", "meeting", "report"]
completed_task = tasks.pop()  # Removes and returns "report"

print(completed_task)
print(tasks)
done_list = tasks.pop(1)
print(done_list)
print("Updated tasks:",tasks)
#####
prod_list = ['pA','pB','pC','pD','pE','pF']

if 'pB' in prod_list:
    print(f'Yes pB is exists at {prod_list.index("pB")} index')
else:
    print("Sorry given product is not exists") 