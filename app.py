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
    # ,
    # "Automatización de Procesos": {
    #     "desc": "Scripts en Python para automatización de procesos repetitivos.",
    #     "link": "",
    #     "img": "https://cdn-icons-png.flaticon.com/512/876/876232.png",
    #     "tech": ["Python"],
    # },
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
    # Después del components.html con typewriter
    st.markdown(
        """
    <div style="margin-top:10px;font-size:14px;color:#374151;">
        📍 Perú - Lima - Comas &nbsp;&nbsp; | &nbsp;&nbsp; 📞 +51 901 439 762 &nbsp;&nbsp; | &nbsp;&nbsp; ✉️ SergioCarbajal421@gmail.com
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    Especialista en <b>Business Intelligence</b>, poseo habilidades destacadas en <b>Estadística, Matematica, Programacion y Estrategia Empresarial</b>. 
    Amplia experiencia en Análisis de Datos y gestión estratégica, impulsando la medición de operaciones y la toma de decisiones oportunas basadas en datos.
    """,
        unsafe_allow_html=True,
    )
    # Palabras clave separadas por guiones
    words = [
        "Python",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "SQL",
        "Git/GitHub",
        "Cloud Computing",
        "Power BI",
        "Excel",
        "Dashboards",
        "Automatización",
        "Big Data",
        "Machine Learning",
        "KPI",
    ]
    text = words.join(" - ") if hasattr(words, "join") else " - ".join(words)

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

    # st.markdown(f'<div class="description">{DESCRIPTION}</div>', unsafe_allow_html=True)

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
        background: #e0f7fa;
        color: #ffffff; /* texto blanco puro */
        padding: 10px 18px;
        border-radius: 10px;
        font-weight: 600;
        text-decoration: none;
        transition: 0.3s ease;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }}
    .btn-primary:hover {{
        background: #b2ebf2;
    }}
    </style>
    """,
            unsafe_allow_html=True,
        )

    with btns[2]:
        sm_html = '<div class="social-links">'
        for name, link in SOCIAL_MEDIA.items():
            sm_html += f'<a href="{link}" target="_blank">{name}</a>'
        sm_html += "</div>"
        st.markdown(sm_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# Quick stats (manteniendo estilo)
# -------------------------
components.html(
    """
    <style>
    .stats-wrap {
        display: flex;
        gap: 20px;
        justify-content: flex-start;
        flex-wrap: wrap;
    }
    .stat-card {
        flex: 1;
        min-width: 250px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 18px 22px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        transition: all 0.25s ease;
    }
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        border-color: #008b8b;
    }
    .stat-left {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .stat-icon {
        background: linear-gradient(135deg, #008b8b, #005b96);
        color: #fff;
        width: 46px;
        height: 46px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        font-weight: 700;
        font-size: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    .stat-title {
        font-weight: 600;
        color: #0f172a;
        font-size: 15px;
    }
    .stat-sub {
        color: #6b7280;
        font-size: 12px;
        margin-top: 2px;
    }
    .stat-value {
        font-size: 22px;
        font-weight: 800;
        color: #0f172a;
        white-space: nowrap;
    }
    </style>

    <div class="stats-wrap">
        <div class="stat-card">
            <div class="stat-left">
                <div class="stat-icon">P</div>
                <div>
                    <div class="stat-title">Proyectos</div>
                    <div class="stat-sub">Entregados / activos</div>
                </div>
            </div>
            <div class="stat-value" data-target="12">0</div>
        </div>

        <div class="stat-card">
            <div class="stat-left">
                <div class="stat-icon">H</div>
                <div>
                    <div class="stat-title">Horas automatizadas</div>
                    <div class="stat-sub">Ahorro mensual</div>
                </div>
            </div>
            <div class="stat-value" data-target="120">0</div>
        </div>

        <div class="stat-card">
            <div class="stat-left">
                <div class="stat-icon">C</div>
                <div>
                    <div class="stat-title">Clientes impactados</div>
                    <div class="stat-sub">Usuarios beneficiados</div>
                </div>
            </div>
            <div class="stat-value" data-target="70">0</div>
        </div>
    </div>

    <script>
    const counters = document.querySelectorAll('.stat-value');
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const increment = target /120; // velocidad
            if (count < target) {
                counter.innerText = Math.ceil(count + increment);
                requestAnimationFrame(updateCount);
            } else {
                counter.innerText = target.toLocaleString();
            }
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
                "Automatize tareas operativas como el procesamiento de bases de clientes para campañas comerciales con Python, reduciendo tiempos de 3h a 20min.",
                "Desarrolle dashboards interactivos en la web con Python permitiendo monitoreo en tiempo real y desiciones rapidas.",
                "Implemente proyectos de SQL Cloud para centralizar bases de datos, asegurando información confiable y accesible.",
                "En todo el desarrollo utilice tecnologías open source, optimizando recursos y logrando desarrollos escalables sin generar ningún costo adicional.",
            ],
        },
        {
            "title": "Practicante de Análisis de Datos y Automatización",
            "company": "Grupo Credigama",
            "period": "02/2022 – 12/2022",
            "details": [
                "Desarrollé y administré reportes interactivos en Power BI, facilitando el análisis de indicadores operativos y comerciales.",
                "Gestioné el entorno Azure y Microsoft 365, administrando licencias, asignando usuarios y garantizando la seguridad de los datos.",
                "Desarrollé aplicaciones empresariales con Power Apps, automatizando flujos de trabajo y optimizando procesos interno.",
                "Automatizé reportes y flujos de trabajo en Excel, mejorando la eficiencia y reduciendo tiempos de ejecución.",
            ],
        },
    ]
    # Crear una pestaña por experiencia
    tabs = st.tabs([item["title"] for item in timeline])

    for tab, item in zip(tabs, timeline):
        with tab:
            st.markdown(f"**{item['company']}**, Lima  \n`{item['period']}`")
            for detail in item["details"]:
                st.markdown(f"- {detail}")
                
    st.markdown("</div>", unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚀 Proyectos Destacados")
    for project, data in PROJECTS.items():
        proj_html = f"""
        <div class="project-card">
            <img src="{data['img']}" alt="icon"/>
            <div>
                <div style="font-weight:700;color:var(--primary);font-size:15px;">{project}</div>
                <div style="color:var(--text-medium);font-size:13px;margin-top:6px;">{data['desc']}</div>
                <div style="margin-top:8px;font-size:12px;color:var(--text-light);">Tecnologías: {' • '.join(data['tech'])}</div>
                <div style="margin-top:8px;"><a href="{data['link']}" target="_blank" style="color:var(--secondary);font-weight:700;text-decoration:none;">Ver proyecto →</a></div>
            </div>
        </div>
        <hr style="border:0;border-top:1px solid #e5e7eb;margin:12px 0;">
        """
        st.markdown(proj_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# EDUCACIÓN / FORMACIÓN (con tabs de Streamlit)
# -------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎓 Formación Académica y Profesional")

tab1, tab2, tab3 = st.tabs(["Universidad", "Especialización", "Certificaciones"])

with tab1:
    st.markdown(
        "**Ingeniería Empresarial**  \n_Universidad Privada del Norte_  \n`2020 - 2025`"
    )
    st.markdown(
        "- Proyecto de Tesis: Implementación de Business Intelligence y su impacto en el Proceso de Gestión de Transporte en la Empresa Apu Runa S.A.C., Lima, 2025"
    )
    st.markdown(
        "- Participación en proyectos de investigación: desarrollo de aplicaciones y dashboards para empresas y casos de estudio asignados por los docentes."
    )

with tab2:
    st.markdown(
        "**Ciencia de Datos y Machine Learning**  \nOTI UNI / WE Educacion Ejecutiva  \n`2022 - Presente`"
    )
    st.markdown(
        '- <a href="https://drive.google.com/file/d/13DDg6z5lodFPhMHTRlpP5F1TIITyMO0R/view?usp=drive_link" target="_blank">Especialización en Supply Chain Analytics con Python</a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '- <a href="https://drive.google.com/file/d/10Rt2kDdfLoHQjuwvxC2pnROg5sdAbp0x/view?usp=drive_link" target="_blank">Especialización en Análisis y Visualización de Datos</a>',
        unsafe_allow_html=True,
    )

with tab3:
    st.markdown("**Escuela de Data Analytics**  \nPlatzi / Codificandobits  \n`2023`")
    st.markdown("- Machine Learning con Python")
    st.markdown("- Ciencia de Datos")
    st.markdown(
        '- <a href="https://drive.google.com/file/d/1m7CEHoZn7ZESAiV6zPc_fiG_rOf12d6H/view?usp=drive_link" target="_blank">Planeamiento estratégico con OKRs</a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '- <a href="https://drive.google.com/file/d/1Ucj3gDyiB9IZieiOCrKZDpT7NyGjEOVC/view?usp=drive_link" target="_blank">Planeamiento y pronóstico de la demanda</a>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
# -------------------------
# HABILIDADES
# -------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🛠 Habilidades & Tecnologías")

skills = {
    "Python": 99,
    "SQL": 90,
    "Visual Studio Code": 80,
    "Inglés": 80,
    "Git/GitHub": 70,
    "Excel": 70,
    "Power BI": 50,
    "Power Apps": 50,
}

cols = st.columns(3)
i = 0
for skill, val in skills.items():
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card">
                <div class="skill-row">
                    <div class="skill-name">{skill}</div>
                    <div style="flex:1;">
                        <div style="height:10px;background:#e5e7eb;border-radius:8px;overflow:hidden;">
                            <div style="width:{val}%;height:10px;background:linear-gradient(90deg,#008b8b,#005b96);"></div>
                        </div>
                        <div style="font-size:12px;color:#6b7280;margin-top:6px;">{val}% dominio</div>
                    </div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
    i += 1

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# CONTACTO
# -------------------------
# Tu correo de destino
TO_EMAIL = "SergioCarbajal421@gmail.com"
# Tu correo de envío (puede ser el mismo)
FROM_EMAIL = "SergioCarbajal421@gmail.com"
# Contraseña de app de Gmail
EMAIL_PASSWORD = "HolaMundo01*"

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("✉️ Contacto")

with st.form("contact_form_v2"):
    name = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    message = st.text_area("Mensaje")
    submitted = st.form_submit_button("Enviar mensaje")

    if submitted:
        try:
            # Crear mensaje
            msg = MIMEText(f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}")
            msg["Subject"] = f"Mensaje desde portafolio de {name}"
            msg["From"] = FROM_EMAIL
            msg["To"] = TO_EMAIL

            # Conexión segura a Gmail SMTP
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(FROM_EMAIL, EMAIL_PASSWORD)
                server.send_message(msg)

            st.success("¡Mensaje enviado! Te responderé pronto.")
        except Exception as e:
            st.error(f"Ocurrió un error al enviar el mensaje: {e}")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown(
    """
    <div class="footer">
        <div>© 2025 Sergio Carbajal — Data & Automation</div>
        <div style="font-size:13px;margin-top:6px;color:#6b7280;">
            Especialista en Python y Business Intelligence • Dashboards interactivos • Procesos automatizados
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)




