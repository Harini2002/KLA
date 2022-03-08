import yaml
from yaml.loader import SafeLoader
with open('Milestone1A.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)

list_of_keys={}
for i in data:
        if type(data[i])=="<class 'dict'>":
            list_of_keys[i]=1
            list_of_keys[values(data[i])]=1
print(list_of_keys)





def values(d):
    for j in d:
        if type(d[j])=="<class 'dict'>":
            values(d)
            return( d[j])








