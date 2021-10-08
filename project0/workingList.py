#Make a list that includes four careers, such as 'programmer' and 'truck driver'.

careers = ["programmer", "Roofer", "Truck Driver", "Teacher"]

#Use the list.index() function to find the index of one career in your list.

careers.index("Roofer")

#Use the in function to show that this career is in your list.

"Roofer" in careers

#Use the append() function to add a new career to your list.

careers.append("Scientist")

#Use the insert() function to add a new career at the beginning of the list.

careers.insert(2, "Soldier")

#Use a loop to show all the careers in your list.

for career in careers:
    print(career)