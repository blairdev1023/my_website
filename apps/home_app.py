import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.Div(
        className='app-header',
        children=[html.Div(className='app-header--title')]
    ),
    html.Div(
        html.Div(children=html.Img(
            className='picture',
            src='assets/headshot.jpg',
            style=dict(height=300, width=300)
        ),
        style={
            # This dict has to be with curlies because of the dashes in the
            # key names, it's annoying, I know
            'display': 'inline-block',
            'width': '100%',
            'text-align': 'center',
            'margin-top': 40,
            'margin-bottom': 40
        }),
        style=dict(
            height=400,
            width='35%',
            float='left',
            display='inline-block',
            backgroundColor='white'
        )
    ),
    html.Div(html.Div([
        html.P('Hello World,', className='title-text'),
        html.P('I\'m Blair Thurman!', className='title-text')
        ], style={'margin-top': 100}),
        style=dict(
            height=400,
            width='65%',
            float='left',
            display='inline-block',
            backgroundColor='white'
        )
    )
], style={'width': '80%', 'margin': 'auto', 'backgroundColor': 'white'})
