#Etapa 1, calculo de IMC
def cal_imc(peso,altura):
    imc = peso / (altura * altura)
    return imc
#Etapa 2, Classicar o IMC
def classificar_imc(valor_imc):
    if valor_imc >= 25:
        return 'ACIMA DO PESO'
    else:
        return 'PESO NORMAL'
    
#Etapa 3- Mensagem de saida
def mensagem(status):
    if status == "ACIMA DO PESO":
        return 'ATENÇÃO, PROCURE UM MEDICO'
    else:
        return 'Muito bom, continue assim!'
#Etapa 4- intregração do projeto
valor_peso = float(input("Digite o seu peso atual: "))
valor_altura = float(input("Digite sua Altura: "))
resultado = cal_imc (valor_peso, valor_altura)
classificar = classificar_imc(resultado)
saida = mensagem(classificar)

print("=" * 50)
print(f"Seu IMC é {resultado: . 1f}")
print(f"{saida}")
print("=" * 50)
