# File Handling
- function `open()`
  
  digunakan untuk read, write, create files. open menerima 2 argument open('file_name'/'lokasi_file', 'mode')
  - `file_name` `lokasi_name` untuk mencari file. 
  - `mode` untuk tindakan read, write ataupun create ini juga menentukan apakah output ingin dalam format teks atau biner.
    - `r` = open dan read.
    - `r+` = open file untuk reading dan writing.
    - `w` = open untuk writing(ini akan menimpa file).
    - `a` = open untuk editing dan appending data.

  dalam python menerima 2 format text dan biner secara default file handling dengan format text, jika ingin membuka dengan format biner perlu menambahkan b diakhir (`rb`, `rb+`, `wb`, `ab`).

- function `close()`
  
  digunakan untuk menutup koneksi file yang terbuka.

- function `with`

  opsi lain jika ingin open file yaitu dengan with, keuntungan menggunakan with adalah ini akan close secara otomatis.

# Create, Write, Read
untuk create file baru dan menulis 1 line.
```python
with open('file_baru.txt', 'w') as f:
    f.write('baris pertama')
```
jika ingin multiple line	
```python
with open('file_baru.txt', 'w') as f:
    f.writelines(['baris pertama\n', 'baris kedua'])
```
jika ingin menambahkan isi file tanpa menimpa gunakan append.
```python
with open('file_baru.txt', 'a') as f:
    f.writelines(['\nbaris ketiga', '\nbaris keempat'])
```
read() -> output string yang akan berisi semua karakter.
```python
with open('file_baru.txt', 'r') as f:
    content = f.read()
    print(content)
```
dapat juga untuk mengeluarkan output beberapa karakter pertama.
```python
with open('file_baru.txt', 'r') as f:
    content = f.read(40)
    print(content)
```
readline() -> output 1 baris sebagai string.
```python
with open('file_baru.txt', 'r') as f:
    content = f.readline()
    print(content)
```
sama seperti sebelumnya ini juga dapat mengeluarkan output beberapa karakter pertama.
```python
with open('file_baru.txt', 'r') as f:
    content = f.readline(10)
    print(content)
```
readlines() -> output semua karakter dalam bentuk order list. bisa menggunakan fungsi for untuk read file.
```python
with open('file_baru.txt', 'r') as f:
    content = f.readlines()
    print(content)
```
