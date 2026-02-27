import streamlit as st
import google.generativeai as genai

# 1. PASTE YOUR KEY (from your earlier screenshot) between the quotes below
genai.configure(api_key="PASTE_YOUR_ACTUAL_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Viral Script Gen", page_icon="🎬")
st.title("🚀 Viral Short-Form Script Gen")
st.write("Built by a 14-year-old Developer")

# Sidebar for monetization (Set this up later!)
with st.sidebar:
    st.write("💰 **Support the Creator**")
    st.markdown("[☕ Buy Me a Coffee](https://www.buymeacoffee.com/YOUR_USERNAME)")

topic = st.text_input("What is your video about?", placeholder="e.g., 5 ways to make money")
tone = st.selectbox("Tone", ["Funny", "High Energy", "Suspenseful"])

if st.button("Generate Script ✨"):
    if topic:
        prompt = f"Write a viral 60-second script about {topic} in a {tone} tone. Include a hook and visual cues."
        response = model.generate_content(prompt)
        st.success("Script Ready!")
        st.write(response.text)
    else:
        st.error("Please enter a topic!")
      
