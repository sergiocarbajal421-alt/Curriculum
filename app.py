from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText

# 1. CONFIGURACIÓN DE PÁGINA (DEBE SER LA PRIMERA LÍNEA DE STREAMLIT)
st.set_page_config(
    page_title="Portafolio | Sergio Carbajal",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CONFIGURACIÓN DE RUTAS Y ARCHIVOS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "CV_SergioCarbajal.pdf"
profile_pic = current_dir / "profile-pic.png"

# 3. METADATOS EXTRAÍDOS DE TU CV ACTUALIZADO
NAME = "SERGIO CARBAJAL" [cite: 32]
TAGLINE = "Ingeniero Empresarial | Data & Automation Engineer" [cite: 33]
EMAIL = "SergioCarbajal421@gmail.com" [cite: 36]
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sergiocarbajalromero/", [cite: 35]
    "GitHub": "https://github.com/sergiocarbajal421-alt",
}

# 4. CARGA DE RECURSOS CON MANEJO DE ERRORES
try:
    with open(resume_file, "rb") as f:
        PDFbyte = f.read()
    profile_img = Image.open(profile_pic)
except:
    PDFbyte = None
    profile_img = None

# 5. ESTILOS CSS (MANTENIENDO TU DISEÑO ORIGINAL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@600;700&display=swap');
    :root { --primary:#005b96; --secondary:#008b8b; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .name { font-family: 'Playfair Display', serif; font-size: 42px; color: var(--primary); margin: 0; }
    .card { background: #f9fafb; border-radius: 12px; padding: 20px; border: 1px solid #d1d5db; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 6. HERO SECTION
hero_col1, hero_col2 = st.columns([1.1, 2.2], gap="medium")
with hero_col1:
    if profile_img:
        st.image(profile_img, width=230)

with hero_col2:
    st.markdown(f'<h1 class="name">{NAME}</h1>', unsafe_allow_html=True)
    st.markdown(f'<div style="color:var(--secondary); font-weight:600; font-size:18px;">{TAGLINE}</div>', unsafe_allow_html=True)
    st.markdown(f"📍 Lima, Perú | 📞 901 439 762 | ✉️ {EMAIL}") [cite: 34, 36]
    
    st.markdown("""
    Ingeniero especializado en **arquitectura de datos y automatización**[cite: 37]. 
    Transformo tareas manuales en **pipelines automatizados** con Python y SQL Cloud[cite: 38].
    """)

    # TYPEWRITER (CORREGIDO PARA EVITAR NAMEERROR)
    words_list = ["Python", "SQL Cloud", "Azure", "T-SQL", "ETL Pipelines", "Stored Procedures"] [cite: 38, 46, 47, 54, 55]
    type_text = " - ".join(words_list)
    
    components.html(f"""
        <div id="tw" style="font-family:sans-serif; font-size:17px; color:#374151; font-weight:500;"></div>
        <script>
            const txt = "{type_text}";
            let i = 0;
            function type() {{
                if (i <= txt.length) {{
                    document.getElementById('tw').innerHTML = txt.substring(0, i);
                    i++;
                    setTimeout(type, 100);
                }} else {{ setTimeout(() => {{ i = 0; type(); }}, 3000); }}
            }}
            type();
        </script>
    """, height=40)

    # BOTONES
    btn1, btn2 = st.columns([1, 1])
    with btn1:
        if PDFbyte:
            st.download_button("📄 Descargar CV Técnico", PDFbyte, "CV_SergioCarbajal.pdf", "application/pdf")
    with btn2:
        st.markdown(f'<a href="mailto:{EMAIL}" style="background:#005b96; color:white; padding:10px; border-radius:10px; text-decoration:none; font-weight:600;">✉️ Contactar</a>', unsafe_allow_html=True)

# 7. MÉTRICAS DE IMPACTO (MANTENIENDO EL DISEÑO DE TU CÓDIGO)
st.markdown("### 📊 Impacto de Ingeniería")
m1, m2, m3 = st.columns(3)
m1.metric("Optimización Tiempo", "88%", "De 3h a 20min") [cite: 41]
m2.metric("Integridad Datos", "95%", "Menos duplicidad") [cite: 47]
m3.metric("Eficiencia Campo", "70%", "vía Power Apps") [cite: 48]

# 8. EXPERIENCIA Y STACK (ACTUALIZADO AL CV MEJORADO)
col_a, col_b = st.columns([2, 1], gap="large")

with col_a:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💼 Experiencia Profesional")
    
    exp1, exp2 = st.tabs(["🚀 Visiva", "⚙️ Credigama"])
    
    with exp1:
        st.markdown("**Data & Automation Developer**") [cite: 40]
        st.markdown("- Procesamiento masivo con Python: **3 horas a 20 minutos**[cite: 41].")
        st.markdown("- Migración estratégica a **SQL Cloud** e infraestructuras open source[cite: 43, 44].")
    
    with exp2:
        st.markdown("**Arquitectura de Datos & Automatización**") [cite: 45]
        st.markdown("- Implementación en **Azure (SQL DB & Blob Storage)**[cite: 46].")
        st.markdown("- Lógica avanzada: **Stored Procedures y Views** en T-SQL[cite: 47].")
        st.markdown("- Digitalización del 100% de registros físicos[cite: 46].")
    st.markdown('</div>', unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🛠 Stack Técnico")
    st.write("**Avanzado:** SQL, Python, VS Code") [cite: 54]
    st.write("**Intermedio:** Azure, GitHub") [cite: 55]
    st.progress(95) # Representación visual de seniority
    st.markdown('</div>', unsafe_allow_html=True)

# 9. PROYECTOS Y FOOTER
st.markdown("### 🚀 Proyectos Destacados") [cite: 57]
p1, p2, p3 = st.columns(3)
p1.info("**Gestión de Lotes** [cite: 60]")
p2.info("**Accidentes Tránsito Perú** [cite: 59]")
p3.info("**Portafolio Web** [cite: 58]")

st.markdown(f"<center style='color:grey;'>© 2026 {NAME} | Ingeniero de Datos</center>", unsafe_allow_html=True)
