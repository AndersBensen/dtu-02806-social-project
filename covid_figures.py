import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df_dates = pd.DataFrame()
df_covid_data = None 
df_covid = None 
df_normal = None 

collisions_borough_covid = None

collisions_borough_normal = None


def initialize_values(df): 
    global df_dates 
    global df_covid_data
    global df_covid 
    global df_normal
    global collisions_borough_covid
    global collisions_borough_normal  

    df_dates['Crash count per day'] = df['CRASH DATE'].value_counts()
    df_dates['Injured persons per day'] = df.groupby('CRASH DATE').sum().loc[:,'NUMBER OF PERSONS INJURED']
    df_dates['Killed persons per day'] = df.groupby('CRASH DATE').sum().loc[:,'NUMBER OF PERSONS KILLED']
    df_dates.index.name="Date"
    df_dates = df_dates.reset_index()
    df_dates['Year'] = df_dates['Date'].dt.year

    df_covid_data = pd.read_csv("data/NYC_covid19_filtered_file.csv")
    df_covid_data['DATE_OF_INTEREST'] = pd.to_datetime(df_covid_data['DATE_OF_INTEREST'])

    df_covid = df[df['CRASH DATE'] >= '03/1/2020']
    df_normal = df[df['CRASH DATE'] < '03/1/2020']  

    collisions_borough_covid = df_covid['BOROUGH'].value_counts()
    collisions_borough_normal = df_normal['BOROUGH'].value_counts()

def covid19_nyc_fig(df): 
    if (df_covid_data == None): 
        initialize_values(df)

    fig = px.line(x=df_covid_data['DATE_OF_INTEREST'], y=df_covid_data['CASE_COUNT'],labels={'x': 'Dates', 'y': 'Amount of COVID19 cases'}, 
        title="Confirmed COVID19 cases in NYC plotted versus dates in 2020")
    return fig

def covid19_time_incidents_fig(df): 
    # input df_dates
    fig = px.scatter(df_dates, x="Date", y=["Crash count per day","Injured persons per day"],
        title='Change in Number of Incidents over Time' ,range_x=['2012-07-01','2021-03-26'], range_y=[0,1200]
        ,labels={'variable':''})
    fig.update_layout(yaxis_title='Count per Day', legend=dict(orientation="h",yanchor="bottom",y=1.0,xanchor="left",x=0), )

    fig.add_vline(x='2020-03-01')
    fig.add_annotation(x='2020-03-01', y=1000,text="1st of March of 2020                                  ", showarrow=True,align='left', font=dict(size=16),valign="bottom")
    fig.add_annotation(x='2020-03-01', y=1200,text="""First confirmed COVID-19 case in NYC""",showarrow=True,yshift=1,font=dict(size=16))
    fig.add_annotation(x='2016-03-01', y=1100,text="""No COVID""",showarrow=False,yshift=1,font=dict(size=16))
    fig.add_annotation(x='2020-10-01', y=1100,text="""COVID""",showarrow=False,yshift=1,font=dict(size=16))
            
    fig.add_vrect(x0='2020-03-01', x1='2021-11-01', line_width=0, fillcolor="red", opacity=0.2)        
    fig.add_vrect(x0='2012-01-01', x1='2020-03-01', line_width=0, fillcolor="green", opacity=0.2)        
    return fig 


def covid_19_incidents_cases_fig(df): 
    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    # create two independent figures with px.line each containing data from multiple columns
    fig = px.scatter(df_dates[df_dates['Year']>2019], x='Date', y=['Crash count per day', 'Injured persons per day',],range_y=[0,100])
    fig2 = px.line(df_covid_data,x='DATE_OF_INTEREST' ,y=['CASE_COUNT'])


    fig2.update_traces(yaxis="y2")
    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title="Date"
    subfig.layout.title= 'Change in Incidents over Time and Daily Corona Cases'
    subfig.layout.yaxis.title="Count per Day"
    subfig.layout.yaxis2.title="New daily COVID Cases"
    subfig.update_xaxes(range=['2020-02-01', '2021-01-01'], row=1, col=1)
    subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    subfig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.0,xanchor="left",x=0))
    return subfig


def covid_19_killed_pr_col_fig(df, boroughs): 
    persons_killed_borough_covid = df_covid.groupby(df_covid['BOROUGH'])['NUMBER OF PERSONS KILLED'].sum()
    persons_killed_per_collisions_borough_covid = persons_killed_borough_covid/collisions_borough_covid
    persons_killed_borough_normal = df_normal.groupby(df_normal['BOROUGH'])['NUMBER OF PERSONS KILLED'].sum()
    persons_killed_per_collisions_borough_normal = persons_killed_borough_normal/collisions_borough_normal

    fig = go.Figure(data=[
        go.Bar(name='No COVID', x=boroughs, y=persons_killed_per_collisions_borough_normal),
        go.Bar(name='COVID', x=boroughs, y=persons_killed_per_collisions_borough_covid)
    ])
    fig.update_layout(title='Persons killed per collision',barmode='group', 
        legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1),
        margin=dict(l=0, r=0, t=100, b=100),
    )
    return fig 

def covid_19_injured_pr_col_fig(df, boroughs): 
    persons_injured_borough_covid = df_covid.groupby(df_covid['BOROUGH'])['NUMBER OF PERSONS INJURED'].sum()
    persons_injured_per_collisions_borough_covid = persons_injured_borough_covid/collisions_borough_covid
    persons_injured_borough_normal = df_normal.groupby(df_normal['BOROUGH'])['NUMBER OF PERSONS INJURED'].sum()
    persons_injured_per_collisions_borough_normal = persons_injured_borough_normal/collisions_borough_normal

    fig = go.Figure(data=[
        go.Bar(name='No COVID', x=boroughs, y=persons_injured_per_collisions_borough_normal),
        go.Bar(name='COVID', x=boroughs, y=persons_injured_per_collisions_borough_covid)
    ])
    fig.update_layout(title='Persons injured per collision',barmode='group', 
        legend=dict( orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1),
        margin=dict(l=0, r=0, t=100, b=100),
        )
    return fig 


def covid_19_crashes_factors_fig(df): 
    crash_count_normal = df_normal['CRASH DATE'].value_counts().sum()
    crash_count_covid = df_covid['CRASH DATE'].value_counts().sum()

    factor_1_n = df_normal.groupby('CONTRIBUTING FACTOR VEHICLE 1').count().sort_values(by='CRASH DATE').iloc[:,0]
    factor_1_c = df_covid.groupby('CONTRIBUTING FACTOR VEHICLE 1').count().sort_values(by='CRASH DATE').iloc[:,0]

    factor_1_c = factor_1_c.sort_values()
    factor_1_n = factor_1_n.reindex(factor_1_c.index)
    n= 18
    fig = go.Figure(data=[
        go.Bar(name='No COVID', x=factor_1_n.index[-n:-1], y=factor_1_n.values[-n:-1]/crash_count_normal*100),
        go.Bar(name='COVID', x=factor_1_c.index[-n:-1], y=factor_1_c.values[-n:-1]/crash_count_covid*100)
    ])
    # Change the bar mode
    fig.update_layout(title='Factors for Crashes',yaxis_title='Percent of Total Number of Crashes' ,barmode='group',
        legend=dict( orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1), margin=dict(l=0, r=0, t=100, b=100),
    )
    return fig 
