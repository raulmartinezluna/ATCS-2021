#Wikipedia has a list of the tallest mountains in the world, with each mountain's elevation. Pick five mountains from this list.
    #Create a dictionary with the mountain names as keys, and the elevations as values.

mountain_names = {
        'Mount Everest': '8,848.86',
        'K2': '8,611',
        'Kangchenjunga': '8,586',
        'Lhotse': '8,516',
        'Makalu': '8,485',
    }

    #Print out just the mountains' names, by looping through the keys of your dictionary.
print("\nPrints out just the mountains' names")
for mountain_name in mountain_names:
    print(mountain_name)

    #Print out just the mountains' elevations, by looping through the values of your dictionary.
print("\nPrints out just the mountains' elevations")
for mountain_name in mountain_names:
    print(mountain_names[mountain_name])

    #Print out a series of statements telling how tall each mountain is: "Everest is 8848 meters tall."
print("\nPrint out a series of statements telling how tall each mountain is: 'Everest is 8848 meters tall.'")
for mountain_name in mountain_names:
    print(mountain_name+" is "+mountain_names[mountain_name]+" meters tall.")

#Revise your output, if necessary.
    #Make sure there is an introductory sentence describing the output for each loop you write.
    #Make sure there is a blank line between each group of statements.

