from stock import Stock
import sys

class Menu:
	def main(self):
		print("\n=========== Aplikasi Retail ===========")
		print("1. Kelola Stok Barang")
		print("2. Kelola Transaksi Konsumen")
		print("\n0. Exit Program")

		choice = input("\nPilih menu: ")

		if choice == '1':
			self.menu_stock()
		elif choice == '2':
			self.menu_transaksi()
		elif choice == '0':
			sys.exit()

	def menu_stock(self):
		while True:
			print("\n=========== Kelola Stock Barang ===========")
			print("1. Input Data Stok Barang")
			print("2. Restock Barang")
			print("3. Tampilkan Data Stok Barang [Tambahan]")
			print("\n0. Kembali")

			choice = input("\nPilih menu: ")

			if choice == '1':
				Stock().create()
			elif choice == '2':
				Stock().restock()
			elif choice == '3':
				Stock().show()
			elif choice == '0':
				self.main()

	def menu_transaksi(self):
		while True:
			print("\n=========== Kelola Transaksi Konsumen ===========")
			print("1. Input Data Transaksi Baru")
			print("2. Lihat Data Seluruh Transaksi Konsumen")
			print("3. Lihat Data Transaksi Berdasarkan Subtotal")
			print("\n0. Kembali")

			choice = input("\nPilih menu: ")

			if choice == '1':
				Stock().create()
			elif choice == '2':
				Stock().restock()
			elif choice == '3':
				Stock().show()
			elif choice == '0':
				self.main()

				
# Jalankan aplikasi
if __name__ == '__main__':
	menu = Menu()
	menu.main()
