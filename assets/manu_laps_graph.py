import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def manuLapGraph(dataframe, schedule):

    #driver = raceLapsCat.groupby(['Name', 'RaceID'])['RunningPos'].apply(lambda x: (x==1).sum()).reset_index(name='count')
    manufacturer = dataframe.replace('frd', 'Frd')

    exhibation = [5143, 5144, 5145, 5159, 5160]

    manufacturer = manufacturer[~manufacturer.RaceID.isin(exhibation)]
    
    manufacturer = manufacturer.groupby(['Manufacturer', 'RaceID'])['RunningPos'].apply(lambda x: (x==1).sum()).reset_index(name='count')

    manufacturer['roll'] = manufacturer.groupby('Manufacturer')['count'].cumsum()

    schedule = schedule.rename(columns={'Race_Id': 'RaceID'})
    scheduleID = schedule[['RaceID', 'RaceID_Text']]
    
    print(scheduleID)

    manufacturer = manufacturer.merge(scheduleID,'inner','RaceID')
    
    fig = px.line(manufacturer, x="RaceID", y="roll", color='Manufacturer', hover_data={'RaceID_Text': False})
    fig.update_layout(hovermode="x unified", xaxis = dict(tickmode = 'array', tickvals = ['5146', '5183'], ticktext = ['First', 'Last']))

    st.plotly_chart(fig, use_container_width=True)