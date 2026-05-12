warkop = "=== SELAMAT DATANG DI WARKOP EMUN ==="
total_belanja = 0

print(warkop)
menu = {
    "1": {"nama": "Roti", "harga": 2000},
    "2": {"nama": "Susu", "harga": 3000},
    "3": {"nama": "Kopi", "harga": 3000},
    "4": {"nama": "Gorengan", "harga": 2000},
    "5": {"nama": "Indomie", "harga": 6000}
}

for item in menu:
    print(f"{item}. {menu[item]['nama']} - Rp {menu[item]['harga']}")
print("=" * len(warkop))

while True:
  try:
    pesanan = input("Pilih menu (1-5): ")
    if pesanan in menu:
      quantity = int(input("Masukkan jumlah pesanan: "))
      total_belanja += menu[pesanan]["harga"] * quantity
    else:
      print("Menu tidak tersedia")
      continue
  except ValueError:
    print("Input tidak valid, pastikan input berupa angka")
    continue 
  
  while True:
    pesanan_tambahan = input("Apakah ada pesanan tambahan? (y/n): ")
    if pesanan_tambahan == "y":
      break
    elif pesanan_tambahan == "n":
      break
    else:
      print("Pastikan ketik y/n")
      continue
  if pesanan_tambahan == "n":
    break
print(f"Total bayar {total_belanja}")
