# aluno 1: Padronizar nome do filme 
def formatar(nome):
    return nome.upper()

#Aluno 2: Verificador de idade
def verificar_idade(idade):
    if idade >= 18:
        return "Autorizado"
    else:
        return "Não Autorizado"

# Aluno 3: Mensagem de retorno
def gerar_mensagem(status):
    if "status" == "Autorizado":
        return "Tenha uma otima Sessão!"
    else:
        return "Sentimos, mas voce não tem idade minima"
    
#Aluno 4: Execução do Algoritimo
filme = input("Digite o filme Escolhido: ")
idade_entrada = int(input("Digite sua idade: "))
nome_final = formatar(filme_entrada)
status_acesso = verificar_idade(idade_entrada)
mensagem = gerar_mensagem(status_acesso)