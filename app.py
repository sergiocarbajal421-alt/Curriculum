from pathlib import Path
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import requests

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV_SergioCarbajal.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portafolio | Sergio Carbajal"
PAGE_ICON = "👋"
NAME = "Sergio Carbajal"
DESCRIPTION = "Especialista en Python y Business Intelligence. Transformo datos en decisiones estratégicas a través de análisis, automatización de procesos y dashboards interactivos."
EMAIL = "SergioCarbajal421@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sergiocarbajal/",
    "GitHub": "https://github.com/sergiocarbajal421-alt",
}

PROJECTS = {
    "Gestión de Venta de Lotes": {
        "desc": "Streamlit + SQL Cloud para automatización de ventas de lotes.",
        "link": "https://github.com/sergiocarbajal421-alt/GestionVentaLotes",
        "img": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        "tech": ["Python", "SQL", "Streamlit"],
    },
    "Dashboards Comerciales": {
        "desc": "Dashboards interactivos con Python y Streamlit para monitoreo comercial.",
        "link": "#",
        "img": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        "tech": ["Python", "Streamlit"],
    },
    "Automatización de Procesos": {
        "desc": "Scripts en Python para automatización de procesos repetitivos.",
        "link": "#",
        "img": "https://cdn-icons-png.flaticon.com/512/876/876232.png",
        "tech": ["Python"],
    },
}

# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- LOAD FILES ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- CUSTOM CSS ---
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');
* {font-family: 'Readex Pro';}

body {background-color: #FFFFFF; color: #1D1D1D;}  
h1, h2, h3, h4 {color: #1D3557;}                   
p, li {color: #1D1D1D; font-size:16px;}            
a {text-decoration: none; color: #E63946; font-weight: 600;}  
a:hover {color: #D62828; text-decoration: underline;}

.stProgress > div > div > div > div {background-color: #E63946; border-radius:10px;}
.stDownloadButton button {background-color:#E63946; color:#FFFFFF; font-weight:600; border-radius:10px;}
.stDownloadButton button:hover {background-color:#D62828; color:#FFFFFF; transition:0.3s;}

hr {border: 1px solid #E63946; margin: 20px 0; border-radius:5px;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.project-card {background:#F1FAEE; padding:15px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); margin-bottom:15px; display:flex; align-items:center;}
.project-card img {margin-right:20px; border-radius:10px;}
.skill-card {background:#E9ECEF; padding:10px; border-radius:10px; margin-bottom:10px; display:flex; align-items:center;}
.skill-card img {margin-right:15px;}
</style>
""",
    unsafe_allow_html=True,
)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="medium")
with col1:
    st.image(profile_pic, width=250)
with col2:
    st.title(NAME)
    st.subheader(DESCRIPTION)
    st.download_button(
        label="📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"[{platform}]({link})", unsafe_allow_html=True)

# --- TABS: EXPERIENCE, PROJECTS, SKILLS, CONTACT ---
tab1, tab2, tab3, tab4 = st.tabs(
    ["Experiencia", "Proyectos", "Habilidades", "Contacto"]
)

# --- EXPERIENCIA ---
with tab1:
    st.subheader("Experiencia Profesional")
    timeline = [
        {
            "title": "Auxiliar Data Analyst Comercial",
            "company": "Grupo Educativo Visiva",
            "period": "05/2025 – Actualidad",
            "details": [
                "🚀 Automatización de bases de clientes para campañas comerciales con Python, reduciendo tiempos de 3h a 20min.",
                "📊 Dashboards interactivos con Python, Matplotlib, Seaborn y Streamlit.",
                "🗄️ Implementación de SQL Cloud para centralizar bases de datos.",
                "💻 Uso de tecnologías open source para desarrollos escalables.",
            ],
        },
        {
            "title": "Analista de Datos",
            "company": "Apu Runa",
            "period": "02/2025 – 04/2025",
            "details": [
                "📈 Análisis estadístico con Python para estimar consumo de combustible.",
                "🗃️ Administración de Bases de Datos SQL Server.",
                "📊 Dashboards en Power BI para decisiones estratégicas.",
                "👥 Capacitación del personal en el uso de dashboards.",
            ],
        },
    ]
    for item in timeline:
        st.markdown(f"### {item['title']} | {item['company']} ({item['period']})")
        for detail in item["details"]:
            st.write(f"- {detail}")
        st.markdown("---")

# --- PROYECTOS ---
with tab2:
    st.subheader("Proyectos Destacados")
    for project, data in PROJECTS.items():
        st.markdown(
            f"""
<div class='project-card'>
<img src='{data["img"]}' width='60'/>
<div>
<h4>{project}</h4>
<p>{data["desc"]}</p>
<p>Tecnologías: {' '.join(data['tech'])}</p>
<a href='{data["link"]}' target='_blank'>Ver proyecto</a>
</div>
</div>
""",
            unsafe_allow_html=True,
        )

# --- HABILIDADES ---
with tab3:
    st.subheader("Habilidades")
    skills = {
        "Python": {
            "level": 95,
            "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        },
        "SQL": {
            "level": 90,
            "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg",
        },
        "Visual Studio Code": {
            "level": 85,
            "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg",
        },
        "Excel": {
            "level": 75,
            "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoft/microsoft-original.svg",
        },
        "Git/GitHub": {
            "level": 80,
            "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg",
        },
        "Power BI": {
            "level": 60,
            "icon": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Power_BI_Logo.png",
        },
        "Streamlit": {
            "level": 85,
            "icon": "https://streamlit.io/images/brand/streamlit-mark-color.svg",
        },
    }
    for skill, info in skills.items():
        col1, col2 = st.columns([1, 6])
        with col1:
            st.image(info["icon"], width=30)
        with col2:
            st.markdown(
                f"<div class='skill-card'><strong>{skill}</strong></div>",
                unsafe_allow_html=True,
            )
            st.progress(info["level"])

# --- CONTACTO ---
with tab4:
    st.subheader("Contacto")
    with st.form("contact_form"):
        name = st.text_input("Nombre")
        email = st.text_input("Email")
        message = st.text_area("Mensaje")
        submitted = st.form_submit_button("Enviar")
        if submitted:
            st.success("¡Mensaje enviado! Te responderé pronto.")

# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#1D3557;'>\"Transformando datos complejos en decisiones estratégicas, línea de Python a la vez.\"</p>",
    unsafe_allow_html=True,
)
