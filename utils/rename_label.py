def rename_label(label: str) -> str:
    '''
    Renames the labels in the chart for specific cases of too long labels.
    ### Parameters:
    - label: A plt.label or an ax.ticklabel.
    ### Returns:
    - The renamed label.
    '''
    replacements = {
        'instrumentos musicais': 'Instrum. musicais',
        'utilidades domesticas': 'Util. domésticas',
        'carrinho controle remoto': 'Carrinho cont. remoto',
    }
    text = label.get_text().lower()
    
    return replacements.get(text, label.get_text().capitalize())