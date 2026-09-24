from translate import Translator
import tkinter as tk
from tkinter import ttk

# Original program logic
def translate_text():
    fr = from_lang.get()
    to = to_lang.get()
    txt = text_input.get("1.0", tk.END).strip()

    translator = Translator(from_lang=fr, to_lang=to)

    translation = translator.translate(txt)

    result_label.config(text=translation)


# GUI
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x650")
root.config(bg="white")

title = tk.Label(
    root,
    text="Language Translator",
    font=("Arial", 22, "bold"),bg="navy",
    fg="white"
)
title.pack(pady=20)

# Language list
languages = [
    "en",
    "hi",
    "fr",
    "de",
    "es",
    "it",
    "pt",
    "ar",
    "ru",
    "ja",
    "ko",
    "zh"
]

# From Language
tk.Label(
    root,
    text="From Language:",
    font=("Arial", 12),
    bg="white"
).pack()

from_lang = ttk.Combobox(
    root,
    values=languages,
    state="readonly",
    font=("Arial", 12)
)
from_lang.pack(pady=5)
from_lang.set("en")

# To Language
tk.Label(
    root,
    text="To Language:",
    font=("Arial", 12),
    bg="white"
).pack()

to_lang = ttk.Combobox(
    root,
    values=languages,
    state="readonly",
    font=("Arial", 12)
)
to_lang.pack(pady=5)
to_lang.set("hi")

# Text
tk.Label(
    root,
    text="Enter Text:",
    font=("Arial", 12),
    bg="white"
).pack(pady=5)

text_input = tk.Text(
    root,
    height=6,
    width=45,
    font=("Arial", 12)
)
text_input.pack()

# Translate button
tk.Button(
    root,
    text="Translate",
    font=("Arial", 12, "bold"),bg='green',fg='white',
    command=translate_text
).pack(pady=10)

tk.Button(root, text="Close", command=root.destroy,
          font=("Arial", 14, "bold"),bg='red',fg='white').pack(pady=10)

# Result
tk.Label(
    root,
    text="Translation:",
    font=("Arial", 12, "bold"),
    bg="black",fg="white"
).pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="black",fg="white",
    wraplength=450
)
result_label.pack(pady=10)

root.mainloop()
