#6. Second Largest Number in an Array: Describe how you would find the second largest number in an array.
numbers=[30,50,35,65,90,45]

numbers.sort() #sorting the given numbers
print(numbers)

#finding second largest number
print("second largest number",numbers[-2]) 
