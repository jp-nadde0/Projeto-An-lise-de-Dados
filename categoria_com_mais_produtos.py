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
    caminho_do_csv = Path("Dados CSV") / "DIM_Products.csv"
    df = carregar_e_exibir_dados(caminho_do_csv)
    if df is not None:
        # Imprime os nomes das colunas para depuração
        print("\nColunas disponíveis no DataFrame:")
        print(df.columns.tolist())
        print("-" * 30)

        try:
            # Agrupa os dados pela coluna de categoria de produto
            coluna_categoria = 'Category'  # Usando a coluna correta identificada na depuração
            produtos_por_categoria = df.groupby(coluna_categoria).size().reset_index(name='Total de Produtos')

            print(f"\nTabela de Produtos por Categoria:")
            print(produtos_por_categoria)
            print("-" * 30)

            # Ordena o DataFrame pela coluna 'Total de Produtos' em ordem decrescente
            ranking_categorias = produtos_por_categoria.sort_values(by='Total de Produtos', ascending=False)

            # O primeiro registro após a ordenação é a categoria com mais produtos
            categoria_com_mais_produtos = ranking_categorias.iloc[0]

            print("\nResultado da Análise:")
            print(f"🏆 A categoria com mais produtos é: **{categoria_com_mais_produtos['Category']}**")
            print(f"📦 Com um total de **{categoria_com_mais_produtos['Total de Produtos']}** produtos.")
            print("\n--- Top 5 Categorias por Número de Produtos ---")
            print(ranking_categorias.head())

            # --- Salva o resultado da análise em um novo arquivo CSV ---
            caminho_saida_csv = Path("ranking_produtos_por_categoria.csv")
            ranking_categorias.to_csv(caminho_saida_csv, index=False, encoding='utf-8')
            print(f"\n✅ Análise salva com sucesso em: {caminho_saida_csv}")
        except KeyError:
            print(f"\nErro: A coluna para agrupamento não foi encontrada no DataFrame. Verifique o nome da coluna e corrija o script.")