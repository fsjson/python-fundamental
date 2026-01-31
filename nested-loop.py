for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)

"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan dalam: 2
Perulangan dalam: 3
Perulangan dalam: 4
Perulangan dalam: 5
Perulangan dalam: 6
Perulangan dalam: 7
Perulangan dalam: 8
Perulangan dalam: 9 --> di sini perulangan luar 0 selesai, karena perulangan dalam sudah selesai dengan (j < 10)
Perulangan luar: 1 --> perulangan luar dimulai kembali, dan ini yang terakhir karena di awal diinisialisasi bahwa range i = 2; artinya i < 2 atau i = 0, 1;
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan dalam: 2
Perulangan dalam: 3
Perulangan dalam: 4
Perulangan dalam: 5
Perulangan dalam: 6
Perulangan dalam: 7
Perulangan dalam: 8
Perulangan dalam: 9


"""