import plotly.express as px
import pandas as pd

def covid19_nyc_fig(): 
    df_covid = pd.read_csv("data/NYC_covid19_filtered_file.csv")
    df_covid['DATE_OF_INTEREST'] = pd.to_datetime(df_covid['DATE_OF_INTEREST'])
    fig = px.line(x=df_covid['DATE_OF_INTEREST'], y=df_covid['CASE_COUNT'],labels={'x': 'Dates', 'y': 'Amount of COVID19 cases'}, 
        title="Confirmed COVID19 cases in NYC plotted versus dates in 2020")
    return fig

def ml_not_merged_fig(): 
    df_nmerged = pd.read_csv("data/ml_data_not_merged.csv")
    fig = px.scatter(data_frame=df_nmerged, x='Date', y=['Collisions','Predicted collisions'], labels={'x': 'Collision dates', 'value': 'Amount of collisions'},
        title="Actual and predicted amount of vehicle collisions plotted versus dates. RMSE of: " + 
        str(40.5))

    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    return fig

def ml_merged_fig(): 
    df_merged = pd.read_csv("data/ml_data_merged.csv")
    fig = px.scatter(data_frame=df_merged, x='Date', y=['Collisions','Predicted collisions'], labels={'x': 'Collision dates', 'value': 'Amount of collisions'},
        title="Actual and predicted amount of vehicle collisions plotted versus dates, merged dataset. RMSE of: " + 
        str(34.95))

    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    return fig 