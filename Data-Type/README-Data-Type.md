# Tipe data dasar

## 1. numeric
- Integer `3` -> bilangan bulat.
- float `3.14` -> bilangan desimal.
- complex number `a = 1 + 1i` -> bilangan kompleks dengan bagian real dan imajiner.

## 2. Sequence
kumpulan data yang terurut dan dapat diakses berdasarkan indeks.
- string `"hallo"` -> urutan karakter.
- list `[]` -> daftar elemen yang bisa berbeda tipe.
- tuple `()` -> mirip list tapi tidak bisa diubah.

## 3. Dictionary `{}`
menyimpan data dalam pasangan {`"key"`: `value`} yang dapat diakses langsung melalui key.

## 4. Boolean
hanya memiliki dua nilai, ` true ` atau ` false `  digunakan untuk kondisi logika.

## 5. set `{}`
kumpulan data unik yang tidak berurutan dan tidak memiliki indeks.

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
