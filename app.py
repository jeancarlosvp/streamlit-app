import streamlit as st
from database import Database
import pandas as pd

# Configuración de la página
st.set_page_config("Mi aplicación Streamlit")

# Sidebar
st.sidebar.title("Navegación")
section = st.sidebar.radio(
    "Selecciona una sección:",
    ["Vista General", "Productos", "Ventas", "Pagos"]
)

# Agrego un comentario sobre la aplicación

database = Database()

if section == "Vista General":
    st.header("Vista General")
    st.write("Contenido de la vista general...")
elif section == "Productos":
    st.header("Productos")
    st.write("Contenido de la sección de productos...")
    tab_list, tab_add_product = st.tabs(["Lista de Productos", "Agregar Producto"])
    with tab_list:
        st.subheader("Lista de Productos")
        # Mostra la lista de productos de la base de datos de sqlite
        st.write("Aquí se mostraría la lista de productos desde la base de datos.")
        products = database.get_products()
        if products:
            df_products = pd.DataFrame(products, columns=["ID", "Nombre", "Precio", "Stock", "Categoría", "Creado En"])
            st.table(df_products)
        else:
            st.info("No hay productos disponibles.")


    with tab_add_product:
        st.subheader("Agregar Nuevo Producto")
        product_name = st.text_input("Nombre del Producto") 
        product_price = st.number_input("Precio del Producto", min_value=0.0, format="%.2f")
        stock_quantity = st.number_input("Cantidad en Stock", min_value=0, step=1)
        category = st.selectbox("Categoría", ["Dessert", "Beverages", "Others"])
    
        if st.button("Agregar Producto"):
            database.add_product(product_name, product_price, stock_quantity, category)
            st.success(f"Producto '{product_name}' agregado con éxito.")


elif section == "Ventas":
    st.header("Ventas")
    st.write("Contenido de la sección de ventas...")
elif section == "Pagos":
    st.header("Pagos")
    st.write("Contenido de la sección de pagos...")

 