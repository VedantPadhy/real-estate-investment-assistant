# Mumbai Real Estate Investment Assistant

A smart data-driven web app that predicts **fair property prices** and identifies **best real estate investment opportunities** in Mumbai.

Built with machine learning, wrapped in Streamlit, guided by data — grounded in tradition, looking forward.

---

## Features

- Predicts **Fair Price per Sqft** using trained ML model  
- Calculates **Discount Percentage** vs listed price  
- Generates an **Investment Score** adjusted for property age  
- Interactive **Streamlit UI** for custom property analysis  
- **Top Deals Page** showing best investment opportunities  

---

## Tech Stack

- Python  
- Pandas, Scikit-learn  
- Streamlit  
- Pickle (ML model storage)  
- Git + Git LFS  

---

## How It Works

1. User enters property details  
2. Model predicts fair price per sqft  
3. App computes:
Discount % = (Fair Price - Listed Price) / Fair Price * 100
Investment Score = Discount % - (Age * 0.3)

4. Output classified as:
- Excellent Deal  
- Fair Deal  
- Overpriced  

📂 Project Structure
Data/
│
├── app.py                 # Main Streamlit app
├── pages/
│   └── top_deals.py       # Top investment deals page
├── mumbai_properties.csv  # Dataset
├── real_estate_model.pkl  # Fair price ML model
├── real_estate_price_model.pkl
├── requirements.txt
Note
Model files are large and tracked using Git LFS.
## 🔧 Model File Setup

This project uses a trained ML model (~700MB).  
Due to GitHub file size limits, the model is hosted separately.

📥 Download model from:
https://drive.google.com/file/d/1oOlkmJtbBDB5Gy6RRhre8CvNdli8svdn/view?usp=sharing
After downloading, place the file in the project root:

Data/
 ├── app.py
 ├── pages/
 ├── real_estate_model.pkl  <-- place here
 └── requirements.txt

Then run:
streamlit run app.py
Vision
This project helps home buyers and investors
see beyond listed prices —
finding value hidden in the city’s concrete rhythm.

Built with tradition in data, vision in future.

— Vedant Padhy
