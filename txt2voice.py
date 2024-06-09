from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def text_to_speech():
    mytext = text_entry.get("1.0", "end-1c")
    language = languages[language_var.get()]
    slow = speed_var.get()
    
    if not mytext.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    try:
        myobj = gTTS(text=mytext, lang=language, slow=slow)
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            myobj.save(file_path)
            os.system(f"start {file_path}")
            messagebox.showinfo("Success", "Audio file saved and played successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def play_audio():
    mytext = text_entry.get("1.0", "end-1c")
    language = languages[language_var.get()]
    slow = speed_var.get()
    
    if not mytext.strip():
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    try:
        myobj = gTTS(text=mytext, lang=language, slow=slow)
        file_path = "temp_audio.mp3"
        myobj.save(file_path)
        os.system(f"start {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def set_defaults():
    text_entry.delete("1.0", "end")
    text_entry.insert("end", "Enter text here...")
    language_var.set("English")
    speed_var.set(False)

# Mapping full language names to gTTS language codes
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it"
}

# Setting up the main window
root = tk.Tk()
root.title("Text to Voice Converter")
root.geometry("1526x850")
root.configure(bg="#2c3e50")

# Font settings
font_name = "Lemon Milk"
font_bold = "Lemon Milk Bold"
times = "Montserrat"

# Top Labels
top_label1 = tk.Label(root, text="M KUMARASAMY COLLEGE OF ENGINEERING - KARUR", font=(font_bold, 18), bg="#2c3e50", fg="white")
top_label1.pack(pady=5)

top_label2 = tk.Label(root, text="PYTHON END SEMESTER PROJECT", font=(font_bold, 17), bg="#2c3e50", fg="white")
top_label2.pack(pady=5)

top_label3 = tk.Label(root, text="M S ARUN SANJEEV", font=(font_name, 16), bg="#2c3e50", fg="white")
top_label3.pack(pady=5)

# Registration Number Label
reg_label = tk.Label(root, text="Reg No: 927623BCS011", font=(font_name, 16), bg="#2c3e50", fg="white")
reg_label.pack(pady=5)

# Title Label
title_label = tk.Label(root, text="Text to Voice Converter", font=(font_bold, 20), bg="#2980b9", fg="white")
title_label.pack(pady=10, fill=tk.X)

# Text Entry Widget
text_entry = tk.Text(root, wrap="word", font=(times, 12), height=5, width=150, fg="grey")
text_entry.pack(pady=10, padx=10)
text_entry.insert("end", "Enter text here...")

# Language Dropdown
language_var = tk.StringVar(root)
language_var.set("English")
language_label = tk.Label(root, text="Select Language:", font=(font_name, 12), bg="#2c3e50", fg="white")
language_label.pack(pady=5)
language_menu = tk.OptionMenu(root, language_var, *languages.keys())
language_menu.pack(pady=5)

# Speed Checkbox
speed_var = tk.BooleanVar()
speed_check = tk.Checkbutton(root, text="Slow Speed", variable=speed_var, font=(font_name, 12), bg="#2c3e50", fg="white")
speed_check.pack(pady=5)

# Play Button
play_button = tk.Button(root, text="Play", command=play_audio, font=(font_bold, 12), bg="#3498db", fg="white", width=10)
play_button.pack(pady=5)

# Start Button
convert_button = tk.Button(root, text="SAVE", command=text_to_speech, font=(font_bold, 14), bg="#27ae60", fg="white", width=15, height=2)
convert_button.pack(pady=20)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=set_defaults, font=(font_bold, 12), bg="#e74c3c", fg="white")
reset_button.pack(pady=5)

# Run the application
root.mainloop()
