#Escreva um programa que leia 5 números inteiros e escreva
#o maior e o menor deles. Considere que todos os valores
#são diferentes. NÃO use as funções embutidas min() e max().

def numeros():
    n1 = input("Digite o 1a numero: ")
    n2 = input("Digite o 2a numero: ")
    n3 = input("Digite o 3a numero: ")
    n4 = input("Digite o 4a numero: ")
    n5 = input("Digite o 5a numero: ")
    
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        print('o maior numero é:' ,n1)
    if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        print('o maior numero é:' ,n2)
    if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        print('o maior numero é:' ,n3)
    if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        print('o maior numero é:' ,n4)
    if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        print('o maior numero é:' , n5)


    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        print('o menor numero é:' , n1)
    if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        print('o menor numero é:' , n2)
    if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        print('o menor numero é:' , n3)
    if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        print('o menor numero é:' , n4)
    if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        print('o menor numero é:' , n5)

   


numeros()
