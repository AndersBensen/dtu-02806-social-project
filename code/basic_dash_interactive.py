import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np 
import json 

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Initial dataframe prep
#df = pd.read_csv("../data/Motor_Vehicle_Collisions_-_Crashes.csv",low_memory=False)
df = pd.read_csv("https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accesType=DOWNLOAD", low_memory=False) #download it directly from url, needed when hosting
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])
available_years = np.sort(df['CRASH DATE'].dt.year.unique())[:-1]
radio_buttons = ['TOTAL COLLISIONS','NUMBER OF PERSONS INJURED','NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
'NUMBER OF PEDESTRIANS KILLED','NUMBER OF CYCLIST INJURED','NUMBER OF CYCLIST KILLED','NUMBER OF MOTORIST INJURED','NUMBER OF MOTORIST KILLED']

# Markdown text
markdown_text = '''
&nbsp;
&nbsp;
&nbsp;
### Dash and Markdown
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non mollis dolor. Fusce ultricies maximus velit, id laoreet ex condimentum eu. Suspendisse fermentum magna id placerat ultrices. Mauris viverra, diam in volutpat ullamcorper, eros arcu vestibulum purus, ornare tempus urna purus eu dui. Proin a diam dolor. Proin sagittis molestie felis, et imperdiet nisl. Mauris posuere velit nulla. Phasellus rutrum tortor nec erat pellentesque dapibus. Pellentesque massa eros, ornare a turpis vel, gravida ultrices dui. Nulla posuere aliquet lorem nec tincidunt. Suspendisse rhoncus fermentum sem. Vivamus feugiat neque ut magna tincidunt, a dapibus metus porta. Integer ac neque vitae felis ultrices efficitur sed in quam.

Vestibulum aliquet porttitor metus, eget eleifend nulla laoreet a. Curabitur semper ipsum turpis, eu finibus ipsum faucibus vel. Fusce vel velit urna. Aliquam sodales rhoncus erat eu tempus. Proin blandit sapien vitae ipsum placerat suscipit. Vivamus semper aliquam laoreet. Nam bibendum tristique sem, eget porttitor turpis dictum sit amet. Aliquam congue tortor leo, et elementum enim accumsan et. Fusce in enim quis sem lacinia convallis. Fusce viverra ex nec odio auctor elementum. Suspendisse quis gravida nunc, et pretium dolor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus vel blandit erat, vel varius risus. Donec quam nisi, facilisis ac purus quis, consequat aliquet nunc.
&nbsp;
'''

markdown_text2 = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non mollis dolor. Fusce ultricies maximus velit, id laoreet ex condimentum eu. Suspendisse fermentum magna id placerat ultrices. Mauris viverra, diam in volutpat ullamcorper, eros arcu vestibulum purus, ornare tempus urna purus eu dui. Proin a diam dolor. Proin sagittis molestie felis, et imperdiet nisl. Mauris posuere velit nulla. Phasellus rutrum tortor nec erat pellentesque dapibus. Pellentesque massa eros, ornare a turpis vel, gravida ultrices dui. Nulla posuere aliquet lorem nec tincidunt. Suspendisse rhoncus fermentum sem. Vivamus feugiat neque ut magna tincidunt, a dapibus metus porta. Integer ac neque vitae felis ultrices efficitur sed in quam.

Vestibulum aliquet porttitor metus, eget eleifend nulla laoreet a. Curabitur semper ipsum turpis, eu finibus ipsum faucibus vel. Fusce vel velit urna. Aliquam sodales rhoncus erat eu tempus. Proin blandit sapien vitae ipsum placerat suscipit. Vivamus semper aliquam laoreet. Nam bibendum tristique sem, eget porttitor turpis dictum sit amet. Aliquam congue tortor leo, et elementum enim accumsan et. Fusce in enim quis sem lacinia convallis. Fusce viverra ex nec odio auctor elementum. Suspendisse quis gravida nunc, et pretium dolor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus vel blandit erat, vel varius risus. Donec quam nisi, facilisis ac purus quis, consequat aliquet nunc.
&nbsp;
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

# A choropleth map 
def borough_choropleth(): 
    with open ('../data/nyu-2451-34490-geojson.json') as f:
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
            #html.H1("Blabla header"),
            dcc.Markdown(children=markdown_text),  
            html.Hr(), 
            dcc.Markdown(children=markdown_text),  
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="borough-choropleth",figure=borough_choropleth())),
                ]
            ),
            dcc.Markdown(children=markdown_text2),
            #html.H1("Blabla header"),
            html.Hr(), 
            dcc.Markdown(children=markdown_text),  
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id="borough-collisions",figure=bar_borough_collisions())),
                ]
            ),
            dcc.Markdown(children=markdown_text2),
            #html.H1("Blabla header"), 
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(dcc.Markdown(children=markdown_text), width=6),
                    dbc.Col(dcc.Graph(id="borough-collisions2",figure=bar_borough_collisions()), width=6),
                ],
                align="center",
            ),
            #html.H1("Blabla header"), 
            html.Hr(),
            dcc.Markdown(children=markdown_text),
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
            dcc.Markdown(children=markdown_text2),
        ], style={
            'width':'60%', 
            'margin':'auto'
            }
        )
    ],
    fluid = True,
    # style = {
    #     'background-image': 'url(https://upload.wikimedia.org/wikipedia/commons/2/22/North_Star_-_invitation_background.png)'
    #     'backgroundColor': '#111111'
    #     },
)

if __name__ == '__main__':
    app.run_server(debug=False)