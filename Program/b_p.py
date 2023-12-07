def pj(panjang, value):
     if panjang == "km":
          km = value
          hm = value * 10
          dam = value * 100
          m = value * 1000
          dm = value * 10000
          cm = value * 100000
          mm = value * 1000000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "hm":
          km = value / 10
          hm = value
          dam = value * 10
          m = value * 100
          dm = value * 1000
          cm = value * 10000
          mm = value * 100000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "dam":
          km = value / 100
          hm = value / 10
          dam = value
          m = value * 10
          dm = value * 100
          cm = value * 1000
          mm = value * 10000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "m":
          km = value / 1000
          hm = value / 100
          dam = value / 10
          m = value 
          dm = value * 10
          cm = value * 100
          mm = value * 1000
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "dm":
          km = value / 10000
          hm = value / 1000
          dam = value / 100
          m = value / 10
          dm = value 
          cm = value * 10
          mm = value * 100
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "cm":
          km = value / 100000
          hm = value / 10000
          dam = value / 1000
          m = value / 100
          dm = value /10
          cm = value 
          mm = value * 10
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     elif panjang == "mm":
          km = value / 1000000
          hm = value / 100000
          dam = value / 10000
          m = value / 1000
          dm = value /100
          cm = value / 10
          mm = value
          print(f"km\thm\tdam\tm\tdm\tcm\tmm\n")
          print("-"*65)
          print(f"{km}\t{hm}\t{dam}\t{m}\t{dm}\t{cm}\t{mm}")
     
def pb(berat, value):
      if berat == "kg":
          kg = value
          hg = value * 10
          dag = value * 100
          g = value * 1000
          dg = value * 10000
          cg = value * 100000
          mg = value * 1000000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
      elif berat == "hg":
          kg = value / 10
          hg = value
          dag = value * 10
          g = value * 100
          dg = value * 1000
          cg = value * 10000
          mg = value * 100000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
      elif berat == "dag":
          kg = value / 100
          hg = value / 10
          dag = value
          g = value * 10
          dg = value * 100
          cg = value * 1000
          mg = value * 10000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
      elif berat == "g":
          kg = value / 1000
          hg = value / 100
          dag = value / 10
          g = value 
          dg = value * 10
          cg = value * 100
          mg = value * 1000
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
      elif berat == "dg":
          kg = value / 10000
          hg = value / 1000
          dag = value / 100
          g = value / 10
          dg = value 
          cg = value * 10
          mg = value * 100
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
      elif berat == "cg":
          kg = value / 100000
          hg = value / 10000
          dag = value / 1000
          g = value / 100
          dg = value /10
          cg = value 
          mg = value * 10
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
      elif berat == "mg":
          kg = value / 1000000
          hg = value / 100000
          dag = value / 10000
          g = value / 1000
          dg = value /100
          cg = value / 10
          mg = value
          print(f"kg\thg\tdag\tg\tdg\tcg\tmg\n")
          print("-"*65)
          print(f"{kg}\t{hg}\t{dag}\t{g}\t{dg}\t{cg}\t{mg}")
      else:
        print("Masukan dengan benar!")