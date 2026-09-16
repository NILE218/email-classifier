import tkinter as tk
from tkinter import filedialog, scrolledtext
from extract_email import extract_email_text
from classify_email import classify_email

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Email files", "*.eml")])
    if file_path:
        text = extract_email_text(file_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)
        
        result = classify_email(text)
        result_label.config(text=f"Result: {result}")

def save_result():
    with open("../saved_results/history.txt", "a") as f:
        f.write(result_label.cget("text") + "\n")

window = tk.Tk()
window.title("Email Classifier")
window.geometry("600x500")

upload_btn = tk.Button(window, text="Upload Email File", command=upload_file)
upload_btn.pack(pady=10)

text_box = scrolledtext.ScrolledText(window, width=70, height=15)
text_box.pack(pady=10)

result_label = tk.Label(window, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

save_btn = tk.Button(window, text="Save Result", command=save_result)
save_btn.pack(pady=10)

window.mainloop()