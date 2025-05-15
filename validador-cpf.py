# [1/3] Questão sobre validação de CPF através de calculo.

import os # Dependencia do código.
os.system("cls") # Limpar o terminal.

try: 

  print("[!] O cpf deve seguir o seguinte formato: 00000000000\n") # Mostrar como deve ser inserido ao usuário.
  cpf = int(input("[?] Digite o seu cpf: ")) # Pedindo o CPF do usuário.

  if len(str(cpf)) < 11:
    os.system("cls") # Limpar o terminal.
    
    print("[!] O cpf possui menos que 11 caracteres.") # Mostrar o alerta do erro.
  elif len(str(cpf)) > 11: 
    os.system("cls") # Limpar o terminal.
    
    print("[!] O cpf possui mais que 11 caracteres.") # Mostrar o alerta do erro.
  else:  
    # cpf[:9] = Primeiro parametro do CPF (9 digitos).
    # cpf[9:] = Segundo parametro do CPF (2 digitos).
    cpf_primeiro_parametro = [int(digito) for digito in str(cpf)[:9]] # Nesta parte vou separar todo o cpf, numero por numero e vai ficar da seguinte forma: [0, 0, 0, 0, 0, 0, 0, 0, 0].
    cpf_segundo_parametro = [int(digito) for digito in str(cpf)[9:]] # Vou realizar a mesma ação porém com os dois ultimos digitos: [0, 0].

    # Calculando os primeiros 9 digitos do cpf separadamente.
    primeiro_calculo = cpf_primeiro_parametro[0] * 10 + cpf_primeiro_parametro[1] * 9 + cpf_primeiro_parametro[2] * 8 + cpf_primeiro_parametro[3] * 7 + cpf_primeiro_parametro[4] * 6 + cpf_primeiro_parametro[5] * 5 + cpf_primeiro_parametro[6] * 4 + cpf_primeiro_parametro[7] * 3 + cpf_primeiro_parametro[8] * 2 
    # Calculando o resto da divisão inteira.
    primeiro_calculo_mod = (primeiro_calculo * 10) % 11 

    # Calculando a segunda parte do cpf separadamente.
    segundo_calculo = cpf_primeiro_parametro[0] * 11 + cpf_primeiro_parametro[1] * 10 + cpf_primeiro_parametro[2] * 9 + cpf_primeiro_parametro[3] * 8 + cpf_primeiro_parametro[4] * 7 + cpf_primeiro_parametro[5] * 6 + cpf_primeiro_parametro[6] * 5 + cpf_primeiro_parametro[7] * 4 + cpf_primeiro_parametro[8] * 3 + cpf_segundo_parametro[0] * 2
    # Calculando o resto da divisão inteira. Caso dê 10, é considera o numero 0.
    segundo_calculo_mod = (segundo_calculo * 10) % 11
    
    # Caso o resultado do segundo calculo de mod seja 10, ele atribui o valor de 0.
    if segundo_calculo_mod == 10:
      segundo_calculo_mod = 0

    os.system("cls") # Limpar terminal.
    if segundo_calculo_mod == cpf_segundo_parametro[1]:
      print("[>] Seu cpf foi validado com sucesso :)") # Retornando a resposta ao usuário.
    else: 
      print("[!] Infelizmente seu cpf é inválido.") # Retornando a resposta ao usuário.
except ValueError as error:
  os.system("cls") # Limpar o terminal.
  print("[!] O cpf deve conter apenas números.") # Retornando o erro formatado.