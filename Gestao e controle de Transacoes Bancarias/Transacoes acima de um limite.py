def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # Itera sobre cada transação na lista:
    for transacao in transacoes:
        # Verifica se o valor absoluto da transação é maior que o limite:
        if abs(transacao) > limite:
            # Adiciona a transação à lista filtrada:
            transacoes_filtradas.append(transacao)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite_str = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
limite = float(limite_str.strip()) # Converte o limite para float


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Filtra as transações que ultrapassam o limite:
resultado = filtrar_transacoes(transacoes, limite)


print(f"Transações: {resultado}")
