from utils import templates as templateUtils
from utils import openai as openaiUtils
import pandas as pd
import time
from openai.error import RateLimitError
final=[]

df = pd.read_csv('test.csv')
df.insert(3, 'category', '')

for i,j in df.iterrows():
    try:
        print(i)
        t = j['Title']
        response = openaiUtils.gpt_turbo(templateUtils.classifier.format(t))
        res = response.choices[0].message.content.replace("\n", "").replace("  ", "").replace("'", "")
        df.at[i, 'category'] = res
        print(res)
        time.sleep(30)
    except RateLimitError as e:
        print(e)
df.to_csv('updated_categ.csv', index=False)