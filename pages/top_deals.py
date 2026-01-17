import streamlit as st
import pandas as pd

st.title("Top Property Investment Deals")

@st.cache_data
def load_data():
    return pd.read_csv("mumbai_properties.csv")

data = load_data()

top_deals = data.sort_values("investment_score", ascending=False).head(20)
csv = top_deals.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download in CSV",
    icon="💾",
    data=csv,
    file_name="top_property_deals.csv",
    mime="text/csv"
)


st.dataframe(top_deals)
st.markdown("---")
st.markdown(
    "<center>Built with tradition in data, vision in future. — Vedant Padhy</center>",
    unsafe_allow_html=True
)
