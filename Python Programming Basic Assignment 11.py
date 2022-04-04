#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python program to find words which are greater than given length k?


def word(k, s):    
    word = s.split(" ")
    for x in word:
        if len(x)>k:
            print(x)
k=5
s ="Python is very good language"
word(k, s)


# In[4]:


# 2.	Write a Python program for removing i-th character from a string?

def remove(string, i): 
    a = string[ : i] 
    b = string[i + 1: ]
    return a + b
if __name__ == '__main__':
      
    string = "titFORtat"
    i = 5
    print(remove(string, i))


# In[2]:


# 3.	Write a Python program to split and join a string?
def split_string(string):
    list_string = string.split(' ')
      
    return list_string
def join_string(list_string):
    string = '-'.join(list_string)
      
    return string
if __name__ == '__main__':
    string = 'tit for tat'
    list_string = split_string(string)
    print(list_string)
    new_string = join_string(list_string)
    print(new_string)


# In[15]:


# 4.	Write a Python to check if a given string is binary string or not?

def check(string) :
    p = set(string)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else :
        print("No")
string = "101010000111"
check(string)


# In[12]:


# 5.	Write a Python program to find uncommon words from two Strings?

def UncommonWords(A, B):
  
    count = {}

    for word in A.split():
        count[word] = count.get(word, 0) + 1
  
    for word in B.split():
        count[word] = count.get(word, 0) + 1
  
    return [word for word in count if count[word] == 1]
  
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A, B))


# In[61]:


# 6.	Write a Python to find all duplicate characters in string?

string = "tutorialspoint"
duplicates = []
for char in string:
     if string.count(char) > 1:
      if char not in duplicates:
                duplicates.append(char)
print(duplicates)


# In[62]:


# 7.	Write a Python Program to check if a string contains any special character?

import re
def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    
    if(regex.search(string) == None):
        print("String is accepted")
         
    else:
        print("String is not accepted.")
if __name__ == '__main__' :
    string = "Geeks$For$Geeks"
    run(string)


# In[ ]:




