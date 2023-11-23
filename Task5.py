#Task1:Calculate the total number of vowels and count of each vowels in "Guvi Greeks Privated Limited"
#Get the input
print("Program for total number of vowels and count of each vowels")
x = "Guvi Greeks Private Limited"
print ("The given text is: ",x)
#initialize the variable
count = 0
#keep string in lowercase
x = x.lower()
#using for loop check the vowels in the given string
for i in x:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        #if True
        count+=1
    #check if any vowel found
if count == 0:
    print('No vowels found')
else:
    print('Total number of vowels in above text is :' + str(count))
#to count the individual vowels     
c = x.count('a')
print('Count of a in above text is :', c)

c = x.count('e')
print('Count of e in above text is :', c)

c = x.count('i')
print('Count of i in above text is :', c)

c = x.count('o')
print('Count of o in above text is :', c)

c = x.count('u')
print('Count of u in above text is :', c)

print("\r")


#Task2: Create a number of pyramids from 1 to 20 using for loop
print("Program for Pyramid of numbers:")
n = int (21)
for p in range(0, n):
        for q in range(0, p+1):
         
            # printing 1 to 20
            print(p,end="")
        # ending line after each row
        print("\r")
print("\r")

#Task3: Take a string and return a new string by removing the vowels
print("Program for removal of vowels in a given link:")

stirng_a= input("Enter the input value: ")
print("Before removing the vowels in the word is: " , stirng_a)
result = str()
#remove vowels in the given string
for i in stirng_a:
    #check condition if alphabet belong to group of vowels
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        pass
    else:
        result = result + i
#check for if the result is not null
if len(result) == 0:
    print('No vowel found in ' + x)
else:
    print('After removing vowels in the word is: ' + result)

print("\r")

#Task4: Takes a string ans return unique charecters in the sring
print("Program for unique charecters in given string:")
#to find the quique value use set() function
uniquevalue=set(stirng_a)
#to print the length use len() function
print("Number of unique charecters in the given string: ", len(uniquevalue))
print("\r")

#Task5: Takes a string and returns True if it is palindrome, False otherwise
print("Program to check given string is palindrome or not")
string_b=input("Enter the value: ")
#to reverse the given string
reverse=string_b[::-1]
if reverse == string_b :
   print("Is it palindrome: TRUE")
else:
   print("Is it palindrome: FALSE")
print("\r")

#Task6: Takes two string and returns the longest string between them
#Task9: Takes a string and returns the total number of letters in the given string
print("Program for longest word between two words and the total number of letters in the given word")
word_1 = input("Enter word one:")
word_2 = input("Enter word two:")
#using if condition print longest word
if len(word_1) == len(word_2):
   print("Both the word has the word lenght")
   print("Length of this string is: ", len(word_2))
elif len(word_1)<len(word_2):
   print ("The longest word is second word and the value is: ", word_2)
   print("Length of this string is: ", len(word_2))
else:
   print ("The longest word is first word and the value is: ", word_1)
   print("Length of this string is: ", len(word_1))
print("\r")

#Task7: Takes a string and returns the most frequent charecter in the given string
print("Program to print most frequent charecter in the given string:")
enter_string_value = input("Enter the word: ")
print ("The original string is : " + enter_string_value)
# initialize a dictionary
freq = {} 
# counting frequency of each character
for char in enter_string_value:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
# finding the character with maximum frequency
max_char = max(freq, key=freq.get)
# printing result
print("The most frequent charecter in the given string is : " + str(max_char))
print("\r")

#Task8: Take a string and return TRUE if it is an anagram of another string, FALSE otherwise
print("Program to check the anagram")
word_x = input("Enter the first word: ")
word_y = input("Enter the second word: ")
#Sort Elements
x = [word_x[i] for i in range(0,len(word_x))]
x.sort()
y = [word_y[i] for i in range(0,len(word_y))]
y.sort()
# the sorted strings are checked
if (x == y):
    print("Is the given string anagrams: TRUE")
else: 
    print("Is the given string anagrams: FALSE")
print("\r")
 
