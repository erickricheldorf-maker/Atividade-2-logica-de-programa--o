nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento

print(f"\nOlá, {nome}! Sua idade é {idade} anos.")
if idade >= 18:
    print("Voce já é de maior e pode fazer a carteira de motorista.")
elif 16 <= idade < 18:
    print("Voce já pode votar.")