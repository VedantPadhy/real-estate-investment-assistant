import joblib
import streamlit as st
import pandas as pd
# ---------- Load Model ----------
@st.cache_resource
def load_model():
    with open("real_estate_price_model.pkl", "rb") as f:
        return joblib.load(f)

pipe = load_model()
st.set_page_config(page_title="Mumbai Real Estate Analyzer", layout="wide")

# ---------- Load Data for dropdowns ----------
@st.cache_data
def load_reference_data():
    df = pd.read_csv("mumbai_properties.csv")
    return df

ref_df = load_reference_data()

numerical_features = ['area','bedroom_num','bathroom_num','balcony_num',
                      'age','total_floors','latitude','longitude']

categorical_features = ['city','locality','property_type','furnished']


# ---------- UI ----------
st.title("🏙️ Mumbai Real Estate Investment Analyzer")
st.write("Find fair price and best investment opportunities")

# --- Sidebar Inputs ---
st.sidebar.header("Enter Property Details")

city = st.sidebar.selectbox("City", sorted(ref_df["city"].unique()))

locality = st.sidebar.selectbox(
    "Locality",
    sorted(ref_df[ref_df["city"]==city]["locality"].unique())
)

property_type = st.sidebar.selectbox("Property Type",
                                      sorted(ref_df["property_type"].unique()))

furnished = st.sidebar.selectbox("Furnishing", 
                                 sorted(ref_df["furnished"].unique()))

area = st.sidebar.number_input("Area (sqft)", 200, 10000, 800)
bedroom = st.sidebar.number_input("Bedrooms", 1, 10, 2)
bathroom = st.sidebar.number_input("Bathrooms", 1, 10, 2)
balcony = st.sidebar.number_input("Balconies", 0, 5, 0)
age = st.sidebar.number_input("Property Age (years)", 0, 50, 5)
total_floors = st.sidebar.number_input("Total Floors", 1, 50, 1)

# Auto-fill lat/long from reference data
loc_row = ref_df[(ref_df["city"]==city) & (ref_df["locality"]==locality)].iloc[0]
latitude = loc_row["latitude"]
longitude = loc_row["longitude"]

st.sidebar.write("Latitude:", latitude)
st.sidebar.write("Longitude:", longitude)

# Asking listed price
listed_price_per_sqft = st.sidebar.number_input(
    "Listed Price per Sqft",
    min_value=2000,
    max_value=150000,
    value=8000,
    step=500
)


# ---------- Prediction ----------
if st.sidebar.button("Analyze Deal"):

    input_dict = {
        "area": area,
        "bedroom_num": bedroom,
        "bathroom_num": bathroom,
        "balcony_num": balcony,
        "age": age,
        "total_floors": total_floors,
        "latitude": latitude,
        "longitude": longitude,
        "city": city,
        "locality": locality,
        "property_type": property_type,
        "furnished": furnished
    }

    input_df = pd.DataFrame([input_dict])

    fair_price = pipe.predict(input_df)[0]

    discount = ((fair_price - listed_price_per_sqft) / fair_price) * 100
    investment_score = discount - (age * 0.3)

    # ---------- Results ----------
    st.subheader("📊 Analysis Result")

    col1, col2, col3 = st.columns(3)
    col1.metric("Fair Price / Sqft", f"₹ {fair_price:,.0f}")
    col2.metric("Discount %", f"{discount:.2f}%")
    col3.metric("Investment Score", f"{investment_score:.2f}")

    # Verdict
    if investment_score > 10:
        st.success("🔥 Strong Investment Opportunity")
    elif investment_score > 0:
        st.info("🙂 Fair Deal")
    else:
        st.error("⚠️ Overpriced Property")
st.markdown("---")
st.markdown(
    "<center>Built with tradition in data, vision in future. — Vedant Padhy </center>",
    unsafe_allow_html=True
)


