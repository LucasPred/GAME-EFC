import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Legado Familiar: El Simulador Narrativo",
    page_icon="🕹️",
    layout="centered"
)

# Estilo visual inmersivo tipo videojuego clásico
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stage-box { padding: 20px; border-radius: 10px; background-color: #1f2937; border: 2px solid #3b82f6; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Control de Sesión del Videojuego
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "player_role" not in st.session_state:
    st.session_state.player_role = ""
if "history_log" not in st.session_state:
    st.session_state.history_log = []

# Pantalla de Inicio de Sesión / Ingreso al Cartucho del Juego
if not st.session_state.player_name:
    st.title("🕹️ LEGADO FAMILIAR: EL VIDEOJUEGO SIMULADOR")
    st.markdown("### *Donde el pasado, el presente y el futuro de la empresa compleja cobran vida.*")
    st.markdown("---")
    
    with st.form("login_form"):
        name = st.text_input("Ingrese su Nombre y Apellido (Identificador de Usuario)")
        role = st.selectbox("Seleccione su Rol en el Grupo Empresario", [
            "Fundador / Patriarca / Matriarca",
            "Directorio Ejecutivo / Externo",
            "Segunda Generación (Sucesión Directa)",
            "Tercera Generación / Nuevos Ingresos",
            "Gerencia Operativa / No Familiar"
        ])
        pwd = st.text_input("Clave de Acceso al Sistema", type="password")
        
        start_game = st.form_submit_button("🎮 INICIAR PARTIDA")
        if start_game and name and pwd:
            st.session_state.player_name = name
            st.session_state.player_role = role
            st.rerun()
        elif start_game:
            st.warning("Por favor complete todos los campos para iniciar.")
else:
    # Cabecera Estilo HUD de Videojuego
    st.markdown(f"**Jugador:** {st.session_state.player_name} | **Rol:** {st.session_state.player_role} | 🕹️ **STAGE ACTUAL: {st.session_state.stage} / 5**")
    st.markdown("---")

    # ---------------------------------------------------------
    # STAGE 1: Fundacional - El Sueño y los Orígenes (Línea de Tiempo)
    # ---------------------------------------------------------
    if st.session_state.stage == 1:
        st.markdown("<div class='stage-box'>", unsafe_allow_html=True)
        st.subheader("🏁 Stage 1: El Sueño Fundacional y las Primeras Grietas")
        st.write("Te encuentras en el año de fundación de la compañía operativa. Los riesgos son altos y el capital es escaso. Se requiere una decisión de carácter histórico.")
        
        dilema_1 = st.radio(
            "Ante una crisis financiera severa en los primeros años, ¿cuál es tu movimiento estratégico?",
            [
                "A) Hipotecar bienes personales familiares para salvar la compañía operativa (Prioridad absoluta al legado productivo).",
                "B) Buscar socios externos y diluir el control accionario familiar para repartir el riesgo.",
                "C) Redimensionar drásticamente la estructura, recortar operaciones y avanzar de forma lenta pero con capital propio."
            ]
        )
        
        if st.button("🚀 Ejecutar Decisión y Avanzar al Stage 2"):
            st.session_state.history_log.append({"stage": 1, "dilema": dilema_1})
            st.session_state.stage = 2
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STAGE 2: El Genograma y la Teoría de Bowen (Triangulaciones)
    # ---------------------------------------------------------
    elif st.session_state.stage == 2:
        st.markdown("<div class='stage-box'>", unsafe_allow_html=True)
        st.subheader("🧬 Stage 2: El Genograma Sistémico y las Triadas")
        st.write("El grupo crece. Las tensiones familiares se trasladan al directorio. Para avanzar, debes revelar la dinámica de alianzas.")
        
        pregunta_bowen = st.selectbox(
            "¿Cómo se comporta habitualmente ante un conflicto grave de intereses con otro miembro de la familia en la empresa?",
            [
                "Busco un tercero influyente (asesor, gerente externo o familiar aliado) para triangular y mediar la tensión.",
                "Afronto la confrontación directa de manera frontal, centralizando la autoridad ejecutiva.",
                "Me repliego patrimonialmente y evito el contacto operativo diario, delegando en mandos medios."
            ]
        )
        
        if st.button("🚀 Consolidar Genograma y Avanzar al Stage 3"):
            st.session_state.history_log.append({"stage": 2, "dinamica": pregunta_bowen})
            st.session_state.stage = 3
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STAGE 3: Grafología Conductual (Modelo Sandra Cerro)
    # ---------------------------------------------------------
    elif st.session_state.stage == 3:
        st.markdown("<div class='stage-box'>", unsafe_allow_html=True)
        st.subheader("✍️ Stage 3: Biometría Escritural y Grafología")
        st.write("Para desbloquear el siguiente nivel de gobernanza, el sistema evalúa la impronta conductual de tu liderazgo a través del modelo grafológico aplicado a RRHH.")
        
        st.text_area("Describa en un párrafo breve su visión personal sobre el liderazgo en la empresa familiar y firme al pie con sus iniciales:")
        
        perfil_graf = st.selectbox(
            "Seleccione el rasgo predominante de su pulso escritural actual:",
            [
                "Trazo firme, vertical, organizado y con presión constante (Liderazgo ejecutivo estructurado).",
                "Trazo dinámico, ascendente, rápido y amplio (Liderazgo visionario expansivo).",
                "Trazo contenido, pausado, márgenes estrictos (Liderazgo conservador de resguardo patrimonial)."
            ]
        )
        
        if st.button("🚀 Registrar Perfil Grafológico y Avanzar al Stage 4"):
            st.session_state.history_log.append({"stage": 3, "grafologia": perfil_graf})
            st.session_state.stage = 4
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STAGE 4: Estrategia Sucesoria y Plexo Normativo (Argentina)
    # ---------------------------------------------------------
    elif st.session_state.stage == 4:
        st.markdown("<div class='stage-box'>", unsafe_allow_html=True)
        st.subheader("⚖️ Stage 4: Arquitectura Legal y Sucesoria (Blindaje Patrimonial)")
        st.write("Has llegado al núcleo patrimonial. Es hora de definir la estrategia jurídica bajo el derecho argentino para evitar costos judiciales y garantizar la continuidad generacional sin fisuras.")
        
        estrategia = st.selectbox(
            "Seleccione el instrumento definitivo para la transición de mando y riqueza:",
            [
                "Cesión de cuotas/acciones con reserva de usufructo vitalicio y voto prioritario (Control político asegurado para fundadores).",
                "Fideicomiso de administración y legado familiar (Protección de activos frente a contingencias externas y profesionales externos trustee).",
                "Protocolo Familiar vinculante con penalidades patrimoniales ante incumplimiento de acuerdos de accionarios."
            ]
        )
        
        if st.button("🚀 Guardar Estrategia y Ver Reporte Final (Stage 5)"):
            st.session_state.history_log.append({"stage": 4, "estrategia": estrategia})
            st.session_state.stage = 5
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STAGE 5: Reporte Final, Legado y Matriz de Posicionamiento
    # ---------------------------------------------------------
    elif st.session_state.stage == 5:
        st.markdown("<div class='stage-box'>", unsafe_allow_html=True)
        st.subheader("🏆 STAGE FINAL COMPLETADO: Matriz de Legado e Instrumentos")
        st.success(f"¡Partida finalizada con éxito para el usuario: {st.session_state.player_name}!")
        
        st.markdown("### 📊 Historial Trazado en el Videojuego:")
        for log in st.session_state.history_log:
            st.write(f"- **Stage {log['stage']}:** Registrado correctamente en la línea evolutiva del grupo.")
            
        st.markdown("### 📄 Corolario Instrumental y Soportes Técnicos Generados:")
        st.info("✓ Reglas y procedimientos de Juntas y Asambleas Familiares homologadas.\n✓ Directrices del Protocolo Constitucional del Grupo.\n✓ Plan estratégico de blindaje sucesorio exento de costas judiciales en jurisdicción argentina.")
        
        if st.button("🔄 Reiniciar Partida / Nuevo Jugador"):
            st.session_state.stage = 1
            st.session_state.player_name = ""
            st.session_state.history_log = []
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
