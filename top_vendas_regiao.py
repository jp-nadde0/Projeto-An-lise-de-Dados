import pandas as pd
from pathlib import Path

def carregar_e_exibir_dados(caminho_arquivo):
    """
    Carrega dados de um arquivo CSV, exibe as primeiras linhas e retorna o DataFrame.
    """
    try:
        df = pd.read_csv(caminho_arquivo)
        print("Amostra dos dados carregados:")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None

if __name__ == "__main__":
    caminho_do_csv = Path("Dados CSV") / "DIM_Customer.csv"
    df = carregar_e_exibir_dados(caminho_do_csv)

    if df is not None:
        # Imprime os nomes das colunas para depuração
        print("\nColunas disponíveis no DataFrame:")
        print(df.columns.tolist())
        print("-" * 30)

        try:
            # 2 Agrupa os dados pela coluna de geografia
            # Usa .size() para contar o número de ocorrências (clientes) para cada local
            coluna_estado = 'State'  # Usando a coluna correta identificada na depuração
            clientes_por_estado = df.groupby(coluna_estado).size().reset_index(name='Total de Clientes')

            print(f"\nTabela de Clientes por '{coluna_estado}':")
            print(clientes_por_estado)
            print("-" * 30)
        except KeyError:
            # Este bloco de erro é mantido para o caso de futuras alterações
            print(f"\nErro: A coluna para agrupamento não foi encontrada no DataFrame. Verifique o nome da coluna e corrija o script.")
        
        # --- Início da Análise (agora dentro do bloco 'if') ---
        
        # Ordena o DataFrame pela coluna 'Total de Clientes' em ordem decrescente
        ranking_estados = clientes_por_estado.sort_values(by='Total de Clientes', ascending=False)
        
        # O primeiro registro após a ordenação é o estado com mais clientes
        estado_com_mais_clientes = ranking_estados.iloc[0] 
        
        print("\nResultado da Análise:")
        print(f"🏆 O estado com mais clientes é: **{estado_com_mais_clientes['State']}**")
        print(f"👥 Com um total de **{estado_com_mais_clientes['Total de Clientes']}** clientes.")
        
        print("\n--- Top 5 Estados por Número de Clientes ---")
        print(ranking_estados.head())

        # --- Salva o resultado da análise em um novo arquivo CSV ---
        caminho_saida_csv = Path("ranking_clientes_por_estado.csv")
        ranking_estados.to_csv(caminho_saida_csv, index=False, encoding='utf-8')
        
        print(f"\n✅ Análise salva com sucesso em: {caminho_saida_csv}")
