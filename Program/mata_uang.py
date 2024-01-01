# Konversi Mata uang
def mu(mataUang, nilai):
     if mataUang == "KWD" or mataUang == 1:
          kwd = nilai
          idr = kwd * 50.100
          bhd = kwd * 1.227
          omr = kwd *1.252
          jod = kwd * 2.307
          gbp = kwd * 2.56
          gip = kwd * 2.56
          kyd = kwd * 2.67
          chf = kwd * 2.74
          eur = kwd * 2.95
          usd = kwd * 3.25
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "omr" or mataUang == 3:
          omr = nilai
          idr = omr * 40.018
          bhd = omr * 0.980
          kwd = omr * 0.799
          jod = omr * 1.843
          gbp = omr * 2.04
          gip = omr * 2.04
          kyd = omr * 2.13
          chf = omr * 2.19
          eur = omr * 2.35
          usd = omr * 2.60
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "bhd"or mataUang == 2:
          bhd = nilai
          idr = bhd * 40.843
          kwd = bhd * 0.815
          omr = bhd / 0.980
          jod = bhd * 1.881
          gbp = bhd * 2.08
          gip = bhd * 2.08
          kyd = bhd * 2.18
          chf = bhd * 2.23
          eur = bhd * 2.40
          usd = bhd * 2.65
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "jod" or mataUang == 4:
          jod = nilai
          idr = jod * 21.716
          bhd = jod * 0.532
          omr = jod * 0.543
          kwd = jod * 0.433
          gbp = jod *1.11
          gip = jod * 1.11
          kyd = jod * 1.16
          chf = jod * 1.19
          eur = jod * 1.28
          usd = jod * 1.41
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "gbp" or mataUang == 5:
          gbp = nilai
          idr = gbp * 19.602
          bhd = gbp * 0.480
          omr = gbp * 0.490
          jod = gbp * 0.903
          kwd = gbp * 0.391
          gip = gbp * 1
          kyd = gbp * 1.04
          chf = gbp * 1.07
          eur = gbp * 1.15
          usd = gbp * 2.55
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "gip"or mataUang == 6:
          gip = nilai
          idr = gip * 19.602
          bhd = gip * 0.480
          omr = gip * 0.490
          jod = gip * 0.903
          gbp = gip * 1
          kwd = gip * 0.391
          kyd = gip *1.04
          chf = gip * 1.07
          eur = gip * 1.15
          usd = gip * 1.27315
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "kyd"or mataUang == 7:
          kyd = nilai
          idr = kyd * 18.776
          bhd = kyd * 0.460
          omr = kyd * 0.469
          jod = kyd * 0.865
          gbp = kyd * 0.96
          gip = kyd * 0.96
          kwd = kyd * 0.375
          chf = kyd * 1.03
          eur = kyd * 1.10
          usd = kyd * 1.20
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "chf"or mataUang == 8:
          chf = nilai
          idr = chf * 18.297
          bhd = chf * 0.448
          omr = chf * 0.457
          jod = chf * 0.843
          gbp = chf * 0.093
          gip = chf * 0.93
          kyd = chf * 0.97
          kwd = chf * 0.365
          eur = chf * 1.08
          usd = chf * 1.19
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "eur" or mataUang == 9:
          eur = nilai
          idr = eur * 16.993
          bhd = eur * 0.416
          omr = eur * 0.425
          jod = eur * 0.783
          gbp = eur * 0.87
          gip = eur * 0.87
          kyd = eur * 0.91
          chf = eur * 0.93
          kwd= eur * 0.339
          usd = eur * 1.11
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "idr"or mataUang == 11:
          idr = nilai
          kwd = idr * 50.100
          bhd = idr * 40.843
          omr = idr * 40.018
          jod = idr * 21.716
          gbp = idr * 19.602
          gip = idr * 19.602
          kyd = idr * 18.776
          chf = idr * 19.297
          eur = idr * 16.993
          usd = idr * 0.000065
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     elif mataUang == "USD"  or mataUang == 10 :
          usd = nilai
          kwd = usd * 0.31
          bhd = usd * 0.38
          omr = usd * 0.38
          jod = usd * 0.71
          gbp = usd * 0.78
          gip = usd * 0.78468
          kyd = usd * 0.83
          chf = usd * 0.84
          eur = usd * 0.90
          idr = usd * 15.390,10
          print(f"""
     1. Dinar Kuwait          : {kwd}
     2. Dinar Bahrain         : {bhd}
     3. Rial Oman             : {omr}
     4. Dinar Yordania        : {jod}
     5. British Pound         : {gbp}
     6. Gibraltar Pound       : {gip}
     7. Cayman Island Dollar  : {kyd}
     8. Swiss Franc           : {chf}
     9. Eur                   : {eur}
     10. United States Dollar : {usd}
     10. Indonesia            : {idr}
""")
     else : 
          print("Masukan dengan benar")