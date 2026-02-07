import tkinter as tk
from tkinter import messagebox, ttk

import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        pp = float(entry_pp.get())
        e_max = float(entry_energy.get())
        tax_rate = float(entry_tax.get())
        loy_bonus = float(entry_loyalty.get()) 
        
        base_lohn = 0.11
        
        # KORRIGIERTE TEILER (2500 und 10000)
        qpy_base = (pp / 2500) + (e_max / 10000)
        
        # FY berechnet auf den Bonusanteil
        fy_extra = qpy_base * (loy_bonus / 100)
        
        final_lohn = base_lohn + qpy_base + fy_extra
        
        # UI Update
        lbl_rbc.config(text=f"{base_lohn:.4f}")
        lbl_qpy.config(text=f"{qpy_base:.4f}")
        lbl_fy.config(text=f"+{fy_extra:.4f}")
        lbl_total.config(text=f"{final_lohn:.4f} Credits")
        
        # FSI Logik
        h_pay = tax_rate if tax_rate <= 18 else (tax_rate * 0.9 if tax_rate <= 25 else tax_rate * 0.7)
        lbl_fsi.config(text=f"FSI Schutz: {h_pay:.1f}% übernommen")
        
    except ValueError:
        messagebox.showerror("Fehler", "Zahlen prüfen!")

# (Rest des UI Codes wie vorher, nur die calculate-Funktion austauschen!)

# Hauptfenster
root = tk.Tk()
root.title("Raffanus Holding - Executive Terminal")
root.geometry("450x650")
root.configure(bg="#0b1622") # Deep Space Blue

# Header
title_font = ("Consolas", 20, "bold")
label_font = ("Consolas", 10)
res_font = ("Consolas", 12, "bold")

tk.Label(root, text="RAFFANUS HOLDING", font=title_font, bg="#0b1622", fg="#00d4ff").pack(pady=20)
tk.Label(root, text="VORSITZENDER: MISTERY_MAN", font=("Consolas", 8), bg="#0b1622", fg="#5a7b9a").pack()

# Input Container
input_frame = tk.Frame(root, bg="#152232", padx=20, pady=20)
input_frame.pack(pady=10, fill="x", padx=30)

def add_input(text, default):
    tk.Label(input_frame, text=text, font=label_font, bg="#152232", fg="#8ea6c0").pack(anchor="w")
    ent = tk.Entry(input_frame, bg="#1c2d40", fg="#ffffff", insertbackground="white", borderwidth=0)
    ent.insert(0, default)
    ent.pack(fill="x", pady=(0, 10))
    return ent

entry_pp = add_input("PRODUCTION POWER (PP)", "25")
entry_energy = add_input("MAX ENERGY (E-MAX)", "70")
entry_loyalty = add_input("FIDELITY LEVEL (1-20%)", "5")
entry_tax = add_input("SECTOR TAX RATE (%)", "9")

# Calc Button
btn = tk.Button(root, text="GENERATE PAYROLL", command=calculate, bg="#00d4ff", fg="#0b1622", 
                font=("Consolas", 12, "bold"), relief="flat", activebackground="#008cb3")
btn.pack(pady=20, fill="x", padx=50)

# Output Container
out_frame = tk.Frame(root, bg="#0b1622", highlightbackground="#00d4ff", highlightthickness=1)
out_frame.pack(pady=10, fill="x", padx=30, ipady=10)

def add_result_row(label):
    f = tk.Frame(out_frame, bg="#0b1622", padx=10)
    f.pack(fill="x", pady=2)
    tk.Label(f, text=label, font=label_font, bg="#0b1622", fg="#5a7b9a").pack(side="left")
    l = tk.Label(f, text="---", font=res_font, bg="#0b1622", fg="#ffffff")
    l.pack(side="right")
    return l

lbl_rbc = add_result_row("BASE CREDIT (RBC):")
lbl_qpy = add_result_row("PERFORMANCE (QPY):")
lbl_fy = add_result_row("FIDELITY BONUS (FY):")
lbl_total = add_result_row("TOTAL NET (CREDITS):")
lbl_total.config(fg="#00ff88") # Neon Green für das Endergebnis

lbl_fsi = tk.Label(root, text="FSI SHIELD: INACTIVE", font=("Consolas", 9, "italic"), bg="#0b1622", fg="#f1c40f")
lbl_fsi.pack(pady=10)

root.mainloop()