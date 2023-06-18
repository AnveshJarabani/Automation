import json,os
from rich import print
cur_dir=os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
with open(os.path.join(cur_dir,'job_data.json'),'r') as f:
    data = json.load(f)
data['Form Data']=[i for i in data['Form Data'] if i is not None]
for i in data['Form Data']:
    for j in i:
        y=j.split('\n')
        for string in y:
            # if 'authorization' in string:
            #     indx=y.index(string)
            #     print(y[indx+2])
            # if 'visa' in string:
            #     indx=y.index(string)
            #     print(y[indx])
            if 'c2c' in string.lower():
                indx=y.index(string)
                print(y[indx])
# for i in data['Desc']:
#         print(i)