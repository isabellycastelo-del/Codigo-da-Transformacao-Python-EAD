# ==========================================
# ATIVIDADE 03: Validação de Entrada de Usuário
# ==========================================

def solicitar_idade_valida():
    """
    Solicita a idade do usuário e valida se a entrada é um número inteiro positivo.
    
    Retorna:
    - int: A idade validada do usuário.
    """
    while True:
       
        entrada = input("Por favor, digite a sua idade: ")
        
        try:
            
            idade = int(entrada)
            
            
            if idade <= 0:
                print("Erro: A idade deve ser um número inteiro positivo (maior que zero).\n")
                continue # Volta para o início do loop para pedir a entrada novamente
            
           
            return idade

        except ValueError:
           
            print("Erro: Entrada inválida! Por favor, digite apenas números inteiros.\n")


# ==========================================
# EXECUÇÃO E TESTES DO CÓDIGO
# ==========================================
if __name__ == "__main__":
    print("--- Teste da Atividade 3: Validação de Idade ---\n")
    
    # Chama a função e armazena o resultado validado
    idade_confirmada = solicitar_idade_valida()
    
    print(f"\nSucesso! Idade de {idade_confirmada} anos registrada no sistema.")