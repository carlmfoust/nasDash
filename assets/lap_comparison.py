import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def lapComparison(dataframe, schedule):
    race, driver, lapType, runNum = st.columns(4)

    dfUnique = dataframe['RaceId'].unique()
    scheduleUnique = schedule[schedule['Race_Id'].isin(dfUnique)].sort_values('Race_Id')

    with race:
        #raceID = st.selectbox('Race', dataframe['RaceID'].unique())
        schedule_value = st.selectbox('Race', scheduleUnique['RaceID_Text'], key='lap')
        raceID = scheduleUnique.loc[scheduleUnique['RaceID_Text'] == schedule_value, 'Race_Id'].iloc[0]
    
    with driver:
        #.isnull().all()
        driver = st.multiselect('Driver Name(s)', options=dataframe.loc[dataframe.RaceId == raceID]['Name'].unique(), default=dataframe.loc[dataframe.RaceId == raceID]['Name'].unique()[0])
    
    with lapType:
        options = ['5LapAverage', '10LapAverage', '25LapAverage', '50LapAverage']
        optionsRefined = []
        for d in driver:
            driverDF = dataframe[(dataframe['Name'] == d) & (dataframe['RaceId'] == raceID)]
            for eachOption in options:
                if not driverDF[eachOption].isnull().all():
                    optionsRefined.append(eachOption)
        
        uniq = []
        for x in optionsRefined:
            if x not in uniq:
                uniq.append(x)
        yAxisVal = st.selectbox('Lap Average #', uniq)

    with runNum:
        driversRun = []
        for d in driver:
            for i in dataframe.loc[dataframe.RaceId == raceID]['Run'].unique():
                h = dataframe[dataframe['RaceId'] == raceID]
                f = h[h['Run'] == i]
                f = f[f['Name'] == d]
                if not f[yAxisVal].isnull().all():
                    driversRun.append(i)

        uniq = []
        for x in driversRun:
            if x not in uniq:
                uniq.append(x)
        run = st.selectbox('Run #', uniq)

    dataframeFiltered = dataframe[(dataframe['RaceId'] == raceID) & (dataframe['Run'] == run)]

    fig = go.Figure()

    for d in driver:
        fig.add_trace(go.Scatter(x = dataframeFiltered[dataframeFiltered['Name'] == d]['Lap'],
                                 y = dataframeFiltered[dataframeFiltered['Name'] == d][yAxisVal],
                                 name = d))

    plotTitle = f'Driver Comparison for {schedule_value}<br><sup>Run #{run}</sup>'    
    
    fig.update_layout(xaxis_title="Race Laps", yaxis_title="Lap Time (Seconds)", title = plotTitle)    
    
    st.plotly_chart(fig, use_container_width=True)