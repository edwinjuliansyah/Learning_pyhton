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
    pesanan = int(input("Pilih menu (1/2/3/4/5): "))
    quantity = int(input("Masukkan jumlah pesanan: "))
    if pesanan == 1:
      total_belanja += menu["1"]["harga"] * quantity
    elif pesanan == 2:
      total_belanja += menu["2"]["harga"] * quantity
    elif pesanan == 3:
      total_belanja += menu["3"]["harga"] * quantity
    elif pesanan == 4:
      total_belanja += menu["4"]["harga"] * quantity
    elif pesanan == 5:
      total_belanja += menu["5"]["harga"] * quantity 
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
  if pesanan_tambahan == no:
    break
print(f"Total bayar {total_belanja}")
