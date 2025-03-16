
#2. Top N Frequent Words from a File: Describe how you would read a text file and return the top N most frequent words along with their counts.

with open("/home/aruna/Documents/fruits.txt","r") as file: #read the textfile
    details=file.read()
    print(details)
    

#removing special charecters 
special_char=",.@#$%^&"  
for char in special_char:
   if char in details:
      details=details.replace(char, '')
      
#split each word in text file
word_split=details.split()``
print(word_split)


#using dictionary to count no of words

word_count={}

for word in word_split:
    if word in word_count:
        word_count[word]=word_count[word]+1
    else:
        word_count[word]=1

for key,value in word_count.items():
    print(f"{key}  count is  {value}")
    
