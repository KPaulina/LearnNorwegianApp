import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import insert

df_words = pd.read_excel('Vocab.xlsx')
df_irregular_verbs = pd.read_excel('verbs.xlsx')
df_irregular_verbs['infinitiv'] = df_irregular_verbs['infinitiv'].str.strip()
df_irregular_verbs['presens'] = df_irregular_verbs['presens'].str.strip()
df_irregular_verbs['preteritum'] = df_irregular_verbs['preteritum'].str.strip()
df_irregular_verbs['presens_perfektum'] = df_irregular_verbs['presens_perfektum'].str.strip()
print(df_words.head())
df_words.index += 1
df_words.rename(columns={'norweski': 'word_in_norwegian', 'polski': 'word_in_polish', 'angielski': 'word_in_english'}, inplace=True)

engine = create_engine('postgresql://postgres:iqejhsfddoznouyzvdty@localhost:5432/Norapp')
# df_words.to_sql('LearnNorwegianApp_vocabulary', con=engine, if_exists='append', index=False)
df_words.to_sql('LearnNorwegianApp_vocabulary', con=engine, if_exists='append', index=False)
