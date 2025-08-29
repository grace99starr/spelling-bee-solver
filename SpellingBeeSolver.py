#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import time


# In[2]:


def load_clean_wordlist():
    import requests
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    response = requests.get(url)
    words = response.text.splitlines()
    return [w for w in words if w.islower()]

dictionary = load_clean_wordlist()
#valid_set = sorted({w for w in dictionary if (4 <= len(w) <= 16 and set(w) <= set(letters))})

# for word in valid_set:
#     if letter_of_the_day in word:
#         print("✅", word)


# In[3]:


def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        definitions = []
        for meaning in data[0]["meanings"]:
            for d in meaning["definitions"]:
                definitions.append(d["definition"])
        print(definitions)
    else:
        print("No definition found.")


# In[4]:


def is_pangram(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True


# In[5]:


def get_pangrams(words, letters):
    pangrams = []
    for word in words:
        if is_pangram(word, letters):
            pangrams.append(word)
    return pangrams


# In[6]:


# print("Today's pangrams:\n")

# for word in valid_set:
#     if (is_pangram(word, letters)):
#         print(word)
#         get_definition(word)


# In[7]:


def get_valid_set(letters):
    return sorted({w for w in dictionary if 4 <= len(w) <= 16 and set(w) <= set(letters)})


# In[8]:


import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading

# Your precomputed solution set
def find_valid_words(letters_input, entry_l, output_box):
    letters = [c.lower() for c in letters_input if c.isalpha()]
    if len(letters) != 7:
        messagebox.showerror("Error", "Please enter exactly 7 letters (A–Z only).")
        return

    letter_of_the_day = entry_l.get().strip().lower()
    if len(letter_of_the_day) != 1 or not letter_of_the_day.isalpha():
        messagebox.showerror("Error", "Letter of the day must be a single A–Z letter.")
        return

    valid_set = get_valid_set(letters)
    valid_set_l = [word for word in valid_set if letter_of_the_day in word]
    pangrams = get_pangrams(valid_set_l, letters)

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Searching...\n")

    if not valid_set_l:
        output_box.insert(tk.END, "No valid words found.\n")
    else:
        for word in sorted(valid_set_l):
            output_box.insert(tk.END, f"{word}\n")
        output_box.insert(tk.END, f"\nFound {len(valid_set_l)} valid words.")
        
    output_box.insert(tk.END, "\nToday's pangrams:\n")
    for pangram in pangrams:
        output_box.insert(tk.END, "\n")
        output_box.insert(tk.END, pangram)
    

def on_submit(entry, entry_l, output_box):
    letters = entry.get().strip()
    thread = threading.Thread(target=find_valid_words, args=(letters, entry_l, output_box))
    thread.start()

# GUI layout
root = tk.Tk()
root.title("Spelling Bee Solver")
root.geometry("500x400")

tk.Label(root, text="Enter the 7 letters:").pack(pady=5)
entry = tk.Entry(root, font=("Arial", 14), width=10, justify='center')
entry.pack(pady=5)

tk.Label(root, text="Enter the letter of the day:").pack(pady=5)
entry_l = tk.Entry(root, font=("Arial", 14), width=10, justify='center')
entry_l.pack(pady=5)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
output_box.pack(padx=10, pady=10)

tk.Button(root, text="Find Words", command=lambda: on_submit(entry, entry_l, output_box)).pack(pady=5)

root.mainloop()


# In[ ]:




