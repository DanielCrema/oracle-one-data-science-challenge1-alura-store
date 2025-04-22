# Html and Mardown big texts used in the Streamlit App
# Exported as variables for a cleaner main code

streamlit_header = """<a name="alura-store-statistics"></a><div style="text-align: center; margin-bottom: 1rem">
    <h1 style="padding: 0 0 0.5rem; font-size: 3rem; letter-spacing: 0.1rem; font-weight: bold">Alura Store 🧊</h1>
    <p style="font-size: 1.25rem; letter-spacing: 0.01rem; margin: 0 0 1.5rem">Análise das lojas do Sr. João</p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; justify-items: start; margin: 0 auto; text-align: left">
        <div>
            <p style="font-size: 1.5rem; letter-spacing: 0.01rem; margin-bottom: 0.5rem">Dados Globais:</p>
            <ul style="font-size: 1rem; padding-left: 0; list-style: none">
                <li style="margin-left: 0; padding-left: 0">💰 Faturamento Total</li>
                <li style="margin-left: 0; padding-left: 0">🌟 Média de Avaliações</li>
                <li style="margin-left: 0; padding-left: 0">💸 Média de Frete</li>
                <li style="margin-left: 0; padding-left: 0">🗺️ Distribuição Geográfica</li>
            </ul>
        </div>
        <div>
            <p style="font-size: 1.5rem; letter-spacing: 0.01rem; margin-bottom: 0">Dados Específicos:</p>
            <p style="font-size: 1rem; margin: 0 0 0.5rem">(Filtros se aplicam)</p>
            <ul style="font-size: 1rem; padding-left: 0; list-style: none">
                <li style="margin-left: 0; padding-left: 0">🛋️ Categorias mais Vendidas</li>
                <li style="margin-left: 0; padding-left: 0">🔢 Ranking de Produtos</li>
                <li style="margin-left: 0; padding-left: 0">🚛 Frete Médio por Produto</li>
            </ul>
        </div>
    </div>
</div>"""

sidebar_credits = """<div style="display: flex; flex-direction: column; gap: 14px; margin-top: 5px">
    <div>
        <p style="font-size: 14px; margin: 0">Desenvolvido por:</p>
        <p style="font-size: 14px; margin: 0">Daniel Crema</p>
    </div>
    <div>
        <img src="https://raw.githubusercontent.com/devicons/devicon/ca28c779441053191ff11710fe24a9e6c23690d6/icons/linkedin/linkedin-original.svg" style="width: 20px; margin-right: 10px"/>
        <a href="https://www.linkedin.com/in/daniel-crema-dev/" target="_blank">LinkedIn</a>
    </div>
    <div>
        <img src="https://raw.githubusercontent.com/devicons/devicon/ca28c779441053191ff11710fe24a9e6c23690d6/icons/github/github-original.svg" style="width: 22px; margin-right: 10px"/>
        <a href="https://github.com/DanielCrema" target="_blank">Github</a>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 18px">
        <p style="font-size: 14px; margin: 0">Agradecimentos:</p>
        <a href="https://www.oracle.com/br/education/oracle-next-education/" target="_blank">ONE - Oracle Next Education</a>
        <a href="https://www.oracle.com/" target="_blank">Oracle</a>
        <a href="https://www.alura.com.br/" target="_blank">Alura</a>
        <img src="https://raw.githubusercontent.com/devicons/devicon/ca28c779441053191ff11710fe24a9e6c23690d6/icons/oracle/oracle-original.svg" style="width: 60px; margin-right: 10px"/>
    </div>
</div>
"""

final_report = """
            O Sr. João, proprietário das lojas Alura Store, precisa vender uma de suas lojas para apriorar a sua eficiência em custos e obter melhores resultados.
            
            ➡️ Considerando os dados avaliados de suas 4 lojas, podemos concluir que:
            1. **Faturamento:**
                - As `lojas 1, 2 e 4` são as que possuem maior faturamento.<br><br>
            2. **Avaliação Média:**
                - As `lojas 3 e 2` são as que possuem maior avaliação média.
                - A `loja 1` tem a menor avaliação média.<br><br>
            3. **Frete Médio:**
                - A `loja 4` possui o menor frete médio, com uma diferença significativa, seguida da `loja 3`.<br><br>
            4. **Vendas por Categoria:**<br>
                As categorias de `móveis`, `eletrônicos` e `brinquedos` são as que possuem maior número de vendas. Nestas categorias:
                - As `lojas 3 e 4` têm o melhor desempenho.
                - A `loja 2` tem o pior desempenho.<br><br>
            5. **Vendas por Produto:**<br>
                `Cômodas`, `carrinhos de controle remoto` e `fornos de micro-ondas` são os produtos que possuem maior número de vendas. Nestes produtos:
                - As `lojas 1 e 4` têm o melhor desempenho.
                - As `loja 2 e 3` têm o pior desempenho.<br><br>
            6. **Distribuição Geográfica:**
                - Das 9421 vendas registradas, 6257 `(66,41%)` foram realizadas no raio de `latitude -20` e `longitude -46`, que corresponde à região central de São Paulo.<br><br>
            
            💡 **Insights significativos:**<br>
            As lojas possuem estatísticas muito similares que dificultam a aferição da pior performance dentre elas. Observa-se que:
            - A `loja 1` possui o melhor desempenho entre os produtos mais vendidos e o maior faturamento.
            - A `loja 3` e a `loja 4` possuem excelente desempenho de vendas entre as categorias e produtos mais vendidos enquanto ao mesmo tempo possuem o menor frete médio, evidência de que os sistemas de distribuição destas lojas atendem com melhor eficiência a região central de São Paulo, onde se registra a maior quantidade de vendas.
            - A `loja 2` possui o pior desempenho em vendas, embora tenha o segundo maior faturamento. Além disso, possui o segundo maior frete médio. O alto faturamento é provavelmente decorrente de um maior valor agregado dos produtos vendidos, o que não se traduz necessariamente em lucros.<br><br>

            ### 📊 Conclusão das Observações
            ➡️ Considerando os dados avaliados anteriormente:
            - Embora nenhuma das lojas apresente um desempenho consideravelmente ruim, dentre todas as observadas a `loja 2` se destaca como a melhor candidata a ser vendida.
            """