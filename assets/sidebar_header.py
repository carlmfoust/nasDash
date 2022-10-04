import streamlit as st
import pandas as pd
import numpy as np
import requests

def sidebar_image():
    drivers_requests = requests.get('https://cf.nascar.com/cacher/drivers.json')
    drivers_json = drivers_requests.json()
    drivers_responce = drivers_json['response']
    drivers_norm = pd.json_normalize(drivers_responce)
    drivers_Cup = drivers_norm[drivers_norm['Driver_Series'] == 'nascar-cup-series']
    drivers_Firesuit = drivers_Cup.loc[drivers_Cup['Firesuit_Image_Small'].str.len() > 0]
    drivers_Firesuit_sub = drivers_Firesuit[['Full_Name', 'Firesuit_Image_Small']]

    randomNumber = np.random.choice(40, replace = True, size = 1)

    link = drivers_Firesuit_sub.iloc[randomNumber]
    print(link['Firesuit_Image_Small'].iloc[0])

    #link = drivers_Firesuit_sub.iloc[5]
    h = link['Firesuit_Image_Small'].iloc[0]

    css = f"""<style>
            [data-testid="stSidebarNav"] {{
                    background-image: url({h});
                    background-repeat: no-repeat;
                    padding-top: 210px;
                    background-position: 20px 20px;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
            }}
            [data-testid="stSidebarNav"]::before {{
                    content: "nasDash";
                    margin-left: 20px;
                    margin-top: 20px;
                    font-size: 40px;
                    position: relative;
                    top: 100px;
                }}
        </style>"""

    st.markdown(
        css,
        unsafe_allow_html=True,
    )