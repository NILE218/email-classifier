def classify_email(text):
    important_words = ["urgent", "important", "asap", "meeting", "deadline", "reminder"]
    
    text_lower = text.lower()
    
    for word in important_words:
        if word in text_lower:
            return "Important"
    
    return "Normal"

# Test it
if __name__ == "__main__":
    sample_text = "This is a reminder that we have a meeting scheduled for tomorrow."
    result = classify_email(sample_text)
    print(result)