import os
from colorama import init, Fore

notas_disponiveis = [5.00, 2.00, 1.00, 0.5, 0.25, 0.1, 0.05, 0.01]

def calcular_troco(valor_mercadoria: float, valor_pago: float): 
  troco = valor_pago - valor_mercadoria 

  if troco < 0:
    os.system("cls")
    print(f"        {Fore.YELLOW}[!]{Fore.RESET} {Fore.LIGHTBLACK_EX}Valor insulficiente. Falta {abs(troco):.2f} {"reais" if abs(troco) >= 2 else "real"} para completar o pagamento.{Fore.RESET}")
  elif troco == 0:
    os.system("cls")
    print(f"        {Fore.GREEN}[+]{Fore.RESET} {Fore.LIGHTBLACK_EX}Não existe troco para a compra. Volte sempre.{Fore.RESET}")
  else:
     for valor in notas_disponiveis:
       quantidade = int(troco // valor)
       if quantidade > 0:
         if valor >= 2:
           print(f"        {Fore.RED}[-]{Fore.RESET} {Fore.LIGHTBLACK_EX}Será preciso devolver {quantidade} nota(s) de {valor:.2f} reais para o cliente, totalizando: {troco:.2f} {"reais" if abs(troco) >= 2 else "real"}.{Fore.RESET}")
         else:
          verificar = "centavo" if valor == 0.01 else "real" if valor >= 1 else "centavos"
          print(f"        {Fore.RED}[-] {Fore.LIGHTBLACK_EX}Será preciso devolver {quantidade} moeda(s) de {valor:.2f} {verificar} para o cliente, totalizando: {troco:.2f} {verificar}.{Fore.RESET}")
               
         troco -= quantidade * valor
         troco = round(troco, 2)

if __name__ == "__main__":
    init(autoreset=True)
    os.system("cls")

    print(f"""
        {Fore.LIGHTBLACK_EX}[Supermercado ThreeBond]{Fore.RESET}
        
        {Fore.YELLOW}[1]{Fore.RESET} {Fore.LIGHTBLACK_EX}Calcular Troco{Fore.RESET}
        {Fore.YELLOW}[0]{Fore.RESET} {Fore.LIGHTBLACK_EX}Sair{Fore.RESET}
    """)
    
    opcao = int(input(f"        {Fore.YELLOW}[?]{Fore.RESET} {Fore.LIGHTBLACK_EX}Escolha uma ação para continuar:{Fore.RESET} "))
    if opcao == 0:
      os._exit()
    elif opcao == 1: 
      os.system("cls")

      valor_mercadoria = float(input(f"        {Fore.GREEN}[$]{Fore.RESET} {Fore.LIGHTBLACK_EX}Valor da Mercadoria:{Fore.RESET} "))
      valor_pago = float(input(f"        {Fore.GREEN}[$]{Fore.RESET} {Fore.LIGHTBLACK_EX}Valor Pago:{Fore.RESET} "))

      calcular_troco(valor_mercadoria, valor_pago)