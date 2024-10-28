# %%
import pandas as pd
import numpy as np

# %%
# configuração de seed para reprodutibilidade
np.random.seed(42)

# list de meses para ambos os datasets
meses_orcados = pd.date_range(start="2024-01-01", end="2024-12-01", freq='MS').strftime('%Y-%m').tolist()
meses_realizados = pd.date_range(start="2024-01-01", end="2024-10-01", freq='MS').strftime('%Y-%m').tolist()

# departamentos, categorias e motivos
departamentos = ['Financeiro', 'Operações', 'RH', 'TI', 'Marketing']
categorias = ['Salários', 'Projetos', 'Treinamentos', 'Outros']

# %%
# Função de gerar o dataset orçado
def gerar_dataset_orcado():
    data = {
        'mes': [],
        'departamento': [],
        'categoria': [],
        'valor_orcado': []
    }
    for mes in meses_orcados:
        for depto in departamentos:
            for cat in categorias:
                data['mes'].append(mes)
                data['departamento'].append(depto)
                data['categoria'].append(cat)
                data['valor_orcado'].append(round(np.random.uniform(5000, 50000), 2))
    return pd.DataFrame(data)

# %%
# Função para gerar o dataset realizado
def gerar_dataset_realizado():
    data = {
        'mes': [],
        'departamento': [],
        'categoria': [],
        'valor_orcado': []
    }
    for mes in meses_realizados:
        for depto in departamentos:
            for cat in categorias:
                data['mes'].append(mes)
                data['departamento'].append(depto)
                data['categoria'].append(cat)
                data['valor_orcado'].append(round(np.random.uniform(4000, 50000), 2))
    return pd.DataFrame(data)

# %%
# Gerar datasets
orcado_df = gerar_dataset_orcado()
realizado_df = gerar_dataset_realizado()
# %%
orcado_df.to_csv('orcado.csv', index=False)
realizado_df.to_csv('realizado.csv', index=False)
# %%
