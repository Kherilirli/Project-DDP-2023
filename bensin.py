from tkinter import *
import ttkbootstrap as ttk

window = ttk.Window(themename= 'darkly')
window.title('Aplikasi Penghitung Bahan Bakar')
window.geometry('500x500')

title = ttk.Label(window, text='Penghitung Biaya Bahan Bakar',font=('arial', 15, 'bold')).pack()

kota = ttk.Label(window, text='Kota yang dituju :',font=('arial', 12,)).pack(pady=15)

kota = Entry()
kota.pack()

bensin = ttk.Label(window, text='Jenis bensin (Pertalite, Pertamax, Pertamax Turbo) :',font=('arial', 12,)).pack(pady=15)

bensin = Entry()
bensin.pack()

jarak = ttk.Label(window, text='Jarak yang dituju (km) :',font=('arial', 12,)).pack(pady=15)

jarak = Entry()
jarak.pack()

def hitung():
    bensin_input = bensin.get().lower()

    if bensin_input.lower() =="pertalite":
        harga = 10000
        jarak_tempuh = 12

    elif bensin_input.lower() =="pertamax":
        harga = 14000
        jarak_tempuh = 13

    elif bensin_input.lower() =="pertamax turbo":
        harga = 17000
        jarak_tempuh = 13.5
    else:
        tidak_valid = f"Jenis Bensin yang Anda masukkan tidak valid!"
        ttk.Label(window, text=tidak_valid).pack()

    kota_hasil = kota.get()
    jenis_bensin = bensin.get()
    jarak_hasil = int(jarak.get())

    pemakaian_bensin = jarak_hasil / jarak_tempuh
    total_harga = pemakaian_bensin * harga


    hasil_kota = f"Kota yang ditempuh: {kota_hasil}"
    ttk.Label(window, text=hasil_kota).pack()

    hasil_bensin = f"Jenis Bensin: {jenis_bensin}"
    ttk.Label(window, text=hasil_bensin).pack()

    hasil = f"Pemakaian bensin: {pemakaian_bensin:.2f} liter"
    ttk.Label(window, text=hasil).pack()

    hasil_harga = f"Total harga bensin: Rp {total_harga:,.2f}"
    ttk.Label(window, text=hasil_harga).pack()

ttk.Button(bootstyle='danger', text='Hitung', command=hitung).pack(pady=10)

window.mainloop()