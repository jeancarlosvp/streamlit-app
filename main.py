import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(
    page_title="Aplicación de ventas y gestión",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar para navegación
st.sidebar.title("📋 Navegación")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    ["Dashboard", "Productos", "Ventas", "Pagos", "Usuarios"]
)

# ============================================
# SECCIÓN: DASHBOARD
# ============================================
if seccion == "Dashboard":
    st.title("📊 Dashboard")
    st.markdown("### Vista general del negocio")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Ventas del mes",
            value="$45,231",
            delta="12%"
        )
    
    with col2:
        st.metric(
            label="Productos activos",
            value="127",
            delta="5"
        )
    
    with col3:
        st.metric(
            label="Pagos pendientes",
            value="$8,400",
            delta="-15%"
        )
    
    with col4:
        st.metric(
            label="Clientes nuevos",
            value="23",
            delta="3"
        )
    
    # Gráficos
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Ventas por día (últimos 30 días)")
        # Datos de ejemplo
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        sales_data = pd.DataFrame({
            'Fecha': dates,
            'Ventas': np.random.randint(500, 2000, 30)
        })
        st.line_chart(sales_data.set_index('Fecha'))
    
    with col2:
        st.markdown("#### 🎯 Productos más vendidos")
        products_data = pd.DataFrame({
            'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
            'Ventas': [450, 380, 320, 280, 210]
        })
        st.bar_chart(products_data.set_index('Producto'))

# ============================================
# SECCIÓN: PRODUCTOS
# ============================================
elif seccion == "Productos":
    st.title("📦 Gestión de Productos")
    
    # Tabs para diferentes acciones
    tab1, tab2, tab3 = st.tabs(["📋 Lista de Productos", "➕ Agregar Producto", "📊 Estadísticas"])
    
    with tab1:
        st.markdown("### Lista de Productos")
        
        # Filtros
        col1, col2 = st.columns(2)
        with col1:
            buscar = st.text_input("🔍 Buscar producto", placeholder="Nombre del producto...")
        with col2:
            categoria = st.selectbox("Categoría", ["Todas", "Electrónica", "Ropa", "Alimentos", "Hogar"])
        
        # Tabla de productos (datos de ejemplo)
        productos_df = pd.DataFrame({
            'ID': range(1, 11),
            'Nombre': [f'Producto {i}' for i in range(1, 11)],
            'Categoría': np.random.choice(['Electrónica', 'Ropa', 'Alimentos', 'Hogar'], 10),
            'Precio': np.random.randint(10, 500, 10),
            'Stock': np.random.randint(0, 100, 10),
            'Estado': np.random.choice(['Activo', 'Inactivo'], 10)
        })
        
        st.dataframe(productos_df, use_container_width=True)
    
    with tab2:
        st.markdown("### Agregar Nuevo Producto")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nombre = st.text_input("Nombre del producto")
            categoria = st.selectbox("Categoría", ["Electrónica", "Ropa", "Alimentos", "Hogar", "Otros"])
            precio = st.number_input("Precio ($)", min_value=0.0, step=0.01)
        
        with col2:
            sku = st.text_input("SKU")
            stock = st.number_input("Stock inicial", min_value=0, step=1)
            estado = st.selectbox("Estado", ["Activo", "Inactivo"])
        
        descripcion = st.text_area("Descripción del producto")
        
        if st.button("💾 Guardar Producto", type="primary"):
            st.success("✅ Producto guardado exitosamente!")
    
    with tab3:
        st.markdown("### Estadísticas de Productos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total de productos", "127")
            st.metric("Productos con bajo stock", "12")
        
        with col2:
            st.metric("Valor total del inventario", "$128,450")
            st.metric("Categorías activas", "8")

# ============================================
# SECCIÓN: VENTAS
# ============================================
elif seccion == "Ventas":
    st.title("💰 Gestión de Ventas")
    
    tab1, tab2, tab3 = st.tabs(["📋 Registro de Ventas", "➕ Nueva Venta", "📊 Reportes"])
    
    with tab1:
        st.markdown("### Historial de Ventas")
        
        # Filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            fecha_inicio = st.date_input("Fecha inicio", datetime.now() - timedelta(days=30))
        with col2:
            fecha_fin = st.date_input("Fecha fin", datetime.now())
        with col3:
            estado_venta = st.selectbox("Estado", ["Todas", "Completada", "Pendiente", "Cancelada"])
        
        # Tabla de ventas (datos de ejemplo)
        ventas_df = pd.DataFrame({
            'ID': range(1, 21),
            'Fecha': pd.date_range(end=datetime.now(), periods=20, freq='D'),
            'Cliente': [f'Cliente {i}' for i in range(1, 21)],
            'Total': np.random.randint(50, 1000, 20),
            'Estado': np.random.choice(['Completada', 'Pendiente', 'Cancelada'], 20),
            'Método de pago': np.random.choice(['Efectivo', 'Tarjeta', 'Transferencia'], 20)
        })
        
        st.dataframe(ventas_df, use_container_width=True)
        
        st.markdown(f"**Total ventas mostradas:** ${ventas_df['Total'].sum():,.2f}")
    
    with tab2:
        st.markdown("### Registrar Nueva Venta")
        
        col1, col2 = st.columns(2)
        
        with col1:
            cliente = st.text_input("Nombre del cliente")
            fecha_venta = st.date_input("Fecha de venta", datetime.now())
        
        with col2:
            metodo_pago = st.selectbox("Método de pago", ["Efectivo", "Tarjeta de crédito", "Tarjeta de débito", "Transferencia"])
            estado = st.selectbox("Estado de la venta", ["Completada", "Pendiente"])
        
        st.markdown("#### Productos")
        
        num_productos = st.number_input("Cantidad de productos", min_value=1, max_value=10, value=1)
        
        total = 0
        for i in range(num_productos):
            col1, col2, col3 = st.columns(3)
            with col1:
                producto = st.selectbox(f"Producto {i+1}", [f"Producto {j}" for j in range(1, 11)], key=f"prod_{i}")
            with col2:
                cantidad = st.number_input(f"Cantidad", min_value=1, value=1, key=f"cant_{i}")
            with col3:
                precio = st.number_input(f"Precio unitario ($)", min_value=0.0, value=10.0, key=f"precio_{i}")
            
            total += cantidad * precio
        
        st.markdown(f"### Total: ${total:,.2f}")
        
        if st.button("💾 Registrar Venta", type="primary"):
            st.success("✅ Venta registrada exitosamente!")
    
    with tab3:
        st.markdown("### Reportes de Ventas")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Ventas del día", "$2,340")
            st.metric("Ventas de la semana", "$15,890")
        
        with col2:
            st.metric("Ventas del mes", "$45,231")
            st.metric("Ticket promedio", "$187")
        
        with col3:
            st.metric("Total de transacciones", "242")
            st.metric("Tasa de conversión", "68%")

# ============================================
# SECCIÓN: PAGOS
# ============================================
elif seccion == "Pagos":
    st.title("💳 Gestión de Pagos")
    
    tab1, tab2, tab3 = st.tabs(["📋 Registro de Pagos", "➕ Nuevo Pago", "📊 Estado de Cuentas"])
    
    with tab1:
        st.markdown("### Historial de Pagos")
        
        # Filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            fecha_inicio = st.date_input("Desde", datetime.now() - timedelta(days=30), key="pago_inicio")
        with col2:
            fecha_fin = st.date_input("Hasta", datetime.now(), key="pago_fin")
        with col3:
            estado_pago = st.selectbox("Estado del pago", ["Todos", "Pagado", "Pendiente", "Vencido"])
        
        # Tabla de pagos (datos de ejemplo)
        pagos_df = pd.DataFrame({
            'ID': range(1, 16),
            'Fecha': pd.date_range(end=datetime.now(), periods=15, freq='2D'),
            'Concepto': [f'Factura #{i}' for i in range(1, 16)],
            'Proveedor/Cliente': [f'Empresa {i}' for i in range(1, 16)],
            'Monto': np.random.randint(100, 5000, 15),
            'Estado': np.random.choice(['Pagado', 'Pendiente', 'Vencido'], 15),
            'Método': np.random.choice(['Transferencia', 'Cheque', 'Efectivo'], 15)
        })
        
        st.dataframe(pagos_df, use_container_width=True)
        
        # Resumen
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total pagado", f"${pagos_df[pagos_df['Estado'] == 'Pagado']['Monto'].sum():,.2f}")
        with col2:
            st.metric("Total pendiente", f"${pagos_df[pagos_df['Estado'] == 'Pendiente']['Monto'].sum():,.2f}")
        with col3:
            st.metric("Total vencido", f"${pagos_df[pagos_df['Estado'] == 'Vencido']['Monto'].sum():,.2f}")
    
    with tab2:
        st.markdown("### Registrar Nuevo Pago")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tipo_pago = st.selectbox("Tipo de pago", ["Pago a proveedor", "Cobro a cliente"])
            concepto = st.text_input("Concepto")
            destinatario = st.text_input("Proveedor/Cliente")
        
        with col2:
            fecha_pago = st.date_input("Fecha del pago", datetime.now(), key="nuevo_pago")
            monto = st.number_input("Monto ($)", min_value=0.0, step=0.01)
            metodo = st.selectbox("Método de pago", ["Transferencia bancaria", "Efectivo", "Cheque", "Tarjeta"])
        
        referencia = st.text_input("Número de referencia/Comprobante")
        notas = st.text_area("Notas adicionales")
        
        if st.button("💾 Registrar Pago", type="primary"):
            st.success("✅ Pago registrado exitosamente!")
    
    with tab3:
        st.markdown("### Estado de Cuentas")
        
        # Resumen financiero
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💰 Ingresos")
            st.metric("Ingresos del mes", "$52,340")
            st.metric("Ingresos pendientes", "$8,400")
            
            st.markdown("#### 📊 Balance")
            st.metric("Balance neto", "$34,890", delta="8%")
        
        with col2:
            st.markdown("#### 💸 Egresos")
            st.metric("Egresos del mes", "$17,450")
            st.metric("Pagos pendientes", "$5,200")
            
            st.markdown("#### 📈 Flujo de caja")
            # Gráfico simple de flujo de caja
            flujo_data = pd.DataFrame({
                'Día': range(1, 31),
                'Flujo': np.random.randint(-1000, 3000, 30).cumsum()
            })
            st.line_chart(flujo_data.set_index('Día'))

# Footer
st.sidebar.markdown("---")
st.sidebar.info("💡 **Aplicación de Gestión**\nVersión 1.0.0")
