#---simulador de investimento---
aparte = float(input("Quanto vc vai depositar por mes? "))
juros = float(input("Qual a taxa de juros da poupança? "))
meses = int(input("Por quantos meses vc ira investir? "))
juros_decimal = juros/100
total = 0
for mes in range (1, meses +1):
    total = total+aparte
    total = total+(total*juros_decimal)
    print(f"Mes {mes}: Saldo total: R${total}")
print(f"Ao final {meses} meses, Voce tera o valor de R$:{total:2f}")

