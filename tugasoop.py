
class Produk:
    def __init__(self, nama, harga):
        self.nama, self.harga = nama, harga

    def tampilkan_info(self):
        print(f"Nama Produk : {self.nama}")
        print(f"Harga       : Rp{self.harga:,}".replace(",", "."))

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total):
        return total * 0.05 if total > 5000 else 0


total_seluruh = 0
daftar_produk = []

n = int(input("Masukkan jumlah produk yang dibeli: "))

for i in range(n):
    print(f"\n=== PRODUK KE-{i+1} ===")
    nama = input("Nama produk  : ")
    harga = int(input("Harga produk : Rp"))
    jumlah = int(input("Jumlah beli  : "))

    p = Produk(nama, harga)
    total = p.hitung_total(jumlah)
    p.tampilkan_info()
    print(f"Jumlah Beli : {jumlah}")
    print(f"Total Harga : Rp{total:,}".replace(",", "."))

    daftar_produk.append(p)
    total_seluruh += total

diskon = p.hitung_diskon(total_seluruh) if n > 0 else 0

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian : Rp{total_seluruh:,}".replace(",", "."))
print(f"Diskon 5%       : Rp{diskon:,.0f}".replace(",", "."))
print(f"Total Bayar     : Rp{total_seluruh-diskon:,.0f}".replace(",", "."))
