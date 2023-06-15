import json
path = r'C:\Users\ajarabani\Downloads\job automation\{}'
with open(path.format('job_data.json')) as f:
    data = json.load(f)
for i in data['Form Data']:
    for j in i:
        y=j.split('\n')
        for string in y:
            if 'authorization' in string:
                indx=y.index(string)
                print(y[indx+2])
            if 'visa' in string:
                indx=y.index(string)
                print(y[indx])
            if 'City' in string:
                indx=y.index(string)
                print(y[indx])
            


