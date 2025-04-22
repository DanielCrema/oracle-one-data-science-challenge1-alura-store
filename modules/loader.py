from pathlib import Path
from modules.pre_processor import pre_process
import pandas as pd
import streamlit as st

def resolve_path(relative_path_str):
    # Assume path is always relative to project root
    project_root = Path(__file__).resolve().parent.parent  # adjust as needed
    return (project_root / relative_path_str).resolve()

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    '''
    Loads and pre processes data from a CSV file.
    Parameters:
    - path (str): The relative path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded and pre processed DataFrame.
    '''
    data_path = resolve_path(path)
    dataframe = pre_process(pd.read_csv(data_path))

    return dataframe