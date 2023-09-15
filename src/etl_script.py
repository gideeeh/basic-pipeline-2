import pandas as pd
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH, "..", "data", "books.csv")

df = pd.read_csv(DATA_PATH)

print(df.head())

from sqlalchemy import create_engine

# FOR SQLite
DATABASE_URL = "sqlite:///etl_project.db"
engine = create_engine(DATABASE_URL)

df.to_sql('books', engine, index=False, if_exists='replace')

loaded_df = pd.read_sql('books', engine)
print(loaded_df.head())
