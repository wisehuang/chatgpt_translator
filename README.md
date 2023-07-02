# Chinese Translator

This script uses the OpenAI API to translate English text to traditional Chinese using the ChatGPT model. It reads an input text file named `article.txt`, splits the text into sentences, and translates each sentence to Chinese using the API. The translated text is then written to an output file named `translated_result.txt`.

## Usage

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Set your OpenAI API key by replacing `<<YOUR API KEY>>` with your actual API key on line 5 of `chinese_translator.py`.
3. Create an input text file named `article.txt` in the same directory as `chinese_translator.py`.
4. Run the script by running `python chinese_translator.py`.
5. The translated text will be written to an output file named `translated_result.txt` in the same directory as `chinese_translator.py`.
