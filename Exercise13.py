# Aim: To count and display the number of vowels, consonants, uppercase, lowercase characters in string.

str1= input("Enter the string : ")
str2=str1.lower()
vowels = 0
consonants = 0
lowercase= 0
uppercase = 0

for i in range(0, len(str2)):
    if(str2[i] == 'a') or (str2[i] == 'e') or (str2[i] == 'i') or (str2[i] == 'o') or (str2[i] == 'u'):
        vowels = vowels + 1
    elif((str2[i] >= 'a') and (str2[i] <= 'z')):
        consonants = consonants + 1
for x in range(0,len(str1)):
    if( str1[x]>='a') and (str1[x]<='z'):
        lowercase = lowercase + 1
    elif(str1[x]>='A') and (str1[x]<='Z'):
        uppercase = uppercase + 1

print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Lowercase: ", lowercase)
print("Uppercase: ", uppercase)

"""
Output:

Enter the string : This is a string in PyThOn
Vowels:  6
Consonants:  15
Lowercase:  17
Uppercase:  4

"""