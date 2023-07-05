from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
import plotly.io as io

io.templates.default = 'plotly_dark'

# Incorporate data
df1 = pd.read_csv('data/heart.csv') # CHANGE THE CSV FILE HERE!!!
df2 = pd.read_csv('data/sleep.csv') # CHANGE THE CSV FILE HERE!!!
df3 = pd.read_csv('data/steps.csv') # CHANGE THE CSV FILE HERE!!!
df4 = pd.read_csv('data/weight.csv') # CHANGE THE CSV FILE HERE!!!
app = Dash(__name__)

# Initialize plots
line = px.line(df1, x='Time', y='Heart Rate')
density = px.density_contour(df3, x='Time', y='Steps')
polar = px.bar_polar(df2, r='Hours', theta='Date', color='Date')
scatter = px.scatter(df4, x='Date', y='Weight', color='Date')
 
# Graph plots + Title
app.layout = html.Div([
    html.Div(dcc.Graph(figure=density), style={'display': 'inline-block'},),
    html.Div(dcc.Graph(figure=line), style={'display': 'inline-block'},),

    html.Div(
        html.P('T‎ ‎ ‎ ‎ ‎ R‎ ‎ ‎ ‎ ‎ U‎ ‎ ‎ ‎ ‎ S‎ ‎ ‎ ‎ ‎ S'), style={'textAlign': 'center', 'color':'lightpink', 'fontSize': '30px'},
        #html.P('T     R     U     S     S'), style={'textAlign': 'center', 'color':'pink', 'fontSize': '20px'},        
    ),

    html.Div(dcc.Graph(figure=polar), style={'display': 'inline-block'},),
    html.Div(dcc.Graph(figure=scatter), style={'display': 'inline-block'},),


], style={'textAlign': 'center', 'backgroundColor':'black', 'margin-top':'0px', 'margin-left':'0px', 'margin-right':'0px', 'margin-bottom':'0px'})

#BACKGROUND COLOR UP HERE^^^^^



# Export to local host http://127.0.0.1:8050/
# Run 'python app.py'
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8888,debug=True)
