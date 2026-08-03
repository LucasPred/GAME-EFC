import streamlit as st
import pandas as pd
import datetime

# Configuración inicial de la página
st.set_page_config(
    page_title="Simulador Integral de Empresas Familiares",
    page_icon="💼",
    layout="wide"
)

# Inicialización de Estados de Sesión (Base de datos en memoria del simulador)
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = ""
if "user_role" not in st.session_state:
    st.session_state.user_role = "Junior"
if "genogram_data" not in st.session_state:
    st.session_state.genogram_data = []
if "grapho_data" not in st.session_state:
    st.session_state.grapho_data = {}

# Panel de Autenticación y Control de Acceso
def authentication_gate():
    st.title("🔐 Acceso al Sistema - Simulador Patrimonial y Familiar")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        username = st.text_input("Usuario / Identificador Familiar")
        password = st.text_input("Contraseña de Acceso", type="password")
        role = st.selectbox("Posición / Función en el Grupo", ["Fundador / Accionista Mayoritario", "Directorio / Director Ejecutivo", "Gerencia Operativa", "Nueva Generación / Sucesión", "Administrador General"])
        
        if st.button("Ingresar al Sistema"):
            if username and password:
                st.session_state.user_authenticated = True
                st.session_state.current_user = username
                st.session_state.user_role = role
                st.rerun()
            else:
                st.warning("Por favor, ingrese credenciales válidas.")

# Módulo 1: Línea de Tiempo e Historia del Grupo
def render_timeline_module():
    st.header("⏳ Línea de Tiempo Histórica y Legado Fundacional")
    st.markdown("Explore los hitos, los sueños fundacionales, los éxitos y los momentos de crisis superados por los fundadores.")
    
    # Simulación de hitos históricos
    hitos = [
        {"año": 1985, "hito": "Fundación de la Compañía Operativa", "detalle": "Inicios con visión de largo plazo y asunción de riesgos calculados."},
        {"año": 1998, "hito": "Expansión Regional e Industrial", "detalle": "Consolidación de activos fijos y apertura hacia nuevos mercados."},
        {"año": 2010, "hito": "Creación de la Oficina Familiar (Family Office)", "detalle": "Institucionalización de la gestión patrimonial y separación del patrimonio."},
        {"año": 2020, "hito": "Implementación del Protocolo Familiar", "detalle": "Primeras normativas consensuadas para regular ingreso y salida de familiares."}
    ]
    
    for item in hitos:
        with st.expander(f"Año {item['año']} - {item['hito']}"):
            st.write(f"**Descripción:** {item['detalle']}")
            st.info("💡 **Reflexión teórica (Escuela Angus):** La institucionalización temprana reduce la entropía relacional.")

# Módulo 2: Genograma Interactivo y Teoría de Bowen
def render_genogram_module():
    st.header("🧬 Genograma Dinámico y Dinámicas de Bowen")
    st.markdown("Construcción interactiva del mapa familiar, triangulaciones y alianzas con terceros.")
    
    with st.form("genogram_form"):
        st.subheader("Agregar o Actualizar Miembro en la Red Familiar")
        nombre_miembro = st.text_input("Nombre del Familiar / Actor Clave")
        generacion = st.selectbox("Generación", ["1° (Fundadores)", "2° (Hijos / Herederos)", "3° (Nietos / Jóvenes)"])
        vinculo_tension = st.slider("Nivel de Tensión Sistémica (Bowen)", 1, 10, 5)
        tercero_involucrado = st.text_input("Participación de Terceros / Asesores / Externos (Triada)")
        
        submitted = st.form_submit_button("Registrar en el Genograma")
        if submitted and nombre_miembro:
            st.session_state.genogram_data.append({
                "nombre": nombre_miembro,
                "generacion": generacion,
                "tension": vinculo_tension,
                "tercero": tercero_involucrado
            })
            st.success(f"Miembro {nombre_miembro} incorporado correctamente al genograma.")
            
    if st.session_state.genogram_data:
        st.subheader("📊 Estado Actual del Genograma Sistémico")
        df_gen = pd.DataFrame(st.session_state.genogram_data)
        st.dataframe(df_gen, use_container_width=True)

# Módulo 3: Análisis Grafológico Aplicado (Modelo Sandra Cerro)
def render_graphology_module():
    st.header("✍️ Panel de Evaluación Grafológica de Recursos Humanos")
    st.markdown("Suba una muestra de escritura en hoja A4 blanca sin pautar (máximo 2 párrafos con firma al pie) para el análisis conductual y de compatibilidad directiva.")
    
    miembro_eval = st.text_input("Nombre del Evaluado para el Análisis Grafológico")
    uploaded_file = st.file_uploader("Cargar imagen de escritura manuscrita y firma (PNG/JPG)", type=["png", "jpg", "jpeg"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        presion = st.slider("Presión del Trazo (Firmeza / Energía)", 1, 10, 5)
    with col2:
        orden = st.slider("Orden y Claridad Estructural", 1, 10, 7)
    with col3:
        velocidad = st.slider("Velocidad Escritural (Dinamismo)", 1, 10, 6)
        
    if st.button("Procesar Perfil Conductual Grafológico"):
        if miembro_eval:
            st.session_state.grapho_data[miembro_eval] = {
                "presion": presion,
                "orden": orden,
                "velocidad": velocidad
            }
            st.success(f"Análisis grafológico procesado bajo los parámetros de la profesora Sandra Cerro para {miembro_eval}.")
            st.info("📝 **Conclusión Preliminar:** El nivel de energía escritural indica alta capacidad de liderazgo operativo con tendencia a la centralización de decisiones.")
        else:
            st.error("Ingrese el nombre del miembro evaluado.")

# Módulo 4: Sucesión, Plexo Normativo Argentino y Blindaje Patrimonial
def render_succession_module():
    st.header("⚖️ Estrategia Jurídica y Sucesoria (Derecho Argentino)")
    st.markdown("Optimización patrimonial, evitación de costos litigiosos y preservación de la unidad empresaria.")
    
    st.info("Herramientas de blindaje y continuidad disponibles bajo normativa argentina vigente:")
    
    opcion_estrategica = st.selectbox(
        "Seleccione el instrumento de arquitectura legal preferido:",
        [
            "Cesión de Cuotas / Acciones con Reserva de Usufructo y Voto Prioritario",
            "Fideicomiso de Administración y Legado (Trustee Familiar)",
            "Protocolo de Acuerdos de Accionarios y Directorio",
            "Planificación Sucesoria Anticipada (Pacto de Herencia Futura Art. 1010 CCCN)"
        ]
    )
    
    if "Usufructo" in opcion_estrategica:
        st.write("**Detalle Técnico:** Permite al fundador conservar el control político (votos) y los frutos económicos (dividendos/usufructo) mientras transmite la nuda propiedad a la siguiente generación, evitando la apertura de procesos sucesorios judiciales onerosos.")
    elif "Fideicomiso" in opcion_estrategica:
        st.write("**Detalle Técnico:** Aislamiento de los activos productivos del patrimonio personal de los herederos, designando un comité técnico o trustee profesional para administrar con reglas estrictas.")
    else:
        st.write("**Detalle Técnico:** Marco normativo contractual destinado a alinear los intereses contrapuestos y establecer mecanismos claros de resolución de conflictos.")

# Flujo Principal de la Aplicación
if not st.session_state.user_authenticated:
    authentication_gate()
else:
    st.sidebar.title(f"👤 Hola, {st.session_state.current_user}")
    st.sidebar.markdown(f"**Rol:** {st.session_state.user_role}")
    st.sidebar.markdown("---")
    
    menu_choice = st.sidebar.radio(
        "Navegación del Simulador",
        [
            "1. Línea de Tiempo e Hitos",
            "2. Genograma y Teoría de Bowen",
            "3. Análisis Grafológico (Sandra Cerro)",
            "4. Estrategia Sucesoria y Legal (Argentina)",
            "5. Panel de Administrador y Reportes"
        ]
    )
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.user_authenticated = False
        st.rerun()

    if menu_choice == "1. Línea de Tiempo e Hitos":
        render_timeline_module()
    elif menu_choice == "2. Genograma y Teoría de Bowen":
        render_genogram_module()
    elif menu_choice == "3. Análisis Grafológico (Sandra Cerro)":
        render_graphology_module()
    elif menu_choice == "4. Estrategia Sucesoria y Legal (Argentina)":
        render_succession_module()
    elif menu_choice == "5. Panel de Administrador y Reportes":
        st.header("🛠️ Panel de Control y Auditoría del Administrador")
        st.write("Historial consolidado de interacciones de todos los usuarios en el simulador:")
        st.json(st.session_state.genogram_data)
        st.json(st.session_state.grapho_data)

