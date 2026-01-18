# Sample demo from Codecademy

# install the bindings first with `pip install openai`
# import openai module
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

#print(client.models.list())

# replace `API_KEY` with your actual OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# synthetic posts from dark web
dark_web_post = [
"Security flaw discovered in Brocadero software, similar to cve-21001",
"Zero-day exploit for sale - target is android games = $100K US",
"Advanced persistent threat vs critical infrastructure",
"Exchange, Trade Privately. Against Tracking and surveilance.",
"Real-time manual penetration data for acquisition of first-hand online loans by overseas teams",
"Receive download site traffic",
"Integrity buys and sells first-hand data on men and women.",
"High salary looking for 3 to 4 Java architects front end engineer jobs in Thailand",
"A large number of financial investment data in the currency circle of Japan, South Korea, Europe and United States",
"Looking for a hacker that can provide cvv sync fish",
"New glock 19 gen4 price ($10,200), Shipping time is about a month. No refuncs will be accepted after payment",
"Because of their own problems, the mobile phone number is not answered, the goods are not received, and refunds are not",
"If you do not receive the goods or do not meet the requirements can be refunded. Please release the money after receiving",
"Save time for those who really need it, don't bother.",
"Customer-made list, if you need anything else, you can send a private message, don't waste everyone's time thank you.",
"Only connect with the big boss, you can also come if you think you have the strength. Don't waste you time consulting if",
"I finally want to say that cheap people deserve to be deceived... Stop believing those in some groups.. All liars can't",
]

# combine posts into one for submission to GPT model
raw_data = "\n".join(dark_web_post)

# Analyze the raw data to identify potential threats
def analyze_info(data):
    engineered_prompt = "We have collected some security-based posts from the dark web,"
    engineered_prompt += "Please identify and highlight any potential threats discussed,"
    engineered_prompt += "exploits for sale, or potential vulnerabilities that our security team should be aware of."
    engineered_prompt += "Also, highlight any potential cve numbers and threats concerning Brocadero in "
    engineered_prompt += f"these posts and provide a concise report on your finds: \n{data}\n"

    response = client.completions.create(
        model = "gpt-3.5-turbo-instruct",
        # engine="text-davinci-002",
        prompt = engineered_prompt,
        max_tokens = 500,
        n = 1,
        stop = None,
        # output will be relatively random
        temperature = 0.8,
    )
    message = response.choices[0].text.strip()
    return message

threat_intel_analysis = analyze_info(raw_data)

print("Summary of posts on Dark Web: ")
print(threat_intel_analysis)

