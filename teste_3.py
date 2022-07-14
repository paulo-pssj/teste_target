"""
 Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
	• O menor valor de faturamento ocorrido em um dia do mês;
	• O maior valor de faturamento ocorrido em um dia do mês;
	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

arquivo = open('dados.json')

dados = json.load(arquivo)

maior_faturamento = dados[0]['valor']
menor_faturamento = dados[0]['valor']
qtd_dias = 0
qtd_dias_faturamento_maior_media = 0
total_faturamento = 0

for dado in dados:
    if dado['valor'] != 0.0:
        if dado['valor'] > maior_faturamento:
            maior_faturamento = dado['valor']

        if dado['valor'] < menor_faturamento:
            menor_faturamento = dado['valor']
        
        total_faturamento += dado['valor']
        qtd_dias += 1

media_faturamento = total_faturamento / qtd_dias

for dado in dados:
    if dado['valor'] > media_faturamento:
        qtd_dias_faturamento_maior_media += 1
        


print(f" Menor Faturamento: {menor_faturamento}\n Maior Faturamento: {maior_faturamento}\n Número de dias em que o valor do faturamento foi maior que a média mensal: {qtd_dias_faturamento_maior_media}")
    
    
    