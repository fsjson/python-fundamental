"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon,
  dan simpan dalam variabel bernama "total_harga".
Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""

# Jangan ubah kode ini
dico = 750000 # 750.000

# TODO: Silakan buat kode Anda di bawah ini.

# Untuk setiap pelanggan yang belanja > 500.000 ribu, dico = 750.000
# Pengecekan
if dico > 500000:
    diskon = 10/100 # 0.1
else:
    diskon = 0

# Potongan harga
potongan_harga = dico * diskon

# Hitung totsl harga sete;ah diskon
total_harga = (1 - diskon) * dico

print(f"Harga belanja       : Rp{dico:,}")
print(f"Diskon              : {int(diskon * 100)}%")
print(f"Potongan harga      : Rp{potongan_harga:,}")
print(f"Harga diskon        : Rp{total_harga:,}")