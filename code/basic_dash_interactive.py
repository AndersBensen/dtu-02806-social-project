import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#initial dataframe prep
df = pd.read_csv("../data/Motor_Vehicle_Collisions_-_Crashes.csv",low_memory=False)
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])
available_years = np.sort(df['CRASH DATE'].dt.year.unique())[:-1]

#make 
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='collision-year',
            options=[{'label': i, 'value': i} for i in available_years],
            value=2020
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic')
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('collision-year', 'value'))
def update_graph(collision_year):
    dff = df[df['CRASH DATE'].dt.year==collision_year]
    fig = px.density_mapbox(dff, lat='LATITUDE', lon='LONGITUDE', radius=1,
                        center=dict(lat=40.730610, lon=-73.935242), zoom=10,
                        mapbox_style="stamen-terrain",height=800)
    return fig

if __name__ == '__main__':
    app.run_server(debug=False)