import Program.suhu
import Program.b_p
import Program.mata_uang
import Program.operator as po
while True:
     print("""
===================================================
           PROGRAM KALKULATOR KONVERSI
             Silahkan Pilih Program  
===================================================
           
     1. Kalkulator Operasi Aritmatika
     2. Konversi
     """)

     selectedProgam = input("Pilih Program (1/2) : ")
     print("-----------------------------------------")

     if selectedProgam == "1":
          print("""
     1. Penambahan 
     2. Pengurangan
     3. Perkalian
     4. Pembagian
     5. modulus
     6. Pemangkatan
     7. Pembagian Dengan hasil Bilangan Bulat
                """)
          fungsi =input("Pilih Operasi Bilangan(1/2/3/4/5/6/7) : ")
          print("-----------------------------------------")
          nilai1 = int(input("Masukan nomor pertama : "))
          nilai2 = int(input("Masukan nomor kedua   : "))
          po.operator(fungsi, nilai1, nilai2)
     elif selectedProgam  == "2":
          print("""
     1. Suhu
     2. Jarak
     3. Berat
     4. Mata uang
          """)
          select = input("Pilih konversi yang anda inginkan  : ")
          print("-----------------------------------------")

     #konversi
     if select == "suhu" or select == "1":
               print("""
     1. Celcius
     2. Fahrenheit
     3. Reamur
     4. Kelvin 
                     """)
               temperatur = int(input("Pilih Temperatur : "))
               suhu = int(input("Masukkan Suhu : "))
               print("-----------------------------------------")
               Program.suhu.mySuhu(temperatur, suhu)
     elif select == "jarak"or select == "2":
               print("""
     1. Kilometer   (KM)
     2. Hektometer  (HM)
     3. Dekameter   (DAM)
     4. Meter       (M)
     5. Desimeter   (DM)
     6. Centimeter  (CM)
     7. Milimeter   (MM)
""")
               panjang = int(input("Pilih jarak   : "))
               value = int(input("Masukan jarak   : "))
               print("-----------------------------------------")
               Program.b_p.pj(panjang, value)
     elif select == "berat" or select == "3":
               print("""
     1. Kilogram    (KG)
     2. Hektogram   (HG)
     3. Dekagram    (DAG)
     4. Gram        (G)
     5. Desigram    (DG)
     6. Sentigram   (CG)
     7. Miligram    (MG)
""")
               berat = int(input("Pilih berat     : "))
               value = int(input("Masukan berat   : "))
               print("-----------------------------------------")
               Program.b_p.pb(berat,value)
     elif select == "mata uang" or select == "4":
               print("""
     1. Dinar Kuwait          (KWD)
     2. Dinar Bahrain         (BHD)
     3. Rial Oman             (OMR)
     4. Dinar Yornania        (JOD)
     5. British Pound         (GBP)
     6. Gibraltar Pound       (GIP)
     7. Cayman Island Dollar  (KYD)
     8. Swiss Franc           (CHF)
     9. Eur                   (EUR)
     10. United States Dollar (USD)
     10. Indonesia            (IDR)
""")
               mataUang = int(input("Masukan mata uang     : "))
               nilai = int(input("Masukan nilai uang   : "))
               print("-----------------------------------------")
               Program.mata_uang.mu(mataUang, nilai)
     else :
            print("Masukan Dengan benar")

     stop = input("Mau Menghitung Lagi? (Ya/Tidak): ")
     if stop == "ya" or stop == "Ya" or stop == "YA" :
          continue
     else:
          print("Program Selesai!")
          break      