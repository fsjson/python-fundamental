
import traceback

nilai = "10"
# nilai + 2
# print(nilai)

# kedua ekspresi di atas akan error

try:
    nilai + 2
    print(nilai)
except Exception as error:
    print(f"Error:\n\t{type(error).__name__}: \n\t{error}\n")


# Raise Error
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan.")
else:
    for n in range(var):
        print(n+1)
