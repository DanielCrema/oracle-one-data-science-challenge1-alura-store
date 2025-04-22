import pandas as pd
import matplotlib.pyplot as plt
from utils.rename_label import rename_label

def plot_horizontal_bar(df: pd.DataFrame, title: str, xlabel: str, ylabel: str, xlim_left: int, color: str=None) -> plt.Figure:
    '''
    Plots a horizontal bar chart.
    ### Parameters:
    - df: DataFrame containing the data to be plotted.
    - title: Title of the plot.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - xlim_left: Left limit for the x-axis.
    - color: Color of the bars.

    Returns:
    - fig: The figure object.
    '''
    fig, ax = plt.subplots(figsize=(9.5, 10))
    df.plot(kind='barh', ax=ax, color=color)
    ax.invert_yaxis()
    ax.set_xlim(left=xlim_left)
    ax.set_title(title, fontsize=24)
    ax.set_xlabel(xlabel, fontsize=22)
    ax.set_ylabel(ylabel, fontsize=22)
    ax.legend(fontsize=12, title="Lojas", title_fontsize=16)
    ax.set_yticklabels(
        [rename_label(label) for label in ax.get_yticklabels()],
        fontsize=16
    )
    plt.yticks(rotation=35)
    plt.tight_layout()

    return fig