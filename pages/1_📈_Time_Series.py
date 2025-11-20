import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf

st.set_page_config(page_title="Time Series", page_icon="📈")

st.sidebar.header("Time Series Plots")

st.title('Time Series Plots')

DATA_PATH = ('cases_month.csv')

# cached data load
@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    return data

with st.spinner('Loading data...'):
    data = load_data()

st.sidebar.success("✅ Data Loaded.")

# Add date column
data["date"] = pd.to_datetime(data[["year", "month"]].assign(DAY=1))
# Add region_name column
region_mapping = {
    "AFR": "African Region",
    "AMR": "American Region",
    "SEAR": "South-East Asian Region",
    "EUR": "European Region",
    "EMR": "East Mediterranean Region",
    "WPR": "West Pacific Region"
}
data["region_name"] = data["region"].map(region_mapping)




# Selected by user
target_column = "measles_total" 
# "measles_suspect", "measles_clinical"， "measles_epi_linked", "measles_lab_confirmed"

filtered = data[["date", "region_name", target_column]]

df_indexed_summed = filtered.groupby(['date', 'region_name']).sum().sort_index()

df_plot = df_indexed_summed[target_column].unstack(level='region_name')

fig, ax = plt.subplots(figsize=(10, 6))

df_plot.plot(
    ax=ax,
    title=f'{target_column} Over Time by Region',
    x_compat=True 
)

locator = mdates.YearLocator()
ax.xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter('%Y')
ax.xaxis.set_major_formatter(formatter)

fig.autofmt_xdate()

ax.set_ylabel('Cases Count')
ax.legend(title='Region')
fig.tight_layout()

st.subheader(f"📈 {target_column} Time Series Plot")
st.pyplot(fig)