import tkinter as tk
from tkinter import ttk
import random

# List of motivational quotes
QUOTES = [
    "Le succès n'est pas la clé du bonheur. Le bonheur est la clé du succès.",
    "Croyez en vous et tout devient possible.",
    "Chaque jour est une nouvelle opportunité.",
    "N'abandonnez jamais vos rêves.",
    "La persévérance est la clé de la réussite.",
    "Vous êtes plus fort que vous ne le pensez.",
    "Faites de votre mieux et le reste suivra.",
    "Le seul échec est de ne pas essayer.",
    "Transformez vos obstacles en opportunités.",
    "Votre avenir commence aujourd'hui."
]

def get_random_quote():
    return random.choice(QUOTES)

def refresh_quote():
    quote_var.set(get_random_quote())

# Main window
root = tk.Tk()
root.title("Application de Motivation")
root.geometry("500x350")
root.configure(bg="#f5f6fa")

# Style
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)
style.configure("TLabel", font=("Helvetica", 16), background="#f5f6fa", foreground="#2d3436")

# Title
title_label = ttk.Label(root, text="🌟 Motivation Quotidienne 🌟", font=("Helvetica", 20, "bold"), background="#f5f6fa", foreground="#0984e3")
title_label.pack(pady=20)

# Quote
quote_var = tk.StringVar(value=get_random_quote())
quote_label = ttk.Label(root, textvariable=quote_var, wraplength=400, justify="center")
quote_label.pack(pady=30)

# Refresh Button
refresh_btn = ttk.Button(root, text="Nouvelle citation", command=refresh_quote)
refresh_btn.pack(pady=10)

# Footer
footer_label = ttk.Label(root, text="Prenez soin de vous et restez motivé !", font=("Helvetica", 12), background="#f5f6fa", foreground="#636e72")
footer_label.pack(side="bottom", pady=15)

root.mainloop()