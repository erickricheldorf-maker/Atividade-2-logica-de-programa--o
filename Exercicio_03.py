soma_total = 0
print("Por favor, informe 10 números:")
for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    soma_total += numero
    print(f"\nA soma de todos os números informados é: {soma_total}")