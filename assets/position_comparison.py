import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def positionComparison(dataframe):
    col1, col2 = st.columns(2)

    with col1:
        raceID = st.selectbox('Race', dataframe['RaceID'].unique(), key="1")
    
    with col2:
        driver = st.multiselect('Driver Name(s)', dataframe.loc[dataframe.RaceID == raceID]['Name'].unique(), default=dataframe.loc[dataframe.RaceID == raceID]['Name'].unique()[0], key='2')

    dataframeFiltered = dataframe[dataframe['RaceID'] == raceID]

    fig = go.Figure(layout_yaxis_range=[0,40])

    for d in driver:
        fig.add_trace(go.Scatter(x = dataframeFiltered[dataframeFiltered['Name'] == d]['Lap'],
                                 y = dataframeFiltered[dataframeFiltered['Name'] == d]['RunningPos'],
                                 name = d))
    fig.update_layout(height=650)
    st.plotly_chart(fig, use_container_width=True)