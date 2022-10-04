import streamlit as st
import pandas as pd
import numpy as np
from assets.sidebar_header import sidebar_image

sidebar_image()

def home(dataframe):
    st.write(dataframe.head())