juros = float(input("Indique os juros: "))
periodo = int(input("Indique o período a ser pago: "))
capital = float(input("Indique o capital do pago: "))
for periodo in range(0, periodo):
    res_juros = (juros /100) * capital
    capital=capital + res_juros
    print(periodo +1, "° será pago ",capital