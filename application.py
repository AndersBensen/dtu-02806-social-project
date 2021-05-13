import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np 
import json 
import time 


import markdown_text as text 
import ml_figures as ml_fig
import basic_stats_figures as basic_fig

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
start = time.time()
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
application = app.server

# Initial dataframe prep
df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv",low_memory=False)
#df = pd.read_csv("https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accesType=DOWNLOAD", low_memory=False) #download it directly from url, needed when hosting
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'], format="%m/%d/%Y")
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'], format="%H:%M")

boroughs = df['BOROUGH'].unique()
boroughs = sorted(boroughs[1:])

available_years = np.sort(df['CRASH DATE'].dt.year.unique())[:-1]
radio_buttons = ['TOTAL COLLISIONS','NUMBER OF PERSONS INJURED','NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
'NUMBER OF PEDESTRIANS KILLED','NUMBER OF CYCLIST INJURED','NUMBER OF CYCLIST KILLED','NUMBER OF MOTORIST INJURED','NUMBER OF MOTORIST KILLED']

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

# A choropleth map 
def borough_choropleth(): 
    with open ('data/nyu-2451-34490-geojson.json') as f:
        boroughs = json.load(f) 
    bnames = []
    ids = []
    for i in boroughs['features']:
        ids.append(i['id'])
        bnames.append(i['properties']['bname'])

    df_test = df.groupby('BOROUGH').count()
    df_test.reset_index(inplace=True)
    df_test = df_test[['BOROUGH','CRASH DATE']]
    df_test['bname']= pd.DataFrame(bnames,columns=['bnames'])

    labels = dict(zip(ids,bnames))

    df_test['id']= pd.DataFrame(ids,columns=['ids'])
    fig = px.choropleth_mapbox(df_test, geojson=boroughs, locations='id', color='CRASH DATE',
                           color_continuous_scale="Viridis",
                           #range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=9, center = {"lat": 40.730610, "lon": -73.935242},
                           opacity=0.5,
                           labels={'CRASH DATE':'Total Collisions','id':'Borough ID'},
                           hover_name=labels,
                           hover_data = {'id':False}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
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
                            mapbox_style="carto-positron", height=800)
        fig.update_layout(coloraxis_showscale=False)
    else: 
        fig = px.density_mapbox(dff, lat='LATITUDE', lon='LONGITUDE', z=data_type, radius=radius_val,
                            center=dict(lat=40.730610, lon=-73.935242), zoom=10,
                            mapbox_style="carto-positron", height=800)
        fig.update_layout(
            coloraxis_colorbar=dict(
                title="Amount"
            )
        )
    return fig

# We assemble all the parts of the website here
app.layout = dbc.Container(
    [
        dbc.Row([
           dbc.Col([
                html.Div([
                    html.H1('The impact of coronavirus on vehicle collisions in New York City', 
                        style={
                            'color': 'white',
                            'font-weight': 'bold',
                            'font-size': '350%',
                            'text-align': 'center',
                            'margin-top': '400px',
                            })
                    ])
            ]),
        ], style= {
            'background-image': 'url("/assets/ny_traffic_pic.jpg")',
            'background-repeat': 'no-repeat',
            'background-position': 'center',
            'background-size': 'cover',
            'height': '950px',
        }),
        html.Div([
            ### INTRODUCTION ### 
            html.Hr(),
            dcc.Markdown(children=text.intro_markdown),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="borough-choropleth",figure=borough_choropleth())),
                ]
            ),
            dcc.Markdown(children=text.intro_post_choro),
            ### BASIC STATS ###
            html.Hr(), 
            dcc.Markdown(children=text.bs_intro_markdown),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="basic-stat-6",figure=basic_fig.persons_killed_per_collision_figure(df,boroughs)), width=6),
                    dbc.Col(dcc.Graph(id="basic-stat-1",figure=basic_fig.persons_injuried_per_collisions_figure(boroughs)), width=6),
                ],
            ),
            dcc.Markdown(children=text.bs_intro_post_markdown),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="basic-stat-4",figure=basic_fig.cyclist_injured_per_collision_fig(boroughs)), width=4),
                    dbc.Col(dcc.Graph(id="basic-stat-5",figure=basic_fig.pedestrian_injured_per_collision_fig(boroughs)), width=4),
                    dbc.Col(dcc.Graph(id="basic-stat-3",figure=basic_fig.motorist_injured_per_collision_fig(boroughs)), width=4),
                ],
            ),
            #dcc.Markdown(children=text.bs_percentage_post_markdown),
            # dbc.Row(
            #     [
            #         dbc.Col(dcc.Graph(id="basic-stat-3",figure=basic_fig.motorist_injured_per_collision_fig(boroughs)), width=6),
            #     ]
            # ),
            dcc.Markdown(children=text.bs_months_pre_markdown),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="basic-stat-7",figure=basic_fig.month_collisions_fig(df))),
                ]
            ),
            dcc.Markdown(children=text.bs_months_post_markdown),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="basic-stat-8",figure=basic_fig.hour_collisions_fig(df))),
                ]
            ),
            dcc.Markdown(children=text.bs_hours_weekly_markdown),
            ### COVID19 ANALYSIS ### 
            html.Hr(), 
            dcc.Markdown(children=text.cv_pre_markdown),
            ### MACHINE LEARNING ### 
            html.Hr(), 
            dcc.Markdown(children=text.ml_intro_markdown),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="covid19_nyc_cases1",figure=ml_fig.ml_not_merged_fig())),
                ],
                align="center",
            ),
            dcc.Markdown(children=text.ml_markdown_1),
            # dbc.Row(
            #     [
            #         dbc.Col(dcc.Graph(id="covid19_nyc_cases3",figure=ml_fig.covid19_nyc_fig())),
            #     ],
            #     align="center",
            # ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="covid19_nyc_cases2",figure=ml_fig.ml_merged_fig())),
                ],
                align="center",
            ),
            dcc.Markdown(children=text.ml_markdown_2),
            ### INTERACTIVE HEATMAP ### 
            html.Hr(),
            dcc.Markdown(children=text.heatmap_pre_markdown),
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(controls, width=3),
                            dbc.Col(dcc.Graph(id="heatmap-graphic"), width=9),
                        ],
                        align='center'
                    ),
                ], style = {
                    'width': '85vw',
                    'position': 'relative',
                    'left': '52%',
                    'right': '50%',
                    'margin-left': '-42.5vw',
                    'margin-right': '-42.5vw'
                }
            ),
            html.Hr(),
            dcc.Markdown(children=text.heatmap_post_markdown),
        ], style={
            'width':'60%', 
            'margin':'auto'
            }
        )
    ],
    fluid = True
)

end = time.time()
print("launch time: "+str(end-start))
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port='8080')