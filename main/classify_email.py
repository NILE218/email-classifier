import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_email(text):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": f"Classify this email as either 'Important' or 'Normal'. Only respond with one word.\n\nEmail:\n{text}"
            }
        ]
    )
    result = response.choices[0].message.content.strip()
    return result

# Test it
if __name__ == "__main__":
    sample_text = "This is a reminder that we have a meeting scheduled for tomorrow."
    result = classify_email(sample_text)
    print(result)