from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText

# -------------------------
# PATH SETTINGS
# -------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "CV_SergioCarbajal.pdf"
profile_pic = current_dir / "profile-pic.png"

# -------------------------
# METADATOS ACTUALIZADOS
# -------------------------
PAGE_TITLE = "Portafolio | Sergio Carbajal - Data & Automation Engineer"
PAGE_ICON = "⚙️"
NAME = "Sergio Carbajal"
EMAIL = "SergioCarbajal421@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sergiocarbajal/",
    "GitHub": "https://github.com/sergiocarbajal421-alt",
}

# -------------------------
# CONFIGURACIÓN DE PÁGINA
# -------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# -------------------------
# CSS AVANZADO (DISEÑO INDUSTRIAL/TECNOLÓGICO)
# -------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono&display=swap');
    
    :root {
        --primary: #005b96;
        --secondary: #008b8b;
        --dark: #0f172a;
    }

    /* Contenedores de tarjetas con efecto de elevación */
    .card {
        background: #ffffff;
        border-radius: 15px;
        padding: 25px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .card:hover { transform: translateY(-5px); border-color: var(--secondary); }
    
    .name-text { font-size: 48px; font-weight: 800; color: var(--primary); margin-bottom: 0px; }
    .tagline { font-size: 22px; color: var(--secondary); font-weight: 600; font-family: 'JetBrains Mono', monospace; }
    
    /* Estilo de botones */
    .stButton>button {
        border-radius: 10px;
        background-color: var(--primary);
        color: white;
        font-weight: 600;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# -------------------------
# HERO SECTION (CON INTERACTIVIDAD)
# -------------------------
h_col1, h_col2 = st.columns([1, 2], gap="large")

with h_col1:
    if profile_pic.exists():
        st.image(Image.open(profile_pic), width=280)

with h_col2:
    st.markdown(f'<h1 class="name-text">{NAME}</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Data & Automation Engineer</p>', unsafe_allow_html=True)
    
    # Efecto Typewriter actualizado con tu nuevo Stack [cite: 54, 55]
    words = ["Python", "SQL Cloud", "Azure", "ETL Pipelines", "Automation", "Stored Procedures"]
    text_to_type = " - ".join(words)
    
    components.html(f"""
        <div style="font-family:'JetBrains Mono',monospace; font-size:18px; color:#475569;">
            <span id="typewriter"></span><span style="border-right:2px solid var(--secondary); animation: blink 0.7s infinite;"></span>
        </div>
        <script>
            const text = "{text_to_type}";
            let i = 0;
            function type() {{
                if (i < text.length) {{
                    document.getElementById('typewriter').innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, 80);
                }}
            }}
            type();
        </script>
        <style> @keyframes blink {{ 50% {{ opacity: 0; }} }} </style>
    """, height=40)

    st.markdown(f"""
    **Ingeniero Empresarial** especializado en la arquitectura de sistemas de datos y optimización de procesos críticos[cite: 33, 37]. 
    Experto en digitalización *end-to-end*, migrando operaciones manuales a infraestructuras en la nube con un enfoque en escalabilidad[cite: 38, 46].
    """)
    
    st.write(f"📍 Lima, Perú | 📞 +51 901 439 762 | ✉️ {EMAIL}")

# -------------------------
# INDICADORES DE IMPACTO (MÉTRICAS)
# -------------------------
st.markdown("### 📊 Impacto de Ingeniería")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Optimización de Procesos", "88%", "De 3h a 20min") [cite: 41]
m2.metric("Digitalización Operativa", "100%", "Papel ➔ Azure") [cite: 46]
m3.metric("Eficiencia en Campo", "70%", "vía Power Apps") [cite: 48]
m4.metric("Integridad de Datos", "95%", "Menos duplicidad") [cite: 47]

# -------------------------
# CUERPO PRINCIPAL
# -------------------------
c_main, c_side = st.columns([2, 1], gap="large")

with c_main:
    st.subheader("🛠 Experiencia Técnica")
    
    # VISIVA [cite: 40, 41, 42, 43, 44]
    with st.expander("🚀 Data & Automation Developer | Grupo Educativo Visiva", expanded=True):
        st.markdown("""
        - **Automatización de Alto Impacto:** Reducción de tiempos de procesamiento de **3 horas a 20 minutos** mediante scripts avanzados en Python[cite: 41].
        - **Arquitectura de Datos:** Lideré la migración estratégica hacia **SQL Cloud**, asegurando la disponibilidad total de activos de información[cite: 43].
        - **Dashboards de Ingeniería:** Desarrollo de visualizaciones en tiempo real para el monitoreo de métricas críticas[cite: 42].
        """)

    # CREDIGAMA [cite: 45, 46, 47, 48, 49]
    with st.expander("⚙️ Arquitectura de Datos & Automatización | Grupo Credigama"):
        st.markdown("""
        - **Despliegue Cloud:** Diseño e implementación de infraestructura en **Azure (SQL DB & Blob Storage)** para la digitalización del 100% de registros físicos[cite: 46].
        - **Lógica de Servidor:** Programación de **Stored Procedures y Views** en T-SQL para garantizar la integridad referencial de los datos[cite: 47].
        - **Ecosistema App-to-Cloud:** Implementación de Power Apps integradas a la base de datos para gestión de cobranza en tiempo real[cite: 48].
        """)

with c_side:
    st.subheader("⚙️ Stack Tecnológico")
    # Barras de habilidades interactivas [cite: 54, 55, 56]
    skills = {"Python (Automation)": 95, "SQL (T-SQL)": 90, "Azure Infrastructure": 75, "ETL / Pipelines": 80}
    for s, v in skills.items():
        st.write(f"{s}")
        st.progress(v)

# -------------------------
# CIERRE Y CONTACTO
# -------------------------
st.markdown("---")
st.subheader("🚀 Proyectos Destacados")
p1, p2 = st.columns(2)
with p1:
    st.info("**Gestión de Venta de Lotes**")
    st.write("Aplicación Full-stack para control de inventario y trazabilidad técnica de activos[cite: 60].")
with p2:
    st.info("**Sistema Analítico de Accidentes**")
    st.write("Pipeline de datos procesando registros históricos para análisis de patrones de riesgo[cite: 59].")

# Footer corporativo
st.markdown(f"<center style='color:#64748b;'>© 2025 {NAME} | Ingeniero de Datos | Construyendo el futuro de la automatización</center>", unsafe_allow_html=True)
