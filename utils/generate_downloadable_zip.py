import streamlit as st
import os
import zipfile
import io

def zip_files(lojas_comparisons: dict) -> bytes:
    original_files = {
        "loja_1.csv": "base-de-dados-challenge-1/loja_1.csv",
        "loja_2.csv": "base-de-dados-challenge-1/loja_2.csv",
        "loja_3.csv": "base-de-dados-challenge-1/loja_3.csv",
        "loja_4.csv": "base-de-dados-challenge-1/loja_4.csv",
    }

    # Unpacking the data
    lojas_stats = lojas_comparisons['lojas_stats']
    lojas_categories = lojas_comparisons['lojas_categories_ranking']
    lojas_products = lojas_comparisons['lojas_products_ranking']
    lojas_top10_products_shipping_mean = lojas_comparisons['top10_products_shipping_mean']
    lojas_sales_distribution = lojas_comparisons['lojas_sales_distribution']

    def convert_df_to_csv(df):
        return df.to_csv(index=True).encode('utf-8')

    # Create a zip file in memory
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        # Add raw original files
        for zip_name, file_path in original_files.items():
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    zip_file.writestr(f"base-de-dados-challenge-1/{zip_name}", f.read())
            else:
                st.warning(f"Arquivo não encontrado: {file_path}")
        
        # Add processed files
        zip_file.writestr("estatisticas_globais.csv", convert_df_to_csv(lojas_stats.T))
        zip_file.writestr("categorias_mais_vendidas.csv", convert_df_to_csv(lojas_categories))
        zip_file.writestr("produtos_mais_vendidos.csv", convert_df_to_csv(lojas_products))
        zip_file.writestr("frete_medio_top10_produtos.csv", convert_df_to_csv(lojas_top10_products_shipping_mean))
        zip_file.writestr("distribuicao_geografica_vendas.csv", convert_df_to_csv(lojas_sales_distribution))

    # Move back to the start of the BytesIO buffer
    zip_buffer.seek(0)

    return zip_buffer