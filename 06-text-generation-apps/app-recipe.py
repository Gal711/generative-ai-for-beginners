from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo-instruct"

no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}: "

completion = client.completions.create(model=model, prompt=prompt, max_tokens=600, temperature=0.1)

# print response
print("Recipes:")
print(completion.choices[0].text)

old_prompt_result = completion.choices[0].text
prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "

new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
completion = client.completions.create(model=model, prompt=new_prompt, max_tokens=600)

# print response
print("\n=====Shopping list ======= \n")
print(completion.choices[0].text)

