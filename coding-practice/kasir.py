warkop = "=== SELAMAT DATANG DI WARKOP EMUN ==="

total_belanja = 0

keranjang = {}

def garis():
  print("=" * len(warkop))

def tampilkan_keranjang(massage):
  print(massage)
  for key, value in keranjang.items():
    print(f"- {value['jumlah']} {value['nama']:<10} x Rp{value['harga']} = Rp{value['subtotal']:>6}")

print(warkop)
menu = {
    1: {"nama": "Roti", "harga": 2000},
    2: {"nama": "Susu", "harga": 3000},
    3: {"nama": "Kopi", "harga": 3000},
    4: {"nama": "Gorengan", "harga": 2000},
    5: {"nama": "Indomie", "harga": 6000}
}

for item in menu:
    print(f"{item}. {menu[item]['nama']:<10} | Rp {menu[item]['harga']:>6}")
garis()

while True:
  try:
    pesanan = int(input("Pilih menu (1-5): ").strip())
    if pesanan in menu:
      quantity = int(input("Masukkan jumlah pesanan: ").strip())
    else:
      print("Menu tidak tersedia")
      continue
  except ValueError:
    print("Input tidak valid, pastikan input berupa angka")
    continue 
  
  nama = menu[pesanan]["nama"]
  harga = menu[pesanan]["harga"]
  subtotal = harga * quantity

  if pesanan in keranjang:
    keranjang[pesanan]["jumlah"] += quantity
    keranjang[pesanan]["subtotal"] += subtotal
  else:
    keranjang[pesanan] = {
        "nama": nama,
        "harga": harga,
        "jumlah": quantity,
        "subtotal": subtotal
    }
  total_belanja += subtotal
  
  garis()
  tampilkan_keranjang("Isi keranjang saat ini:")
  garis()

  while True:
    pesanan_tambahan = input("Apakah ada pesanan tambahan? (y/n): ").lower().strip()
    if pesanan_tambahan == "y":
      break
    elif pesanan_tambahan == "n":
      break
    else:
      print("Pastikan ketik y/n")
      continue
  if pesanan_tambahan == "n":
    break

garis()
tampilkan_keranjang("Pesanan kamu:")
garis()
print(f"Total bayar Rp{total_belanja}")
