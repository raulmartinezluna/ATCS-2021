#Find a calculation whose result depends on the order of operations.

#Print the result of this calculation using the standard order of operations.
calculation_1 = 3*21+5/2
print("Without Parenthesis: ", str(calculation_1))

#Use parentheses to force a nonstandard order of operations. Print the result of this calculation.
calculation_2 = 3*(21+5)/2
print("With Parenthesis: ", str(calculation_2))