# Konversi suhu
def mySuhu(temperatur, suhu):
    if temperatur == "celcius" or temperatur == 1:
            celcius = suhu
            reamur = (4/5) * suhu
            fahrenhait = ((9/5) * suhu) + 32
            kelvin = suhu + 273.15
            print(f"""
        Celcius         : {celcius}
        Reamur          : {reamur}
        Fahrenhait      : {fahrenhait}
        Kelvin          : {kelvin}
                  """)
    elif temperatur == "reamur" or temperatur == 2:
            reamur = suhu
            celcius = (5/4) * suhu
            fahrenhait = (9/4) * suhu + 32
            kelvin = (5/4) * suhu + 273
            print(f"""
        Celcius         : {celcius}
        Reamur          : {reamur}
        Fahrenhait      : {fahrenhait}
        Kelvin          : {kelvin}
                  """)
    elif temperatur == "fahrenhait"or temperatur == 3:
            fahrenhait = suhu
            celcius = 5/9 * (suhu-32)
            reamur = 4/9 * (suhu-32)
            kelvin = 5/9 * (suhu-32) + 273
            print(f"""
        Celcius         : {celcius}
        Reamur          : {reamur}
        Fahrenhait      : {fahrenhait}
        Kelvin          : {kelvin}
                  """)
    elif temperatur == "kelvin" or temperatur == 4:
            kelvin = suhu
            celcius =suhu - 273
            reamur = 4/5 * (suhu - 273)
            fahrenhait = 9/5 * (suhu-273) + 32
            print(f"""
        Celcius         : {celcius}
        Reamur          : {reamur}
        Fahrenhait      : {fahrenhait}
        Kelvin          : {kelvin}
                  """)
    else:
            print("Masukan value dengan benar!")