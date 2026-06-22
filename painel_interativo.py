fila_espera = ["senha 0", "senha 1", "senha 2", "senha 3", "senha 4"]
senha_atual = 0
while senha_atual < len(fila_espera):
    print("\n = ============")
    print(f"Senha atual: {fila_espera[senha_atual -1]}")
    if senha_atual > 0:
        print(f"Senha anterior: {fila_espera[senha_atual -1]}")
    else:
        print("Senha anterior: Nenhuma(Primeiro socorros)")
print("=" *10)
if senha_atual + 1 < len(fila_espera):
    print(f"Próximo da fila: {fila_espera[senha_atual + 1]}")
else:
    print(f"Fila Vazia! Não há mais senhas na fila.")