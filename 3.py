m = int(input("Введите массу\n"))
h = int(input("Введите высоту\n"))
G = 6.67 * 10**(-11)
M = 6*10**24
R = 6371 * 10**3
Ft = G * ((M * m)/((R + h)**2))
Ft = str(Ft)
for i in range(0,len(Ft)):
    if Ft[i] == '.':
        break
print(Ft[0:i]," - сила тяжести")
