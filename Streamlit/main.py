import streamlit as st
import pandas as pd

table = pd.DataFrame({"Column 1": [1,2,3,4,5,6,7],
"Column 2": [11,12,13,14,15,16,17]})

st.title("Hi! I´m streamlit web app")
st.header("Este es un encabezado")
st.subheader("Este es un sub-encabezado")
st.text("Esta función se usa para crear textos")

st.markdown("**Hello** *world*")
st.markdown("~~The world is flat.~~")
st.markdown("I need to highlight these ==very important words==")

st.markdown("---")

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json = {"a":"1,2,3",
"b":"4,5,6"}
st.json(json)
code = """
print("hello world")
def funct():
    return 0
"""
st.code(code, language="Python")
st.write("## H2")
st.metric(label = "Wind Speed", value="120ms⁻¹", delta = "-1.4ms⁻¹")

st.table(table)
st.dataframe(table)

st.image("mapa colombia.jpg", caption="Esta es una imagen de la bandera de Colombia",
width=500)

video_url = "https://www.youtube.com/embed/LxsMdHrNS-o"
st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

