num_01 = int(input("Digite o primeiro número: "))
num_02 = int(input("Digite o segundo número: "))
num_03 = int(input("Digite o terceiro número: "))
num_04 = int(input("Digite o quarto número: "))
num_05 = int(input("Digite o quinto número: "))
numeros = num_01 , num_02 , num_03 , num_04 , num_05
maior = max(numeros)
menor = min(numeros)
soma = maior + menor
media = soma/2
print(f'O maior número é: {maior:.0f}')
print(f'O menor número é: {menor:.0f}')
print(f'A média é igual a: {media:.0f}')

