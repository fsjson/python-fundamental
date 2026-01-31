"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini.

evenNumber = []
for n in range(0, 501):
  if n % 2 == 0: # Setiap nilai n yang habis dibagi 2 akan ditambahkan ke dalam list evenNumber. Setelah seluruh perulangan selesai, isi list evenNumber kemudian dicetak.
    evenNumber.append(n)
print(evenNumber)

# using list comprehension
evenNumber = [x for x in range(0, 501, 2)]
print(evenNumber)