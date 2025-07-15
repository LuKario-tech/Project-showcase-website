import streamlit as st

st.set_page_config(layout = 'wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width = 400)

with col2:
    st.title('Yatharth Negi')
    content = """Hi, I'm Yatharth Negi, a BBA student from India with a strong interest in data science and analytics.
                 I'm learning tools like Python, SQL, Power BI, and Excel to turn data into insights.
                 I've also gained experience through internships in HR and operations,
                 and I'm passionate about using data to solve real-world problems.
                 This site showcases my projects as I continue to grow and explore the field of data."""
    
    st.info(content)