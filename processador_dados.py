# MIT License
# 
# Copyright (c) 2025, Dev Airton Jr
# 
# Permitted use, copying, modification, merging, publishing, distributing, sublicensing, and/or selling copies of the Software, and to permit persons to whom the Software is provided to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import pandas as pd
import matplotlib.pyplot as plt

# Função para ler os dados a partir de um arquivo CSV
def ler_dados(arquivo):
    try:
        df = pd.read_csv(arquivo)  # Lê o arquivo CSV usando pandas
        print("Dados lidos com sucesso!")
        return df
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")  # Trata o caso onde o arquivo não é encontrado
        return None

# Função para limpar os dados, removendo valores ausentes e duplicados
def limpar_dados(df):
    print("Limpando dados...")
    df = df.dropna()  # Remove as linhas que contêm valores ausentes
    df = df.drop_duplicates()  # Remove as linhas duplicadas
    print("Dados limpos!")
    return df

# Função para transformar os dados, aumentando o salário em 10%
def transformar_dados(df):
    print("Transformando dados...")
    df['salario'] = df['salario'] * 1.1  # Aumenta os valores de salário em 10%
    print("Dados transformados!")
    return df

# Função para analisar os dados, calculando a média do salário
def analisar_dados(df):
    print("Analisando dados...")
    media_salario = df['salario'].mean()  # Calcula a média dos salários
    print(f"A média do salário é: {media_salario:.2f}")  # Exibe a média
    return media_salario

# Função para filtrar os dados com base em um salário mínimo
def filtrar_dados(df, salario_minimo):
    print(f"Filtrando dados com salário maior que {salario_minimo}...")
    df_filtrado = df[df['salario'] > salario_minimo]  # Filtra os dados onde o salário é maior que o valor fornecido
    print(f"{len(df_filtrado)} registros encontrados com salário superior a {salario_minimo}.")  # Exibe a quantidade de registros filtrados
    return df_filtrado

# Função para visualizar a distribuição dos salários em um gráfico
def visualizar_dados(df):
    print("Visualizando a distribuição do salário...")
    plt.hist(df['salario'], bins=10, color='skyblue', edgecolor='black')  # Cria o histograma para visualizar a distribuição salarial
    plt.title("Distribuição de Salários")  # Título do gráfico
    plt.xlabel("Salário")  # Rótulo do eixo X
    plt.ylabel("Frequência")  # Rótulo do eixo Y
    plt.show()  # Exibe o gráfico

# Função para salvar os dados processados em um novo arquivo CSV
def salvar_dados(df, arquivo_saida):
    try:
        df.to_csv(arquivo_saida, index=False)  # Salva os dados no arquivo CSV especificado
        print(f"Dados salvos com sucesso em {arquivo_saida}!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")  # Trata erros ao tentar salvar os dados

# Função para calcular estatísticas avançadas dos salários (média, mediana e desvio padrão)
def calcular_estatisticas(df):
    print("Calculando estatísticas dos salários...")
    media = df['salario'].mean()  # Calcula a média do salário
    mediana = df['salario'].median()  # Calcula a mediana do salário
    desvio_padrao = df['salario'].std()  # Calcula o desvio padrão do salário
    print(f"Média do salário: {media:.2f}")  # Exibe a média do salário
    print(f"Mediana do salário: {mediana:.2f}")  # Exibe a mediana do salário
    print(f"Desvio padrão do salário: {desvio_padrao:.2f}")  # Exibe o desvio padrão do salário

# Bloco principal do programa
if __name__ == "__main__":
    # Lê os dados do arquivo CSV
    dados = ler_dados('dados.csv')
    
    if dados is not None:
        # Limpa os dados
        dados_limpos = limpar_dados(dados)
        # Aplica a transformação (aumento de 10% nos salários)
        dados_transformados = transformar_dados(dados_limpos)
        # Analisa os dados (cálculo da média salarial)
        analisar_dados(dados_transformados)
        
        # Filtra os dados com salários superiores a 5000
        dados_filtrados = filtrar_dados(dados_transformados, 5000)
        
        # Visualiza a distribuição salarial com um gráfico
        visualizar_dados(dados_transformados)
        
        # Calcula estatísticas avançadas (média, mediana e desvio padrão)
        calcular_estatisticas(dados_transformados)
        
        # Salva os dados transformados em um novo arquivo CSV
        salvar_dados(dados_transformados, 'dados_transformados.csv')
