jumlah_deret = int(input("Masukkan jumlah deret Fibonacci: "))
a, b = 1, 1
print("Output:")

for i in range(jumlah_deret):
    print(a, end=", ")
    a, b = b, a + b