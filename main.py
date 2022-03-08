import yaml
from yaml.loader import SafeLoader

import time
import logging

def value(d,fn):
    for i in d:
        if type(d[i]) is dict:
            if d[i]!= 'Activities':
                for k,v in d[i].items():

                   if type(v) is dict and  v!='Inputs':
                       arr.append(k)
                       value(v,fn)
                   if 'Inputs' in v:
                       input_values=v['Inputs']
                       exc_delay=input_values['ExecutionTime']
                       time.sleep(int(exc_delay))
                       filename=input_values['FunctionInput']
                       str = ".".join(arr)
                       logger.info('%s Entry',str)
                       logger.info('%s Executing DataLoad (%s)',str,filename)
                       logger.info('%s Exit',str)
                       arr.pop()



logging.basicConfig(filename="output2.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
with open('Milestone1B.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)

arr=[]
for i in data:
    logger.info('%s Entry',i)
    arr.append(i)
    value(data[i],arr)

logger.info('%s Exit',arr[0])










