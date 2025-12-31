import pandas as pd
from pathlib import Path

class MenosVendas:
    """
    Uma classe para analisar dados de vendas de produtos a partir de um arquivo CSV.
    """
    def __init__(self, caminho_arquivo):
        """
        Inicializa o analisador com o caminho para o arquivo de dados.
        """
        self.caminho_arquivo = Path(caminho_arquivo)
        self.df = None
        self.ranking_produtos = None

    def carregar_dados(self):
        """Carrega os dados do arquivo CSV para um DataFrame pandas."""
        try:
            self.df = pd.read_csv(self.caminho_arquivo)
            print(f"Dados carregados com sucesso de '{self.caminho_arquivo}'")
            return True
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.caminho_arquivo}' não foi encontrado.")
            return False
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao carregar os dados: {e}")
            return False
        
    def analisador_de_produtos_menos_vendidos(self):
        """
        Analisa o DataFrame para encontrar os produtos menos vendidos com base na quantidade.
        """
        if self.df is None:
            print("Dados não carregados. A análise não pode ser executada.")
            return
        try:
            print("\nAnalisando os produtos menos vendidos...")
            # Agrupa por 'Product' e soma a 'Quantity'
            produtos_vendidos = self.df.groupby('Product')['Quantity'].sum().reset_index()
            # Ordena do menor para o maior
            self.ranking_produtos = produtos_vendidos.sort_values(by='Quantity', ascending=True)
            print("Análise concluída.")
        except KeyError:
            print(f"Erro: Uma das colunas 'Product' ou 'Quantity' não foi encontrada.")

    def exibir_ranking(self, top_n=10):
        """Exibe o ranking dos N produtos menos vendidos."""
        if self.ranking_produtos is not None:
            print(f"\nTop {top_n} produtos menos vendidos:")
            print(self.ranking_produtos.head(top_n).to_string(index=False))

    def salvar_ranking_csv(self, caminho_saida):
        """Salva o DataFrame do ranking de produtos em um arquivo CSV."""
        if self.ranking_produtos is None:
            print("⚠️  Análise não foi executada. Nada para salvar.")
            return

        try:
            self.ranking_produtos.to_csv(caminho_saida, index=False, encoding='utf-8')
            print(f"\n✅ Análise salva com sucesso em: {caminho_saida}")
        except Exception as e:
            print(f"❌ Ocorreu um erro ao salvar o arquivo CSV: {e}")

if __name__ == "__main__":
    caminho_arquivo = Path("Dados CSV") / "DIM_Shopping.csv"
    analisador = MenosVendas(caminho_arquivo)
    if analisador.carregar_dados():
        analisador.analisador_de_produtos_menos_vendidos()
        analisador.exibir_ranking(top_n=10)
        
        # Salva o resultado completo em um novo arquivo CSV
        caminho_saida = Path("ranking_produtos_menos_vendidos.csv")
        analisador.salvar_ranking_csv(caminho_saida)