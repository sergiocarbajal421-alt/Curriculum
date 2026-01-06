from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText

# -------------------------
# CONFIG (DEBE SER LO PRIMERO)
# -------------------------
st.set_page_config(
    page_title="Portafolio | Sergio Carbajal",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------
# PATH SETTINGS
# -------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "CV_SergioCarbajal.pdf"
profile_pic = current_dir / "profile-pic.png"

# -------------------------
# METADATOS (DE TU MODELO CLÁSICO)
# -------------------------
NAME = "SERGIO CARBAJAL"
TAGLINE = "Ingeniero Empresarial | Data & Automation Engineer"
EMAIL = "SergioCarbajal421@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sergiocarbajalromero/",
    "GitHub": "https://github.com/sergiocarbajal421-alt",
}

# -------------------------
# CARGA ARCHIVOS
# -------------------------
try:
    with open(resume_file, "rb") as f:
        PDFbyte = f.read()
    profile_img = Image.open(profile_pic)
except:
    PDFbyte = None
    profile_img = None

# -------------------------
# CSS CORPORATIVO
# -------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@600;700&display=swap');
    :root { --primary:#005b96; --secondary:#008b8b; }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .name { font-family: 'Playfair Display', serif; font-size: 42px; color: var(--primary); margin: 0; }
    .card { background: #f9fafb; border-radius: 12px; padding: 20px; border: 1px solid #d1d5db; margin-bottom: 15px; }
    .btn-primary { background: #005b96; color: white !important; padding: 10px 18px; border-radius: 10px; text-decoration: none; font-weight: 600; display: inline-block; }
    </style>
    """, unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------
hero_col1, hero_col2 = st.columns([1.1, 2.2], gap="medium")
with hero_col1:
    if profile_img:
        st.image(profile_img, width=230)

with hero_col2:
    st.markdown(f'<h1 class="name">{NAME}</h1>', unsafe_allow_html=True)
    st.markdown(f'<div style="color:var(--secondary); font-weight:600; font-size:18px; margin-bottom:10px;">{TAGLINE}</div>', unsafe_allow_html=True)
    st.markdown(f"📍 Lima, Perú | 📞 901 439 762 | ✉️ {EMAIL}")
    
    st.markdown("""
    Ingeniero con sólida formación en **arquitectura de datos y automatización**. 
    Especialista en transformar tareas manuales en **pipelines automatizados** con Python y SQL Cloud.
    """)

    # TYPEWRITER (CORREGIDO)
    words_list = ["Python", "SQL Cloud", "Azure", "T-SQL", "ETL Pipelines", "Stored Procedures"]
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

    btns = st.columns([1.2, 1, 1.5])
    with btns[0]:
        if PDFbyte:
            st.download_button("📄 Descargar CV Técnico", PDFbyte, "CV_SergioCarbajal.pdf", "application/pdf")
    with btns[1]:
        st.markdown(f'<a class="btn-primary" href="mailto:{EMAIL}">✉️ Contactar</a>', unsafe_allow_html=True)

# -------------------------
# MÉTRICAS DE IMPACTO (DATOS DEL CV)
# -------------------------
st.markdown("### 📊 Impacto de Ingeniería")
m1, m2, m3 = st.columns(3)
m1.metric("Optimización Tiempo", "88%", "De 3h a 20min")
m2.metric("Integridad Datos", "95%", "Menos duplicidad")
m3.metric("Eficiencia Campo", "70%", "vía Power Apps")

# -------------------------
# EXPERIENCIA PROFESIONAL
# -------------------------
st.markdown("### 💼 Trayectoria Técnica")
col_a, col_b = st.columns([2, 1], gap="large")

with col_a:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    exp1, exp2 = st.tabs(["🚀 Visiva", "⚙️ Credigama"])
    
    with exp1:
        st.markdown("**Data & Automation Developer** | `05/2025 – 11/2025`")
        st.markdown("- **Automatización:** Scripts en Python para procesamiento masivo, optimizando tiempos de **3 horas a 20 minutos**.")
        st.markdown("- **Infraestructura:** Lideré migración a **SQL Cloud**, asegurando integridad y disponibilidad.")
        st.markdown("- **Open Source:** Implementé soluciones escalables sin costos de licenciamiento.")
    
    with exp2:
        st.markdown("**Arquitectura de Datos & Automatización** | `02/2022 – 04/2024`")
        st.markdown("- **Azure Cloud:** Diseñé infraestructura en **SQL DB & Blob Storage**, migrando el 100% de registros físicos.")
        st.markdown("- **Lógica SQL:** Programación de **Stored Procedures y Views** en T-SQL, eliminando duplicidad en un 95%.")
        st.markdown("- **BI Automático:** Ecosistema Power BI con modelado directo a BD y latencia cero.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🛠 Stack Tecnológico")
    st.write("**Avanzado:** SQL, Python, VS Code")
    st.write("**Intermedio:** Azure, GitHub")
    st.progress(95, text="Python & SQL")
    st.progress(75, text="Azure Infrastructure")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# PROYECTOS Y FORMACIÓN
# -------------------------
st.markdown("---")
p_col, e_col = st.columns(2)

with p_col:
    st.subheader("🚀 Proyectos Destacados")
    st.info("**Gestión de Venta de Lotes**\n\nStreamlit + SQL Cloud para automatización de inventario.")
    st.info("**Sistema Analítico de Accidentes**\n\nDashboard interactivo procesando datos históricos de Perú.")

with e_col:
    st.subheader("🎓 Formación")
    st.markdown("- **Ingeniería Empresarial** (Egresado 2025) - UPN")
    st.markdown("- **Supply Chain Analytics** con Python")
    st.markdown("- **Análisis y Visualización de Datos**")

st.markdown(f"<center style='color:grey; font-size:14px; padding:20px;'>© 2026 {NAME} | Ingeniero de Datos</center>", unsafe_allow_html=True)
