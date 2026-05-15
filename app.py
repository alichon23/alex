import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Glow & Care Co.", page_icon="✨", layout="wide")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main {
        background-color: #fff5f8;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b91;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar el carrito en el estado de la sesión
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- BARRA LATERAL (Sidebar) ---
st.sidebar.title("🌸 Glow & Care")
st.sidebar.subheader("Navegación")
menu = st.sidebar.radio("Ir a:", ["Inicio", "Catálogo", "Mi Carrito", "Contacto"])

# --- DATOS DE PRODUCTOS ---
productos = [
    {"id": 1, "nombre": "Sérum de Vitamina C", "precio": 25.0, "categoria": "Cuidado Facial", "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=300"},
    {"id": 2, "nombre": "Labial Mate Velvet", "precio": 12.5, "categoria": "Maquillaje", "img": "https://images.unsplash.com/photo-1586776977607-310e9c725c37?w=300"},
    {"id": 3, "nombre": "Crema Hidratante Pro", "precio": 30.0, "categoria": "Cuidado Facial", "img": "https://images.unsplash.com/photo-1570194065650-d99fb4b8ccb0?w=300"},
    {"id": 4, "nombre": "Paleta de Sombras Nude", "precio": 45.0, "categoria": "Maquillaje", "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=300"},
]

# --- LÓGICA DE NAVEGACIÓN ---

if menu == "Inicio":
    st.title("✨ Bienvenidos a Glow & Care Co.")
    st.image("https://images.unsplash.com/photo-1596462502278-27bfdc4033c8?w=1000", caption="Realza tu belleza natural")
    st.write("""
    Explora nuestra colección exclusiva de productos diseñados para consentir tu piel. 
    Desde tratamientos avanzados hasta el maquillaje más chic.
    """)
    if st.button("Ver Catálogo"):
        st.info("¡Usa el menú de la izquierda para empezar a comprar!")

elif menu == "Catálogo":
    st.title("🛍️ Nuestro Catálogo")
    
    # Filtro por categoría
    categoria_filtro = st.selectbox("Filtrar por categoría:", ["Todos", "Cuidado Facial", "Maquillaje"])
    
    cols = st.columns(2)
    
    for i, prod in enumerate(productos):
        if categoria_filtro == "Todos" or prod["categoria"] == categoria_filtro:
            with cols[i % 2]:
                st.image(prod["img"], use_container_width=True)
                st.subheader(prod["nombre"])
                st.write(f"**Precio:** ${prod['precio']}")
                st.caption(f"Categoría: {prod['categoria']}")
                if st.button(f"Añadir al carrito", key=prod['id']):
                    st.session_state.cart.append(prod)
                    st.success(f"{prod['nombre']} añadido.")

elif menu == "Mi Carrito":
    st.title("🛒 Tu Carrito de Compras")
    
    if not st.session_state.cart:
        st.warning("Tu carrito está vacío.")
    else:
        total = 0
        for item in st.session_state.cart:
            col1, col2 = st.columns([3, 1])
            col1.write(f"✅ {item['nombre']}")
            col2.write(f"${item['precio']}")
            total += item['precio']
        
        st.divider()
        st.subheader(f"Total a pagar: ${total:.2f}")
        
        if st.button("Finalizar Compra"):
            st.balloons()
            st.success("¡Gracias por tu compra! Procesando pedido...")
            st.session_state.cart = [] # Limpiar carrito

elif menu == "Contacto":
    st.title("📩 Contáctanos")
    with st.form("contacto_form"):
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo electrónico")
        mensaje = st.text_area("¿En qué podemos ayudarte?")
        submit = st.form_submit_button("Enviar Mensaje")
        
        if submit:
            st.write(f"Gracias {nombre}, nos pondremos en contacto contigo pronto.")