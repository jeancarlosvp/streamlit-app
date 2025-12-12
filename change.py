
import streamlit as st

if 'number_state' not in st.session_state:
    st.session_state.number_state = 5

number = 5
st.write("El número es:", number)

st.write("El número persistente es:", st.session_state.number_state)

if st.button("say hello"):
    st.write("Hello, button on !")
    number += 1
    st.session_state.number_state += 1
    st.write("El número es ahora:", number)
    st.write("El número persistente es ahora:", st.session_state.number_state)

# Número de elementos
st.write(f"Total de elementos: {len(st.session_state)}")
for key, value in st.session_state.items():
    st.write(f"- **{key}**: {value}")