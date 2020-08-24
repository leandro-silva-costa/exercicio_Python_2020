valor_da_mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = valor_da_mercadoria * 0.09
valor_a_vista = valor_da_mercadoria - desconto
prestaçao_cinco = valor_da_mercadoria / 5
juros = valor_da_mercadoria * 0.17
prestação_com_juros = valor_da_mercadoria + juros
prestaçao_dez = prestação_com_juros / 10
#print(f'Para pagamento àvista: ({valor_a_vista:.0f}:{minuto:.0f}:{segundo:.0f})')
print(f'Para pagamento àvista: {valor_a_vista:.2f}')
print(f'Valor da prestação em 5X:  {prestaçao_cinco:.2f}')
print(f'Valor da prestação em 10X: {prestaçao_dez:.2f}')

