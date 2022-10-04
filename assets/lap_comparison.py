import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def lapComparison(dataframe):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        raceID = st.selectbox('Race', dataframe['RaceID'].unique())
    
    with col2:
        #.isnull().all()
        driver = st.multiselect('Driver Name(s)', options=dataframe.loc[dataframe.RaceID == raceID]['Name'].unique(), default=dataframe.loc[dataframe.RaceID == raceID]['Name'].unique()[0])
    
    with col3:
        options = ['5LapAverage', '10LapAverage', '25LapAverage', '50LapAverage']
        optionsRefined = []
        for d in driver:
            driverDF = dataframe[(dataframe['Name'] == d) & (dataframe['RaceID'] == raceID)]
            for eachOption in options:
                if not driverDF[eachOption].isnull().all():
                    optionsRefined.append(eachOption)
        
        uniq = []
        for x in optionsRefined:
            if x not in uniq:
                uniq.append(x)
        yAxisVal = st.selectbox('Lap Average #', uniq)

    with col4:
        driversRun = []
        for d in driver:
            for i in dataframe.loc[dataframe.RaceID == raceID]['Run'].unique():
                h = dataframe[dataframe['RaceID'] == raceID]
                f = h[h['Run'] == i]
                f = f[f['Name'] == d]
                if not f[yAxisVal].isnull().all():
                    driversRun.append(i)

        uniq = []
        for x in driversRun:
            if x not in uniq:
                uniq.append(x)
        run = st.selectbox('Run #', uniq)

    dataframeFiltered = dataframe[(dataframe['RaceID'] == raceID) & (dataframe['Run'] == run)]

    fig = go.Figure()

    for d in driver:
        fig.add_trace(go.Scatter(x = dataframeFiltered[dataframeFiltered['Name'] == d]['Lap'],
                                 y = dataframeFiltered[dataframeFiltered['Name'] == d][yAxisVal],
                                 name = d))
    st.plotly_chart(fig, use_container_width=True)