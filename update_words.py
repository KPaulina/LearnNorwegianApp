import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import insert

df_words = pd.read_excel('Vocab.xlsx', sheet_name='nowe')
print(df_words.head())
df_words.index += 1
df_words.rename(columns={'norweski': 'word_in_norwegian', 'polski': 'word_in_polish', 'angielski': 'word_in_english'}, inplace=True)

engine = create_engine('postgresql://admin:Hyec7LgMvrrTkw@localhost:5432/Norapp')
df_words.to_sql('LearnNorwegianApp_vocabulary', con=engine, if_exists='append', index=False)

