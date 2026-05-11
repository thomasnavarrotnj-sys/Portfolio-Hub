import streamlit as st
from datetime import datetime

# ============================================================
# CONFIG PAGE
# ============================================================
st.set_page_config(
    page_title="CV - Thomas Navarro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# STYLE CSS
# ============================================================
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    .title-name {
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
        color: #0F172A;
    }

    .title-role {
        font-size: 1.15rem;
        font-weight: 600;
        color: #334155;
        margin-bottom: 1rem;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0F172A;
        margin-top: 1.2rem;
        margin-bottom: 0.6rem;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 0.2rem;
    }

    .card {
        background-color: #F8FAFC;
        padding: 1rem 1.2rem;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        margin-bottom: 1rem;
    }

    .small-muted {
        color: #64748B;
        font-size: 0.92rem;
    }

    .tag {
        display: inline-block;
        background-color: #E2E8F0;
        color: #0F172A;
        padding: 0.35rem 0.7rem;
        margin: 0.2rem 0.25rem 0.2rem 0;
        border-radius: 999px;
        font-size: 0.88rem;
        font-weight: 600;
    }

    .timeline-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.2rem;
    }

    .timeline-subtitle {
        font-size: 0.95rem;
        font-weight: 600;
        color: #334155;
        margin-bottom: 0.5rem;
    }

    .metric-card {
        background-color: white;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1rem;
        text-align: center;
    }

    .metric-value {
        font-size: 1.5rem;
        font-weight: 800;
        color: #0F172A;
    }

    .metric-label {
        font-size: 0.9rem;
        color: #64748B;
        font-weight: 600;
    }

    .footer-note {
        color: #94A3B8;
        font-size: 0.85rem;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DONNEES CV (A MODIFIER)
# ============================================================
cv = {
    "name": "Thomas Navarro",
    "role": "Python Developer | Data / Finance / Portfolio Analytics",
    "location": "France",
    "email": "thomas.navarro@email.com",
    "phone": "+33 6 00 00 00 00",
    "linkedin": "linkedin.com/in/thomas-navarro",
    "github": "github.com/thomas-navarro",
    "website": "portfolio-thomas-navarro.com",
    "summary": (
        "Développeur Python orienté data, finance et architecture applicative, "
        "avec une forte appétence pour l’analyse quantitative, l’optimisation de portefeuille, "
        "les applications métier et l’automatisation. "
        "Je conçois des outils structurés, robustes et exploitables pour la gestion, "
        "l’analyse et le pilotage de données financières."
    ),
    "skills": {
        "Langages": ["Python", "SQL", "VBA", "JSON"],
        "Frameworks & Apps": ["FastAPI", "Streamlit", "PyQt", "Pandas", "NumPy"],
        "Data / IA": ["Machine Learning", "Data Analysis", "Feature Engineering", "Backtesting"],
        "Finance": ["Portfolio Optimization", "Markowitz", "Asset Analysis", "Financial Statements"],
        "Dev Tools": ["Git", "GitHub", "VS Code", "Poetry", "Virtual Environments"],
        "Architecture": ["Modular Design", "Error Handling", "Threading", "JSON-based Data Models"]
    },
    "experience": [
        {
            "title": "Développeur Python / Data / Finance (Projet personnel avancé)",
            "company": "Projet indépendant",
            "period": "2024 - Aujourd’hui",
            "details": [
                "Conception d’un écosystème applicatif Python pour l’analyse et la gestion de portefeuilles financiers.",
                "Développement d’une base d’actifs, d’un espace de calcul et d’une base de portefeuilles en JSON structuré.",
                "Implémentation de modules d’optimisation de portefeuille inspirés de Markowitz et enrichis par des critères fondamentaux.",
                "Création d’interfaces PyQt dédiées à l’exploration, au traitement et à la supervision de données financières."
            ]
        },
        {
            "title": "Analyste / Profil technique orienté automatisation",
            "company": "Environnement finance / données",
            "period": "Expérience antérieure",
            "details": [
                "Automatisation de traitements et structuration de données financières.",
                "Travail sur la fiabilité des données, les flux d’analyse et la restitution métier.",
                "Utilisation d’Excel/VBA et montée en puissance vers une architecture Python plus robuste."
            ]
        }
    ],
    "projects": [
        {
            "name": "ATLAS - Asset Tuning & Learning Analytical System",
            "description": (
                "Application modulaire Python dédiée à l’analyse financière, "
                "à la gestion de bases d’actifs et à l’optimisation de portefeuilles."
            ),
            "stack": ["Python", "PyQt", "Pandas", "JSON", "Finance"],
            "highlights": [
                "Architecture modulaire orientée classes",
                "Explorateurs JSON dédiés (MADb / EspC / MPDb / GMDb)",
                "Gestion d’erreurs hybride via structures de sortie + exceptions",
                "Optimisation portefeuille et logique de simulation"
            ]
        },
        {
            "name": "API Finance / Backend applicatif",
            "description": (
                "Structuration d’un backend métier pour exposer des fonctionnalités "
                "d’analyse et de traitement via API."
            ),
            "stack": ["Python", "FastAPI", "PostgreSQL", "Architecture backend"],
            "highlights": [
                "Découpage applicatif propre",
                "Interopérabilité avec modules métier finance",
                "Préparation à l’intégration cloud / API"
            ]
        },
        {
            "name": "Dashboard CV / Portfolio Streamlit",
            "description": (
                "Interface web légère pour présenter un profil, des projets et des compétences."
            ),
            "stack": ["Streamlit", "Python"],
            "highlights": [
                "Présentation interactive",
                "Mise en page responsive",
                "Facilement déployable"
            ]
        }
    ],
    "education": [
        {
            "degree": "Formation / montée en compétences en développement & data",
            "school": "Autoformation / Projets / Pratique intensive",
            "period": "En continu",
            "details": [
                "Python avancé",
                "Architecture logicielle",
                "Data analysis",
                "Finance quantitative appliquée"
            ]
        }
    ],
    "languages": ["Français (natif)", "Anglais (professionnel / technique)"],
    "interests": [
        "Finance de marché",
        "Analyse fondamentale",
        "Optimisation",
        "Applications métier",
        "Machine Learning"
    ]
}

# ============================================================
# FONCTIONS D'AFFICHAGE
# ============================================================
def render_tags(items):
    html = ""
    for item in items:
        html += f'<span class="tag">{item}</span>'
    st.markdown(html, unsafe_allow_html=True)

def render_section_title(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

def render_timeline_item(title, subtitle, period, details):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="timeline-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="timeline-subtitle">{subtitle}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="small-muted"><b>Période :</b> {period}</div>', unsafe_allow_html=True)
    for d in details:
        st.markdown(f"- {d}")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.title("📌 Navigation")
    section = st.radio(
        "Aller à",
        [
            "Vue générale",
            "Expérience",
            "Projets",
            "Compétences",
            "Formation",
            "Contact"
        ]
    )

    st.markdown("---")
    st.markdown("### 👤 Infos rapides")
    st.write(f"**Nom :** {cv['name']}")
    st.write(f"**Rôle :** {cv['role']}")
    st.write(f"**Localisation :** {cv['location']}")
    st.write(f"**Email :** {cv['email']}")

    st.markdown("---")
    st.markdown("### 🧠 Points forts")
    st.write("• Python orienté projet")
    st.write("• Finance & portefeuille")
    st.write("• Data & structuration")
    st.write("• Architecture modulaire")

# ============================================================
# HEADER
# ============================================================
st.markdown(f'<div class="title-name">{cv["name"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="title-role">{cv["role"]}</div>', unsafe_allow_html=True)

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">Python</div>
            <div class="metric-label">Langage principal</div>
        </div>
        """,
        unsafe_allow_html=True
    )
with col_b:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">Finance</div>
            <div class="metric-label">Domaine métier</div>
        </div>
        """,
        unsafe_allow_html=True
    )
with col_c:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">Data / IA</div>
            <div class="metric-label">Axe d’évolution</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("")

# ============================================================
# CONTENU PRINCIPAL
# ============================================================
if section == "Vue générale":
    render_section_title("Profil")
    st.markdown(f'<div class="card">{cv["summary"]}</div>', unsafe_allow_html=True)

    render_section_title("Compétences clés")
    for category, items in cv["skills"].items():
        st.markdown(f"**{category}**")
        render_tags(items)

    render_section_title("Projet principal")
    p = cv["projects"][0]
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### {p['name']}")
    st.write(p["description"])
    st.markdown("**Technos :**")
    render_tags(p["stack"])
    st.markdown("**Points forts :**")
    for h in p["highlights"]:
        st.markdown(f"- {h}")
    st.markdown('</div>', unsafe_allow_html=True)

elif section == "Expérience":
    render_section_title("Expérience professionnelle / projets")
    for exp in cv["experience"]:
        render_timeline_item(
            title=exp["title"],
            subtitle=exp["company"],
            period=exp["period"],
            details=exp["details"]
        )

elif section == "Projets":
    render_section_title("Projets")
    for proj in cv["projects"]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"### {proj['name']}")
        st.write(proj["description"])
        st.markdown("**Stack :**")
        render_tags(proj["stack"])
        st.markdown("**Highlights :**")
        for h in proj["highlights"]:
            st.markdown(f"- {h}")
        st.markdown('</div>', unsafe_allow_html=True)

elif section == "Compétences":
    render_section_title("Compétences détaillées")
    for category, items in cv["skills"].items():
        st.markdown(f"### {category}")
        render_tags(items)

elif section == "Formation":
    render_section_title("Formation")
    for edu in cv["education"]:
        render_timeline_item(
            title=edu["degree"],
            subtitle=edu["school"],
            period=edu["period"],
            details=edu["details"]
        )

    render_section_title("Langues")
    render_tags(cv["languages"])

    render_section_title("Centres d’intérêt")
    render_tags(cv["interests"])

elif section == "Contact":
    render_section_title("Contact")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"📧 **Email :** {cv['email']}")
    st.write(f"📱 **Téléphone :** {cv['phone']}")
    st.write(f"🔗 **LinkedIn :** {cv['linkedin']}")
    st.write(f"💻 **GitHub :** {cv['github']}")
    st.write(f"🌐 **Site / Portfolio :** {cv['website']}")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
current_year = datetime.now().year
st.markdown(
    f'<div class="footer-note">CV interactif • Streamlit • {current_year}</div>',
    unsafe_allow_html=True
)
