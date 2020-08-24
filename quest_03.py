tempo_segundo = int(input("Digite o total de segundos: "))
hora = tempo_segundo // 3600
tempo_segundo = tempo_segundo % 3600
minuto = tempo_segundo // 60
segundo = tempo_segundo % 60
print(f'Tempo total: ({hora:.0f}:{minuto:.0f}:{segundo:.0f})')
