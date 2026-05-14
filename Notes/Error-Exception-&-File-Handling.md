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

