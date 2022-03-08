import yaml
from yaml.loader import SafeLoader

import time
import logging

def value(d,imp):
    for i in d:
        if type(d[i]) is dict:
            if d[i]!= 'Activities':
                for k,v in d[i].items():
                    if 'Inputs' in v:
                       input_values=v['Inputs']
                       exc_delay=input_values['ExecutionTime']
                       time.sleep(int(exc_delay))
                       input_file=input_values['FunctionInput']
                    logger.info('imp. %s Entry', k)
                    logger.info('imp. %s Executing DataLoad(%s)', k,input_file)
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










