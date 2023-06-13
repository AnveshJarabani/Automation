import json,re
import pandas as pd
from collections import Counter
import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
path = r"C:\Users\ajarabani\Downloads\job automation\{}"
data_dict=json.load(open(path.format('data_eng_job_source_data.json'),'r'))
# df_lst=[pd.DataFrame(i,index=[0]) for i in data_dict]
df=pd.DataFrame(data_dict)
patrn=re.compile(r"\b\w+\b")
nltk.download('stopwords')
stop_words=set(stopwords.words('english'))
filterd_phrases=[]
for i in df['Desc']:
    words=patrn.findall(i.lower())
    filterd_words=[wrd for wrd in words if wrd not in stop_words]
    phrases=list(ngrams(filterd_words,2)) # generate 2 word phrases
    filterd_phrases.extend(phrases)
phrase_frequencies=Counter(filterd_phrases)
keywords={'word':[i for i,_ in phrase_frequencies.items()],
          'freq':[i for _,i in phrase_frequencies.items()]}
df_phrases=pd.DataFrame(keywords)
df_phrases=df_phrases.sort_values(by='freq',ascending=False,ignore_index=True)
print(df_phrases.head(100))
# df_phrases.to_csv(path.format('key_phrases.csv'),index=False)
"""
1. FIND THE TOP 25 KEYWORDS WITH THE FREQUENCY FROM Desc
2. EXTRACT COMPANY NAMES, LOCATION, SALARY RANGE. 
3. DOES IT HAVE EASY APPLY ON THEM. 
"""

