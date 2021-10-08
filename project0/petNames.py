#Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.
    #For example, 'ziggy': 'canary'
#Put at least 3 key-value pairs in your dictionary.

animal_names = {
    'ziggy': 'Dog',
    'canary': 'Bird',
    'danny': 'Turtle'
}

#Use a for loop to print out a series of statements such as "Willie is a dog."
for animal in animal_names:
    print(animal+" is a "+animal_names[animal].lower())