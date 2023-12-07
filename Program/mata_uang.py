def mu(mataUang, nilai):
     if mataUang == "USA" or mataUang == "usa":
          usa = nilai
          idn = 16000*nilai
          dinar = 16000*nilai
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     elif mataUang =="idn" or mataUang == "IDN":
          idn = nilai
          usa = nilai / 16000
          dinar = nilai / 5000
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     elif mataUang == "DINAR" or mataUang == "dinar":
          idn = nilai*3500
          usa = nilai*13000
          dinar = nilai
          print(f"indonesia dinar \t usa\n")
          print("-"*65)
          print(f"{idn}\t {dinar} \t {usa}")
     else:
          print("Masukan mata uang yang telah di tentukan")