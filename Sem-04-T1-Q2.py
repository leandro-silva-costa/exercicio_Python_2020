def data1():
    d1 = int(input("Digite o dia: "))
    m1 = int(input("Digite o mes: "))
    a1 = int(input("Digite o ano: "))
def data2():
    d2 = int(input("Digite o dia: "))
    m2 = int(input("Digite o mes: "))
    a2 = int(input("Digite o ano: "))
def data3():
    d3 = int(input("Digite o dia: "))
    m3 = int(input("Digite o mes: "))
    a3 = int(input("Digite o ano: "))

data1 = d1 + m1 + a1
data2 = d2 + m2 + a2
data3 = d3 + m3 + a3
data_recente = max(data1, data2, data3)
print("A data mais recente é: ", data_recente)


data1()
data2()
data3()
