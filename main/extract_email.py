import email
from bs4 import BeautifulSoup

def extract_email_text(file_path):
    with open(file_path, 'r') as f:
        msg = email.message_from_file(f)
    
    subject = msg['subject']
    body = ""
    
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload()
    else:
        body = msg.get_payload()
    
    full_text = subject + "\n" + body
    return full_text.strip()

# Test it
if __name__ == "__main__":
    result = extract_email_text("test_files/sample1.eml")
    print(result)