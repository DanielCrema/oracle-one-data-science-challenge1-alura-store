import sys
sys.path

import pandas as pd

link = "./base-de-dados-challenge-1/loja_1.csv"
link2 = "./base-de-dados-challenge-1/loja_2.csv"
link3 = "./base-de-dados-challenge-1/loja_3.csv"
link4 = "./base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(link)
loja2 = pd.read_csv(link2)
loja3 = pd.read_csv(link3)
loja4 = pd.read_csv(link4)

loja.head()