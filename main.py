import Program.suhu
import Program.b_p
import Program.mata_uang

while True:
     print("""
          PROGRAM KALKULATOR DAN KONVERSI
               Silahkan Pilih Program
          1. Kalkulator
          2. Konversi
     """)

     selectedProgam = input("Pilih Program (1/2) : ")

     #kakulator
     def kalkulator(value1, value2, fungsi):
          if fungsi == 1 :  
               hasil = value1+value2
               print(f"Hasil dari {value1} tambah {value2} adalah {hasil}")
          elif fungsi == 2 : 
               hasil = value1-value2
               print(f"Hasil dari {value1} kurang {value2} adalah {hasil}")
          elif fungsi == 3 : 
               hasil = value1*value2
               print(f"Hasil dari {value1} kali {value2} adalah {hasil}")
          elif fungsi == 4 : 
               hasil = value1/value2
               print(f"Hasil dari {value1} bagi {value2} adalah {hasil}")
          else:
               print("Pilihan Tidak Terdaftar!")
               
     #konversi
     def konversi(select):
          if select == "suhu" or select == "1":
               print(" 1. Celcius \n 2. Fahrenheit \n 3. Reamur \n 4. Kelvin ")
               temperatur = input("Pilih Temperatur : ")
               suhu = int(input("Masukkan Suhu : "))
               Program.suhu.mySuhu(temperatur, suhu)
          elif select == "jarak"or select == "2":
               panjang = input("Pilih jarak dalam (km/m/dam/m/dm/cm/mm)")
               value = int(input("Masukan jarak yang kamu inginkan : "))
               Program.b_p.pj(panjang, value)   
          elif select == "berat" or select == "3":
               berat = input("Pilih berat dalam (kg/hg/dag/g/dg/cg/mg)")
               value = int(input("Masukan berat yang kamu inginkan : "))
               Program.b_p.pb(berat,value)
          elif select == "mata uang" or select == "4":
               mataUang = input("Masukan nilai mata uang [USA/IDN/DINAR] : ")
               nilai = int(input("Masukan nilai uang : "))
               Program.mata_uang.mu(mataUang, nilai)

     if selectedProgam == "1":
          print(" 1. Tambah \n 2. Kurang \n 3. Kali \n 4. Bagi ")
          fungsi = int(input("Pilih Operasi Bilangan(1/2/3/4) : "))
          value1 = int(input("Masukan nomor pertama : "))
          value2 = int(input("Masukan nomor kedua   : "))
          kalkulator(value1, value2, fungsi)
     elif selectedProgam  == "2":
          print("""
          1. Suhu
          2. Jarak
          3. Berat
          4. Mata uang
          """)
          select = input("Pilih konversi yang anda inginkan  : ")
          konversi(select)

     stop = input("Mau Menghitung Lagi? (Ya/Tidak): ")
     if stop == "ya":
          continue
     else:
          print("Program Selesai!")
          break          


