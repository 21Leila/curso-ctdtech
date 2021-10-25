# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
    #input salario_mensal 	input horas_trabalhadas_por_mes valor_hora=salario_mensal/ 	horas_trabalhadas_por_mes 	print valor_hora


salario_mensal = input("Qual é o seu sálario Mensal?")
horas_trabalhadas_por_mes = input("Quantas horas trabalhadas por mês?")
valor_hora = int(salario_mensal)/ int(horas_trabalhadas_por_mes)
print(valor_hora)