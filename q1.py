
#4. Finding the Tallest Student: Given the heights of all students in a class, describe how you would determine the student with the highest height.
heigts=["150cm","157cm","130cm","120cm","110cm"]

if heigts[0]<heigts[1]:  #using index comparing all element in the list
    print(heigts[1])
elif heigts[1]<heigts[2]:
    print(heigts[1])
elif heigts[2]<heigts[3]:
    print(heigts[2])
elif heigts[3]<heigts[4]:
    print(heigts[3])
elif heigts[4]<heigts[0]:
    print(heigts[0])
else:
    print("minimum value ")

heigts=["150cm","157cm","130cm","120cm","110cm"]#using max function to find largest number
heights_large=max(heigts)
print(heights_large)