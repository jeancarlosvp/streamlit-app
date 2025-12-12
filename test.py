import streamlit as st

st.title("Ejemplo con Tabs en Streamlit")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📁 Datos", "⚙️ Configuración"])

# --- Tab 1 -----------------------
with tab1:
    st.header("Dashboard")
    st.write("Aquí puedes mostrar gráficos, KPIs, etc.")
    st.line_chart({"Ventas": [10, 20, 40, 30, 50]})

# --- Tab 2 -----------------------
with tab2:
    st.header("Datos")
    st.write("Carga o muestra tus datasets.")
    st.dataframe({
        "Producto": ["A", "B", "C"],
        "Precio": [10, 20, 30]
    })

# --- Tab 3 -----------------------
with tab3:
    st.header("Configuración")
    st.write("Opciones de usuario o de aplicación.")
    usuario = st.text_input("Nombre del usuario")
    activar = st.checkbox("Activar modo avanzado")

    if activar:
        st.success("Modo avanzado activado.")
