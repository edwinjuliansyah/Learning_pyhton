harga = {
  "HARGA_PER_KG": 2000,
  "HARGA_PER_KM": 3000
}

surcharge = {
    "BERAT_15KG": 5000,
    "JARAK_50KM": 10000
}

print(f"Harga per Kg {harga["HARGA_PER_KG"]} dan Harga per Km {harga["HARGA_PER_KM"]}\nSurcharge berat > 15Kg {surcharge["BERAT_15KG"]} dan \
Surcharge > 50Km {surcharge["JARAK_50KM"]}\n\n")

try:
  inp1 = float(input("Masukan berat barang: "))
  inp2 = float(input("Masukan jarak: "))
except ValueError:
  print("Input tidak valid, pastikan input berupa angka (berikan titik jika desimal)")

if inp1 <= 0 or inp2 <=0:
  print("Angka tidak valid")

biaya_berat = inp1 * harga["HARGA_PER_KG"]
biaya_jarak = inp2 * harga["HARGA_PER_KM"]
total_biaya = biaya_berat + biaya_jarak

if inp1 > 15:
    total_biaya += 5000

if inp2 > 50:
  total_biaya += 10000  

print(f"Total biaya: {total_biaya}")
