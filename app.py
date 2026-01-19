from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import smtplib
from email.mime.text import MIMEText
import requests
from io import BytesIO

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
NAME = "SERGIO CARBAJAL"
EMAIL = "SergioCarbajal421@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sergiocarbajalromero/",
    "GitHub": "https://github.com/sergiocarbajal421-alt",
}

PROJECTS = {
    "Gestión de Venta de Lotes": {
        "desc": "Streamlit + SQL Cloud para automatización de inventario y trazabilidad técnica.",
        "link": "https://gestionventalotes.streamlit.app/",
        "img": "https://img.icons8.com/color/48/real-estate.png",
        "tech": ["Python", "SQL Cloud", "Streamlit", "Git/GitHub"],
    },
    "Sistema Analítico de Accidentes de Tránsito – Perú 2020–2021": {
        "desc": "Dashboard analítico procesando datos históricos para identificación de patrones de riesgo.",
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
# CARGA ARCHIVOS (OPTIMIZADO)
# -------------------------
FILE_ID = "1xukRqxU079e7S7hYEMHltVuEp8w8WzHz"
# Añadimos confirm=t para saltar verificaciones manuales de Google
DIRECT_URL = f"https://docs.google.com/uc?export=download&id={FILE_ID}&confirm=t"

@st.cache_data(show_spinner="Sincronizando con Azure SQL & Drive...")
def get_pdf_data(url):
    try:
        # User-Agent para evitar ser bloqueados como "Scrapers" simples
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=15)
        
        # Validación de integridad: Verificamos el 'Magic Number' del PDF
        if response.status_code == 200 and b"%PDF" in response.content[:4]:
            return response.content
        else:
            # Si Google devuelve un HTML de error, esto lo detectará
            return None
    except Exception as e:
        st.error(f"Error de infraestructura: {e}")
        return None

PDFbyte = get_pdf_data(DIRECT_URL)


# -------------------------
# CSS CORPORATIVO MODERNO
# -------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

    :root {
        --primary:#005b96; /* azul petróleo */
        --secondary:#008b8b; /* teal */
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

    /* HERO */
    .hero {
        background: var(--bg-light);
        border-radius: 18px;
        padding: 24px;
        border: 1px solid var(--border);
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    }
    .name {
        font-family: 'Playfair Display', serif;
        font-size: 36px;
        color: var(--primary);
        margin: 0;
    }
    .description {
        color: var(--text-medium);
        font-size: 16px;
        margin-top: 8px;
        margin-bottom: 14px;
    }

    /* Social links */
    .social-links a {
        margin-right: 14px;
        color: var(--primary);
        font-weight: 600;
        text-decoration: none;
    }
    .social-links a:hover {
        color: var(--secondary);
    }

    /* Cards */
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

    /* Proyectos */
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
    .project-card div {
        color: var(--text-dark);
    }

    /* Skills */
    .skill-row {
        display:flex;
        align-items:center;
        gap:12px;
    }
    .skill-name {
        min-width:140px;
        font-weight:700;
        color: var(--text-dark);
    }

    /* Footer */
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
    st.markdown("</div>", unsafe_allow_html=True)

with hero_col2:
    st.markdown(f'<h1 class="name">{NAME}</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:var(--secondary); font-weight:600; font-size:18px;">Ingeniero Empresarial | Data & Automation Engineer</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
    <div style="margin-top:10px;font-size:14px;color:#374151;">
        📍 Comas, Lima | 📞 +51 901 439 762 | ✉️ {EMAIL}
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    Ingeniero con sólida formación en <b>arquitectura de datos, automatización de procesos y optimización operativa</b>. 
    Especialista en transformar tareas manuales ineficientes en <b>pipelines de datos automatizados</b> utilizando Python y SQL Cloud.
    """,
        unsafe_allow_html=True,
    )
    
    words = [
        "Python", "SQL DB", "Azure","Blob Storage","VS Code" ,"Virtual Environment",
        "ETL Pipelines", "Git/GitHub", "Automation",
        "Business Intelligence", "Supply Chain Analytics", "Cloud Computing",
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
        const speed = 100; // velocidad de cada letra

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
                }}, 2000); // espera 2s y reinicia
            }}
        }};
        typeWriter();
        </script>
        """,
        height=50,
    )

    btns = st.columns([1, 1, 1])
    with btns[0]:
        if PDFbyte:
            st.download_button(
                label="📄 Descargar CV",
                data=PDFbyte,
                file_name="CV_Sergio_Carbajal.pdf",
                mime="application/pdf",
            )
        else:
            st.error("Archivo no disponible")
            
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
    st.markdown("</div>", unsafe_allow_html=True)

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
                <div class="stat-icon">O</div>
                <div><div style="font-weight:600;">Optimización</div><div style="color:#6b7280; font-size:12px;">Reducción tiempo</div></div>
            </div>
            <div class="stat-value" data-target="88">0</div><div style="font-size: 22px; font-weight: 800; margin-left:-40px;">%</div>
        </div>
        <div class="stat-card">
            <div style="display:flex; align-items:center; gap:14px;">
                <div class="stat-icon">I</div>
                <div><div style="font-weight:600;">Integridad</div><div style="color:#6b7280; font-size:12px;">Menos duplicidad</div></div>
            </div>
            <div class="stat-value" data-target="95">0</div><div style="font-size: 22px; font-weight: 800; margin-left:-40px;">%</div>
        </div>
        <div class="stat-card">
            <div style="display:flex; align-items:center; gap:14px;">
                <div class="stat-icon">E</div>
                <div><div style="font-weight:600;">Eficiencia</div><div style="color:#6b7280; font-size:12px;">Registro en campo</div></div>
            </div>
            <div class="stat-value" data-target="70">0</div><div style="font-size: 22px; font-weight: 800; margin-left:-40px;">%</div>
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
            "title": "Data & Automation Developer",
            "company": "Grupo Educativo Visiva",
            "period": "05/2025 – 11/2025",
            "details": [
                "**Ingeniería de Automatización:** Diseñé y ejecuté scripts en Python para el procesamiento masivo de 10 millones de registros, optimizando el tiempo de ejecución de 3 horas a solo 10 minutos.",
                "**Desarrollo de Software Analítico:** Creé dashboards interactivos web (Python), facilitando el monitoreo de métricas operativas en tiempo real.",
                "**Infraestructura de Datos:** Lideré la migración y centralización de bases de datos hacia SQL Cloud, asegurando la integridad y disponibilidad de la información.",
                "**Optimización de Recursos:** Implementé soluciones basadas en tecnologías open source, logrando desarrollos escalables sin costos adicionales de licenciamiento."
            ],
        },
        {
            "title": "Arquitectura de Datos & Automatización",
            "company": "Grupo Credigama",
            "period": "01/2023 – Actualidad",
            "details": [
                "**Arquitectura Cloud:** Diseñé e implementé la infraestructura en Azure (SQL DB & Blob Storage), migrando el 100% de registros físicos a un entorno relacional.",
                "**Modelado y Lógica:** Programé Stored Procedures y Views en T-SQL, optimizando la integridad de datos y eliminando errores de duplicidad en un 95%.",
                "**Desarrollo App-to-Cloud:** Creé aplicaciones en Power Apps conectadas en tiempo real, reduciendo el tiempo de registro en campo en un 70%.",
                "**BI Automático:** Desarrollé el ecosistema en Power BI con modelado directo a la base de datos, logrando visualización de KPIs con latencia cero.",
                "**Sostenibilidad Técnica:** Brindo consultoría y soporte continuo a la arquitectura desplegada, asegurando la escalabilidad y disponibilidad del ecosistema de datos."
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
st.markdown("**Ingeniería Empresarial** | Universidad Privada del Norte | `Egresado 2025` ")
st.markdown("- Especialización en **Supply Chain Analytics con Python**")
st.markdown("- Especialización en **Análisis y Visualización de Datos**")
st.markdown("---")
st.subheader("🛠 Habilidades Técnicas")
skills_dict = {
    "SQL (T-SQL)": 95, 
    "Python": 95, 
    "Azure Cloud": 75, 
    "Git/GitHub": 75, 
    "VS Code": 80, 
    "Power BI": 70, 
    "Excel": 70
}
skill_cols = st.columns(4)
for i, (skill, val) in enumerate(skills_dict.items()):
    with skill_cols[i % 4]:
        st.write(f"**{skill}**")
        st.progress(val)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown('<div class="footer">© 2026 Sergio Carbajal — Data & Automation Engineer</div>', unsafe_allow_html=True)








