#*******************************
#
#assignment file Aug 30 2024
#
#by Russel Roberts
#
#git hub repository https://github.com/russelroberts/SOP
#*************************
str = "The quick brown fox jumps over the lazy dog"

#a. print the string to the page
print(str)

#b.Print the length of the string to the page
print("The length of the string is : ", len(str))

#c. Print the string in all uppercase letters
print(str.upper())

#d.Print the string in all lowercase letters
print(str.lower())

#e.Print the string in title case
print(str.title())

#f.Print the string in reverse
print(str[::-1])

#g. Print the string in reverse title case
print(str.title()[::-1])

#h. Count the number f times the letter "a" appears in the string
print(str.count('a'))

#i.Count the number of times the word "the" appears in the string
print(str.count("the"))
#or if we need case insensitivity ?
print(str.lower().count("the"))

#J. replace the word "the" with the word "a"
print(str.replace("the","a"))
#case insensitivity..?
print(str.lower().replace("the","a"))


#4 freq of each letter in str

#reset str so we are working with original
str = "The quick brown fox jumps over the lazy dog"

# uncomment below if case sensitivity of characters needs to be ignored
# str = str.lower()

letter_freq = dict()
for strpos in range(len(str)):
    # next two lines are just for my testing, can be commented out for increased efficiency
    print("Current Char :", str[strpos])
    print("fequency of char :",str.count(str[strpos]))

    #store in dictionary, we don't need to check if exists as no duplication
    letter_freq[str[strpos]] = str.count(str[strpos])
else:
    print("all done")
    print(letter_freq)
    
#**********************************************************
#5.interpolate list into long string
people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for cnt in range(len(people)):
    print(people[cnt],'the' ,sex[cnt],'is',age[cnt])
#********************************************************