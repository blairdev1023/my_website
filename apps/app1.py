import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('App 1'),
    dcc.Link('Go to App 2', href='/apps/app2'),
    dcc.Link('Go to App 3', href='/apps/app3')
])
