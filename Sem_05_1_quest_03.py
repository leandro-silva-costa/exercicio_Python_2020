n = int(input(''))
soma = 0
media = soma//100

for n in range(n, n+100):
    print(n, end=' ')
    soma = soma + n
media = soma//100
print(f'Média: {media}')
        
