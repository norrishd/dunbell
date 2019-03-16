"""
Main app launching point
"""
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from utils import read_friend_deets, lookup_facts, generate_table, add_person

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(style={
        'textAlign': 'center'
    }, children="Dunbell: A dumbbell for your Dunbar's number"),

    html.H3(style={
        'textAlign': 'center'
    }, children="Keep track of interesting people and shared interests"),

    html.Div([
        html.Div(style={
            'width': '48%', 'maxWidth': '200px', 'display': 'inline-block'},
                 children=[
                     html.Label('Person'),
                     dcc.Dropdown(id='person-selector')
                     ]
                 ),
        html.Div(id='person-adder-div', style={'width': '48%'},
                 hidden=True, children=[
                     dcc.Input(id='add-person-input', placeholder="Person's name"),
                     html.Button(id='add-person-button', n_clicks=0, children='Add')
                     ])
    ]),

    html.Div(id='fact-table')
])


@app.callback(
    Output(component_id='fact-table', component_property='children'),
    [Input(component_id='person-selector', component_property='value')]
)
def update_fact_table(person_id):
    """"Get facts for selected person"""
    df = lookup_facts(person_id)
    return generate_table(df)


@app.callback(
    Output(component_id='person-adder-div', component_property='hidden'),
    [Input(component_id='person-selector', component_property='value')]
)
def show_person_adder(selected):
    """Show the dialogue to add a friend if 'Add person' chosen"""
    if selected == -1:
        return False
    return True

### Add a friend callbacks
@app.callback(
    Output('person-selector', 'options'),
    [Input('add-person-button', 'n_clicks')]
)
def regenerate_friend_options(n_clicks):
    """Read friends file and generate options"""
    return [{'label': df['display_name'], 'value': df['id']} for
            i, df in read_friend_deets().iterrows()] + [{
                'label': 'Add person...', 'value': -1
            }]

@app.callback(
    Output('add-person-input', 'value'),
    [Input('add-person-button', 'n_clicks')],
    [State('add-person-input', 'value')]
)
def add_a_person(n_clicks, name):
    """Add a person to file"""
    add_person(name)
    return ""

if __name__ == '__main__':
    app.run_server(debug=True)
