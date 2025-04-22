import pandas as pd

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