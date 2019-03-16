"""Helper functions for wrangling Pandas tables and whatnot"""
from pathlib import Path

import dash_html_components as html
import pandas as pd


DATA_PATH = Path('static/data')
FRIEND_FILE = 'friends.csv'
FACTS_FILE = 'facts.csv'

def read_friend_deets(id=None):
    """Return details of a friend as a Pandas series"""
    df = pd.read_csv(DATA_PATH / FRIEND_FILE, dtype=str)
    if id is not None:
        return df[df['id'] == str(id)]
    return df


def lookup_facts(id):
    """Look up all facts about a given person"""
    df = pd.read_csv(DATA_PATH / FACTS_FILE, dtype=str)
    df = df[df['person_id'] == str(id)]
    return df.sort_values('fact_importance', ascending=False)


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )