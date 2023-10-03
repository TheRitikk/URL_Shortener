import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import requests

def short_url():
    api_key = "9f42b330545d88e96e2b7344a42f1bbe99f47"
    url = url_entry.get()
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        shortened_url = data["shortLink"]
        short_url_frame.pack(pady=5)
        # Clear the existing text in the text widget
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, shortened_url)

    else:
        short_url_frame.pack(pady=5)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, data)

# Function to copy text to the clipboard
def copy_to_clipboard():
    result = result_text.get(1.0, tk.END)  
    window.clipboard_clear()  
    window.clipboard_append(result)  
    window.update() 

window = tk.Tk()
window.title("URL Shortener")
window.geometry("350x250")
window.configure(bg="lightblue")

# Url Entry
url_label = tk.Label(window, text="Enter URL")
url_label.pack(pady=5)
url_entry = tk.Entry(window)
url_entry.pack(pady=5)

# Short URL Button
short_button = tk.Button(window, text="Short URL", command=short_url)
short_button.pack(pady=5)

# Frame to contain short URL and show (initially hidden)
short_url_frame = tk.Frame(window)
short_url_frame.pack_forget()

# Create a text widget to display the result
result_text = scrolledtext.ScrolledText(short_url_frame, wrap=tk.WORD, width=30, height=1)
result_text.pack(pady=5)

# Create a button to copy the result to the clipboard
copy_button = tk.Button(short_url_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)


window.mainloop()