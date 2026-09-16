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
    from extract_email import extract_email_text
    
    text1 = extract_email_text("../test_files/sample1.eml")
    print("Sample 1:", classify_email(text1))
    
    text2 = extract_email_text("../test_files/sample2.eml")
    print("Sample 2:", classify_email(text2))