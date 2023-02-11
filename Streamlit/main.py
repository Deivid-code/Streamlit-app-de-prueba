import streamlit as st

st.title("Hi! I´m streamlit web app")
st.header("Este es un encabezado")
st.subheader("Este es un sub-encabezado")
st.text("Esta función se usa para crear textos")
st.markdown("**Hello** *world*")
st.markdown("~~The world is flat.~~")
st.markdown("I need to highlight these ==very important words==")

lista = ["First item", "Second item", "Third item"]

st.write("## Lista ordenada:")

for i, item in enumerate(lista):
    st.write("{}. {}".format(i+1, item))

from PIL import Image

imagen = Image.open("C:/Users/David/Pictures/Screenshots/Captura de pantalla 2023-02-07 182007.png")
st.image(imagen, caption="Captura de pantalla", use_column_width=True)

