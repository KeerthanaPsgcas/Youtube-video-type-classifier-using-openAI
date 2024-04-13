from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
import time
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



prompt="""
Consider yourself as expert in english , provided with the youtube title ,predict what the video is about.
Note:the output should have only 3 to 6 words. In output,the word "answer" should not be present.
Question 1:
t:"PM Modi addresses a public meeting in Chandrapur, Maharashtra"
Answer 1: 
PM Modi public meeting - Maharashtra

Question 2:
t:"Teachers must listen to this message of PM Modi…(Kashmiri)"
Answer 2: 
PM Modi about teachers - Kashmiri

Question 3:
t:"PM Modi at the 'Friends of India' event at Russia"
Answer 3: 
Foreign visit - Russia

Question 4:
t:"PM Narendra Modi's 69th Independence Day Speech from Red Fort"
Answer 4: 
PM Modi Independence day speech

Question 5:
t:"PM Narendra Modi's Mann Ki Baat LIVE: 107th Episode with the Nation"
Answer 5: 
PM Modi Mann Ki Baat


now find the same for the following titles:       
		 Question: 
                                       t:
										{0}

                Answer: 

"""
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text
final=[]

df = pd.read_csv('test.csv')
df.insert(3, 'category', '')

for i,j in df.iterrows():
    try:
        print(i)
        t = j['Title']
        question = prompt.format(t)   # Use the title as the question
        response = get_gemini_response(question, prompt)
        res = response
        df.at[i, 'category'] = res
        print(res)
        time.sleep(1)
    except Exception as e:
        print(e)
df.to_csv('updated_categ.csv', index=False)
