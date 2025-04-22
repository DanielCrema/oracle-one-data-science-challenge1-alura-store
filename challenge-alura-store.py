import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

def pre_process(loja: pd.DataFrame) -> pd.DataFrame:
    """
    🧼 **Function Description:**
    Pre-processes the **store sales data** to prepare it for analysis.

    📥 **Parameters:**
    - `loja` : `pd.DataFrame`  
    The raw input DataFrame containing sales data.

    📤 **Returns:**
    - `loja` : `pd.DataFrame`  
    The cleaned and pre-processed DataFrame, ready for analysis.

    🔧 **Transformations Applied:**
    - 🕒 Converts `'Data da Compra'` to `datetime` format.
    - 🏷️ Converts the following columns to `categorical` types:
    
    • `'Produto'`  
    • `'Categoria do Produto'`  
    • `'Vendedor'`  
    • `'Local da compra'`  
    • `'Tipo de pagamento'`
    """
    # Convert 'Data da Compra' to datetime
    loja['Data da Compra'] = pd.to_datetime(loja['Data da Compra'], format='%d/%m/%Y')

    # Convert 'Produto', 'Categoria do Produto', 'Vendedor', 'Local da compra' and 'Tipo de pagamento' to categorical
    loja['Produto'] = loja['Produto'].astype('category')
    loja['Categoria do Produto'] = loja['Categoria do Produto'].astype('category')
    loja['Vendedor'] = loja['Vendedor'].astype('category')
    loja['Local da compra'] = loja['Local da compra'].astype('category')
    loja['Tipo de pagamento'] = loja['Tipo de pagamento'].astype('category')

    return loja

def analyze_data(loja: pd.DataFrame) -> dict:
    """
    📊 **Function Description:**
    Analyzes **store sales data** and returns key insights in a structured dictionary format.

    📥 **Parameters:**
    - `loja` : `pd.DataFrame`  
    A DataFrame containing sales data. Expected columns include:  
    `'Preço'`, `'Categoria do Produto'`, `'Produto'`,  
    `'Avaliação da compra'`, `'Frete'`, `'lat'`, `'lon'`.

    📤 **Returns:**
    - `loja_data` : `dict`  
    A dictionary with the following analysis results:

    - 💰 **'revenue'** (`float`):  
        Total revenue generated from sales (sum of all product prices).

    - 🗂️ **'categories_ranking'** (`pd.Series`):  
        Ranking of product categories by sales (most to least sold).

    - 🛍️ **'products_ranking'** (`pd.Series`):  
        Ranking of individual products by sales.

    - ⭐ **'rating_mean'** (`float`):  
        Average customer rating from purchases.

    - 🚚 **'shipping_mean'** (`float`):  
        Average shipping cost.

    - 📍 **'sales_distribution'** (`pd.Series`):  
        Number of sales grouped by geographic coordinates (latitude & longitude).
    """

    revenue = loja['Preço'].sum()
    categories_ranking = loja['Categoria do Produto'].value_counts()
    products_ranking = loja['Produto'].value_counts()
    rating_mean = loja['Avaliação da compra'].mean()
    shipping_mean = loja['Frete'].mean()
    sales_distribution = loja[['lat', 'lon']].value_counts()

    loja_data = {
        'revenue': revenue,
        'categories_ranking': categories_ranking,
        'products_ranking': products_ranking,
        'rating_mean': rating_mean,
        'shipping_mean': shipping_mean,
        'sales_distribution': sales_distribution
    }

    return loja_data

def build_global_statistics(lojas_data: dict) -> dict:
    """
    🔄 **Function Description:**
    Builds **statistical comparison DataFrames** from multiple store sales analyses.

    📥 **Parameters:**
    - `lojas_data` : `dict`  
    A dictionary where each key is a store identifier and each value is another dictionary containing the following analysis results:

    - 📈 **'revenue'** (`float`):  
        Total revenue generated from sales.

    - 🗂️ **'categories_ranking'** (`pd.Series`):  
        Ranking of product categories based on sales.

    - 🛍️ **'products_ranking'** (`pd.Series`):  
        Ranking of individual products based on sales.

    - ⭐ **'rating_mean'** (`float`):  
        Average customer rating.

    - 🚚 **'shipping_mean'** (`float`):  
        Average shipping cost.

    - 📍 **'sales_distribution'** (`pd.Series`):  
        Count of sales per geographic location (latitude & longitude).

    📤 **Returns:**
    - `lojas_comparisons` : `dict`  
    A dictionary containing several comparison DataFrames:

    - 📊 **'lojas_stats'** (`pd.DataFrame`):  
        Summary statistics for each store (e.g., revenue, average rating, average shipping).

    - 🏷️ **'lojas_categories_ranking'** (`pd.DataFrame`):  
        Product category rankings by store.

    - 📦 **'lojas_products_ranking'** (`pd.DataFrame`):  
        Individual product rankings by store.

    - 🌍 **'lojas_sales_distribution'** (`pd.DataFrame`):  
        Sales count per geographic location by store.
    """
    def rename_dataframe_columns(lojas_stats: pd.DataFrame) -> pd.DataFrame:
        '''
        Renames the columns of lojas statistical comparison DataFrames to plot prettier graphs.
        ## Renames:
        - **'loja1'** to **'Loja 1'**
        And so on...
        -------
        ### Parameters:
        - **lojas_stats** : pd.DataFrame
            A DataFrame or Series containing statistical data for multiple stores.

        ### Returns:
        - **lojas_stats** : pd.DataFrame
            The DataFrame or Series with renamed columns.
        '''
        rename_map = {
            'loja1': 'Loja 1',
            'loja2': 'Loja 2',
            'loja3': 'Loja 3',
            'loja4': 'Loja 4',
        }
        # If the input is a DataFrame
        if isinstance(lojas_stats, pd.DataFrame):
            # Rename index if it contains lojas
            if any(label in lojas_stats.index for label in rename_map):
                lojas_stats = lojas_stats.rename(index=rename_map)

            # Rename columns if they contain lojas
            if any(label in lojas_stats.columns for label in rename_map):
                lojas_stats = lojas_stats.rename(columns=rename_map)

        # If it's a Series, rename the index
        elif isinstance(lojas_stats, pd.Series):
            lojas_stats.index = [rename_map.get(i, i) for i in lojas_stats.index]

        return lojas_stats
    # Extract the data from the dictionary
    lojas_revenues = {loja_name: loja_data['revenue'] for loja_name, loja_data in lojas_data.items()}
    lojas_categories_ranking = {loja_name: loja_data['categories_ranking'] for loja_name, loja_data in lojas_data.items()}
    lojas_products_ranking = {loja_name: loja_data['products_ranking'] for loja_name, loja_data in lojas_data.items()}
    lojas_rating_mean = {loja_name: loja_data['rating_mean'] for loja_name, loja_data in lojas_data.items()}
    lojas_shipping_mean = {loja_name: loja_data['shipping_mean'] for loja_name, loja_data in lojas_data.items()}
    lojas_sales_distribution = {loja_name: loja_data['sales_distribution'] for loja_name, loja_data in lojas_data.items()}

    # Create dataframes
    lojas_revenues_df = pd.Series(lojas_revenues, name='Faturamento')
    lojas_rating_mean_df = pd.Series(lojas_rating_mean, name='Média Avaliações')
    lojas_shipping_mean_df = pd.Series(lojas_shipping_mean , name='Frete Médio')

    lojas_stats = pd.concat([lojas_revenues_df, lojas_rating_mean_df, lojas_shipping_mean_df], axis=1)
    lojas_categories_ranking_df = pd.DataFrame(lojas_categories_ranking)
    lojas_products_ranking_df = pd.DataFrame(lojas_products_ranking)
    lojas_sales_distribution_df = pd.DataFrame(lojas_sales_distribution)
    lojas_categories_ranking_df['TOTAL'] = lojas_categories_ranking_df.sum(axis=1)
    lojas_products_ranking_df['TOTAL'] = lojas_products_ranking_df.sum(axis=1)
    lojas_sales_distribution_df['TOTAL'] = lojas_sales_distribution_df.sum(axis=1)
    
    # Sort the dataframes
    lojas_stats.sort_values(by='Faturamento', ascending=False, inplace=True)
    lojas_categories_ranking_df.sort_values(by='TOTAL', ascending=False, inplace=True)
    lojas_products_ranking_df.sort_values(by='TOTAL', ascending=False, inplace=True)
    lojas_sales_distribution_df.sort_values(by='TOTAL', ascending=False, inplace=True)

    # Format dataframes
    lojas_stats = lojas_stats.round(2)
    lojas_sales_distribution_df.dropna(inplace=True)
    cols_to_convert = ['loja1', 'loja2', 'loja3', 'loja4', 'TOTAL']
    lojas_sales_distribution_df[cols_to_convert] = lojas_sales_distribution_df[cols_to_convert].astype(int)

    lojas_comparisons = {
        'lojas_stats': rename_dataframe_columns(lojas_stats),
        'lojas_categories_ranking': rename_dataframe_columns(lojas_categories_ranking_df),
        'lojas_products_ranking': rename_dataframe_columns(lojas_products_ranking_df),
        'lojas_sales_distribution': rename_dataframe_columns(lojas_sales_distribution_df)
    }

    return lojas_comparisons

def get_top10_products_and_shipping_mean(
        lojas_comparisons: dict,
        loja1: pd.DataFrame,
        loja2: pd.DataFrame,
        loja3: pd.DataFrame,
        loja4: pd.DataFrame,
) -> dict:
    """
    🔍 **Function Description:**
    Fills the statistical comparisons with a DataFrame containing the **average shipping cost per product** for the **top 10 selling products** across the 4 stores.

    📥 **Parameters:**
    - `lojas_comparisons` : `dict`  
    A dictionary containing statistical comparisons for multiple stores.

    - `loja1`, `loja2`, `loja3`, `loja4` : `pd.DataFrame`  
    DataFrames containing the raw data of each store.

    📤 **Returns:**
    - `lojas_comparisons` : `dict`  
    The original dictionary, now with an added key:

    - `'top10_products_shipping_mean'` : `pd.DataFrame`  
        A DataFrame with the **average shipping cost** per top-selling product. Columns include:
        - 🛒 **Produto**: Name of the product.
        - 🏬 **Loja 1**: Average shipping cost in Store 1.
        - 🏬 **Loja 2**: Average shipping cost in Store 2.
        - 🏬 **Loja 3**: Average shipping cost in Store 3.
        - 🏬 **Loja 4**: Average shipping cost in Store 4.
        - 📊 **Média Global**: Global average shipping cost across the four stores  
        (see `shipping_mean` from the `analyze_data()` function for more info).
    """
    top10_products = lojas_comparisons['lojas_products_ranking'].drop(columns='TOTAL').head(10)
    stores = [loja1, loja2, loja3, loja4]
    store_frete_dfs = [
        store[store['Produto'].isin(list(top10_products.index))][['Produto', 'Frete']]
        .groupby('Produto')['Frete'].mean().dropna()
        for store in stores
    ]
    top10_products_shipping_mean = pd.concat(store_frete_dfs, axis=1)
    top10_products_shipping_mean.columns = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']
    top10_products_shipping_mean.loc['Média Global'] = lojas_comparisons['lojas_stats']['Frete Médio']
    top10_products_shipping_mean.title = 'Média de Frete por Produto'

    # Order by top 10 selling products
    top10_products_shipping_mean = top10_products_shipping_mean.reindex(top10_products.index.tolist() + ['Média Global'])
    lojas_comparisons['top10_products_shipping_mean'] = top10_products_shipping_mean

    return lojas_comparisons

# # #
# Main code
# # #

# Importing and pre processing the data
link = "./base-de-dados-challenge-1/loja_1.csv"
link2 = "./base-de-dados-challenge-1/loja_2.csv"
link3 = "./base-de-dados-challenge-1/loja_3.csv"
link4 = "./base-de-dados-challenge-1/loja_4.csv"

loja1 = pre_process(pd.read_csv(link))
loja2 = pre_process(pd.read_csv(link2))
loja3 = pre_process(pd.read_csv(link3))
loja4 = pre_process(pd.read_csv(link4))

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
st.set_page_config(
    page_title="Alura Store",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown("""<a name="alura-store-statistics"></a><div style="text-align: center; margin-bottom: 1rem">
    <h1 style="padding: 0 0 0.5rem; font-size: 3rem; letter-spacing: 0.1rem; font-weight: bold">Alura Store 🧊</h1>
    <p style="font-size: 1.25rem; letter-spacing: 0.01rem; margin: 0 0 1.5rem">Análise das lojas do Sr. João</p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; justify-items: start; margin: 0 auto; text-align: left">
        <div>
            <p style="font-size: 1.5rem; letter-spacing: 0.01rem; margin-bottom: 0.5rem">Dados Globais:</p>
            <ul style="font-size: 1rem; padding-left: 0; list-style: none">
                <li style="margin-left: 0; padding-left: 0">💰 Faturamento Total</li>
                <li style="margin-left: 0; padding-left: 0">🌟 Média de Avaliações</li>
                <li style="margin-left: 0; padding-left: 0">💸 Média de Frete</li>
                <li style="margin-left: 0; padding-left: 0">🗺️ Distribuição Geográfica</li>
            </ul>
        </div>
        <div>
            <p style="font-size: 1.5rem; letter-spacing: 0.01rem; margin-bottom: 0">Dados Específicos:</p>
            <p style="font-size: 1rem; margin: 0 0 0.5rem">(Filtros se aplicam)</p>
            <ul style="font-size: 1rem; padding-left: 0; list-style: none">
                <li style="margin-left: 0; padding-left: 0">🛋️ Categorias mais Vendidas</li>
                <li style="margin-left: 0; padding-left: 0">🔢 Ranking de Produtos</li>
                <li style="margin-left: 0; padding-left: 0">🚛 Frete Médio por Produto</li>
            </ul>
        </div>
    </div>
</div>""", unsafe_allow_html=True)

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
""", unsafe_allow_html=True)
# Filter the data based on selection
filtered_categories = lojas_categories.T.loc[selected_lojas]
filtered_products = lojas_products.head(10).T.loc[selected_lojas]
filtered_top10_shipping = lojas_top10_products_shipping_mean.T.loc[selected_lojas]

# Generating the charts
# 

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
# plt.yticks(rotation=35)
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

# Displaying raw data
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

# Download data
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

# Displaying conclusions
st.markdown("""<a name="final-report"></a><h1 style="font-size: 2rem; letter-spacing: 0.04rem; margin-bottom: 0.5rem">📝 Relatório Final</h1>""", unsafe_allow_html=True)
st.markdown("""
            O Sr. João, proprietário das lojas Alura Store, precisa vender uma de suas lojas para apriorar a sua eficiência em custos e obter melhores resultados.
            
            ➡️ Considerando os dados avaliados de suas 4 lojas, podemos concluir que:
            1. **Faturamento:**
                - As `lojas 1, 2 e 4` são as que possuem maior faturamento.<br><br>
            2. **Avaliação Média:**
                - As `lojas 3 e 2` são as que possuem maior avaliação média.
                - A `loja 1` tem a menor avaliação média.<br><br>
            3. **Frete Médio:**
                - A `loja 4` possui o menor frete médio, com uma diferença significativa, seguida da `loja 3`.<br><br>
            4. **Vendas por Categoria:**<br>
                As categorias de `móveis`, `eletrônicos` e `brinquedos` são as que possuem maior número de vendas. Nestas categorias:
                - As `lojas 3 e 4` têm o melhor desempenho.
                - A `loja 2` tem o pior desempenho.<br><br>
            5. **Vendas por Produto:**<br>
                `Cômodas`, `carrinhos de controle remoto` e `fornos de micro-ondas` são os produtos que possuem maior número de vendas. Nestes produtos:
                - As `lojas 1 e 4` têm o melhor desempenho.
                - As `loja 2 e 3` têm o pior desempenho.<br><br>
            6. **Distribuição Geográfica:**
                - Das 9421 vendas registradas, 6257 `(66,41%)` foram realizadas no raio de `latitude -20` e `longitude -46`, que corresponde à região central de São Paulo.<br><br>
            
            💡 **Insights significativos:**<br>
            As lojas possuem estatísticas muito similares que dificultam a aferição da pior performance dentre elas. Observa-se que:
            - A `loja 1` possui o melhor desempenho entre os produtos mais vendidos e o maior faturamento.
            - A `loja 3` e a `loja 4` possuem excelente desempenho de vendas entre as categorias e produtos mais vendidos enquanto ao mesmo tempo possuem o menor frete médio, evidência de que os sistemas de distribuição destas lojas atendem com melhor eficiência a região central de São Paulo, onde se registra a maior quantidade de vendas.
            - A `loja 2` possui o pior desempenho em vendas, embora tenha o segundo maior faturamento. Além disso, possui o segundo maior frete médio. O alto faturamento é provavelmente decorrente de um maior valor agregado dos produtos vendidos, o que não se traduz necessariamente em lucros.<br><br>

            ### 📊 Conclusão das Observações
            ➡️ Considerando os dados avaliados anteriormente:
            - Embora nenhuma das lojas apresente um desempenho consideravelmente ruim, dentre todas as observadas a `loja 2` se destaca como a melhor candidata a ser vendida.
            """, unsafe_allow_html=True)
print(lojas_sales_distribution['TOTAL'][0:3].sum())