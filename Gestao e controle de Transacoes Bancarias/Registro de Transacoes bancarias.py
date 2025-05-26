''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    saldo = 0  # Inicializa o saldo
    # Itera sobre cada transacao na lista de transacoes
    for transacao in transacoes:
        saldo += transacao  # Adiciona o valor da transacao ao saldo
    
    # Retorna o saldo formatado em moeda brasileira com duas casas decimais
    return f"Saldo: R$ {saldo:.2f}"

# A linha abaixo é responsável por garantir que o código dentro do if seja executado apenas
# quando o script é rodado diretamente, e não quando é importado como módulo.
if __name__ == "__main__":
    # Lê a entrada do usuário (a lista de transações como string)
    entrada_usuario = input()

    # Remove os colchetes e espaços, depois divide a string pelos separadores de vírgula
    # para criar uma lista de strings representando os valores.
    # Converte cada valor da string para float.
    transacoes_str = entrada_usuario.strip("[]").replace(" ", "")
    
    # Verifica se a string de transações não está vazia antes de tentar dividir
    if transacoes_str: 
        transacoes = [float(valor) for valor in transacoes_str.split(",")]
    else:
        transacoes = [] # Lista vazia se a entrada for vazia

    # Calcula o saldo com base nas transações informadas:
    resultado = calcular_saldo(transacoes)

    # Imprime o resultado
    print(resultado)
