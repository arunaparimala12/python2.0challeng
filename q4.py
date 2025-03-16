#7. First Non-Repeating Character in a String: Describe how you would find the first non-repeating character in a given string.

def non_repeat_letters(string):
    letter_count={}
    for  val in string:
        letter_count[val]=letter_count.get(val,0)+1  #count no of occurance in each charecter

    for val in string:
        if letter_count[val]==1:
            return val
    return None
input_string="aruna"
result=non_repeat_letters(input_string)
print("non repeating leters:",result)