# ##########################################
# Upload excel file ########################
# ##########################################

# Required lib
# env

from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm

import pandas as pd

import streamlit as st

import openpyxl

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Data Analytics",
    layout="wide",page_icon="📊"
)

# streamlit markdown element

st.markdown("""
    <style>


            .viewerBadge_link__qRIco
            {
                visibility:hidden;
            }

            .p-1.5 opacity-70 hover:opacity-100
            {
                visibility:hidden;
            }
            
            .st-emotion-cache-zq5wmm.ezrtsby0
            {
                visibility:hidden;
            }
            
           .stActionButtonLabel
            {
               visibility:hidden;
            }
        
           .viewerBadge_container__r5tak styles_viewerBadge__CvC9N
            {
                 visibility:hidden;
            }
            
           .viewerBadge_text.fzr3E
            {
                visibility:hidden;
            }
        
           .viewerBadge_text__fzr3E
            {
                 visibility:hidden;
            }   
            
          .viewerBadge_link__qRIco
            {
                visibility:hidden;
            }
            
          .p-1.5.opacity-70
            {
                visibility:hidden;
            }

          .sc-ewnqHT.vufNk
            {
                visibility:hidden;
            }

           img 
            {
                visibility:hidden;
            }
            
           .p-1\.5
            {
                visibility:hidden;
            }

           #kanaries-logo
            {
                visibility:hidden;
            }

    </style>
    
""", unsafe_allow_html=True)

# Establish communication between pygwalker and streamlit
init_streamlit_comm()

# Add a title
st.title("Data Analytics")
# @st.cache_data
# data_file = st

# @st.cache
data_file = st.file_uploader("Upload Excel file :file_folder:",type='.xlsx',accept_multiple_files=False)

# @st.cache_data
# Get an instance of pygwalker's renderer. You should cache this instance to effectively prevent the growth of in-process memory.
if data_file:
    # @st.cache_resource
    def get_pyg_renderer() -> "StreamlitRenderer":
        df = pd.read_excel(data_file,
                        engine='openpyxl',
                        header=0,
                        index_col=0
                        )
        # df["Value"] = round(df["Value"],0)
        # df["Quantity"] = round(df["Quantity"],0)

        # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
        return StreamlitRenderer(df, spec="./gw_config.json", debug=False)

    renderer = get_pyg_renderer()

    # Render your data exploration interface. Developers can use it to build charts by drag and drop.
    renderer.render_explore()
