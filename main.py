import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "./")))

import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from modules.loader import load_data
from modules.analyze_stores import analyze_data
from modules.build_statistics import build_global_statistics, get_top10_products_and_shipping_mean
from app_ui import streamlit_header, sidebar_credits, final_report

# # #
# Main code
# # #

# Importing and pre processing the data
link = "./base-de-dados-challenge-1/loja_1.csv"
link2 = "./base-de-dados-challenge-1/loja_2.csv"
link3 = "./base-de-dados-challenge-1/loja_3.csv"
link4 = "./base-de-dados-challenge-1/loja_4.csv"

loja1 = load_data(link)
loja2 = load_data(link2)
loja3 = load_data(link3)
loja4 = load_data(link4)

# Analyzing the data
loja1_data = analyze_data(loja1)
loja2_data = analyze_data(loja2)
loja3_data = analyze_data(loja3)
loja4_data = analyze_data(loja4)
lojas_data = {
    'loja1': loja1_data,
    'loja2': loja2_data,
    'loja3': loja3_data,
    'loja4': loja4_data
}

# Generating global statistical data
lojas_comparisons = build_global_statistics(lojas_data)
lojas_comparisons = get_top10_products_and_shipping_mean(lojas_comparisons, loja1, loja2, loja3, loja4)

# Unpacking the data
lojas_stats = lojas_comparisons['lojas_stats']
lojas_categories = lojas_comparisons['lojas_categories_ranking']
lojas_products = lojas_comparisons['lojas_products_ranking']
lojas_top10_products_shipping_mean = lojas_comparisons['top10_products_shipping_mean']
lojas_sales_distribution = lojas_comparisons['lojas_sales_distribution']

# Initializing a Streamlit app
# 
# Set page config
st.set_page_config(
    page_title="Alura Store",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Create header section
st.markdown(streamlit_header, unsafe_allow_html=True)

# Configure sidebar
# 
# Create Filters section
st.sidebar.header('🔎 Filtros')
selected_lojas = st.sidebar.multiselect(
    "Selecionar loja(s):",
    options=["Loja 1", "Loja 2", "Loja 3", "Loja 4"],
    default=["Loja 1", "Loja 2", "Loja 3", "Loja 4"]
)

# Create summary section
st.sidebar.markdown("""
### 🧭 Sumário

- [Gráficos Estatísticos](#alura-store-statistics)
- [Dados Brutos](#raw-data)
- [Baixar Dados (CSV)](#download-data)
- [Relatório Final](#final-report)
<hr/>
""", unsafe_allow_html=True)
# Filter the data based on selection
filtered_categories = lojas_categories.T.loc[selected_lojas]
filtered_products = lojas_products.head(10).T.loc[selected_lojas]
filtered_top10_shipping = lojas_top10_products_shipping_mean.T.loc[selected_lojas]

# Create credits section
st.sidebar.markdown("""### 🎓 Créditos""")
st.sidebar.markdown(sidebar_credits, unsafe_allow_html=True)

# Generating the charts
# # #

# Globals
# 
# Revenue pie chart
fig_revenue, ax_revenue = plt.subplots()
ax_revenue.pie(lojas_stats['Faturamento'], explode=(0.07, 0, 0, 0), labels=lojas_stats.index, autopct='%1.1f%%',
       shadow=True, startangle=90)
ax_revenue.set_title('Faturamento por Loja')

# Rating mean chart
fig_ratings, ax_ratings = plt.subplots(figsize=(6,3))
lojas_stats['Média Avaliações'].plot(ax=ax_ratings, label='Avaliação Média')
plt.title('Média de Avaliações', fontsize=16)
plt.ylabel('Avaliação Média', fontsize=14)
plt.xlabel('Lojas', fontsize=14)
plt.xticks(rotation=0)
plt.legend()
plt.tight_layout()

# Shipping mean bar chart
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
fig_shippings, ax_shippings = plt.subplots(figsize=(6,3))
lojas_stats['Frete Médio'].plot(kind='bar', ax=ax_shippings, color=bar_colors, label='Frete Médio')
ax_shippings.set_ylim(bottom=30)
plt.title('Custo de Frete Médio', fontsize=16)
plt.ylabel('Frete Médio (R$)', fontsize=14)
plt.xlabel('Lojas', fontsize=14)
plt.xticks(rotation=0)
plt.legend()
plt.tight_layout()

# Sales distribution scatter plot
lats = lojas_sales_distribution.index.get_level_values('lat')
lons = lojas_sales_distribution.index.get_level_values('lon')
fig_sales_distribution, ax_sales_distribution = plt.subplots(figsize=(8, 8))
sc = ax_sales_distribution.scatter(lons, lats, 
                c=lojas_sales_distribution['TOTAL'], cmap='viridis', s=100, edgecolors='k', alpha=0.7)
cbar = fig_sales_distribution.colorbar(sc, label='Total de Vendas')
cbar.ax.tick_params(labelsize=18)
cbar.set_label('Total de Vendas', fontsize=16)
ax_sales_distribution.set_xlabel('Longitude', fontsize=20)
ax_sales_distribution.set_ylabel('Latitude', fontsize=20)
ax_sales_distribution.set_title('Distribuição Geográfica Vendas\n(Dados Globais)', fontsize=22)
plt.tight_layout()

# Specifics
# 
# Top 10 categories horizontal bars chart
top10_categories = filtered_categories.T
fig_top10_categories, ax_top10_categories = plt.subplots(figsize=(9.5,10))
top10_categories.plot(kind='barh', ax=ax_top10_categories)
ax_top10_categories.invert_yaxis()
ax_top10_categories.set_xlim(left=150)
ax_top10_categories.tick_params(axis='y', labelsize=16)
ax_top10_categories.legend(fontsize=12, title="Lojas", title_fontsize=16)
ax_top10_categories.set_yticklabels(
    [
        'Instrum. musicais' if label.get_text().lower() == 'instrumentos musicais'
        else 'Util. domésticas' if label.get_text().lower() == 'utilidades domesticas'
        else label.get_text().capitalize()
        for label in ax_top10_categories.get_yticklabels()
    ],
    fontsize=16
)
plt.title('Top 10 Categorias mais vendidas\n(Ordem Decrescente)', fontsize=24)
plt.xlabel('Quantidade Vendida', fontsize=22)
plt.ylabel('Categoria', fontsize=22)
plt.yticks(rotation=35)
plt.tight_layout()

# Top 10 products horizontal bars chart
top10_products = filtered_products.T
fig_top10_products, ax_top10_products = plt.subplots(figsize=(9.5,10))
top10_products.plot(kind='barh', ax=ax_top10_products)
ax_top10_products.invert_yaxis()
ax_top10_products.set_xlim(left=33)
ax_top10_products.tick_params(axis='x', labelsize=16)
ax_top10_products.legend(fontsize=12, title="Lojas", title_fontsize=16)
ax_top10_products.set_yticklabels(
    [
        'Carrinho cont. remoto' if label.get_text().lower() == 'carrinho controle remoto'
        else label.get_text().capitalize()
        for label in ax_top10_products.get_yticklabels()
    ],
    fontsize=15
)
plt.title('Top 10 Produtos mais vendidos\n(Ordem Decrescente)', fontsize=24)
plt.xlabel('Quantidade Vendida', fontsize=22)
plt.ylabel('Produto', fontsize=22)
plt.yticks(rotation=35)
plt.tight_layout()

# Shipping mean compared to products shipping mean heatmap
data = filtered_top10_shipping.T
fig_top10_shipping, ax_top10_shipping = plt.subplots(figsize=(10, 10))
sns.heatmap(data, annot=True, fmt=".1f", cmap="coolwarm", cbar_kws={'label': 'Custo de Frete'})
colorbar = ax_top10_shipping.collections[0].colorbar
colorbar.ax.yaxis.label.set_size(18)
ax_top10_shipping.tick_params(axis='x', labelsize=18)
ax_top10_shipping.tick_params(axis='y', labelsize=14)
ax_top10_shipping.set_yticklabels(
    [
        'Carrinho cont. remoto' if label.get_text().lower() == 'carrinho controle remoto'
        else label.get_text().capitalize()
        for label in ax_top10_shipping.get_yticklabels()
    ],
    fontsize=15
)
plt.title('Heatmap: Preço Médio de Fretes\n(Top 10 Produtos)', fontsize=22)
plt.ylabel('Produto', fontsize=20)
plt.tight_layout()

# Displaying the data
# 
# Columns layout setup
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7 = st.columns(1)

# Displaying global data charts
col1.pyplot(fig_revenue)
with col3:
    st.pyplot(fig_ratings)
    st.pyplot(fig_shippings)
col5.pyplot(fig_sales_distribution)

# Displaying specific data charts
col2.pyplot(fig_top10_categories)
col4.pyplot(fig_top10_products)
col6.pyplot(fig_top10_shipping)

# Raw data section
# 
st.markdown("""<a name="raw-data"></a><h1 style="font-size: 2rem; letter-spacing: 0.04rem; margin-bottom: 0.5rem">🗿 Dados Brutos</h1>""", unsafe_allow_html=True)
st.subheader("Estatísticas Globais")
st.dataframe(lojas_stats.T, use_container_width=True)

st.subheader("Categorias mais Vendidas")
st.dataframe(lojas_categories, use_container_width=True)

st.subheader("Produtos mais Vendidos")
st.dataframe(lojas_products, use_container_width=True)

st.subheader("Top 10 Produtos - Frete Médio")
st.dataframe(lojas_top10_products_shipping_mean, use_container_width=True)

st.subheader("Distribuição Geográfica de Vendas")
st.dataframe(lojas_sales_distribution, use_container_width=True)

# Download data section
# 
st.markdown("""<a name="download-data"></a><h1 style="font-size: 2rem; letter-spacing: 0.04rem; margin-bottom: 0.5rem">⬇️ Download dos Dados</h1>""", unsafe_allow_html=True)

def convert_df_to_csv(df):
    return df.to_csv(index=True).encode('utf-8')

st.download_button(
    label="📥 Baixar Estatísticas Globais (CSV)",
    data=convert_df_to_csv(lojas_stats.T),
    file_name='estatisticas_globais.csv',
    mime='text/csv',
)

st.download_button(
    label="📥 Baixar Categorias mais Vendidas (CSV)",
    data=convert_df_to_csv(lojas_categories),
    file_name='categorias_mais_vendidas.csv',
    mime='text/csv',
)

st.download_button(
    label="📥 Baixar Produtos mais Vendidos (CSV)",
    data=convert_df_to_csv(lojas_products),
    file_name='produtos_mais_vendidos.csv',
    mime='text/csv',
)

st.download_button(
    label="📥 Baixar Frete Médio por Produto (CSV)",
    data=convert_df_to_csv(lojas_top10_products_shipping_mean),
    file_name='frete_medio_por_produto.csv',
    mime='text/csv',
)

st.download_button(
    label="📥 Baixar Distribuição Geográfica de Vendas (CSV)",
    data=convert_df_to_csv(lojas_sales_distribution),
    file_name='distribuicao_geografica_vendas.csv',
    mime='text/csv',
)

# Final report section
# 
st.markdown("""<a name="final-report"></a><h1 style="font-size: 2rem; letter-spacing: 0.04rem; margin-bottom: 0.5rem">📝 Relatório Final</h1>""", unsafe_allow_html=True)
st.markdown(final_report, unsafe_allow_html=True)