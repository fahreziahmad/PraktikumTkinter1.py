# Praktikum/Praktikum.py

import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not(0 <= nilai <= 100):
                raise ValueError("Nilai harus 0-100")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
        
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka 0-100")

# Membuat 
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")
root.configure(bg="white")

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.pack(pady=10)

# Frame untuk input nilai
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Membuat 10 input nilai mata pelajaran dengan label
entries = []
for i in range(10):
    label = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i+1}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(input_frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol untuk hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=10)

# Label untuk menampilkan hasil produksi
hasil_label = tk.Label(root, text="Hasil Produksi: ", font=("Arial", 12),bg="#563A9C", fg="#FAB12F")
hasil_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()