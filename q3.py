#1. FLAMES Game Design: Describe how you would design the FLAMES game.
name1={"p","e","r","i","n","b","a"}
name2={"r","a","j","i"}


difference_letters=name1.symmetric_difference(name2) #finding non common letters
print(difference_letters)
print(len(difference_letters))

total_letters=len(name1)+len(name2)
print(total_letters)

flames=["friends","love","affection","marriage","enemy","sister"]
i=0
while len(flames)>1: #finding relation between two names
  i=(i+len(difference_letters)-1)%len(flames)
  flames.pop(i)
  

print("welcome to flames game")
print("relation between two member is",flames)










    
    