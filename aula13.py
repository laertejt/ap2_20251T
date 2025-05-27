import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard da Escola DNA")

uploaded_file = st.file_uploader("Escolha um arquivo", type=["csv", "xlsx", "txt"])

botao1 = st.button("mostrar grafico")
if botao1:
    # Checkboxes para seleção de gráficos
    mostrar_barras = st.checkbox("Mostrar gráfico de barras")
    mostrar_pizza = st.checkbox("Mostrar gráfico de pizza")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Pré-visualização dos dados:", df)

    grafico = df.groupby("CARGOS")["VALOR FINAL"].sum().sort_values(ascending=False)
    cores = sns.color_palette("viridis", len(grafico))

    # Gráfico de Barras
    if mostrar_barras:
        fig = plt.figure(figsize=(12, 6))
        bars = plt.bar(grafico.index, grafico.values, color=cores)
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, height, f'R${height:,.2f}', ha='center', va='bottom', fontsize=9)
        plt.title("Total de Despesas por Cargo", fontsize=16)
        plt.xlabel("Cargos", fontsize=12)
        plt.ylabel("Valor Final (R$)", fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

    # Gráfico de Pizza
    if mostrar_pizza:
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(
            grafico.values,
            labels=grafico.index,
            autopct=lambda pct: f'{pct:.1f}%\n(R${pct/100*sum(grafico):,.0f})',
            startangle=90,
            colors=cores,
            textprops={'fontsize': 10}
        )
        ax.set_title("Distribuição de Despesas por Cargo", fontsize=16)
        ax.axis('equal')
        st.pyplot(fig)
