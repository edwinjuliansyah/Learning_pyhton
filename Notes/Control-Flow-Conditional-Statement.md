# Conditional statement 

## If statement

Digunakan untuk mengecek kondisi berdasarkan nilai Boolean (True/False). Python mengevaluasi dari atas ke bawah dan akan berhenti di kondisi pertama yang terpenuhi.

- if: Kondisi utama yang pertama kali dicek.

- elif (else if): Kondisi tambahan jika if sebelumnya salah. Bisa ada banyak elif.

- else: "Pilihan terakhir" jika semua kondisi di atas tidak ada yang benar.
```python
status = 404

if status == 200:
    print("OK")
elif status == 404:
    print("Not Found")
elif status == 500:
    print("Server Error")
else:
    print("Unknown status")
#output
#Not Found
```

## Match statement

Diperkenalkan pada Python 3.10. Lebih bersih dan efisien daripada if-elif yang panjang jika kamu hanya ingin mencocokkan nilai spesifik atau pola tertentu.

- case: Nilai yang dicocokkan.

- case _: Wildcard (seperti else). Menangkap apa pun yang tidak cocok dengan case sebelumnya.
```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")
#output
#Not Found
```

## Loop statement 

untuk mengeksekusi blok kode secara berulang sampai kondisi tertentu terpenuhi.

- for: digunakan untuk perulangan yang sudah diketahui angka akhirnya

- while: untuk angka akhir yang tidak kita ketahui jadi tetap loop selama kondisi true

- enumerate: untuk menambahkan index atau penomoran di loop

- break: berhenti Ketika kondisi benar 

- continue: lewati kondisi benar

- pass: tidak melakukan apapun, gunakan ini jika ingin test tanpa error karna ia akan membuat blok kode kosong

