import plotly.express as px
import pandas as pd

person_killed_per_crash_borough = []
person_injured_per_crash_borough = []

cyclist_injured_per_collision_borough = []
pedestrian_injured_per_collision_borough = []
motorist_injured_per_collision_borough = []


def persons_injuried_per_collisions_figure(bos):
    fig = px.bar(x=bos, y=person_injured_per_crash_borough, title='Persons injured per collision in different boroughs', 
        labels={'x':'Borough', 'y':'Injury per collision','color':''}, color=bos)
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.0,
            xanchor="left",
            x=0,
            font=dict(size=9),
        ), 
        margin=dict(l=0, r=0, t=100, b=100),
    )
    return fig 
    
def persons_killed_per_collision_figure(df,boroughs): 
    fill_maps(df, boroughs) 
    fig = px.bar(x=boroughs, y=person_killed_per_crash_borough, title='Persons killed per collision in different boroughs', 
        labels={'x':'Borough', 'y':'Killed per collision','color':''}, color=boroughs)
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.0,
            xanchor="left",
            x=0,
            font=dict(size=9),
        ), 
        margin=dict(l=0, r=0, t=100, b=100),
    )
    return fig 

def cyclist_injured_per_collision_fig(boroughs): 
    fig = px.bar(x=boroughs, y=cyclist_injured_per_collision_borough, title='Cyclist injured per collision', 
        labels={'x':'', 'y':'Injury per collision','color':''}, color=boroughs)
    fig.update_layout(
        legend=dict(
            # orientation="h",
            # yanchor="bottom",
            # y=1.0,
            # xanchor="left",
            # x=0,
            font=dict(size=7),
        ), 
        margin=dict(l=0, r=0, t=100, b=100),
    )
    return fig 

def motorist_injured_per_collision_fig(boroughs): 
    fig = px.bar(x=boroughs, y=motorist_injured_per_collision_borough, title='Motorists injured per collision', 
        labels={'x':'', 'y':'','color':''}, color=boroughs)
    fig.update_layout(
        legend=dict(
            # orientation="h",
            # yanchor="bottom",
            # y=1.0,
            # xanchor="left",
            # x=0,
            font=dict(size=7),
        ), 
        margin=dict(l=0, r=0, t=100, b=100),
    )
    return fig 

def pedestrian_injured_per_collision_fig(boroughs):
    fig = px.bar(x=boroughs, y=pedestrian_injured_per_collision_borough, title='Pedestrians injured per collision', 
        labels={'x':'Borough', 'y':'','color':''}, color=boroughs)
    fig.update_layout(
        legend=dict(
            # orientation="h",
            # yanchor="bottom",
            # y=1.0,
            # xanchor="left",
            # x=0,
            font=dict(size=7),
        ), 
       margin=dict(l=0, r=0, t=100, b=100),
    )
    return fig 

def month_collisions_fig(df):
    df['Month'] = df['CRASH DATE'].dt.month_name()
    
    collisions_months = df.groupby(df['Month']).size()

    fig = px.bar(collisions_months, title='Collisions per month', labels={'value':'Collisions'}, 
        category_orders={'Month': ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]}, hover_data={'variable':False})

    fig.update_layout(showlegend=False)
    return fig 

def hour_collisions_fig(df):
    df['HourOfTheWeek'] = df['CRASH DATE'].dt.dayofweek * 24 + df['CRASH TIME'].dt.hour

    collisions_hoursoftheweek = df.groupby(df['HourOfTheWeek']).size()

    fig = px.bar(collisions_hoursoftheweek, title='Collisions per hour of the week', 
        labels={'HourOfTheWeek': 'Hours of the week', 'value':'Collisions'}, hover_data={'variable':False})
    fig.update_layout(showlegend=False)
    return fig 

def fill_maps(df, boroughs): 
    if not person_injured_per_crash_borough: ## see if maps already are filledd 
        for b in boroughs: 
            df_borough = df[df['BOROUGH'] == b]

            df_person_killed = df_borough['NUMBER OF PERSONS KILLED'].sum()
            person_killed_borough = df_person_killed/len(df_borough)
            person_killed_per_crash_borough.append(person_killed_borough)

            df_person_injured = df_borough['NUMBER OF PERSONS INJURED'].sum()
            person_injured_borough = df_person_injured/len(df_borough)
            person_injured_per_crash_borough.append(person_injured_borough)
            
            df_borough_cyclists = df_borough['NUMBER OF CYCLIST INJURED'].sum()
            cyclists_injured_borough = df_borough_cyclists/len(df_borough)
            cyclist_injured_per_collision_borough.append(cyclists_injured_borough)

            df_pedestrians_injured = df_borough['NUMBER OF PEDESTRIANS INJURED'].sum()
            pedestrians_injured_borough = df_pedestrians_injured/len(df_borough)
            pedestrian_injured_per_collision_borough.append(pedestrians_injured_borough)

            df_motorist_injured = df_borough['NUMBER OF MOTORIST INJURED'].sum()
            motorist_injured_borough = df_motorist_injured/len(df_borough)
            motorist_injured_per_collision_borough.append(motorist_injured_borough)