import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Note that we can set different env variables to different OPENAI keys and just map the right one to openai.api_key here
# Example: have both OPENAI_API_KEY (for OpenAI) and AOAI_API_KEY (for Azure OpenAI) as options 
# openai.api_key  = os.getenv('OPENAI_API_KEY')



client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# dotenv.load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY") 

# enable below if you use Azure Open AI
# openai.api_type = 'azure' 
# openai.api_version = '2023-05-15'
# openai.api_base = os.getenv("API_BASE")

# add your completion code
prompt = "Complete the following: Once upon a time there was a"

# engine
engine = "davinci-002"

# deployment_id, azure specific
deployment_name = os.getenv("DEPLOYMENT_NAME")

completion = client.completions.create(model=engine, prompt=prompt, max_tokens=100)

# print response
print(completion.choices[0].text)


#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.

