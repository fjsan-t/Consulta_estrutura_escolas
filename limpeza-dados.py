import pandas as pd

arquivo_nome = 'microdados_ed_basica_2022.csv (1).zip'
df = pd.read_csv(arquivo_nome, sep=';', encoding='latin1', nrows=5)
df.head()

df_completo = pd.read_csv(arquivo_nome, sep=';', encoding='latin1', low_memory=False)
df_bahia_publica = df_completo[(df_completo['SG_UF'] == 'BA') & (df_completo['TP_DEPENDENCIA'] <= 3)]
print(f"Filtragem concluída! Foram encontradas {df_bahia_publica.shape[0]} escolas públicas na Bahia.")
df_bahia_publica.head()

colunas_selecionadas = [
    'CO_ENTIDADE',
    'NO_ENTIDADE',
    'NO_MUNICIPIO',
    'TP_DEPENDENCIA',
    'IN_LABORATORIO_INFORMATICA',
    'IN_FUND',
    'IN_MED',
    'IN_PROF_TEC'
]
df_mvp = df_bahia_publica[colunas_selecionadas]
df_mvp.head()
