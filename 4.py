b1 = int(input("Введите первый член геометрической прогрессии\n"))
q = int(input("Введите первый шаг геометрической прогрессии\n"))
n = int(input("Введите какой по счету член геометрической прогрессии нужно найти\n"))
bn=b1*q**(n-1)
print(bn, " - ", str(n)+"ый член прогрессии")