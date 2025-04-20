# import sys
# sys.path

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Alura Store",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title('Alura Store')
st.write('Análise da loja do Sr. João')

def space():
    print('\n# # # # # # # # # # # #\n')

def pre_process(loja):
    # Convert 'Data da Compra' to datetime
    loja.info()
    loja['Data da Compra'] = pd.to_datetime(loja['Data da Compra'], format='%d/%m/%Y')

    # Convert 'Produto', 'Categoria do Produto', 'Vendedor', 'Local da compra' and 'Tipo de pagamento' to categorical
    loja['Produto'] = loja['Produto'].astype('category')
    loja['Categoria do Produto'] = loja['Categoria do Produto'].astype('category')
    loja['Vendedor'] = loja['Vendedor'].astype('category')
    loja['Local da compra'] = loja['Local da compra'].astype('category')
    loja['Tipo de pagamento'] = loja['Tipo de pagamento'].astype('category')
    space()
    loja.info()

    return loja

link = "./base-de-dados-challenge-1/loja_1.csv"
link2 = "./base-de-dados-challenge-1/loja_2.csv"
link3 = "./base-de-dados-challenge-1/loja_3.csv"
link4 = "./base-de-dados-challenge-1/loja_4.csv"

loja = pre_process(pd.read_csv(link))
loja2 = pre_process(pd.read_csv(link2))
loja3 = pre_process(pd.read_csv(link3))
loja4 = pre_process(pd.read_csv(link4))

loja.info()

def analyze_data(loja):
    revenue = loja['Preço'].sum()
    categories_ranking = loja['Categoria do Produto'].value_counts()
    products_ranking = loja['Produto'].value_counts()
    rating_mean = loja['Avaliação da compra'].mean()
    shipping_mean = loja['Frete'].mean()
    lat_lon = loja[['lat', 'lon']]
    lat_lon['lat/lon'] = lat_lon.apply(lambda row: f"{row['lat']:.2f}, {row['lon']:.2f}", axis=1)
    lat_lon.drop(columns=['lat', 'lon'], inplace=True)
    sales_distribution = lat_lon.value_counts()

    loja_data = {
        'revenue': revenue,
        'categories_ranking': categories_ranking,
        'products_ranking': products_ranking,
        'rating_mean': rating_mean,
        'shipping_mean': shipping_mean,
        'lat_lon': lat_lon,
        'sales_distribution': sales_distribution
    }

    return loja_data

def build_comparison_dataframes(lojas_data: dict):
    # Extract the data from the dictionary
    lojas_revenues = {loja_name: loja_data['revenue'] for loja_name, loja_data in lojas_data.items()}
    print(lojas_revenues)
    lojas_categories_ranking = {loja_name: loja_data['categories_ranking'] for loja_name, loja_data in lojas_data.items()}
    lojas_products_ranking = {loja_name: loja_data['products_ranking'] for loja_name, loja_data in lojas_data.items()}
    lojas_rating_mean = {loja_name: loja_data['rating_mean'] for loja_name, loja_data in lojas_data.items()}
    lojas_shipping_mean = {loja_name: loja_data['shipping_mean'] for loja_name, loja_data in lojas_data.items()}
    lojas_sales_distribution = {loja_name: loja_data['sales_distribution'] for loja_name, loja_data in lojas_data.items()}

    # Create dataframes
    lojas_revenues_df = pd.Series(lojas_revenues, name='Revenue')
    lojas_rating_mean_df = pd.Series(lojas_rating_mean, name='Rating mean')
    lojas_shipping_mean_df = pd.Series(lojas_shipping_mean , name='Shipping mean')

    lojas_stats = pd.concat([lojas_revenues_df, lojas_rating_mean_df, lojas_shipping_mean_df], axis=1)
    lojas_categories_ranking_df = pd.DataFrame(lojas_categories_ranking)
    lojas_products_ranking_df = pd.DataFrame(lojas_products_ranking)
    lojas_sales_distribution_df = pd.DataFrame(lojas_sales_distribution)
    lojas_categories_ranking_df['TOTAL'] = lojas_categories_ranking_df.sum(axis=1)
    lojas_products_ranking_df['TOTAL'] = lojas_products_ranking_df.sum(axis=1)
    lojas_sales_distribution_df['TOTAL'] = lojas_sales_distribution_df.sum(axis=1)
    
    # Sort the dataframes
    lojas_stats.sort_values(by='Revenue', ascending=False)
    lojas_stats.sort_values(by='Rating mean', ascending=False)
    lojas_stats.sort_values(by='Shipping mean', ascending=True)
    lojas_categories_ranking_df.sort_values(by='TOTAL', ascending=False, inplace=True)
    lojas_products_ranking_df.sort_values(by='TOTAL', ascending=False, inplace=True)
    lojas_sales_distribution_df.sort_values(by='TOTAL', ascending=False, inplace=True)

    # Format dataframes
    lojas_stats = lojas_stats.round(2)
    lojas_sales_distribution_df.dropna(inplace=True)
    cols_to_convert = ['loja1', 'loja2', 'loja3', 'loja4', 'TOTAL']
    lojas_sales_distribution_df[cols_to_convert] = lojas_sales_distribution_df[cols_to_convert].astype(int)

    lojas_comparisons = {
        'lojas_stats': lojas_stats,
        'lojas_categories_ranking': lojas_categories_ranking_df,
        'lojas_products_ranking': lojas_products_ranking_df,
        'lojas_sales_distribution': lojas_sales_distribution_df
    }

    return lojas_comparisons

loja1_data = analyze_data(loja, 'loja 1')
loja2_data = analyze_data(loja2, 'loja 2')
loja3_data = analyze_data(loja3, 'loja 3')
loja4_data = analyze_data(loja4, 'loja 4')
lojas_data = {
    'loja1': loja1_data,
    'loja2': loja2_data,
    'loja3': loja3_data,
    'loja4': loja4_data
}

lojas_comparisons = build_comparison_dataframes(lojas_data)
lojas_comparisons['lojas_stats']
lojas_comparisons['lojas_categories_ranking']
lojas_comparisons['lojas_products_ranking']
lojas_comparisons['lojas_sales_distribution']