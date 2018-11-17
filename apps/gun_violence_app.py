import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('Gun Violence in America, 2014-2018'),
    dcc.Link('Go Home', href='/home'),
])
