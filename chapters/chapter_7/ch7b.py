#!/usr/bin/python3

#7-8 deli
sandwich_orders = ['ham', 'chicken', 'brocoli']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	
	print("making you a " + sandwich.title() + " sandwich")
	finished_sandwiches.append(sandwich)
print("\n")

print("following sandwiches have been made")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())
	
	
