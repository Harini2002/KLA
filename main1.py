import yaml
from yaml.loader import SafeLoader

import time
import logging
def conc(d,arr):
     for i in d:
         if type(d[i]) is dict:
             if d[i] != 'Activities':
                 for k, v in d[i].items():
                     entry(k,v,arr)
                     exit(v,arr)

threading.Thread(target=entry).start()
threading.Thread(target=exit).start()
def entry(k,v,arr):
    if type(v) is dict and v != 'Inputs':
        arr.append(k)
        str = ".".join(arr)
        logger.info(';%s Entry', str)
        arr.pop()
        value(v, arr)

def exit(v,arr):
    if 'Inputs' in v:
        input_values = v['Inputs']
        exc_delay = input_values['ExecutionTime']
        filename = input_values['FunctionInput']
        time.sleep(int(exc_delay))
        arr.pop()
        logger.info(';%s Executing TimeFunction (%s,%s)', str, filename, exc_delay)
        logger.info(';%s Exit', str)


def value(d,arr):
    for i in d:
        if type(d[i]) is dict:

            if d[i]!= 'Activities':
                for k,v in d[i].items():
                   if k=='Execution' and v=='Concurrent':
                       conc(d[i],arr)
                   if type(v) is dict and  v!='Inputs':
                       arr.append(k)
                       str = ".".join(arr)

                       logger.info(';%s Entry', str)
                       value(v,fn)

                   if 'Inputs' in v:
                       input_values=v['Inputs']
                       exc_delay=input_values['ExecutionTime']


                       filename=input_values['FunctionInput']

                       time.sleep(int(exc_delay))
                       logger.info(';%s Executing TimeFunction (%s,%s)',str,filename,exc_delay)
                       logger.info(';%s Exit',str)
                       arr.pop()



logging.basicConfig(filename="output2.log",
                    format='%(asctime)s.000000%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
with open('Milestone1B.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)

arr=[]
for i in data:
    logger.info(';%s Entry',i)
    arr.append(i)
    value(data[i],arr)

while len(arr)>0:
    str = ".".join(arr)
    logger.info(';%s Exit',str)
    arr.pop()



