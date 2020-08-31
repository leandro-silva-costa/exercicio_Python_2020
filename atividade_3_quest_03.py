print("Qual a cor do sinal de trânsito?")
resposta = input("Digite 'V' para verde, 'A' para amarelo e 'E' para vermelho: ")
if resposta == "V":
    print("Siga")
elif resposta == "A":
       print("Atenção")
elif resposta == "E":
    print("Pare")
else:
    print("Escolha 'V', 'A' ou 'E")
