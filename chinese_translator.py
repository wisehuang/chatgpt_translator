import re
import openai
from tqdm import tqdm

openai.api_key = "<<YOUR API KEY>>"

# Define a function to translate a string to traditional Chinese using ChatGPT
def translate_to_chinese(text):
    # Use the OpenAI API to generate a translation
    
    messages=[{"role": "user", "content": "Translate the following text to zh-tw: " + text }]

    response = openai.ChatCompletion.create(
    model="gpt-4",
    max_tokens=4096,
    temperature=1,
    messages = messages)
        
    # Extract the translated text from the API response
    translation = response.choices[0].message.content.strip()

    # Remove any newline characters from the translation
    translation = re.sub(r'\n', '', translation)

    return translation

# Open the text file and read its contents
with open('article.txt', 'r') as file:
    article = file.read()

# Trim the article by removing leading and trailing whitespace from each line
trimmed_article = [line.strip() for line in article.split('\n')]

# Remove newlines from the trimmed article
trimmed_article = ''.join(trimmed_article)

# Remove tab spaces from the trimmed article
trimmed_article = trimmed_article.replace('\t', '')

# Split the article into sentences using regular expressions
sentences = re.split(r'(?<=\.)\s+', trimmed_article)

# Initialize variables for the output strings
output_strings = []
current_string = ''

# Loop through the sentences and add them to the output strings
for sentence in sentences:
    # If adding the current sentence would make the current string too long, add it to the output strings and start a new string
    if len(current_string + ' ' + sentence) > 15000:
        output_strings.append(current_string)
        current_string = ''
    # Add the current sentence to the current string
    current_string += ' ' + sentence

# Add the final string to the output strings
output_strings.append(current_string)

# Translate each output string to traditional Chinese using ChatGPT
chinese_strings = []
for string in tqdm(output_strings, desc='Translating to Chinese'):
    chinese_string = translate_to_chinese(string)    
    chinese_strings.append(chinese_string)

# # Print the translated strings
# for i, string in enumerate(chinese_strings):
#     print(f'String {i+1}: {string} \n')

with open('translated_result.txt', 'w') as f:
    f.write(chinese_strings)