#5. Palindrome Check: Describe how you would determine if a given string is a palindrome.
a=input("enter te word")
if a==a[::-1]:   #using slicing to check given string is palindrome
    print("given word is palindrome")
else:
    print("given word not a palindrome")

name=["m","o","o","n"]

if ((name[0])==(name[3])):#usig indexing to compare each letter
    print("give string is palindrome")
elif (name[1])==(name[2]):
    print("given string is palindrome")
else:
    print("string is not a palindrome")



  