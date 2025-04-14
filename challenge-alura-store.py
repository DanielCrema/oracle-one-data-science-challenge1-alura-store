import sys
sys.path

import pandas as pd
import numpy as np

link = "./base-de-dados-challenge-1/loja_1.csv"
link2 = "./base-de-dados-challenge-1/loja_2.csv"
link3 = "./base-de-dados-challenge-1/loja_3.csv"
link4 = "./base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(link)
loja2 = pd.read_csv(link2)
loja3 = pd.read_csv(link3)
loja4 = pd.read_csv(link4)

# print(loja)
# print(loja)

def study():
    # Display the first 5 rows
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.head()\n')
    print(loja.head())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Display the last 5 rows
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.tail()\n')
    print(loja.tail())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Show shape (rows, columns)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.shape\n')
    print(loja.shape)
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Show info (data types and nulls)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.info()\n')
    print(loja.info())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Show summary statistics (numerical)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.describe()\n')
    print(loja.describe())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Show column names
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.columns\n')
    print(loja.columns)
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Convert 'Produto' column to list (first 10 items)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja["Produto"].tolist()\n')
    print(loja['Produto'].tolist()[0:10])
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Show first 10 ['Produto', 'Preço'] as list of rows
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja[["Produto", "Preço"]].values.tolist()\n')
    print(loja[['Produto', 'Preço']].values.tolist()[0:10])
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Convert all values to list (first 10 rows)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.values.tolist()\n')
    print(loja.values.tolist()[0:10])
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Convert columns to list (first 10 columns)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.columns.tolist()\n')
    print(loja.columns.tolist())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Convert DataFrame to NumPy array (first 10 rows)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.to_numpy()\n')
    print(loja.to_numpy()[0:10])
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Check for null values per column
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.isnull().sum()\n')
    print(loja.isnull().sum())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Check for NA values per column (same as isnull)
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.isna().sum()\n')
    print(loja.isna().sum())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Count duplicated rows
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print('\n\n=> loja.duplicated().sum()\n')
    print(loja.duplicated().sum())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Group by vendedor and sum 'Preço'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja.groupby('Vendedor')['Preço'].sum()\n")
    print(loja.groupby('Vendedor')['Preço'].sum())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Filter rows where 'Categoria do Produto' is 'brinquedos'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja[loja['Categoria do Produto'] == 'brinquedos']\n")
    print(loja[loja['Categoria do Produto'] == 'brinquedos'])
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Count frequency of 'Local da compra'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja['Local da compra'].value_counts()\n")
    print(loja['Local da compra'].value_counts())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Sort values by 'Preço' in descending order
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja.sort_values('Preço', ascending=False)\n")
    print(loja.sort_values('Preço', ascending=False).head(10))
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Create a new column 'Total' as sum of 'Preço' and 'Frete'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja['Total'] = loja['Preço'] + loja['Frete']\n")
    loja['Total'] = loja['Preço'] + loja['Frete']
    print(loja[['Preço', 'Frete', 'Total']].head())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Get unique values in 'Tipo de pagamento'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja['Tipo de pagamento'].unique()\n")
    print(loja['Tipo de pagamento'].unique())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Create a pivot table with mean 'Preço' by 'Categoria do Produto'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja.pivot_table(index='Categoria do Produto', values='Preço', aggfunc='mean')\n")
    print(loja.pivot_table(index='Categoria do Produto', values='Preço', aggfunc='mean'))
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Filter rows with 'Data da Compra' after '2021-01-01'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja[loja['Data da Compra'] > '2021-01-01']\n")
    print(loja[loja['Data da Compra'] > '01/01/2021'])
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Get correlation matrix for numerical columns
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja.corr(numeric_only=True)\n")
    print(loja.corr(numeric_only=True))
    print("\n# # # # # # # # # # # # # # # # #\n\n")

    # Get unique values in 'Produto'
    print("\n# # # # # # # # # # # # # # # # #\n\n")
    print("\n\n=> loja['Produto'].unique()\n")
    print(loja['Produto'].unique())
    print("\n# # # # # # # # # # # # # # # # #\n\n")

study()

def treat_data(data):
    treated_data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return treated_data

treated_data = treat_data(loja)
print(loja['Produto'].tolist()[0:10])
print('\n\n\n\n')
print(treated_data['Produto'].tolist()[0:10])