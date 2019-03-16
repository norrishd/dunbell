"""
Main app launching point
"""
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from utils import read_friend_deets, lookup_facts, generate_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(style={
        'textAlign': 'center'
        }, children="DunBell: A dumbbell for your Dunbar's number"),

    html.Div(style={
        'textAlign': 'center'
    }, children="Keep track of interesting acquaintances and common interests"),

    html.Label('Acquaintance'),
    dcc.Dropdown(id='friend-selector', options=[
            {'label': df['display_name'], 'value': df['id']}
            for i, df in read_friend_deets().iterrows()]
    ),

    html.Div(id='fact-table')
])


@app.callback(
    Output(component_id='fact-table', component_property='children'),
    [Input(component_id='friend-selector', component_property='value')]
)
def update_fact_table(friend_id):
    df = lookup_facts(friend_id)
    return generate_table(df)

if __name__ == '__main__':
    app.run_server(debug=True)
