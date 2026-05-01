import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Glow & Bloom | Tienda de Cosméticos", layout="wide")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .main {
        background-color: #fff5f8;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4bb4;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ---
menu = ["Inicio", "Catálogo", "Carrito", "Contacto"]
choice = st.sidebar.selectbox("Ir a:", menu)

# --- BASE DE DATOS FICTICIA (PRODUCTOS) ---
# Aquí es donde usarás las rutas de imagen que te explicaré abajo
productos = [
    {"nombre": "Sérum Facial Vitamina C", "precio": 25.0, "img": "img/serum.jpg", "desc": "Piel radiante en segundos."},
    {"nombre": "Labial Mate 'Rose'", "precio": 12.0, "img": "img/labial.jpg", "desc": "Larga duración y color intenso."},
    {"nombre": "Paleta de Sombras Nude", "precio": 35.0, "img": "img/sombras.jpg", "desc": "12 tonos para cualquier ocasión."},
    {"nombre": "Máscara de Pestañas", "precio": 15.0, "img": "img/mascara.jpg", "desc": "Volumen extremo sin grumos."}
]

# --- LÓGICA DE LA PÁGINA ---
if choice == "Inicio":
    st.title("✨ Bienvenidos a Glow & Bloom")
    st.subheader("Tu destino favorito para la belleza natural.")
    st.write("Explora nuestra nueva colección de temporada.")
    # Imagen de banner (Explicación abajo)
    st.image("img/banner.jpg", use_container_width=True)

elif choice == "Catálogo":
    st.title("Nuestros Productos")
    
    # Crear columnas para los productos
    cols = st.columns(2)
    
    for i, p in enumerate(productos):
        with cols[i % 2]:
            st.image(p["img"], width=300) # Espacio para la imagen
            st.subheader(p["nombre"])
            st.write(p["desc"])
            st.write(f"**Precio:** ${p['precio']}")
            if st.button(f"Añadir al carrito", key=i):
                st.success(f"¡{p['nombre']} añadido!")

elif choice == "Carrito":
    st.title("Tu Carrito 🛒")
    st.info("Aún no has agregado productos.")

elif choice == "Contacto":
    st.title("Contáctanos")
    with st.form("contacto"):
        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo")
        mensaje = st.text_area("Mensaje")
        submit = st.form_submit_button("Enviar")
        if submit:
            st.balloons()
            st.success("Mensaje enviado con éxito")