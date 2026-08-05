import streamlit as st



pages = [
    st.Page("pages/home_page.py", title="Home", icon="🏠"),
    st.Page("pages/exercises_page.py", title="Exercises", icon="🏋"),
]

nav = st.navigation(pages)
nav.run()

