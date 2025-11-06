#!/usr/bin/env python
# coding: utf-8

# In[42]:


n=int(input("Enter the number for star pattern: "))
for i in range(1,n+1):
    for j in range(i,n):
        print(' ',end=" ")
    for k in range(1,2*i):
            print('*',end=" ")
    print()


# In[ ]:





# In[ ]:




