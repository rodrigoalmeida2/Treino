# calcula os dias que uma pessoa tem an terra, contado os anos, meses e dias desde o último aniversário
def idade_em_dias(anos, meses, dias):
  # Considerando um ano com 365 dias e um mês com 30 dias
  dias_total = (anos * 365) + (meses * 30) + dias
  return dias_total

# Entrada de dados
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

# Chamada da função e exibição do resultado
resultado = idade_em_dias(anos, meses, dias)
print("A idade em dias é:", resultado)