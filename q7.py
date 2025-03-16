#2. Missing Number in a Sequence: Given an array containing (n-1) unique numbers from the range 1 to n, 
# describe how you would find the missing number.
numbers=[1,2,3,4,5,7]
n=7

#finding sum of natural numbers
sum_numbers=(n*(n+1))//2
print(sum_numbers)

#finding sum of given numbers
total_sum=sum(numbers)
print(total_sum)

#find missing number
missing_number =sum_numbers-total_sum
print(missing_number)