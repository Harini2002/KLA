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
                       value(v,fn)
                   if 'Inputs' in v:
                       input_values=v['Inputs']
                       exc_delay=input_values['ExecutionTime']
                       time.sleep(int(exc_delay))
                       filename=input_values['FunctionInput']
                       logger.info('%s. %s Entry', fn,k)
                       logger.info('%s. %s Executing DataLoad (%s)',fn, k,filename)
                       logger.info('Exit')



logging.basicConfig(filename="output.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
with open('Milestone1A.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
imp=""
for i in data:
    imp=imp+i
    logger.info('%s Entry',imp)
    value(data[i],imp)
logger.info('%s Exit',imp)










