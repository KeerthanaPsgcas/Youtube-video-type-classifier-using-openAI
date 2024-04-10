import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')
# openai.api_key = os.getenv('OPENAI_API_KEY')
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI')
openai.api_key = os.getenv('OPENAI_API_KEY')


# prompt=query.get_reports(report_id, format = True, include_conclusion =True, only_conclusion = False)
def gpt_turbo(prompt):
    return openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {'role'  : 'user', 
                'content':  prompt}
            ],
            temperature = 0.2
            )

def gpt(prompt, model):
    print(prompt)
    return openai.Completion.create(
            model = model,
            messages = [
                {'role'  : 'user', 
                'content':  prompt}
            ],
            temperature = 0.2
            )
