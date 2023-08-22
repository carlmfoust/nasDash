import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def positionComparison(dataframe, schedule):
    col1, col2 = st.columns(2)

    dfUnique = dataframe['RaceId'].unique()
    scheduleUnique = schedule[schedule['Race_Id'].isin(dfUnique)].sort_values('Race_Id')

    with col1:
        schedule_value = st.selectbox('Race', scheduleUnique['RaceID_Text'])
        raceID = scheduleUnique.loc[scheduleUnique['RaceID_Text'] == schedule_value, 'Race_Id'].iloc[0]
    
    with col2:
        driver = st.multiselect('Driver Name(s)', dataframe.loc[dataframe.RaceId == raceID]['Name'].unique(), default=dataframe.loc[dataframe.RaceId == raceID]['Name'].unique()[0], key='2')

    dataframeFiltered = dataframe[dataframe['RaceId'] == raceID]

    fig = go.Figure(layout_yaxis_range=[0,40])

    for d in driver:
        fig.add_trace(go.Scatter(x = dataframeFiltered[dataframeFiltered['Name'] == d]['Lap'],
                                 y = dataframeFiltered[dataframeFiltered['Name'] == d]['RunningPos'],
                                 name = d))
    fig.update_layout(height=650)
    st.plotly_chart(fig, use_container_width=True)