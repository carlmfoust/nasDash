import streamlit as st
import pandas as pd
import numpy as np
from assets.sidebar_header import sidebar_image
from assets.lap_comparison import lapComparison
from assets.position_comparison import positionComparison
from assets.manu_laps_graph import manuLapGraph

st.set_page_config(page_title='Lap',layout="wide")
sidebar_image()

st.title('Manufacture Laps Lead')
st.markdown('Loop data from the 2022 Nascar Cup season.')
csv = pd.read_csv('Data/2023_Nascar_Lap_Perc.csv')
schedule_csv = pd.read_csv('Data/2023   _Nascar_Schedule.csv')
manuLapGraph(csv, schedule_csv)