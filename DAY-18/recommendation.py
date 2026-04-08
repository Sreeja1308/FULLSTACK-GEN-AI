import streamlit as st
import pandas as pd

# Cache the data loading function
@st.cache_data
def load_data():
    return pd.read_csv("movies_with_clusters.csv")

# Load data
df = load_data()

# Title of the app
st.title("📽 Simple Movie Recommendation")

# Search bar
search = st.text_input("Search for a movie title:")

# Show results if search is not empty
if search:
    results = df[df['title'].str.contains(search, case=False, na=False)]
    
    if not results.empty:
        st.write("### Search Results:")
        st.dataframe(results)
    else:
        st.write("No matching movies found.")
        for i, row in results.iterrows():
            st.write(f"-{row['title']}(Rating:{row['rating']})")
    selected=st.selectbox("choose move rec",results['title'])