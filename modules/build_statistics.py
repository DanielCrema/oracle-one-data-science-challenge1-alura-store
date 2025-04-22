import pandas as pd

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