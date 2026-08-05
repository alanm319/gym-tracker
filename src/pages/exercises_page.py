import streamlit as st
from pipeline import get_session_data
from charts import plot_volume

st.title("Exercises")

@st.cache_data
def load_data():
    return get_session_data()

all_exercises = load_data()

for exercise in sorted(all_exercises["exercise_title"].unique()):
    with st.expander(exercise):
        # exercise_df = all_exercises[all_exercises["exercise_title"] == exercise]
        fig = plot_volume(all_exercises, exercise)
        st.pyplot(fig)
    