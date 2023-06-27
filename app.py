'''------IMPORTS------'''
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import plotly.io as io
io.templates.default = 'plotly_dark'


'''------INCORPORATING DATA------'''
df = pd.read_csv('heartrate.csv') #target csv file
app = Dash(__name__) #dash constructor to initialize site


'''------INITIALIZING PLOTS------'''
line = px.line(df, x='Time', y='Rate')
density = px.density_contour(df, x='Time', y='Rate')
polar = px.bar_polar(df, r='Rate', theta='Time', color='Rate')
scatter = px.scatter(df, x='Time', y='Rate', color='Rate')


'''------GRAPHING PLOTS------'''
app.layout = html.Div([ #create layout of site
    html.Div(dcc.Graph(figure=density), style={'display': 'inline-block'},),
    html.Div(dcc.Graph(figure=line), style={'display': 'inline-block'},),
    html.Div(html.P('COMPANY NAME'), style={'textAlign': 'center', 'color':'lightpink', 'fontSize': '30px'},),
    html.Div(dcc.Graph(figure=polar), style={'display': 'inline-block'},),
    html.Div(dcc.Graph(figure=scatter), style={'display': 'inline-block'},),
], style={'textAlign': 'center', 'backgroundColor':'black', 'margin-top':'0px', 'margin-left':'0px', 'margin-right':'0px', 'margin-bottom':'0px'})


'''------RUN SITE------'''
if __name__ == '__main__': #runs site if script is called directly through command-line
    app.run_server(debug=True)
    print
# Export to localhost http://127.0.0.1:8050/
# Run 'python app.py'