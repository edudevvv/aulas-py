# [2/3] Questão sobre eleição e porcentagem da votação.

import os # Dependencia do código.
import time # Dependencia do código.

# Variaveis da votação.
votos_eymael = 0
votos_levy = 0
votos_cabo = 0

votos_nulo = 0
votos_branco = 0
votos_totais = 0

# Sistema de Votação
while True:
  os.system("cls") # Limpar o terminal.

  # Mostrar as opções de candidatos.
  print("""
    [Eleição Presidencial - 3 Candidatos]
   
    [1] Eymael
    [2] Levy Fidelix
    [3] Cabo Daciolo
    [4] Voto Nulo
    [5] Voto em Branco
    [0] Finalizar votação
    
    [!] Lembre-se: Seu voto é SECRETO, não revele a ninguém.
  """) 

  # Questiona o usuário sobre a escolha.
  try: 
    escolha = int(input("    [?] Digite o número do candidato: "))
  except ValueError:
    os.system("cls") # Limpar terminal.
    print("    [!] Os votos devem ser apenas número de 1 à 5.")

    continue

  if escolha in [0, 1, 2, 3, 4, 5]:
        print("    ", "-" * 42)

        confirmacao = str(input("    [?] Deseja confirmar seu voto? <y/n>: ")).lower()
        if confirmacao == "y":
          if escolha == 1:
            votos_eymael = votos_eymael + 1 # Adicionando um voto ao candidato.
            votos_totais = votos_totais + 1 # Adicionando um voto ao total.

            print("    [*] Você votou no candidato EYMAEL.")
            time.sleep(1)
          elif escolha == 2:
            votos_levy = votos_levy + 1 # Adicionando um voto ao candidato.
            votos_totais = votos_totais + 1 # Adicionando um voto ao total.

            print("    [*] Você votou no candidato LEVY FIDELIX.")
            time.sleep(1)
          elif escolha == 3:
            votos_cabo = votos_cabo + 1 # Adicionando um voto ao candidato.
            votos_totais = votos_totais + 1 # Adicionando um voto ao total.

            print("    [*] Você votou no candidato CABO DACIOLO.")
            time.sleep(1)
          elif escolha == 4: 
            votos_nulo = votos_nulo + 1 # Adicionando um voto nulo.
            votos_totais = votos_totais + 1 # Adicionando um voto ao total.

            print("    [*] Você votou NULO, sem candidatos.")
            time.sleep(1)
          elif escolha == 5:
            votos_branco = votos_branco + 1 # Adicionando um voto branco.
            votos_totais = votos_totais + 1 # Adicionando um voto ao total.

            print("    [*] Você votou BRANCO, sem candidatos.")
            time.sleep(1)
          elif escolha == 0:
            os.system("cls") # Limpar terminal.

            # Calcular a porcentagem de cada candidato.
            candidato_eymael = (votos_eymael / votos_totais) * 100 # Votos Eymael
            candidato_levy = (votos_levy / votos_totais) * 100 # Votos Levy Fidelix
            candidato_cabo = (votos_cabo / votos_totais) * 100 # Votos Cabo Daciolo
            candidato_nulo = (votos_nulo / votos_totais) * 100 # Votos Nulos
            candidato_branco = (votos_branco / votos_totais) * 100 # Votos em Branco

            print(f"""
              [Apuração Votos Eleitorais - 3 Candidatos]

              [*] Total de Votos: {votos_totais}
              [1] Votos Eymael: {votos_eymael} voto(s) - {round(candidato_eymael, 2)}%  
              [2] Votos Levy Fidelix: {votos_levy} voto(s) - {round(candidato_levy, 2)}%    
              [3] Votos Cabo Daciolo: {votos_cabo} voto(s) - {round(candidato_cabo, 2)}% 
              [4] Votos Nulos: {votos_nulo} voto(s) - {round(candidato_nulo, 2)}% 
              [5] Votos em Branco: {votos_branco} voto(s) - {round(candidato_branco, 2)}% 
            """)

            break
        else: 
           print("    [!] Voto cancelado.")
           time.sleep(1)
  else:
    print("    [!] Número inválido, temos apenas de 1 à 5.")
    time.sleep(1)