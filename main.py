import tkinter as tk
from tkinter import ttk

class SearchBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Bar")
        self.root.geometry("500x300")

        self.search_entry = tk.Entry(self.root, width=50)
        self.search_entry.pack(pady=10)

        self.autocomplete_listbox = tk.Listbox(self.root, width=50)
        self.autocomplete_listbox.pack(pady=10)

        self.suggestions = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

        self.search_entry.focus_set()
        self.search_entry.after(100, self.autocomplete)

    def autocomplete(self):
        query = self.search_entry.get()
        self.autocomplete_listbox.delete(0, tk.END)
        for suggestion in self.suggestions:
            if suggestion.startswith(query):
                self.autocomplete_listbox.insert(tk.END, suggestion)
        self.root.after(100, self.autocomplete)

root = tk.Tk()
search_bar = SearchBar(root)
root.mainloop()
