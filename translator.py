import urllib.request
import urllib.parse
import json

text = input("Enter English text: ")
print("Translating to Urdu... Please wait")

# Make URL safe
encoded_text = urllib.parse.quote(text)
url = f"https://api.mymemory.translated.net/get?q={encoded_text}&langpair=en|ur"

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        translated = data['responseData']['translatedText']
        print("Translated:", translated)
except Exception as e:
    print("Error:", e)
    print("Check your internet is ON")
