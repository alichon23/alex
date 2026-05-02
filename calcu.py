import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora Smart", page_icon="🔢")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        height: 3em;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        background-color: #6c757d;
        color: white;
    }
    .stButton>button:hover {
        background-color: #495057;
        color: #ffca28;
    }
    /* Estilo para el resultado */
    .resultado-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #dee2e6;
        text-align: right;
        font-size: 30px;
        font-family: monospace;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔢 Calculadora Minimalista")

# Inicializar el estado de la pantalla si no existe
if 'expresion' not in st.session_state:
    st.session_state.expresion = ""

# --- PANTALLA DE RESULTADOS ---
st.markdown(f'<div class="resultado-box">{st.session_state.expresion if st.session_state.expresion else "0"}</div>', unsafe_allow_html=True)

# --- BOTONES ---
# Creamos una cuadrícula de 4 columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"): st.session_state.expresion += "7"; st.rerun()
    if st.button("4"): st.session_state.expresion += "4"; st.rerun()
    if st.button("1"): st.session_state.expresion += "1"; st.rerun()
    if st.button("C"): st.session_state.expresion = ""; st.rerun()

with col2:
    if st.button("8"): st.session_state.expresion += "8"; st.rerun()
    if st.button("5"): st.session_state.expresion += "5"; st.rerun()
    if st.button("2"): st.session_state.expresion += "2"; st.rerun()
    if st.button("0"): st.session_state.expresion += "0"; st.rerun()

with col3:
    if st.button("9"): st.session_state.expresion += "9"; st.rerun()
    if st.button("6"): st.session_state.expresion += "6"; st.rerun()
    if st.button("3"): st.session_state.expresion += "3"; st.rerun()
    if st.button("."): st.session_state.expresion += "."; st.rerun()

with col4:
    if st.button("➕"): st.session_state.expresion += "+"; st.rerun()
    if st.button("➖"): st.session_state.expresion += "-"; st.rerun()
    if st.button("✖️"): st.session_state.expresion += "*"; st.rerun()
    if st.button("✔️"): # Botón de Igual
        try:
            # Evaluar la expresión matemática
            st.session_state.expresion = str(eval(st.session_state.expresion))
        except:
            st.session_state.expresion = "Error"
        st.rerun()

# --- OPERACIÓN ADICIONAL ---
if st.button("➗"): 
    st.session_state.expresion += "/"
    st.rerun()