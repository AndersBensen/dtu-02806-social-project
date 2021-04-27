import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np 

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Initial dataframe prep
df = pd.read_csv("../data/Motor_Vehicle_Collisions_-_Crashes.csv",low_memory=False)
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])
available_years = np.sort(df['CRASH DATE'].dt.year.unique())[:-1]
radio_buttons = ['TOTAL COLLISIONS','NUMBER OF PERSONS INJURED','NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
'NUMBER OF PEDESTRIANS KILLED','NUMBER OF CYCLIST INJURED','NUMBER OF CYCLIST KILLED','NUMBER OF MOTORIST INJURED','NUMBER OF MOTORIST KILLED']

# Markdown text
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

# This is a variable which contains the dropdown of the heatmap
controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year of collision: "),
                dcc.Dropdown(
                    id='collision-year-dropdown',
                    options=[{'label': i, 'value': i} for i in available_years],
                    value=2020
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Choose which kind of data you want to see: "),
                dbc.RadioItems(
                    id="data-type-radio",
                    options=[{'label': i, 'value': i} for i in radio_buttons],
                    value='TOTAL COLLISIONS',
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label('Radius: '),
                dcc.Slider(
                    id="radius-slider", 
                    min=1,
                    max=20,
                    step=1,
                    value=1,
                    marks={1:'1', 5:'5', 10:'10', 15:'15', 20:'20'}
                    )
            ]
        )
    ],
    body = True, 
    #color='dark'
)

# This method simply plots the amount of collisions in each borough
def bar_borough_collisions(): 
    borough_cols = df['BOROUGH'].value_counts()
    fig = px.bar(x=list(borough_cols.index),y=list(borough_cols.values))
    return fig 

# This method takes input from the dropdown and spits out a figure, we use callback for this scenario
@app.callback(
    Output('heatmap-graphic', 'figure'),
    Input('collision-year-dropdown', 'value'),
    Input('data-type-radio', 'value'),
    Input('radius-slider', 'value'))
def update_graph(collision_year, data_type, radius_val):
    dff = df[df['CRASH DATE'].dt.year==collision_year]
    fig = None 
    if (data_type == 'TOTAL COLLISIONS'): 
        fig = px.density_mapbox(dff, lat='LATITUDE', lon='LONGITUDE', radius=radius_val,
                            center=dict(lat=40.730610, lon=-73.935242), zoom=10,
                            mapbox_style="carto-positron",height=800)
    else: 
        fig = px.density_mapbox(dff, lat='LATITUDE', lon='LONGITUDE', z=data_type, radius=radius_val,
                            center=dict(lat=40.730610, lon=-73.935242), zoom=10,
                            mapbox_style="carto-positron",height=800)
    return fig

# We assemble all the parts of the website here
app.layout = dbc.Container(
    [
        html.H1("Blabla header"),
        html.Hr(), 
        dcc.Markdown(children=markdown_text),  
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="borough-collisions",figure=bar_borough_collisions())),
            ]
        ),
        html.H1("Blabla header"), 
        html.Hr(),
        dcc.Markdown(children=markdown_text),
        dbc.Row(
            [
                dbc.Col(controls, md=3),
                dbc.Col(dcc.Graph(id="heatmap-graphic"), md=8),
            ],
            align='center'
        ),
    ],
    fluid = True,
    # style = {
    #     'background-image': 'url(https://upload.wikimedia.org/wikipedia/commons/2/22/North_Star_-_invitation_background.png)'
    #     'backgroundColor': '#111111'
    #     },
)

if __name__ == '__main__':
    app.run_server(debug=False)