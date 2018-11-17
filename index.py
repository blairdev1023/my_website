import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import home_app, gun_violence_app, google_revenue_app


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
         return home_app.layout
    elif pathname == '/gun_violence':
         return gun_violence_app.layout
    elif pathname == '/google_revenue':
         return google_revenue_app.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
