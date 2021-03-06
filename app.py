import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                static_folder='static')
server = app.server
app.config.suppress_callback_exceptions = True
