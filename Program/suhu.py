def mySuhu(temperatur, suhu):
        #konversi from celcius
    if temperatur == "celcius":
            reamur = (4/5) * suhu
            fahrenhait = ((9/5) * suhu) + 32
            kelvin = suhu + 273.15
            print("reamur  fahrenhait  kelvin")
            print("-"*45)
            print(f"{reamur}\t{fahrenhait}\t{kelvin}")
    elif temperatur == "reamur":
            celcius = (5/4) * suhu
            fahrenhait = (9/4) * suhu + 32
            kelvin = (5/4) * suhu + 273
            print("celcius  fahrenhait  kelvin")
            print("-"*45)
            print(f"{celcius}\t{fahrenhait}\t{kelvin}")
    elif temperatur == "fahrenhait":
            celcius = 5/9 * (suhu-32)
            reamur = 4/9 * (suhu-32)
            kelvin = 5/9 * (suhu-32) + 273
            print("reamur  celcius  kelvin")
            print("-"*45)
            print(f"{reamur}\t{celcius}\t{kelvin}")
    elif temperatur == "kelvin":
            celcius =suhu - 273
            reamur = 4/5 * (suhu - 273)
            kelvin = 9/5 * (suhu-273) + 32
            print("reamur  fahrenheit  kelvin")
            print("-"*45)
            print(f"{reamur}\t{fahrenhait}\t{kelvin}")
    else:
            print("Masukan value dengan benar!")