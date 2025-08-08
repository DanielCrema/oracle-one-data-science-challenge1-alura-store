# Alura Store 📊🛍️
This project offers a complete **statistical analysis** platform for different stores, helping to visualize, compare, and download key data about sales, ratings, categories, products, and shipping costs.

Developed with **Streamlit**, it provides an intuitive, interactive, and responsive web application, accessible on desktops, laptops, tablets, and smartphones.

## ➡️ Data Pipeline
This project features an **organized modular structure** for data processing and analysis, separating logic into clearly defined layers and modules.

### Data Flow:
- 🛒 Load and preprocess raw store data.

- 🔍 Analyze individual store statistics.

- 🏛️ Build comparative global statistics.

- 📈 Generate professional charts and plots.

- 📦 Provide downloadable processed datasets in a single ZIP file.

*🎞️ Explore a comprehensive dashboard with real-time chart generation and interactive filters!*

## 🌐 Access
🔗 [Application](https://alurastore.streamlit.app)

🔗 [Code: For students and analysts](https://github.com/DanielCrema/oracle-one-data-science-challenge1-alura-store/tree/main)

## ✨ Features
- 📂 Load and preprocess multiple store datasets.

- 📊 Interactive data visualizations:

    - Revenue distribution pie chart.

    - Ratings mean comparison.

    - Average shipping cost bar chart.

    - Geographical sales distribution map.

    - Top 10 best-selling categories and products.

    - Heatmap of shipping costs by product.

- 📈 Real-time filters by store selection.

- 📥 Download processed data (CSV/ZIP).

- 📄 Final report section with overall insights.

## 🛠️ Stack
[Python 3](https://www.python.org)

[Pandas](pandas.pydata.org) – Data manipulation.

[Matplotlib](https://matplotlib.org) – Chart generation.

[Seaborn](https://seaborn.pydata.org) – Enhanced statistical plotting.

[Streamlit](https://streamlit.io) – Web application framework.


## 🗂️ Project Structure
```bash
.
├── main.py              # Main Streamlit application
│
├── modules/
│   ├── loader.py           # Data loading
│   ├── pre_processor.py    # Preprocessing module
│   ├── analyze_stores.py   # Store-specific data analysis
│   └── build_statistics.py # Statistical dataframes generator
│
├── utils/
│   ├── plot_horizontal_bar.py        # Horizontal bar plot utility
│   ├── rename_label.py               # Label renaming utility
│   └── generate_downloadable_zip.py  # ZIP generator
│
├── app_ui.py            # Streamlit UI HTML elements
│
└── base-de-dados-challenge-1/
    └── loja_1.csv          # Example input files
    └── loja_2.csv
    └── loja_3.csv
    └── loja_4.csv
```

## 📑 How to Run Locally
1. Clone the repository:

```bash
git clone https://github.com/DanielCrema/oracle-one-data-science-challenge1-alura-store.git
cd oracle-one-data-science-challenge1-alura-store
```

2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run main.py
```

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🎓 Credits
Developed by [**Daniel Crema**](https://github.com/DanielCrema) for educational and analytical purposes as part of the Alura Challenge 1 of the **ONE - Oracle Next Education** program.
Special thanks to Oracle and Alura, as well as all contributors, mentors, and the amazing Python open-source community!

<a href="https://github.com/DanielCrema/oracle_one-data-science-course/blob/main/certificates/Daniel%20Borges%20Crema%20-%20Program%20ONE%20Certificate.pdf" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/ca28c779441053191ff11710fe24a9e6c23690d6/icons/oracle/oracle-original.svg" alt="logo-oracle" style="width: 70px"/>  
</a>

<a href="https://github.com/DanielCrema/oracle_one-data-science-course/blob/main/certificates/Daniel%20Borges%20Crema%20-%20Programa%20ONE%20Certificado%20-%20Es.pdf" target="_blank" rel="noreferrer">
    <img src="https://moebius78.github.io/moebius78-sprint03-aluraONE.github.io/assets/Oracle_Alura.png" alt="logo-oracle-alura-latam" style="width: 115px; background: #FCFCFC; color: #333; padding: 2px 3px"/>  
</a>