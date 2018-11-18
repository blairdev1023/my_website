import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('Predicting Google Revenue'),
    dcc.Link('Go Home', href='/home'),
    dcc.Input(id='input'),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'),
             [Input('input', 'value')])
def some_foo(val):
    return "The input reversed is: " + val[::-1]
