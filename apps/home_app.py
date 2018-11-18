import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    # Page Header
    html.Div(className='app-header'),
    # Headshot
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
    # Title
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
    ),
    # About
    html.Div(
        html.Div('About:', className='section-header'),
        style=dict(
            height=200,
            width='35%',
            float='left',
            display='inline-block',
            backgroundColor='white',
        )
    ),
    html.Div([
        html.P(className='text-block', children=
        '''
        I'm an unabashed data nerd, father of two cats, wannabe historian, and an awful dancer. This site serves as my portfolio for my passion projects.
        '''),
        html.P(className='text-block', children=
        '''
        Born and raised in Colorado, I spent 2018 exploring and getting lost in the Western United States. Now that I've satiated my wanderlust I'm setting down roots. Being the sun-creature that I am - I've decided on Phoenix!
        ''')],
        style=dict(
            height=200,
            width='65%',
            float='left',
            display='inline-block',
            backgroundColor='white',
        )
    ),
    # Project
    # About
    html.Div(
        html.Div('Projects:', className='section-header'),
        style=dict(
            height=200,
            width='35%',
            float='left',
            display='inline-block',
            backgroundColor='white',
        )
    ),
    html.Div([

        html.A(
            html.Button('Gun Violence'),
            href='/gun_violence'
        ),
        html.A(
            html.Button('Telco'),
            href='/telco'
        ),

        html.P(className='text-block', children=
        '''
        '''),
        html.P(className='text-block', children=
        '''
        ''')],
        style=dict(
            height=200,
            width='65%',
            float='left',
            display='inline-block',
            backgroundColor='white',
        )
    )
], style={'width': '80%', 'margin': 'auto', 'backgroundColor': 'white'})
