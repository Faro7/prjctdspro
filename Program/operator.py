# Operator Aritmatika dan logika
def operator (cara, nilai1, nilai2) :
    if cara == "1" or cara == "Penjumlahan" :
        hasil = nilai1 + nilai2 
        print(f"Hasil dari {nilai1} di tambah {nilai2} adalah : {hasil}")
    elif cara == "2" or cara == "Pengurangan" :
        hasil = nilai1 - nilai2
        print(f"Hasil dari {nilai1} di kurangi {nilai2} adalah : {hasil}")
    elif cara == "3" or cara == "Perkalian" :
        hasil = nilai1 * nilai2 
        print(f"Hasil dari {nilai1} di kali {nilai2} adalah : {hasil}")
    elif cara == "4" or cara == "Pembagian" :
        hasil = nilai1 / nilai2 
        print(f"Hasil dari {nilai1} di bagi {nilai2} adalah : {hasil}")
    elif cara == "5" or cara == "Modulus" :
        hasil = nilai1 % nilai2 
        print(f"Hasil dari {nilai1} Modulus {nilai2} adalah : {hasil}")
    elif cara == "6" or cara == "Pemangkatan" :
        hasil = nilai1 ** nilai2 
        print(f"Hasil dari {nilai1} pangkat {nilai2} adalah : {hasil}")
    elif cara == "7" or cara == "Pembagian dengan hasil Bilangan Bulat" :
        hasil = nilai1 // nilai2 
        print(f"Hasil dari {nilai1} Pembagian {nilai2} dimana hasilnya bilangan nulat yaitu : {hasil}")
    else :
        print("Masukan dengan benar")
