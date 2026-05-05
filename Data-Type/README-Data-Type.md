# Tipe data dasar

## 1. numeric
- Integer `3`
- float `3.14`
- complex number `a = 1 + 1i`

## 2. Sequence
- string `"hallo", "1", "3.14"`
- list `[]`
- tuple `()`

## 3. Dictionary `{}`

## 4. Boolean
` true `
` false `

## 5. set `{}`

## Type Casting
`implicit` sudah otomatis dari python

`explicit` kita yang mengubahnya

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
