#Store the first ten letters of the alphabet in a list.

firstTenAlpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#Use a slice to print out the first three letters of the alphabet.
slice_1 = slice(3)
print(firstTenAlpha[slice_1])

#Use a slice to print out any three letters from the middle of your list.
slice_2 = slice(3, 6)
print(firstTenAlpha[slice_2])

#Use a slice to print out the letters from any point in the middle of your list, to the end.
slice_3 = slice(4,7)
print(firstTenAlpha[slice_3])