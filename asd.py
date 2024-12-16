fasz2 = input("Adj meg egy ip címet: ")
fasz = fasz2.isdecimal()
if fasz == True:
    print(f"{fasz2} az integer.")
else:
    print(f"{fasz2} az string.")