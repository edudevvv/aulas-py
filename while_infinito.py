import os # Dependencia do código

# Ação que o WHILE vai processar.
acao = "y" # y = SIM | n = NAO

# Votos para fazer a PORCENTAGEM FINAL.
votos_totais = 0

# Votos de cada prato do menu.
votos_pizza = 0
votos_feijoada = 0
votos_churrasco = 0
votos_outros = 0 

# Ação que se repete infinitamente.
while acao == "y":
  # Limpando o terminal.
  os.system("cls")

  # Mostrando ao usuário as opções da enquete.
  print("""
      [Enquete Comida Favorita - Aula Python - 12/03/2025]
      
      [1] Pizza
      [2] Feijoada
      [3] Churrasco
      [4] Outros pratos
  """)

  # Questiona o usuário e aceita apenas numeros inteiros (INT).
  prato_selecionado = int(input("      [?] Qual o seu prato favorito? "))

  # Verificando o prato que o usuário escolheu.
  if prato_selecionado == 1: # Prato 1 = Pizza
    votos_pizza = votos_pizza + 1 # Adicionado um voto no prato pizza.
    votos_totais = votos_totais + 1 # Adicionando um voto no valor de votos totais.

    print("    ", "-"*42) # Multiplicando o "-" 30x vezes.    
    print(f"      Prato Escolhido: Pizza | Votos Totais: {votos_pizza}") # Mostrando o prato escolhido e a quantidade de votos.
    print("    ", "-"*42) # Multiplicando novamente

  elif prato_selecionado == 2: # Prato 2 = Feijoada
    votos_feijoada = votos_feijoada + 1 # Adicionado um voto no prato feijoada.
    votos_totais = votos_totais + 1 # Adicionando um voto no valor de votos totais.

    print("    ", "-"*42) # Multiplicando o "-" 30x vezes.    
    print(f"      Prato Escolhido: Feijoada | Votos Totais: {votos_feijoada}") # Mostrando o prato escolhido e a quantidade de votos.
    print("    ", "-"*42) # Multiplicando novamente 

  elif prato_selecionado == 3: # Prato 3 = Churrasco
    votos_churrasco = votos_churrasco + 1 # Adicionado um voto no prato churrasco.
    votos_totais = votos_totais + 1 # Adicionando um voto no valor de votos totais.

    print("    ", "-"*42) # Multiplicando o "-" 30x vezes.    
    print(f"      Prato Escolhido: Churrasco | Votos Totais: {votos_churrasco}") # Mostrando o prato escolhido e a quantidade de votos.
    print("    ", "-"*42) # Multiplicando novamente 

  elif prato_selecionado == 4: # Prato 4 = Outros pratos.
    votos_outros = votos_outros + 1 # Adicionado um voto no prato outros.
    votos_totais = votos_totais + 1 # Adicionando um voto no valor de votos totais.

    print("    ", "-"*42) # Multiplicando o "-" 30x vezes.    
    print(f"      Prato Escolhido: Outros | Votos Totais: {votos_outros}") # Mostrando o prato escolhido e a quantidade de votos.
    print("    ", "-"*42) # Multiplicando novamente 

    
  acao = str(input("      [?] Deseja votar em outro prato? [y/n]: ")) # Atribuindo um novo valor a variavel "ACAO"

if acao == "n": 
  # Limpar o terminal
  os.system("cls")

  # Calcular a porcentagem de cada prato.
  prato_pizza = (votos_pizza / votos_totais) * 100
  prato_feijoada = (votos_feijoada / votos_totais) * 100
  prato_churrasco = (votos_churrasco / votos_totais) * 100
  prato_outros = (votos_outros / votos_totais) * 100

  # Exibindo os resultados ao usuário.
  # ROUND = Arredonda o valor com apenas 2 casas após o decimal.
  print(f"""
      [Enquete Comida Favorita - Aula Python - 12/03/2025]
        
      [!] Você finalizou a enquete, abaixo vai estar os resultados.
        
      [1] Pizza: {votos_pizza} votos e foi escolhido por {round(prato_pizza, 2)}% das pessoas.
      [2] Feijoada: {votos_feijoada} votos e foi escolhido por {round(prato_feijoada, 2)}% das pessoas.
      [3] Churrasco: {votos_churrasco} votos e foi escolhido por {round(prato_churrasco, 2)}% das pessoas.
      [4] Outros: {votos_outros} votos e foi escolhido por: {round(prato_outros, 2)}% das pessoas.
  """)