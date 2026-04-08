import streamlit as st
import pandas as pd
import google.generativeai as genai

genai.configure(api_key="AIzaSyCHLQebOP_v_Z1iFp7iVNfrpVW0GmECOoo")
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_roadmap(TechStack, Year, Speed_level, Goal, Duration):
    prompt = f"""
    Generate a **Day-wise roadmap** to learn {TechStack} for {Year} year engineering students 
    with {Speed_level} learning speed to achieve the goal: {Goal}. 
    Include LeetCode problem links, reference YouTube videos, and websites 
    to complete in {Duration} days.
    Format:
    Day | Topic | LeetCode Link | Questions | YouTube Link
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="RoadMap Generator")
st.title("AI RoadMap Generator")

TechStack = st.selectbox("Select the subject to learn:", ["Python", "Java", "C", "C++"])
Year = st.selectbox("Select your year:", ["1st", "2nd", "3rd", "4th"])
Speed_level = st.selectbox("Select learning speed:", ["Fast", "Moderate", "Slow"])
Goal = st.selectbox("Select your goal:", [
    "Software Developer", "To master a Programming Language", 
    "Data Scientist", "Master the AI", 
    "To crack the programming tests", "To place in an MNC company"
])
Duration = st.number_input("Enter duration (days):", min_value=1, max_value=365)

if st.button("Generate RoadMap"):
    with st.spinner("Working on your RoadMap..."):
        roadmap_text = generate_roadmap(TechStack, Year, Speed_level, Goal, Duration)
        roadmap_data = []

        for line in roadmap_text.strip().split("\n"):
            if "|" in line and "Day" not in line:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 5:
                    day, topic, leetcode, questions, yt_link = parts[:5]
                    # Convert to Markdown clickable links
                    leetcode = f"[LeetCode]({leetcode})" if "http" in leetcode else ""
                    yt_link = f"[Watch]({yt_link})" if "http" in yt_link else ""
                    roadmap_data.append([day, topic, leetcode, questions, yt_link])

        if roadmap_data:
            st.subheader("Your AI-Generated RoadMap")
            st.markdown(f"**Goal**: {Goal}  \n**Speed**: {Speed_level}  \n**Duration**: {Duration} days")
            df = pd.DataFrame(roadmap_data, columns=["Day", "Topic", "LeetCode", "Questions", "YouTube"])
            st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)
        else:
            st.error("No roadmap data was generated. Try adjusting your inputs.")
