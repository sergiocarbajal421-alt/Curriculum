
from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText

# -------------------------
# PATH SETTINGS (MISMO NIVEL)
# -------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "CV_SergioCarbajal.pdf"
profile_pic = current_dir / "profile-pic.png"

# -------------------------
# METADATOS
# -------------------------
PAGE_TITLE = "Portafolio | Sergio Carbajal"
PAGE_ICON = "💼"
NAME = "Sergio Carbajal"
EMAIL = "SergioCarbajal421@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sergiocarbajal/",
    "GitHub": "https://github.com/sergiocarbajal421-alt",
}

PROJECTS = {
    "Gestión de Venta de Lotes": {
        "desc": "Streamlit + SQL Cloud para automatización de ventas de lotes.",
        "link": "https://gestionventalotes.streamlit.app/",
        "img": "https://img.icons8.com/color/48/real-estate.png",
        "tech": ["Python", "SQL", "Streamlit", "Git/GitHub", "VS Code"],
    },
    "Sistema Analítico de Accidentes de Tránsito – Perú 2020–2021": {
        "desc": "Dashboard analítico con visualizaciones y mapas sobre accidentes de tránsito en Perú.",
        "link": "https://accidentestransito.streamlit.app/",
        "img": "https://img.icons8.com/color/96/traffic-light.png",
        "tech": ["Python", "Streamlit", "Git/GitHub", "VS Code"],
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
with open(resume_file, "rb") as f:
    PDFbyte = f.read()
profile_img = Image.open(profile_pic)

# -------------------------
# CSS CORPORATIVO MODERNO
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
        --card-bg:#ffffff;
        --border:#d1d5db;
        --bg-light:#f8fafc;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text-dark);
        background-color: #ffffff;
    }

    .stApp {
        background-color: #ffffff;
    }

    .card {
        background: #f9fafb;
        border-radius: 12px;
        margin-bottom: 15px;
        padding: 18px;
        transition: all 0.25s ease;
        box-shadow: 0 1px 2px rgba(0,0,0,0.08);
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    }
    .skill-row {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .skill-name {
        font-weight: 600;
        color: #333;
        width: 140px;
    }

    .project-card {
        display:flex;
        gap:16px;
        align-items:center;
    }
    .project-card img {
        width:58px;
        height:58px;
        border-radius:10px;
        object-fit:cover;
    }

    .footer {
        color: var(--text-light);
        text-align:center;
        padding:20px 0 40px 0;
        font-size:14px;
    }

    @media (max-width:768px){
        .name { font-size:28px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# HERO
# -------------------------
hero_col1, hero_col2 = st.columns([1.1, 2.2], gap="medium")
with hero_col1:
    st.image(profile_img, width=230)

with hero_col2:
    st.markdown(f'<h1 class="name">{NAME}</h1>', unsafe_allow_html=True)
    st.markdown(
        f"""
    <div style="margin-top:10px;font-size:14px;color:#374151;">
        📍 Perú - Lima - Comas | 📞 +51 901 439 762 | ✉️ {EMAIL}
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    Especialista en <b>Business Intelligence</b>, poseo habilidades destacadas en <b>Estadística, Matemática, Programación y Estrategia Empresarial</b>. 
    Amplia experiencia en Análisis de Datos y gestión estratégica, impulsando la medición de operaciones y la toma de decisiones oportunas basadas en datos.
    """,
        unsafe_allow_html=True,
    )
    
    words = [
        "Python", "Pandas", "NumPy", "Matplotlib", "SQL",
        "Git/GitHub", "Cloud Computing", "Power BI", "Excel",
        "Dashboards", "Automatización", "Big Data", "Machine Learning", "KPI",
    ]
    text = " - ".join(words)

    components.html(
        f"""
        <div style="font-size:18px;color:#374151;margin-top:8px;font-weight:500;">
            <span id="typewriter"></span>
        </div>

        <script>
        const text = "{text}";
        let i = 0;
        const speed = 100;

        const typeWriter = () => {{
            const el = document.getElementById('typewriter');
            if (i <= text.length) {{
                el.innerHTML = text.substring(0, i);
                i++;
                setTimeout(typeWriter, speed);
            }} else {{
                setTimeout(() => {{
                    i = 0;
                    el.innerHTML = '';
                    typeWriter();
                }}, 2000);
            }}
        }};
        typeWriter();
        </script>
        """,
        height=50,
    )

    btns = st.columns([1, 1, 1])
    with btns[0]:
        st.download_button(
            label="📄 Descargar CV",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/pdf",
        )
    with btns[1]:
        st.markdown(
            f"""
    <a class="btn-primary" href="mailto:{EMAIL}?subject=Contacto%20desde%20portafolio">
        ✉️ Contactar
    </a>
    <style>
    .btn-primary {{
        background: #005b96;
        color: #ffffff !important;
        padding: 10px 18px;
        border-radius: 10px;
        font-weight: 600;
        text-decoration: none;
        transition: 0.3s ease;
    }}
    .btn-primary:hover {{
        background: #008b8b;
    }}
    </style>
    """,
            unsafe_allow_html=True,
        )

    with btns[2]:
        sm_html = '<div class="social-links">'
        for name_sm, link_sm in SOCIAL_MEDIA.items():
            sm_html += f'<a href="{link_sm}" target="_blank" style="margin-right:14px; color:#005b96; font-weight:600; text-decoration:none;">{name_sm}</a>'
        sm_html += "</div>"
        st.markdown(sm_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# Quick stats
# -------------------------
components.html(
    """
    <style>
    .stats-wrap { display: flex; gap: 20px; justify-content: flex-start; flex-wrap: wrap; font-family: sans-serif; }
    .stat-card { flex: 1; min-width: 250px; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 14px; padding: 18px 22px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
    .stat-icon { background: linear-gradient(135deg, #008b8b, #005b96); color: #fff; width: 46px; height: 46px; display: flex; align-items: center; justify-content: center; border-radius: 12px; font-weight: 700; }
    .stat-value { font-size: 22px; font-weight: 800; color: #0f172a; }
    </style>

    <div class="stats-wrap">
        <div class="stat-card">
            <div style="display:flex; align-items:center; gap:14px;">
                <div class="stat-icon">P</div>
                <div><div style="font-weight:600;">Proyectos</div><div style="color:#6b7280; font-size:12px;">Entregados</div></div>
            </div>
            <div class="stat-value" data-target="12">0</div>
        </div>
        <div class="stat-card">
            <div style="display:flex; align-items:center; gap:14px;">
                <div class="stat-icon">H</div>
                <div><div style="font-weight:600;">Ahorro horas</div><div style="color:#6b7280; font-size:12px;">Mensual</div></div>
            </div>
            <div class="stat-value" data-target="120">0</div>
        </div>
    </div>

    <script>
    const counters = document.querySelectorAll('.stat-value');
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            if (count < target) {
                counter.innerText = Math.ceil(count + (target/100));
                setTimeout(updateCount, 20);
            } else { counter.innerText = target; }
        };
        updateCount();
    });
    </script>
    """,
    height=120,
)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# EXPERIENCIA Y PROYECTOS
# -------------------------
col_a, col_b = st.columns([2, 1], gap="large")

with col_a:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💼 Experiencia Profesional")
    timeline = [
        {
            "title": "Auxiliar Data Analyst Comercial",
            "company": "Grupo Educativo Visiva",
            "period": "05/2025 – Actualidad",
            "details": [
                "Automatice tareas operativas con Python, reduciendo tiempos de 3h a 20min.",
                "Desarrolle dashboards interactivos en Python para monitoreo en tiempo real.",
                "Implemente proyectos de SQL Cloud para centralizar bases de datos.",
                "Utilice tecnologías open source optimizando recursos sin costo adicional."
            ],
        },
        {
            "title": "Practicante de Análisis de Datos y Automatización",
            "company": "Grupo Credigama",
            "period": "02/2022 – 12/2022",
            "details": [
                "Desarrollé reportes interactivos en Power BI.",
                "Gestioné el entorno Azure y Microsoft 365.",
                "Desarrollé aplicaciones con Power Apps para automatización.",
                "Automatizé reportes en Excel mejorando la eficiencia."
            ],
        },
    ]
    tabs = st.tabs([item["title"] for item in timeline])
    for tab, item in zip(tabs, timeline):
        with tab:
            st.markdown(f"**{item['company']}** | `{item['period']}`")
            for detail in item["details"]:
                st.markdown(f"- {detail}")
    st.markdown("</div>", unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚀 Proyectos Destacados")
    for project, data in PROJECTS.items():
        st.markdown(f"""
        <div class="project-card">
            <img src="{data['img']}" alt="icon"/>
            <div>
                <div style="font-weight:700;color:var(--primary);">{project}</div>
                <div style="font-size:12px;color:var(--text-light);">{data['desc']}</div>
                <a href="{data['link']}" target="_blank" style="color:var(--secondary);font-size:12px;text-decoration:none;font-weight:700;">Ver proyecto →</a>
            </div>
        </div>
        <hr style="margin:10px 0; border:0; border-top:1px solid #eee;">
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# EDUCACIÓN / HABILIDADES
# -------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎓 Formación")
st.markdown("**Ingeniería Empresarial** | Universidad Privada del Norte | `2020 - 2025`")
st.markdown("---")
st.subheader("🛠 Habilidades")
skills_dict = {"Python": 99, "SQL": 90, "VS Code": 80, "Inglés": 80, "Git": 70, "Excel": 70, "Power BI": 50}
skill_cols = st.columns(4)
for i, (skill, val) in enumerate(skills_dict.items()):
    with skill_cols[i % 4]:
        st.write(f"**{skill}**")
        st.progress(val)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown('<div class="footer">© 2025 Sergio Carbajal — Data & Automation Engineer</div>', unsafe_allow_html=True)
