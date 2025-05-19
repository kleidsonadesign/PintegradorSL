import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Carregar os dados
caminho_arquivo = 'Dados_Vacinacao_Todos_Estados.xlsx'
df = pd.read_excel(caminho_arquivo)

# Adicionar coluna de Região
regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 'PE': 'Nordeste',
    'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}
df['Região'] = df['Estado'].map(regioes)

def analise_1():
    media_por_faixa_etaria = df.groupby("Faixa Etária com Maior Cobertura")["Cobertura Vacinal (%)"].mean().reset_index()
    st.write("Média de Cobertura Vacinal por Faixa Etária:")
    st.dataframe(media_por_faixa_etaria)
    plt.figure(figsize=(10, 6))
    plt.bar(media_por_faixa_etaria["Faixa Etária com Maior Cobertura"], media_por_faixa_etaria["Cobertura Vacinal (%)"], color=["lightblue", "lightgreen", "salmon", "gold"])
    plt.title("Média da Cobertura Vacinal por Faixa Etária")
    plt.xlabel("Faixa Etária")
    plt.ylabel("Média da Cobertura Vacinal (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def analise_2():
    media_por_estado = df.sort_values(by="Cobertura Vacinal (%)", ascending=False)
    st.write("Cobertura Vacinal por Estado (ordem decrescente):")
    st.dataframe(media_por_estado[["Estado", "Cobertura Vacinal (%)"]])
    plt.figure(figsize=(12, 6))
    plt.bar(media_por_estado["Estado"], media_por_estado["Cobertura Vacinal (%)"], color="skyblue")
    plt.title("Média de Cobertura Vacinal por Estado")
    plt.xlabel("Estado")
    plt.ylabel("Cobertura Vacinal (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def analise_3():
    st.write("Relação entre Vacinas Aplicadas e Cobertura Vacinal (primeiros 10 registros):")
    st.dataframe(df[["Vacinas Aplicadas", "Cobertura Vacinal (%)"]].head(10))
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Vacinas Aplicadas"], df["Cobertura Vacinal (%)"], color="blue", alpha=0.7)
    plt.title("Relação entre Vacinas Aplicadas e Cobertura Vacinal")
    plt.xlabel("Vacinas Aplicadas")
    plt.ylabel("Cobertura Vacinal (%)")
    plt.tight_layout()
    st.pyplot(plt)

def analise_4():
    df_grouped = df.groupby('Faixa Etária com Maior Cobertura')['Cobertura Vacinal (%)'].mean().sort_values(ascending=False)
    st.write("Cobertura Vacinal Média por Faixa Etária com Maior Cobertura:")
    st.dataframe(df_grouped)
    df_grouped.plot(kind='bar', figsize=(10, 6), color='teal')
    plt.title("Cobertura Vacinal Média por Faixa Etária com Maior Cobertura")
    plt.xlabel("Faixa Etária")
    plt.ylabel("Cobertura Vacinal (%)")
    plt.tight_layout()
    st.pyplot(plt)

def analise_5():
    covid = df[df['Vacinas Mais Aplicadas'] == 'Covid-19']
    polio = df[df['Vacinas Mais Aplicadas'] == 'Poliomielite']
    medias = pd.Series({
        'Covid-19': covid['Cobertura Vacinal (%)'].mean(),
        'Poliomielite': polio['Cobertura Vacinal (%)'].mean()
    })
    st.write("Cobertura Vacinal Média por Tipo de Vacina:")
    st.dataframe(medias)
    medias.plot(kind='bar', color=['orange', 'green'])
    plt.title("Cobertura Vacinal Média por Tipo de Vacina Mais Aplicada")
    plt.ylabel("Cobertura Vacinal (%)")
    plt.tight_layout()
    st.pyplot(plt)

def analise_6():
    filtro = df[(df['Vacinas Aplicadas'] < 1851698) & (df['Cobertura Vacinal (%)'] > 88.15)]
    st.write("Estados com Alta Cobertura e Baixa Aplicação:")
    st.dataframe(filtro[["Estado", "Vacinas Aplicadas", "Cobertura Vacinal (%)"]])
    plt.figure(figsize=(10, 6))
    plt.bar(filtro['Estado'], filtro['Cobertura Vacinal (%)'], color='green')
    plt.title("Alta Cobertura com Baixo Número de Vacinas Aplicadas")
    plt.xlabel("Estado")
    plt.ylabel("Cobertura Vacinal (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def analise_7():
    filtro = df[(df['Vacinas Aplicadas'] > 5022521) & (df['Cobertura Vacinal (%)'] < 76.15)]
    st.write("Estados com Alta Aplicação e Baixa Cobertura:")
    st.dataframe(filtro[["Estado", "Vacinas Aplicadas", "Cobertura Vacinal (%)"]])
    plt.figure(figsize=(10, 6))
    plt.bar(filtro['Estado'], filtro['Cobertura Vacinal (%)'], color='red')
    plt.title("Baixa Cobertura com Alta Quantidade de Vacinas Aplicadas")
    plt.xlabel("Estado")
    plt.ylabel("Cobertura Vacinal (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

def analise_8():
    media_por_regiao = df.groupby('Região')['Cobertura Vacinal (%)'].mean().sort_values(ascending=False)
    st.write("Cobertura Vacinal Média por Região:")
    st.dataframe(media_por_regiao)
    media_por_regiao.plot(kind='bar', color='purple')
    plt.title("Cobertura Vacinal Média por Região")
    plt.ylabel("Cobertura Vacinal (%)")
    plt.xlabel("Região")
    plt.tight_layout()
    st.pyplot(plt)

def analise_9():
    vacinas_por_regiao = df.groupby(['Região', 'Vacinas Mais Aplicadas']).size().unstack(fill_value=0)
    st.write("Vacinas Mais Aplicadas por Região:")
    st.dataframe(vacinas_por_regiao)
    vacinas_por_regiao.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title("Tipos de Vacinas Mais Aplicadas por Região")
    plt.xlabel("Região")
    plt.ylabel("Quantidade de Estados")
    plt.xticks(rotation=45)
    plt.legend(title='Vacina')
    plt.tight_layout()
    st.pyplot(plt)

def main():
    st.title("Análise de Dados de Vacinação")
    st.write("Escolha a análise que deseja visualizar:")
    
    analises = {
        "Diferença de vacinação entre faixas etárias": analise_1,
        "Média de vacinação por estado": analise_2,
        "Relação entre vacinas aplicadas e cobertura vacinal": analise_3,
        "Faixas etárias com maior cobertura vacinal": analise_4,
        "Comparativo: Covid-19 vs Poliomielite": analise_5,
        "Alta cobertura com baixa aplicação": analise_6,
        "Baixa cobertura com alta aplicação": analise_7,
        "Regiões com maior cobertura vacinal": analise_8,
        "Vacinas mais aplicadas por região": analise_9,
    }
    
    escolha = st.selectbox("Escolha uma análise", list(analises.keys()))
    
    if st.button("Executar Análise"):
        analises[escolha]()

if __name__ == "__main__":
    main()