import streamlit as st
import pandas as pd
import numpy as np
from assets.sidebar_header import sidebar_image

## To run, use: py -m streamlit run app.py

st.set_page_config(page_title='Lap',layout="wide")

sidebar_image()

st.title('nasDash')
st.markdown('Loop data from the 2023 Nascar Cup season.')

# csv = pd.read_csv('Data/2023_Nascar_Lap_Perc.csv')
# schedule_csv = pd.read_csv('Data/2023_Nascar_Schedule.csv')
# del csv[csv.columns[0]]