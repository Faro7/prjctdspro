# Konversi Panjang dan Berat 
def pj(panjang, value):
     if panjang == "km" or panjang == 1:
          km = value
          hm = value * 10
          dam = value * 100
          m = value * 1000
          dm = value * 10000
          cm = value * 100000
          mm = value * 1000000
          print(f"""
      Kilometer   : {km}
      Hektometer  : {hm}
      Dekameter   : {dam}
      Meter       : {m}
      Desimeter   : {dm}
      Centimeter  : {cm}
      Milimeter   : {mm}
""")
     elif panjang == "hm" or panjang == 2:
          km = value / 10
          hm = value
          dam = value * 10
          m = value * 100
          dm = value * 1000
          cm = value * 10000
          mm = value * 100000
          print(f"""
      Kilometer   : {km}
      Hektometer  : {hm}
      Dekameter   : {dam}
      Meter       : {m}
      Desimeter   : {dm}
      Centimeter  : {cm}
      Milimeter   : {mm}
""")
     elif panjang == "dam" or panjang == 3:
          km = value / 100
          hm = value / 10
          dam = value
          m = value * 10
          dm = value * 100
          cm = value * 1000
          mm = value * 10000
          print(f"""
      Kilometer   : {km}
      Hektometer  : {hm}
      Dekameter   : {dam}
      Meter       : {m}
      Desimeter   : {dm}
      Centimeter  : {cm}
      Milimeter   : {mm}
""")
     elif panjang == "m"  or panjang == 4:
          km = value / 1000
          hm = value / 100
          dam = value / 10
          m = value 
          dm = value * 10
          cm = value * 100
          mm = value * 1000
          print(f"""
      Kilometer   : {km}
      Hektometer  : {hm}
      Dekameter   : {dam}
      Meter       : {m}
      Desimeter   : {dm}
      Centimeter  : {cm}
      Milimeter   : {mm}
""")
     elif panjang == "dm" or panjang == 5:
          km = value / 10000
          hm = value / 1000
          dam = value / 100
          m = value / 10
          dm = value 
          cm = value * 10
          mm = value * 100
          print(f"""
      Kilometer   : {km}
      Hektometer  : {hm}
      Dekameter   : {dam}
      Meter       : {m}
      Desimeter   : {dm}
      Centimeter  : {cm}
      Milimeter   : {mm}
""")
     elif panjang == "cm" or panjang == 6:
          km = value / 100000
          hm = value / 10000
          dam = value / 1000
          m = value / 100
          dm = value /10
          cm = value 
          mm = value * 10
          print(f"""
      Kilometer   : {km}
      Hektometer  : {hm}
      Dekameter   : {dam}
      Meter       : {m}
      Desimeter   : {dm}
      Centimeter  : {cm}
      Milimeter   : {mm}
""")
     elif panjang == "mm" or panjang == 7:
          km = value / 1000000
          hm = value / 100000
          dam = value / 10000
          m = value / 1000
          dm = value /100
          cm = value / 10
          mm = value
          print(f"""
      Kilometer   : {km}
      Hektometer  : {hm}
      Dekameter   : {dam}
      Meter       : {m}
      Desimeter   : {dm}
      Centimeter  : {cm}
      Milimeter   : {mm}
""")
          
def pb(berat, value):
      if berat == "kg" or berat == 1:
          kg = value
          hg = value * 10
          dag = value * 100
          g = value * 1000
          dg = value * 10000
          cg = value * 100000
          mg = value * 1000000
          print(f"""
      Kilogram   : {kg}
      Hektogram  : {hg}
      Dekagram   : {dag}
      Gram       : {g}
      Desigram   : {dg}
      Sentigram  : {cg}
      Miligram   : {mg}
""")
      elif berat == "hg" or berat == 2:
          kg = value / 10
          hg = value
          dag = value * 10
          g = value * 100
          dg = value * 1000
          cg = value * 10000
          mg = value * 100000
          print(f"""
      Kilogram   : {kg}
      Hektogram  : {hg}
      Dekagram   : {dag}
      Gram       : {g}
      Desigram   : {dg}
      Sentigram  : {cg}
      Miligram   : {mg}
""")
      elif berat == "dag" or berat == 3:
          kg = value / 100
          hg = value / 10
          dag = value
          g = value * 10
          dg = value * 100
          cg = value * 1000
          mg = value * 10000
          print(f"""
      Kilogram   : {kg}
      Hektogram  : {hg}
      Dekagram   : {dag}
      Gram       : {g}
      Desigram   : {dg}
      Sentigram  : {cg}
      Miligram   : {mg}
""")
      elif berat == "g" or berat == 4:
          kg = value / 1000
          hg = value / 100
          dag = value / 10
          g = value 
          dg = value * 10
          cg = value * 100
          mg = value * 1000
          print(f"""
      Kilogram   : {kg}
      Hektogram  : {hg}
      Dekagram   : {dag}
      Gram       : {g}
      Desigram   : {dg}
      Sentigram  : {cg}
      Miligram   : {mg}
""")
      elif berat == "dg" or berat == 5:
          kg = value / 10000
          hg = value / 1000
          dag = value / 100
          g = value / 10
          dg = value 
          cg = value * 10
          mg = value * 100
          print(f"""
      Kilogram   : {kg}
      Hektogram  : {hg}
      Dekagram   : {dag}
      Gram       : {g}
      Desigram   : {dg}
      Sentigram  : {cg}
      Miligram   : {mg}
""")
      elif berat == "cg" or berat == 6:
          kg = value / 100000
          hg = value / 10000
          dag = value / 1000
          g = value / 100
          dg = value /10
          cg = value 
          mg = value * 10
          print(f"""
      Kilogram   : {kg}
      Hektogram  : {hg}
      Dekagram   : {dag}
      Gram       : {g}
      Desigram   : {dg}
      Sentigram  : {cg}
      Miligram   : {mg}
""")
      elif berat == "mg" or berat == 7:
          kg = value / 1000000
          hg = value / 100000
          dag = value / 10000
          g = value / 1000
          dg = value /100
          cg = value / 10
          mg = value
          print(f"""
      Kilogram   : {kg}
      Hektogram  : {hg}
      Dekagram   : {dag}
      Gram       : {g}
      Desigram   : {dg}
      Sentigram  : {cg}
      Miligram   : {mg}
""")
      else:
        print("Masukan dengan benar!")