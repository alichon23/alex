import streamlit as st

# Configuración de la página (¡Importante!)
st.set_page_config(page_title="Glow & Bloom | Tu Tienda", layout="wide")

# --- ESTILO PERSONALIZADO ---
# Mantenemos un estilo limpio y elegante
st.markdown("""
    <style>
    .main {
        background-color: #fffcf2; /* Un beige muy suave */
    }
    .stButton>button {
        border-radius: 20px;
        background-color: #d4a373; /* Tono tierra suave */
        color: white;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #a98467; /* Un tono más oscuro al pasar el mouse */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ---
menu = ["Inicio", "Catálogo", "Carrito"]
choice = st.sidebar.selectbox("Ir a:", menu)

# --- BASE DE DATOS FICTICIA (PRODUCTOS) ---
# Usamos las mismas URLs de imágenes genéricas para que funcione de inmediato
productos = [
    {
        "nombre": "Sérum Facial Vitamina C", 
        "precio": 25.0, 
        "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=500", 
        "desc": "Piel radiante en segundos."
    },
    {
        "nombre": "Labial Mate 'Rose'", 
        "precio": 12.0, 
        "img": "https://http2.mlstatic.com/D_Q_NP_2X_655870-MLM110060389605_042026-P.webpw=500", 
        "desc": "Larga duración, color intenso."
    },
    {
        "nombre": "Paleta de Sombras Nude", 
        "precio": 35.0, 
        "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=500", 
        "desc": "12 tonos para cualquier ocasión."
    },
    {
        "nombre": "Máscara de Pestañas", 
        "precio": 15.0, 
        "img": "https://avobeauty.mx/cdn/shop/products/PROSAMASCARAMAXIVOLUMEN4EN1_1200x1200.jpg?v=1736527332w=500", 
        "desc": "Volumen extremo, sin grumos."
    }
]

# --- LÓGICA DE LA PÁGINA ---
if choice == "Inicio":
    st.title("✨ Bienvenidos a Glow & Bloom")
    st.subheader("Tu destino favorito para la belleza natural.")
    st.write("Explora nuestra nueva colección de temporada, diseñada para realzar tu brillo natural.")
    # Imagen de banner (mantenemos el ancho completo aquí)
    st.image("https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=1200", use_container_width=True)

elif choice == "Catálogo":
    st.title("Nuestros Productos")
    st.write("Haz clic en 'Añadir al carrito' para agregar tus favoritos.")
    
    # Crear columnas para los productos (hemos aumentado a 3 columnas)
    cols = st.columns(3)
    
    for i, p in enumerate(productos):
        # Distribuir productos en las columnas
        with cols[i % 3]:
            # --- AJUSTE DE TAMAÑO DE IMAGEN ---
            # Aquí está el cambio clave: hemos establecido 'width=200'
            # y quitado 'use_container_width=True'
            st.image(p["img"], width=200) 
            
            st.subheader(p["nombre"])
            st.write(p["desc"])
            st.write(f"**Precio:** ${p['precio']}")
            # Botón con una clave única para cada producto
            st.button(f"Añadir al carrito", key=f"add_{i}")

elif choice == "Carrito":
    st.title("Tu Carrito 🛒")
    # Mensaje temporal, luego se puede añadir la lógica del carrito
    st.info("Aún no has agregado productos a tu carrito.")