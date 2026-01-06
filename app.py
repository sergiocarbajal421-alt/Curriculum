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
# METADATOS ACTUALIZADOS SEGÚN CV
# -------------------------
PAGE_TITLE = "Portafolio | Sergio Carbajal - Data & Automation Engineer"
PAGE_ICON = "⚙️"
NAME = "Sergio Carbajal"
EMAIL = "SergioCarbajal421@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sergiocarbajalromero/",
    "GitHub": "https://github.com/sergiocarbajal421-alt",
}

PROJECTS = {
    "Aplicación Web para gestión de Lotes": {
        "desc": "Sistema Full-stack con Streamlit + SQL Cloud para automatización de inventario y trazabilidad de activos.",
        "link": "https://gestionventalotes.streamlit.app/",
        "img": "https://img.icons8.com/color/48/real-estate.png",
        "tech": ["Python", "SQL Cloud", "Streamlit", "Git/GitHub"],
    },
    "Sistema Analítico de Accidentes – Perú": {
        "desc": "Pipeline de datos y Dashboard interactivo sobre accidentes de tránsito (2020-2021) con mapas de calor.",
        "link": "https://accidentestransito.streamlit.app/",
        "img": "https://img.icons8.com/color/96/traffic-light.png",
        "tech": ["Python", "Pandas", "Streamlit", "Visualización"],
    },
}

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------
# CARGA ARCHIVOS
# -------------------------
try:
    with open(resume_file, "rb") as f:
        PDFbyte = f.read()
    profile_img = Image.open(profile_pic)
except Exception as e:
    st.error(f"Error cargando recursos: {e}")
    PDFbyte = None
    profile_img = None

# -------------------------
# CSS CORPORATIVO (MANTENIDO)
# -------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
    :root {
        --primary:#005b96;
        --secondary:#008b8b;
        --text-dark:#1a1a1a;
        --text-medium:#374151;
        --text-light:#6b7280;
        --bg-light:#f8fafc;
    }
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: var(--text-dark); background-color: #ffffff; }
    .stApp { background-color: #ffffff; }
    .name { font-family: 'Playfair Display', serif; font-size: 42px; color: var(--primary); margin: 0; }
    .card { background: #f9fafb; border-radius: 12px; margin-bottom: 15px; padding: 18px; transition: all 0.25s ease; box-shadow: 0 1px 2px rgba(0,0,0,0.08); }
    .card:hover { transform: translateY(-4px); box-shadow: 0 6px 16px rgba(0,0,0,0.12); }
    .project-card { display:flex; gap:16px; align-items:center; }
    .project-card img { width:58px; height:58px; border-radius:10px; object-fit:cover; }
    .footer { color: var(--text-light); text-align:center; padding:20px 0 40px 0; font-size:14px; }
    .btn-primary { background: #005b96; color: #ffffff !important; padding: 10px 18px; border-radius: 10px; font-weight: 600; text-decoration: none; display: inline-block; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# HERO SECTION
# -------------------------
hero_col1, hero_col2 = st.columns([1.1, 2.2], gap="medium")
with hero_col1:
    if profile_img:
        st.image(profile_img, width=250)

with hero_col2:
    st.markdown(f'<h1 class="name">{NAME}</h1>', unsafe_allow_html=True)
    st.markdown(
        f"""
    <div style="margin-top:5px; font-size:18px; font-weight:600; color:var(--secondary);">
        Ingeniero Empresarial | Data & Automation Engineer
    </div>
    <div style="margin-top:10px;font-size:14px;color:#374151;">
        📍 Lima, Perú | 📞 +51 901 439 762 | ✉️ {EMAIL}
    </div>
    <div style="margin-top:15px; line-height:1.6;">
        Ingeniero con sólida formación en <b>arquitectura de datos y automatización</b>. 
        Especialista en transformar tareas manuales ineficientes en <b>pipelines de datos automatizados</b> utilizando Python y SQL Cloud.
        Enfocado en soluciones escalables y medición de operaciones críticas.
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Typewriter con Stack Técnico del CV
    words = ["Python", "SQL Cloud", "Azure", "T-SQL", "ETL Pipelines", "Automation", "Stored Procedures"]
    text_typewriter = " - ".join(words)

    components.html(
        f"""
        <div style="font-size:18px; color:#374151; margin-top:8px; font-weight:500; font-family:'Inter', sans-serif;">
            <span id="typewriter"></span>
        </div>
        <script>
        const text = "{text_typewriter}";
        let i = 0;
        const typeWriter = () => {{
            const el = document.getElementById('typewriter');
            if (i <= text.length) {{
                el.innerHTML = text.substring(0, i);
                i++;
                setTimeout(typeWriter, 100);
            }} else {{
                setTimeout(() => {{ i = 0; typeWriter(); }}, 3000);
            }}
        }};
        typeWriter();
        </script>
        """,
        height=50,
    )

    btns = st.columns([1.2, 1, 1.5])
    with btns[0]:
        if PDFbyte:
            st.download_button(label="📄 Descargar CV Técnico", data=PDFbyte, file_name="CV_SergioCarbajal_Engineer.pdf", mime="application/pdf")
    with btns[1]:
        st.markdown(f'<a class="btn-primary" href="mailto:{EMAIL}">✉️ Contactar</a>', unsafe_allow_html=True)
    with btns[2]:
        sm_html = '<div class="social-links" style="margin-top:10px;">'
        for name, link in SOCIAL_MEDIA.items():
            sm_html += f'<a href="{link}" target="_blank" style="margin-right:15px; color:#005b96; font-weight:600; text-decoration:none;">{name}</a>'
        st.markdown(sm_html + '</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# INDICADORES (MÉTRICAS ANIMADAS)
# -------------------------
# Datos calculados según el nuevo CV
components.html(
    """
    <style>
    .stats-wrap { display: flex; gap: 20px; justify-content: flex-start; flex-wrap: wrap; font-family: 'Inter', sans-serif; }
    .stat-card { flex: 1; min-width: 220px; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 14px; padding: 18px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
    .stat-icon { background: linear-gradient(135deg, #008b8b, #005b96); color: #fff; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 10px; font-weight: 700; }
    .stat-title { font-weight: 600; color: #0f172a; font-size: 14px; }
    .stat-value { font-size: 20px; font-weight: 800; color: #005b96; }
    </style>
    <div class="stats-wrap">
        <div class="stat-card">
            <div><div class="stat-title">Optimización Tiempo</div><div style="font-size:11px; color:#6b7280;">Procesos masivos</div></div>
            <div class="stat-value" data-target="88">0</div><div class="stat-value">%</div>
        </div>
        <div class="stat-card">
            <div><div class="stat-title">Digitalización Cloud</div><div style="font-size:11px; color:#6b7280;">Registros físicos a Azure</div></div>
            <div class="stat-value" data-target="100">0</div><div class="stat-value">%</div>
        </div>
        <div class="stat-card">
            <div><div class="stat-title">Integridad de Datos</div><div style="font-size:11px; color:#6b7280;">Reducción de duplicidad</div></div>
            <div class="stat-value" data-target="95">0</div><div class="stat-value">%</div>
        </div>
    </div>
    <script>
    const counters = document.querySelectorAll('.stat-value[data-target]');
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            if (count < target) {
                counter.innerText = Math.ceil(count + (target/50));
                setTimeout(updateCount, 30);
            } else { counter.innerText = target; }
        };
        updateCount();
    });
    </script>
    """,
    height=100,
)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# EXPERIENCIA Y PROYECTOS (ACTUALIZADO CON CV)
# -------------------------
col_a, col_b = st.columns([2.2, 1.2], gap="large")

with col_a:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💼 Experiencia Técnica en Ingeniería")
    
    tab_exp1, tab_exp2 = st.tabs(["🚀 Visiva (Actualidad)", "⚙️ Credigama (Consultoría)"])

    with tab_exp1:
        st.markdown("**Data & Automation Developer** | Grupo Educativo Visiva")
        st.markdown("`Mayo 2025 – Noviembre 2025`")
        st.markdown("- **Ingeniería de Automatización:** Procesamiento masivo con Python, optimizando tiempos de **3 horas a 20 minutos**.")
        st.markdown("- **Desarrollo Analítico:** Dashboards interactivos web para monitoreo operativo en tiempo real.")
        st.markdown("- **Infraestructura:** Migración estratégica a **SQL Cloud**, garantizando integridad y disponibilidad.")
        st.markdown("- **Open Source:** Soluciones escalables sin costos adicionales de licenciamiento.")

    with tab_exp2:
        st.markdown("**Arquitectura de Datos & Automatización** | Grupo Credigama")
        st.markdown("`Febrero 2022 – Abril 2024`")
        st.markdown("- **Arquitectura Cloud:** Diseño e implementación en **Azure (SQL DB & Blob Storage)**, digitalizando el 100% de registros físicos.")
        st.markdown("- **Lógica de Servidor:** Programación de **Stored Procedures y Views** en T-SQL, eliminando duplicidad en un 95%.")
        st.markdown("- **Desarrollo App-to-Cloud:** Aplicaciones en Power Apps con registro en campo reducido en un 70%.")
        st.markdown("- **BI Automático:** Ecosistema Power BI con modelado directo a BD y latencia cero.")
        
    st.markdown("</div>", unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚀 Proyectos de Ingeniería")
    for project, data in PROJECTS.items():
        st.markdown(f"""
        <div class="project-card">
            <img src="{data['img']}" alt="icon"/>
            <div>
                <div style="font-weight:700; color:var(--primary); font-size:14px;">{project}</div>
                <div style="color:var(--text-medium); font-size:12px; margin-top:4px;">{data['desc']}</div>
                <div style="margin-top:6px;"><a href="{data['link']}" target="_blank" style="color:var(--secondary); font-weight:700; text-decoration:none; font-size:12px;">Ver Pipeline →</a></div>
            </div>
        </div>
        <hr style="border:0; border-top:1px solid #e5e7eb; margin:10px 0;">
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# EDUCACIÓN / FORMACIÓN
# -------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎓 Formación Profesional")
t1, t2 = st.tabs(["Grado Académico", "Especializaciones Técnicas"])

with t1:
    st.markdown("**Egresado de Ingeniería Empresarial**")
    st.markdown("_Universidad Privada del Norte (2025)_")
    st.markdown("- Enfoque en optimización de procesos y estrategia basada en datos.")

with t2:
    st.markdown("- **Especialización en Supply Chain Analytics con Python**")
    st.markdown("- **Especialización en Análisis y Visualización de Datos**")
    st.markdown("- Especialista en Machine Learning y Planeamiento Estratégico.")
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# STACK TÉCNICO (GRÁFICO)
# -------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🛠 Stack Tecnológico")
col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    st.markdown("**Avanzado**")
    st.progress(95, text="Python & SQL")
    st.progress(90, text="VS Code")
with col_s2:
    st.markdown("**Intermedio**")
    st.progress(75, text="Azure Infrastructure")
    st.progress(70, text="Git / GitHub")
with col_s3:
    st.markdown("**Herramientas BI**")
    st.progress(50, text="Power BI & Apps")
    st.progress(50, text="Excel Técnico")
st.markdown("</div>", unsafe_allow_html
