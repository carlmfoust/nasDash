import streamlit as st
import pandas as pd
import numpy as np
from assets.sidebar_header import sidebar_image
from assets.lap_comparison import lapComparison
from assets.position_comparison import positionComparison

st.set_page_config(page_title='Lap',layout="wide")
sidebar_image()

st.title('Driver Comparison Tool')
st.markdown('Loop data from the 2022 Nascar Cup season.')

csv = pd.read_csv('Data/2022_Nascar_Lap_Perc.csv')
schedule_csv = pd.read_csv('Data/2022_Nascar_Schedule.csv')

tab1, tab2 = st.tabs(['Lap Average', 'Position'])

with tab1:
    lapComparison(csv, schedule_csv)
with tab2:
    positionComparison(csv, schedule_csv)