# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'azcbobobegghakl'
validstr = ['a', 'e', 'i', 'o', 'u']

count = 0
for char in s:
    if char in validstr:
        count +=1
print(f'Number of vowels: {count}')

#%%
#Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'azcbobobegbobghakl'
count = 0
for i in range(0,len(s)):
    if s[i:i+3] == 'bob':
        count +=1
print(f'Number of times bob occurs is: {count}')

#%%
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

mydict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

s = 'abcbcd'
sub = s[0]
long, length = sub, 1
for i in s[1:]:
    if ord(sub[-1]) <= ord(i):
        sub += i
        if len(sub) > length:
            length = len(sub)
            long = sub
    else:
        sub = i
print(long)

