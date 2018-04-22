
# coding: utf-8

# In[156]:

#将http://cnn.csail.mit.edu/上下载的数据处理为其模型训练需要的格式
import os


# In[157]:

validnum = 1000
with open('train.data','r') as trainfile, open('valid.data','w') as validfile:
    for i in range(validnum):
        line = trainfile.readline()
        validfile.writelines(line)
    #validfile.seek(0)
    #print(validfile.readlines())
        
    


# In[158]:

with open('train.data','r') as trainfile:
    lines = trainfile.readlines()[validnum:]
with open('train.data','w') as trainfile:
    for i in lines :
        trainfile.write(i)
    #f.seek(0)
    #print(f.readlines())
    


# In[159]:

with open('test.data', 'r') as datafile:
    label = []
    for x in datafile:
        label.append(x.strip().split()[2])

with open('test.target', 'w') as targetfile:
    for x in label:
        targetfile.write(x + '\n')


# In[160]:

with open('train.data', 'r') as datafile:
    label = []
    for x in datafile:
        label.append(x.strip().split()[2])

with open('train.target', 'w') as targetfile:
    for x in label:
        targetfile.write(x + '\n')


# In[161]:

with open('valid.data', 'r') as datafile:
    label = []
    for x in datafile:
        label.append(x.strip().split()[2])

with open('valid.target', 'w') as targetfile:
    for x in label:
        targetfile.write(x + '\n')


# In[ ]:




# In[ ]:



