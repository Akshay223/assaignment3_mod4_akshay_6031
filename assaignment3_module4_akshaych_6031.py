#!/usr/bin/env python
# coding: utf-8

# In[1]:


#appendlist
f = open('sample1.txt', 'a')
myStr = input("Enter text to append to file: ")
f.write(myStr)
print("File contents: ")
f.close()
rf = open('sample1.txt', 'r')
print(rf.read())
rf.close()


# In[3]:


#clonelist
f = open('sample1.txt', 'r')
f1 = open('sample2.txt', 'w')

f1.write(f.read())
f.close()
f1.close()


# In[ ]:


#countline
n = len(open('sample1.txt').readlines())
print("No. of lines: ", n)


# In[ ]:


#filesize
fileSize = os.path.getsize('sample1.txt')
print("File size in bytes of a plain file: ", fileSize, "bytes")


# In[ ]:


#filetolist
n = len(open('sample1.txt').readlines())
f = open('sample1.txt', 'r')
fList = [next(f) for x in range(n)]
print(fList)
f.close()


# In[ ]:


#firstnline
n = int(input("Enter value of n: "))
f = open('sample1.txt','r')
for x in range(n):
    print(next(f))
f.close()


# In[ ]:


Python is an interpreted, high-level,
general-purpose programming language.
Created by Guido van Rossum and first released in 1991,
Python's design philosophy emphasizes code readability-
with its notable use of significant whitespace.

