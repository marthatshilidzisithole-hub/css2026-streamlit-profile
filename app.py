import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Professional Profile",
    layout="centered"
)

# ===== NAME & TITLE =====
st.title("MS MT Sithole")
st.subheader("IT Technician | Aspiring Data Scientist")

st.write(
    "Welcome to my Streamlit profile page. This page showcases my professional background, "
    "learning journey, and interests in Data Science and technology."
)

st.divider()

# ===== ABOUT ME =====
st.header("About Me")
st.write(
    "I am an IT Technician with professional experience in system support, troubleshooting, "
    "and maintaining IT infrastructure. While my current role is not data-focused, "
    "I am actively transitioning into the field of Data Science."
)

st.write(
    "I am developing skills in Python, data analysis, and data visualization, "
    "and I enjoy building interactive applications using Streamlit."
)

st.divider()

# ===== CAREER FOCUS =====
st.header("Career Focus")
st.write(
    "My goal is to move into a data-oriented role by combining my IT background "
    "with analytical thinking and programming skills. I am particularly interested in "
    "data visualization, data pipelines, and practical data-driven solutions."
)

st.divider()

# ===== SKILLS =====
st.header("Skills and Tools")
st.markdown(
    """
    - Python  
    - Pandas and NumPy (learning)  
    - Streamlit  
    - Data Visualization (learning)  
    - IT Support and Troubleshooting  
    - SQLite (basic)  
    """
)

st.divider()

# ===== INTERESTS =====
st.header("Interests")
st.markdown(
    """
    - Data Science and Analytics  
    - Data Visualization  
    - Cybersecurity 
    - Networks
    - Continuous Learning  
    - Technology and Problem Solving  
    """
)

st.divider()

# ===== PROJECTS =====
st.header("Projects")
st.write(
    "Currently working on coursework-based projects in Data Science and Streamlit. "
    "More projects will be added as I continue developing my skills."
)

st.divider()

# ===== CONTACT =====
st.header("Contact")
st.write("Email: marthatshilidzisithole@gmail.com")
st.write("GitHub: https://github.com/marthatshilidzisithole")

st.divider()

st.caption("Built using Streamlit")




