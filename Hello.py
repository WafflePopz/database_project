import streamlit as st

# INSTALL "requirements.txt" FIRST
# pip install -r requirements.txt

# TEST APP
# use "streamlit run Hello.py" in terminal to run

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# WHO Measles Cases Data")

st.sidebar.success("Select a tab above.")

st.markdown(
    """
    This data was downloaded from the World Health Organisation 
    [Provisional monthly measles and rubella data](https://immunizationdata.who.int/global?topic=Provisional-measles-and-rubella-data&location=)
     on 2025-06-12.
    
    Both measles and rubella cases are tracked at the same time by WHO.

    The data was cleaned and posted on **TidyTuesday**, a 
    [weekly social data project](https://github.com/rfordatascience/tidytuesday/tree/main). 

    Select a tab from the sidebar to explore the data with different visualization tools.
"""
)