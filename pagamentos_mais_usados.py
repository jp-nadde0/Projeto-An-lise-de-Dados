import pandas as pd
from pathlib import Path

def carregar_exibir_dados(caminho_arquivo):

    #Carrega dados de um arquivo CSV, exibe as primeiras linhas e retorna o DataFrame.

    try:
        df=pd.read_csv(caminho_arquivo)
        print("Amostra dos Dados Carregados:")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    
if __name__ == "__main__":
    caminho_do_csv = Path("Dados CSV") / "FACT_Orders.csv"
    df = carregar_exibir_dados(caminho_do_csv)
    if df is not None:
        # Imprime os nomes das colunas para depuração
        print("\nColunas disponíveis no DataFrame:")
        print(df.columns.tolist())
        print("-" * 30)
        
        try:
            # Agrupa os dados pela coluna de método de pagamento
            coluna_pagamento = 'payment'  # Usando a coluna correta identificada na depuração
            pagamentos_mais_usados = df.groupby(coluna_pagamento).size().reset_index(name='Total de Pagamentos')

            print(f"\nTabela de Métodos de Pagamento Mais Usados:")
            print(pagamentos_mais_usados)
            print("-" * 30)

            # Salva o resultado da análise em um novo arquivo CSV
            caminho_saida_csv = Path("pagamentos_mais_usados.csv")
            pagamentos_mais_usados.to_csv(caminho_saida_csv, index=False, encoding='utf-8')
            print(f"\n✅ Análise salva com sucesso em: {caminho_saida_csv}")

        except KeyError:
            print(f"\nErro: A coluna para agrupamento não foi encontrada no DataFrame. Verifique o nome da coluna e corrija o script.")
