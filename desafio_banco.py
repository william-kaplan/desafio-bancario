menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("---------- Depósito ----------")
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        
        if valor_deposito <= 0:
            print("Valor inválido, por favor selecione novamente a operação desejada.")
        else:
            saldo += valor_deposito
            extrato += f"\nDepósitado: R$ {valor_deposito:.2f}"
            print("Depósito realizado com sucesso!")
        print("------------------------------")
            
    elif opcao == "s":
        print("---------- Sacar ----------")
        valor_saque = float(input("Informe o valor do saque: R$ "))
        
        if numero_saques >= LIMITE_SAQUE:
            print(f"Limite de {LIMITE_SAQUE} saques diários atingido, por favor selecione novamente a operação desejada.")
        elif valor_saque > limite:
            print(f"Valor acima do limite de R$ {limite:.2f} permitido, por favor selecione novamente a operação desejada.")
        elif valor_saque <= 0:
            print("Valor inválido, por favor selecione novamente a operação desejada.")
        elif valor_saque > saldo:
            print("Saldo indiponível, por favor selecione novamente a operação desejada.")
        else: 
            saldo -= valor_saque 
            numero_saques += 1
            extrato += f"\nSaque: - R$ {valor_saque:.2f}"
            print("Saque realizado com sucesso!")
        print("---------------------------")

            
    elif opcao == "e":
        print("---------- Extrato ----------")
        print(extrato)
        print(f"\nSaldo: R$ {saldo}")
        print("-----------------------------")
                
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")