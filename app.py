
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="ProductMatch AI",
    page_icon="🛍️",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
PRODUCT_FILE = BASE_DIR / "products.csv"

st.title("🛍️ ProductMatch AI")
st.subheader("AI-driven Electronics Product Recommendation System")
st.write(
    "Find electronics that match your needs, preferences, and budget."
)

@st.cache_data
def load_products():
    return pd.read_csv(PRODUCT_FILE)

try:
    products = load_products()

    st.success("Application started successfully!")

    st.metric("Products in catalogue", len(products))

    categories = sorted(products["category"].dropna().unique())
    selected_category = st.selectbox(
        "Choose a product category",
        ["All categories"] + categories,
    )

    budget = st.number_input(
        "Maximum budget (₹)",
        min_value=0,
        value=65000,
        step=1000,
    )

    results = products[products["price_inr"] <= budget]

    if selected_category != "All categories":
        results = results[
            results["category"] == selected_category
        ]

    st.subheader("Available products")
    st.dataframe(
        results[
            ["name", "category", "brand", "price_inr", "rating"]
        ],
        use_container_width=True,
        hide_index=True,
    )

except Exception as exc:
    st.error(f"Unable to load the product catalogue: {exc}")
    st.info("Check that products.csv exists and has the expected columns.")
