import pandas as pd
import streamlit as st

@st.cache_data
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