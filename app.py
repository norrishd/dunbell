"""
Main app launching point
"""
import dash
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
    dcc.Dropdown(
        options=[
            {'label': df['display_name'], 'value': df['id']}
            for i, df in read_friend_deets().iterrows()]
    ),

    generate_table(lookup_facts(1))

    # dcc.Graph(
    #     id='example-graph',
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Groovy'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Grand'},
    #         ],
    #         'layout': {
    #         }
    #     }
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)
