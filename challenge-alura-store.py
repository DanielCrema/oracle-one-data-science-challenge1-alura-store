import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def pre_process(loja: pd.DataFrame) -> pd.DataFrame:
    '''
    🧼 Pre-processes the store sales data for analysis.

    ### Parameters:
    - **loja** : pd.DataFrame  
        The raw input DataFrame containing sales data.

    ### Returns:
    - **loja** : pd.DataFrame  
        The cleaned and pre-processed DataFrame ready for analysis.

    Transformations Applied:
    ------------------------
    🕒 Converts 'Data da Compra' to datetime format.  
    🏷️ Converts the following columns to *categorical* types:

        • 'Produto'  
        • 'Categoria do Produto'  
        • 'Vendedor'  
        • 'Local da compra'  
        • 'Tipo de pagamento'
    '''
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
    📊 Analyzes store sales data and returns key insights in a dictionary format.
    
    ### Parameters:
    - **loja** : pd.DataFrame
        A DataFrame containing sales data. Expected columns include:
        'Preço', 'Categoria do Produto', 'Produto',
        'Avaliação da compra', 'Frete', 'lat', 'lon'.

    ### Returns:
    - **loja_data** : dict
        A dictionary containing the following analysis results:

        🔸 'revenue' (float):  
            Total revenue generated from sales (sum of all product prices).

        🔸 'categories_ranking' (pd.Series):  
            Frequency ranking of product categories sold (most to least sold).

        🔸 'products_ranking' (pd.Series):  
            Frequency ranking of individual products sold.

        🔸 'rating_mean' (float):  
            Average customer rating from purchases.

        🔸 'shipping_mean' (float):  
            Average shipping cost.

        🔸 'sales_distribution' (pd.Series):  
            Number of sales grouped by geographical coordinates (latitude & longitude pairs).
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

def build_comparison_dataframes(lojas_data: dict) -> dict:
    '''
    🔄 Builds comparison DataFrames from multiple store sales analyses.

    ### Parameters:
    - **lojas_data** : dict  
        A dictionary where each key is a store identifier and each value is a dictionary
        containing the following analysis results:

        📌 'revenue' (float):  
            Total revenue generated from sales.

        📌 'categories_ranking' (pd.Series):  
            Product category frequency ranking.

        📌 'products_ranking' (pd.Series):  
            Individual product frequency ranking.

        📌 'rating_mean' (float):  
            Average customer rating.

        📌 'shipping_mean' (float):  
            Average shipping cost.

        📌 'sales_distribution' (pd.Series):  
            Count of sales per geographic location (latitude & longitude).

    ### Returns:
    - **lojas_comparisons** : dict  
        A dictionary containing comparison DataFrames:

        📊 'lojas_stats' (pd.DataFrame):  
            Summary statistics for each store (revenue, average rating, average shipping).

        🏷️ 'lojas_categories_ranking' (pd.DataFrame):  
            Product category rankings by store.

        📦 'lojas_products_ranking' (pd.DataFrame):  
            Individual product rankings by store.

        🌍 'lojas_sales_distribution' (pd.DataFrame):  
            Sales count per geographic location by store.
    '''
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

# # #
# Main code
# # #

# Importing and pre processing the data
link = "./base-de-dados-challenge-1/loja_1.csv"
link2 = "./base-de-dados-challenge-1/loja_2.csv"
link3 = "./base-de-dados-challenge-1/loja_3.csv"
link4 = "./base-de-dados-challenge-1/loja_4.csv"

loja = pre_process(pd.read_csv(link))
loja2 = pre_process(pd.read_csv(link2))
loja3 = pre_process(pd.read_csv(link3))
loja4 = pre_process(pd.read_csv(link4))

# Analyzing the data
loja1_data = analyze_data(loja)
loja2_data = analyze_data(loja2)
loja3_data = analyze_data(loja3)
loja4_data = analyze_data(loja4)
lojas_data = {
    'loja1': loja1_data,
    'loja2': loja2_data,
    'loja3': loja3_data,
    'loja4': loja4_data
}

# Generating statistical comparisons
lojas_comparisons = build_comparison_dataframes(lojas_data)

# Unpacking the data
lojas_stats = lojas_comparisons['lojas_stats']
lojas_categories = lojas_comparisons['lojas_categories_ranking']
lojas_products = lojas_comparisons['lojas_products_ranking']
lojas_geo = lojas_comparisons['lojas_sales_distribution']