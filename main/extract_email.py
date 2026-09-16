import email
from bs4 import BeautifulSoup
import re

def extract_email_text(file_path):
    with open(file_path, 'r') as f:
        msg = email.message_from_file(f)
    
    subject = msg['subject'] or ""
    sender = msg['from'] or ""
    body = ""
    
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            
            # Skip attachments
            if "attachment" in content_disposition:
                continue
            
            if content_type == "text/plain":
                body = part.get_payload()
                break
            elif content_type == "text/html":
                html_content = part.get_payload()
                soup = BeautifulSoup(html_content, "html.parser")
                body = soup.get_text()
    else:
        content_type = msg.get_content_type()
        if content_type == "text/html":
            soup = BeautifulSoup(msg.get_payload(), "html.parser")
            body = soup.get_text()
        else:
            body = msg.get_payload()
    
    # Clean up extra blank lines and spaces
    body = re.sub(r'\n\s*\n', '\n', body)
    body = body.strip()
    
    full_text = subject + "\n" + body
    return full_text.strip()

# Test it
if __name__ == "__main__":
    result = extract_email_text("test_files/sample2.eml")
    print(result)