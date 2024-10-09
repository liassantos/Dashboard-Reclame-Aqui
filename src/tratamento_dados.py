import pandas as pd
from config import HAPVIDA_CSV_PATH, IBYTE_CSV_PATH, NAGEM_CSV_PATH

#Importando os dados
df_hapvida = pd.read_csv(HAPVIDA_CSV_PATH)
df_ibyte = pd.read_csv(IBYTE_CSV_PATH)
df_nagem = pd.read_csv(NAGEM_CSV_PATH)

#Tratando dados do Hapvida
df_hapvida['TEMPO'] = pd.to_datetime(df_hapvida['TEMPO'])
df_hapvida['LOCAL'] = df_hapvida['LOCAL'].replace('naoconsta - --', 'NÃO CONSTA')
df_hapvida['LOCAL'] = df_hapvida['LOCAL'].replace('-- - --', 'NÃO CONSTA')

#Criando a lista de Estados do Hapvida
df_hapvida[['CIDADE', 'ESTADO']] = df_hapvida['LOCAL'].str.split('-', expand=True)
df_hapvida['CIDADE'] = df_hapvida['CIDADE'].str.strip()
df_hapvida['ESTADO'] = df_hapvida['ESTADO'].str.strip()
estados_hapvida = list(pd.unique(df_hapvida['ESTADO']))
estados_hapvida.pop(10)
estados_hapvida.sort()
estados_hapvida.insert(0, "TODOS")

#Criando a coluna de tamanho do texto Hapvida
df_hapvida['TAMANHO_TEXTO'] = df_hapvida['DESCRICAO'].str.len()

#Tratando dados do Ibyte
df_ibyte['TEMPO'] = pd.to_datetime(df_ibyte['TEMPO'])
df_ibyte['LOCAL'] = df_ibyte['LOCAL'].replace('-- - --', 'NÃO CONSTA')
df_ibyte['LOCAL'] = df_ibyte['LOCAL'].replace('naoconsta - naoconsta', 'NÃO CONSTA')
df_ibyte['LOCAL'] = df_ibyte['LOCAL'].replace('Ceará-Mirim - RN', 'Ceará Mirim - RN')
df_ibyte['LOCAL'] = df_ibyte['LOCAL'].replace('JUAZEIRO DO NORTE - C', 'JUAZEIRO DO NORTE - CE')
df_ibyte['LOCAL'] = df_ibyte['LOCAL'].replace('IPOJUCA - P', 'IPOJUCA - PE')

#Criando a lista de Estados do Ibyte
df_ibyte[['CIDADE', 'ESTADO']] = df_ibyte['LOCAL'].str.split('-', expand=True)
df_ibyte['CIDADE'] = df_ibyte['CIDADE'].str.strip()
df_ibyte['ESTADO'] = df_ibyte['ESTADO'].str.strip()
estados_ibyte = list(pd.unique(df_ibyte['ESTADO']))
estados_ibyte.pop(17)
estados_ibyte.sort()
estados_ibyte.insert(0, "TODOS")

#Criando a coluna de tamanho do texto Ibyte
df_ibyte['TAMANHO_TEXTO'] = df_ibyte['DESCRICAO'].str.len()

#Tratando dados da Nagem
df_nagem['TEMPO'] = pd.to_datetime(df_nagem['TEMPO'])
df_nagem['LOCAL'] = df_nagem['LOCAL'].replace('naoconsta - naoconsta', 'NÃO CONSTA')
df_nagem['LOCAL'] = df_nagem['LOCAL'].replace('-- - MA', 'NÃO CONSTA - MA')

#Criando a lista de Estados da Nagem
df_nagem[['CIDADE', 'ESTADO']] = df_nagem['LOCAL'].str.split('-', expand=True)
df_nagem['CIDADE'] = df_nagem['CIDADE'].str.strip()
df_nagem['ESTADO'] = df_nagem['ESTADO'].str.strip()
estados_nagem = list(pd.unique(df_nagem['ESTADO']))
estados_nagem.pop(13)
estados_nagem.sort()
estados_nagem.insert(0, "TODOS")

#Criando a coluna de tamanho do texto Nagem
df_nagem['TAMANHO_TEXTO'] = df_nagem['DESCRICAO'].str.len()

#Criando a lista de Status (aplicável às 3 empresas)
lista_status = list(pd.unique(df_hapvida['STATUS']))
lista_status.sort()
lista_status.insert(0, "TODOS")

