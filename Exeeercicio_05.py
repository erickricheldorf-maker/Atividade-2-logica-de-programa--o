nome_mais_velho = ""
idade_mais_velha = 0

for i in range(5):
    nome = input(f"Informe o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Informe a idade de {nome}: "))

    if i == 0 or idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velho = nome

print(f"Pessoa mais velha: {nome_mais_velho}")
print(f"Idade: {idade_mais_velha} anos")