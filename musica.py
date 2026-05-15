import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Reproductor sin Límites", page_icon="🎵", layout="centered")

st.title("🎵 Reproductor de Música Ilimitado")
st.write("Sube tus canciones favoritas y crea tu lista de reproducción al instante.")

# 1. Zona de carga de archivos (Sin límite de cantidad)
uploaded_files = st.file_uploader(
    "Arrastra o selecciona tus archivos de audio (MP3, WAV, OGG)", 
    type=["mp3", "wav", "ogg"], 
    accept_multiple_files=True
)

# Inicializar el estado de la sesión para controlar la canción actual
if "playlist" not in st.session_state:
    st.session_state.playlist = []
if "current_track_index" not in st.session_state:
    st.session_state.current_track_index = 0

# 2. Procesar las canciones subidas
if uploaded_files:
    # Actualizar la lista de reproducción si cambia la subida
    st.session_state.playlist = uploaded_files
    
    # Crear una lista con los nombres de las canciones para el menú
    song_names = [file.name for file in st.session_state.playlist]
    
    # 3. Interfaz de control
    st.subheader("Lista de Reproducción")
    
    # Selector de canción
    selected_song_name = st.selectbox(
        "Selecciona una canción para reproducir:", 
        options=song_names,
        index=st.session_state.current_track_index
    )
    
    # Actualizar el índice según la selección del usuario
    st.session_state.current_track_index = song_names.index(selected_song_name)
    current_file = st.session_state.playlist[st.session_state.current_track_index]
    
    # 4. Reproductor de Audio
    st.markdown(f"### 📻 Sonando ahora: **{current_file.name}**")
    
    # Leer el archivo en bytes para el reproductor de Streamlit
    audio_bytes = current_file.read()
    st.audio(audio_bytes, format=f"audio/{current_file.name.split('.')[-1]}")
    
    # 5. Controles de navegación (Anterior / Siguiente)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⏮️ Anterior"):
            if st.session_state.current_track_index > 0:
                st.session_state.current_track_index -= 1
                st.rerun()
                
    with col3:
        if st.button("Siguiente ⏭️"):
            if st.session_state.current_track_index < len(st.session_state.playlist) - 1:
                st.session_state.current_track_index += 1
                st.rerun()

else:
    st.info("👋 Por favor, sube algunos archivos de audio en el panel de arriba para empezar a escuchar.")