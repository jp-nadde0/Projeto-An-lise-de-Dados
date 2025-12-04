import pandas as pd
from pathlib import Path

def carregar_exibir_dados(caminho_arquivo):

    #Carrega dados de um arquivo CSV, exibe as primeiras linhas e retorna o DataFrame.

    try:
        df=pd.read_csv(caminho_arquivo)
        print("Amostra dos dados carregados:")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    
if __name__ == "__main__":
    caminho_do_csv = Path("Dados CSV") / "DIM_Delivery.csv"
    df=carregar_exibir_dados(caminho_do_csv)
    if df is not None:
        # Imprime os nomes das colunas para depuração
        print("\nColunas disponíveis no DataFrame:")
        print(df.columns.tolist())
        print("-" * 30)

        try:
            # Agrupa os dados pela coluna de status de entrega
            coluna_status = 'Status'  # Usando a coluna correta identificada na depuração
            pedidos_entregues = df[df[coluna_status] == 'Entregue']
            total_pedidos_entregues = pedidos_entregues.shape[0]

            print(f"\nTotal de Pedidos Entregues: {total_pedidos_entregues}")
            print("-" * 30)

            # --- Salva os pedidos entregues em um novo arquivo CSV ---
            caminho_saida = Path("pedidos_entregues.csv")
            pedidos_entregues.to_csv(caminho_saida, index=False, encoding='utf-8')
            print(f"✅ Dados dos pedidos entregues salvos com sucesso em: {caminho_saida}")
        except KeyError:
            print(f"\nErro: A coluna para análise não foi encontrada no DataFrame. Verifique o nome da coluna e corrija o script.")
