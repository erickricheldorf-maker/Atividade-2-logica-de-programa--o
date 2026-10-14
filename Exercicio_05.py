soma_pares = 0
qtd_pares = 0

for i in range(5):
    numero = int(input(f"Informe o {i + 1}º número: "))

    if numero % 2 == 0:
        soma_pares += numero
        qtd_pares += 1

if qtd_pares > 0:
    media = soma_pares / qtd_pares
    print(f"Média dos números pares: {media:.2f}")
else:
    print("Nenhum número par foi digitado, não é possível calcular a média.")