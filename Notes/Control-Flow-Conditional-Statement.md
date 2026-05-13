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
```python
#basic code
for i in range(10):
    print(i) #output 0-9

#for juga bisa digunakan untuk type sting, list, set, tuple, dan dictonary
favorit = 'pisang', 'apel', 'anggur', 'jeruk', 'pepaya'
for i in favorit:
    print(i)

favorit = ['pisang', 'apel', 'anggur', 'jeruk', 'pepaya']
for i in favorit:
    print(i)

favorit = {'pisang', 'apel', 'anggur', 'jeruk', 'pepaya'}
for i in favorit:
    print(i)

favorit = ('pisang', 'apel', 'anggur', 'jeruk', 'pepaya')
for i in favorit:
    print(i)
#output
#pisang
#apel
#anggur
#jeruk
#pepaya

favorit = {1:'pisang', 2:'apel', 3:'anggur', 4:'jeruk', 5:'pepaya'}
for i in favorit:
    print(i, favorit[i], sep=" -> ")
#output
#1 -> pisang
#2 -> apel
#3 -> anggur
#4 -> jeruk
#5 -> pepaya
```    
jika ingin mencari suatu item dalam dafar, bisa menggunakan if dalam for
```python
favorit = ['pisang', 'apel', 'anggur', 'jeruk', 'pepaya']
for buah in favorit:
    if buah == 'anggur':
        print('Ya, buah', buah, "ada dalam daftar") 
    else:
        print('tidak, buah itu tidak ada dalam daftar')
#output
#tidak, buah itu tidak ada dalam daftar
#tidak, buah itu tidak ada dalam daftar
#Ya, buah anggur ada dalam daftar
#tidak, buah itu tidak ada dalam daftar
#tidak, buah itu tidak ada dalam daftar
```

outputnya adalah "tidak" akan dicetak sebanyak 4 kali dan "ya" 1 kali karna fungsi for tetap memutar, ia akan mengecek semua list sampai selesai. untuk mengatasi hal ini gunakan for-else cukup sejajarkan saja identasi for dengan else dan tambakan break di Bawah baris print dalam if.

```python
favorit = ['pisang', 'apel', 'anggur', 'jeruk', 'pepaya']
for buah in favorit:
  if buah == 'anggur':
    print('Ya, buah', buah, "ada dalam daftar")
    break
else:
    print('tidak, buah itu tidak ada dalam daftar')
#output
#Ya, buah anggur ada dalam daftar  
```
- while: untuk angka akhir yang tidak kita ketahui jadi tetap loop selama kondisi true

- enumerate: untuk menambahkan index atau penomoran di loop

- break: berhenti Ketika kondisi benar 

- continue: lewati kondisi benar

- pass: tidak melakukan apapun, gunakan ini jika ingin test tanpa error karna ia akan membuat blok kode kosong

