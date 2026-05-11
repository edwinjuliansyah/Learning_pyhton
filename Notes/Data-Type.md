# Tipe data dasar

## 1. numeric
- Integer `3` -> bilangan bulat.
- float `3.14` -> bilangan desimal.
- complex number `a = 1 + 1i` -> bilangan kompleks dengan bagian real dan imajiner.

## 2. Sequence
kumpulan data yang terurut dan dapat diakses berdasarkan indeks.
- string `"hallo"` -> urutan karakter.
- list `[]` -> daftar elemen yang bisa berbeda tipe.
    - list = [1, 2, 3, 4, 5]
    - list.insert(len(list), 6)
    - list.append(6)
    - list.extend([6, 7, 8, 9])
    - list.pop(4)
    - del list[2]
- tuple `()` -> mirip list tapi tidak bisa diubah.
    - tuple = (1, "strings", 4.5, True)
    - print(tuple.count('strings')) #output 1
    - print(tuple.index(4.5)) #output 2


## 3. Dictionary `{}`
menyimpan data dalam pasangan {`"key"`: `value`} yang dapat diakses langsung melalui key.

## 4. Boolean
hanya memiliki dua nilai, ` true ` atau ` false `  digunakan untuk kondisi logika.

## 5. set `{}`
kumpulan data unik yang tidak berurutan, tidak memiliki indeks, dan immutable.
- set = {1, 2, 3, 4, 5, 5} set tidak bisa menerima nilai duplikat
  - set.add(6)
  - set.remove(2)
  - set.discard(2)

- set1 = {1, 2, 3, 4, 5}
- set2 = {4, 5, 6, 7, 8}
  - print(set1.union(set2)) # menggabungkan 2 set menjadi 1
  #or
  - print(set1 | set2)
 
  - print(set1.intersection(set2)) hasil {4, 5}
  #or
  - print(set1 & set2)

  - print(set1.difference(set2)) hasil {1, 2, 3} yang ada di 1 tidak ada di 2 
  #or 
  - print(set1 - set2)

  - print(set1.symmetric_difference(set2)) hasil {1, 2, 3, 6, 7, 8} yang ada di 1 dan 2 tidak di tampilkan
  #or 
  - print(set1 ^ set2)

## Type Casting
`implicit` sudah otomatis dari python.

`explicit` kita yang mengubahnya.

`int()` `float()` `bool()` `str()` `ord()` `hex()` `oct()` `tuple()` `dict()` `set()` `list()`

# Indexing
## Dasar
`x[0]` : Mengambil elemen pertama.

`x[1]` : Mengambil elemen kedua.

`x[-1]` : Mengambil elemen terakhir.

`x[-2]` : Mengambil elemen kedua dari belakang.

## Slicing (Mengambil Range/Rentang)
format `x[start:stop]` stop bersifat exclusive elemen di index tersebut tidak diikutkan.

`x[1:4]` : Mengambil index 1, 2, dan 3.

`x[:3]` : Mengambil dari awal sampai sebelum index 3 (index 0, 1, 2).

`x[2:]` : Mengambil dari index 2 sampai paling akhir.

`x[:]` : Mengambil seluruh elemen (copy list).

## Slicing dengan Step (Lompatan)

Formatnya `x[start:stop:step]`

`x[::2]` : Mengambil elemen dengan melompat setiap 2 langkah (index 0, 2, 4, ...).

`x[::-1]` : Membalik urutan list (reverse).

`x[::-2]` : Membalik urutan list dengan lompatan setiap 2 (index ..., 4, 2)

Note: Jika mengambil data dari belakang / reserve lalu angka `start` lebih kecil dari `stop` maka akan error `x[1:4:-1]` hasil tuple kosong
