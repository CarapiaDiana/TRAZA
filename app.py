import streamlit as st
import html
import math
import csv
import io
from pathlib import Path

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="TRAZA | Generadores de Obra",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# IDENTIDAD VISUAL TRAZA
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #F4F1E8;
    color: #252923;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   SIDEBAR
============================================================ */

section[data-testid="stSidebar"] {
    background-color: #344238;
}

section[data-testid="stSidebar"] * {
    color: #F4F1E8;
}

.sidebar-logo {
    font-size: 34px;
    font-weight: 700;
    letter-spacing: 7px;
    color: #F4F1E8;
    margin-bottom: 4px;
}

.sidebar-sub {
    color: #C9D0C3;
    font-size: 13px;
    letter-spacing: 1px;
    margin-bottom: 30px;
}

.sidebar-titulo {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #A8B59F;
    margin-top: 25px;
    margin-bottom: 10px;
}

.sidebar-item-activo {
    background: #F4F1E8;
    color: #344238 !important;
    padding: 11px 14px;
    border-radius: 9px;
    font-weight: 700;
    margin-bottom: 8px;
}

.sidebar-item {
    padding: 8px 14px;
    color: #D9DED5 !important;
    margin-bottom: 4px;
}


/* ============================================================
   ENCABEZADO
============================================================ */

.marca {
    font-size: 18px;
    letter-spacing: 6px;
    font-weight: 700;
    color: #6F8068;
    margin-bottom: 8px;
}

.titulo-principal {
    font-size: 46px;
    line-height: 1.05;
    font-weight: 700;
    color: #252923;
    margin-bottom: 8px;
}

.subtitulo {
    font-size: 17px;
    color: #6F746B;
    margin-bottom: 32px;
}


/* ============================================================
   SECCIONES
============================================================ */

.seccion {
    font-size: 27px;
    font-weight: 700;
    color: #344238;
    margin-top: 34px;
    margin-bottom: 15px;
}

.seccion-mini {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #6F8068;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.linea {
    border-top: 1px solid #DCD8CA;
    margin: 28px 0;
}


/* ============================================================
   TARJETAS
============================================================ */

.tarjeta {
    background-color: #FCFBF7;
    border: 1px solid #DDD9CE;
    border-radius: 16px;
    padding: 22px 24px;
    margin-bottom: 18px;
    box-shadow: 0px 2px 10px rgba(37, 41, 35, 0.04);
}

.tarjeta-verde {
    background-color: #344238;
    border-radius: 16px;
    padding: 24px 26px;
    margin: 20px 0;
}

.tarjeta-verde .label {
    color: #C8D1C3;
    font-size: 13px;
    letter-spacing: 2px;
}

.tarjeta-verde .numero {
    color: #F4F1E8;
    font-size: 42px;
    font-weight: 600;
    margin-top: 3px;
}

.tarjeta-resultado {
    background-color: #E3E8DE;
    border-left: 5px solid #6F8068;
    border-radius: 10px;
    padding: 15px 18px;
    margin-top: 14px;
}

.muro-titulo {
    font-size: 22px;
    font-weight: 700;
    color: #344238;
    margin-bottom: 4px;
}

.muro-numero {
    color: #6F8068;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}


/* ============================================================
   RESULTADOS
============================================================ */

.resumen {
    font-size: 16px;
    color: #252923;
    padding: 10px 0;
    border-bottom: 1px solid #E2DED3;
}

.detalle {
    font-size: 15px;
    line-height: 1.75;
    color: #383D37;
    background-color: #FCFBF7;
    border: 1px solid #E2DED3;
    border-radius: 12px;
    padding: 17px 20px;
    margin-bottom: 12px;
}

.clave {
    display: inline-block;
    background-color: #344238;
    color: #F4F1E8;
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.dato {
    margin-top: 10px;
}

.dato strong {
    color: #6F8068;
    font-size: 12px;
    letter-spacing: 1px;
}


/* ============================================================
   INPUTS
============================================================ */

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
textarea {
    background-color: #FCFBF7 !important;
    border-color: #D5D1C7 !important;
    border-radius: 9px !important;
}

div[data-testid="stFileUploader"] {
    background-color: #FCFBF7;
    border: 1px dashed #A8B59F;
    border-radius: 14px;
    padding: 10px;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

.stButton > button {
    background-color: #344238;
    color: #F4F1E8;
    border: none;
    border-radius: 9px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #6F8068;
    color: #F4F1E8;
    border: none;
}

.stDownloadButton > button {
    background-color: #344238;
    color: #F4F1E8;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.2rem;
    font-weight: 600;
    min-height: 46px;
}

.stDownloadButton > button:hover {
    background-color: #6F8068;
    color: #F4F1E8;
    border: none;
}

.stDownloadButton > button:focus {
    border: none;
    box-shadow: none;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    from pathlib import Path

    logo_path = Path(__file__).parent / "traza_logo.png"

    st.markdown(
        """
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            padding-top: 8px;
            margin-bottom: 22px;
        ">
        """,
        unsafe_allow_html=True
    )

    st.image(str(logo_path), width=245)

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="sidebar-titulo">PROYECTO</div>
<div class="sidebar-item">⌂ Información general</div>
<div class="sidebar-item">▱ Plano arquitectónico</div>

<div class="sidebar-titulo">CUANTIFICACIÓN</div>
<div class="sidebar-item-activo">Muros</div>
<div class="sidebar-item">Pisos · Próximamente</div>
<div class="sidebar-item">Plafones · Próximamente</div>
<div class="sidebar-item">Acabados · Próximamente</div>

<div class="sidebar-titulo">RESULTADOS</div>
<div class="sidebar-item">Resumen</div>
<div class="sidebar-item">Catálogo de conceptos</div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ENCABEZADO PRINCIPAL
# ============================================================

st.markdown(
    '<div class="marca">TRAZA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="titulo-principal">Generadores de Obra</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="subtitulo">
Sistema de cuantificación y generación de conceptos para proyectos de construcción.
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# DATOS DEL PROYECTO
# ============================================================

st.markdown(
    '<div class="seccion-mini">01 / Proyecto</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Información del proyecto</div>',
    unsafe_allow_html=True
)

col_proy1, col_proy2 = st.columns(2)

with col_proy1:

    nombre_proyecto = st.text_input(
        "Nombre del proyecto",
        placeholder="Ej. Casa Habitación Morelia"
    )

with col_proy2:

    ubicacion_proyecto = st.text_input(
        "Ubicación",
        placeholder="Ej. Morelia, Michoacán"
    )


# ============================================================
# CARGA DEL PLANO PDF
# ============================================================

st.markdown(
    '<div class="seccion">Plano arquitectónico</div>',
    unsafe_allow_html=True
)

st.write(
    "Carga el plano de referencia del proyecto en formato PDF."
)

archivo_plano = st.file_uploader(
    "Seleccionar plano",
    type=["pdf"],
    accept_multiple_files=False
)

if archivo_plano is not None:

    nombre_pdf = html.escape(archivo_plano.name)
    tamano_kb = archivo_plano.size / 1024

    st.success(
        f"Plano cargado correctamente: {archivo_plano.name}"
    )

    st.markdown(
        f"""
<div class="tarjeta">
<div class="seccion-mini">ARCHIVO DEL PROYECTO</div>
<strong>{nombre_pdf}</strong><br>
<span style="color:#747A71;">
PDF · {tamano_kb:,.1f} KB
</span>
</div>
""",
        unsafe_allow_html=True
    )


st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)


# ============================================================
# GENERADOR DE MUROS
# ============================================================

st.markdown(
    '<div class="seccion-mini">02 / Cuantificación</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Generador de muros</div>',
    unsafe_allow_html=True
)

st.write(
    "Captura las dimensiones de cada muro y TRAZA calculará automáticamente el área neta."
)


# ============================================================
# CANTIDAD DE MUROS
# ============================================================

cantidad_muros = st.number_input(
    "¿Cuántos muros deseas cuantificar?",
    min_value=1,
    max_value=100,
    value=1,
    step=1
)


# ============================================================
# TIPOS DE MURO
# ============================================================

tipos_muro = [
    "Muro de tablaroca",
    "Muro de block",
    "Muro de ladrillo",
    "Muro de tabique rojo recocido",
    "Muro de concreto",
    "Muro de concreto armado",
    "Muro de mampostería",
    "Muro de piedra"
]

muros = []


# ============================================================
# CAPTURA DE MUROS
# ============================================================

for i in range(int(cantidad_muros)):

    numero_muro = i + 1

    st.markdown(
        '<div class="linea"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="muro-numero">MURO {numero_muro:02d}</div>
<div class="muro-titulo">Datos del muro</div>
""",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        tipo = st.selectbox(
            "Tipo de muro",
            tipos_muro,
            key=f"tipo_muro_{numero_muro}"
        )

    with col2:

        largo = st.number_input(
            "Largo (m)",
            min_value=0.0,
            value=0.0,
            step=0.10,
            format="%.2f",
            key=f"largo_muro_{numero_muro}"
        )

    with col3:

        alto = st.number_input(
            "Alto (m)",
            min_value=0.0,
            value=2.90,
            step=0.10,
            format="%.2f",
            key=f"alto_muro_{numero_muro}"
        )


    # ========================================================
    # ÁREA BRUTA
    # ========================================================

    area_bruta = largo * alto

    st.markdown(
        f"""
<div class="tarjeta-resultado">
<strong>Área bruta</strong><br>
<span style="font-size:26px;">
{area_bruta:,.2f} m²
</span>
</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # VANOS
    # ========================================================

    cantidad_vanos = st.number_input(
        f"¿Cuántos vanos tiene el muro {numero_muro}?",
        min_value=0,
        max_value=50,
        value=0,
        step=1,
        key=f"cantidad_vanos_{numero_muro}"
    )

    descuento_total = 0.0


    if cantidad_vanos > 0:

        st.markdown("#### Vanos")

        for j in range(int(cantidad_vanos)):

            numero_vano = j + 1

            col_a, col_b = st.columns(2)

            with col_a:

                ancho_vano = st.number_input(
                    f"Ancho del vano {numero_vano} (m)",
                    min_value=0.0,
                    value=0.0,
                    step=0.10,
                    format="%.2f",
                    key=f"ancho_vano_{numero_muro}_{numero_vano}"
                )

            with col_b:

                alto_vano = st.number_input(
                    f"Alto del vano {numero_vano} (m)",
                    min_value=0.0,
                    value=0.0,
                    step=0.10,
                    format="%.2f",
                    key=f"alto_vano_{numero_muro}_{numero_vano}"
                )

            area_vano = ancho_vano * alto_vano

            descuento_total += area_vano

            st.caption(
                f"Vano {numero_vano}: {area_vano:,.2f} m²"
            )


    # ========================================================
    # ÁREA NETA
    # ========================================================

    area_neta = max(
        area_bruta - descuento_total,
        0.0
    )

    st.markdown(
        f"""
<div class="tarjeta-resultado">
<strong>Área neta del muro</strong><br>
<span style="font-size:28px; color:#344238;">
{area_neta:,.2f} m²
</span><br>
<span style="font-size:13px; color:#70766E;">
Descuento de vanos: {descuento_total:,.2f} m²
</span>
</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # GUARDAR DATOS
    # ========================================================

    muros.append(
        {
            "numero": numero_muro,
            "tipo": tipo,
            "largo": largo,
            "alto": alto,
            "area_bruta": area_bruta,
            "descuento": descuento_total,
            "area_neta": area_neta
        }
    )


# ============================================================
# CÁLCULOS GENERALES
# ============================================================

total_muros = sum(
    muro["area_neta"]
    for muro in muros
)

total_bruto = sum(
    muro["area_bruta"]
    for muro in muros
)

total_descuentos = sum(
    muro["descuento"]
    for muro in muros
)


# ============================================================
# RESULTADOS
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">03 / Resultados</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Resumen del generador</div>',
    unsafe_allow_html=True
)


col_r1, col_r2, col_r3, col_r4 = st.columns(4)

with col_r1:

    st.metric(
        "Muros",
        len(muros)
    )

with col_r2:

    st.metric(
        "Área bruta",
        f"{total_bruto:,.2f} m²"
    )

with col_r3:

    st.metric(
        "Descuentos",
        f"{total_descuentos:,.2f} m²"
    )

with col_r4:

    st.metric(
        "Área neta",
        f"{total_muros:,.2f} m²"
    )


# ============================================================
# TOTAL DE MUROS
# ============================================================

st.markdown(
    f"""
<div class="tarjeta-verde">
<div class="label">TOTAL DE MUROS</div>
<div class="numero">{total_muros:,.2f} m²</div>
</div>
""",
    unsafe_allow_html=True
)

# ============================================================
# RESUMEN POR TIPO
# ============================================================

# Crear el resumen automáticamente a partir de los muros capturados
resumen_final = {}

for muro in muros:
    tipo_actual = muro.get("tipo", "")
    area_actual = muro.get("area_neta", 0.0)

    if tipo_actual not in resumen_final:
        resumen_final[tipo_actual] = 0.0

    resumen_final[tipo_actual] += area_actual


# ============================================================
# MOSTRAR RESUMEN
# ============================================================

st.markdown(
    '<div class="seccion">Resumen por tipo de muro</div>',
    unsafe_allow_html=True
)

for tipo_resumen, area_resumen in resumen_final.items():

    st.markdown(
        f"""
        <div class="resumen">
            <strong>{html.escape(tipo_resumen)}</strong>
            <span style="float:right;">
                {area_resumen:,.2f} m²
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# DETALLE DE COMPROBACIÓN
# ============================================================

with st.expander("Ver detalle de comprobación"):

    for muro in muros:

        tipo_seguro = html.escape(muro["tipo"])

        st.markdown(
            f"""
<div class="detalle">
<strong>Muro {muro["numero"]:02d}</strong><br>
{tipo_seguro}<br>
Área bruta: {muro["area_bruta"]:,.2f} m²<br>
Descuento: {muro["descuento"]:,.2f} m²<br>
<strong>Área neta: {muro["area_neta"]:,.2f} m²</strong>
</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# CONCEPTOS
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">04 / Conceptos</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Catálogo de conceptos</div>',
    unsafe_allow_html=True
)

st.write(
    "Escribe el concepto correspondiente a cada tipo de muro."
)


conceptos = {}

# ============================================================
# CONCEPTOS AUTOMÁTICOS
# ============================================================

conceptos_automaticos = {

    "Muro de tablaroca":
        "Suministro e instalación de muro de tablaroca de acuerdo con "
        "las dimensiones y especificaciones del proyecto, compuesto por "
        "estructura metálica, placas de yeso, tornillería y accesorios, "
        "incluyendo trazo, nivelación, colocación de canales y postes, "
        "fijación de placas, tratamiento de juntas, colocación de "
        "esquineros, materiales, mano de obra, herramienta y equipo "
        "necesarios para su correcta ejecución y acabado.",

    "Muro de block":
        "Suministro y construcción de muro de block de concreto de acuerdo "
        "con las dimensiones y especificaciones del proyecto, incluyendo "
        "suministro y colocación de piezas, preparación y aplicación de "
        "mortero, cortes, ajustes, alineación, nivelación, plomeo, "
        "herramienta, mano de obra y todos los trabajos necesarios para "
        "su correcta ejecución y acabado.",

    "Muro de concreto":
        "Suministro y construcción de muro de concreto ejecutado de acuerdo "
        "con las dimensiones, niveles y especificaciones del proyecto, "
        "incluyendo preparación, habilitado y colocación de acero de refuerzo "
        "cuando corresponda, cimbra, colado, vibrado, descimbrado, curado "
        "y todos los materiales, mano de obra, herramienta y equipo "
        "necesarios para su correcta ejecución y acabado.",

    "Muro de ladrillo":
        "Suministro y construcción de muro de ladrillo asentado con mortero "
        "cemento-arena, de acuerdo con las dimensiones y especificaciones "
        "del proyecto, incluyendo suministro y colocación de piezas, "
        "preparación y aplicación del mortero, cortes, ajustes, alineación, "
        "nivelación, plomeo, mano de obra, herramienta y todos los trabajos "
        "necesarios para su correcta ejecución y acabado.",

    "Muro de tabique":
        "Suministro y construcción de muro de tabique asentado con mortero "
        "cemento-arena, incluyendo suministro y colocación de piezas, "
        "preparación y aplicación del mortero, cortes, ajustes, alineación, "
        "nivelación, plomeo, mano de obra, herramienta y trabajos necesarios "
        "para su correcta ejecución y acabado.",

    "Muro de tabique rojo recocido":
        "Suministro y construcción de muro de tabique rojo recocido, asentado con mortero cemento-arena, de acuerdo con las dimensiones, niveles y especificaciones del proyecto, incluyendo suministro y colocación de piezas, preparación y aplicación del mortero, cortes, ajustes, alineación, nivelación, plomeo, desperdicios, mano de obra, herramienta y equipo necesarios para su correcta ejecución y acabado.",

    "Muro de concreto armado":
        "Suministro y construcción de muro de concreto armado de acuerdo con las dimensiones, niveles y especificaciones del proyecto, incluyendo habilitado, suministro y colocación de acero de refuerzo, cimbra, preparación, colocación, vibrado y curado del concreto, descimbrado, materiales, mano de obra, herramienta y equipo necesarios para su correcta ejecución y acabado.",

    "Muro de mampostería":
        "Suministro y construcción de muro de mampostería con piezas de piedra y mortero cemento-arena, de acuerdo con las dimensiones, niveles y especificaciones del proyecto, incluyendo selección y colocación de piezas, preparación y aplicación del mortero, ajustes, alineación, nivelación, plomeo, juntas, materiales, mano de obra, herramienta y equipo necesarios para su correcta ejecución y acabado.",

    "Muro de piedra":
        "Suministro y construcción de muro de piedra de acuerdo con las dimensiones, niveles y especificaciones del proyecto, incluyendo suministro, selección y colocación de piedra, preparación y aplicación de mortero cemento-arena, acomodo de piezas, ajustes, alineación, nivelación, plomeo, juntas, materiales, mano de obra, herramienta y equipo necesarios para su correcta ejecución y acabado.",

}

conceptos = {}

for tipo_concepto in tipos_muro:
    conceptos[tipo_concepto] = conceptos_automaticos.get(
        tipo_concepto,
        f"Suministro y construcción de {tipo_concepto.lower()}, "
        "incluyendo materiales, mano de obra, herramienta y trabajos "
        "necesarios para su correcta ejecución."
    )

# ============================================================
# TIPOS UTILIZADOS
# ============================================================

tipos_utilizados = []


for muro in muros:

    if (
        muro["area_neta"] > 0
        and muro["tipo"] not in tipos_utilizados
    ):

        tipos_utilizados.append(
            muro["tipo"]
        )


# ============================================================
# CATÁLOGO FINAL DE CONCEPTOS
# ============================================================

st.markdown(
    '<div class="seccion">📑 Catálogo final de conceptos</div>',
    unsafe_allow_html=True
)


if len(tipos_utilizados) == 0:

    st.info(
        "Captura al menos un muro con un área mayor a 0.00 m² para generar el catálogo."
    )


else:

    for indice, tipo in enumerate(tipos_utilizados, start=1):

        # ----------------------------------------------------
        # CANTIDAD TOTAL DEL TIPO DE MURO
        # ----------------------------------------------------

        cantidad_tipo = sum(
            muro["area_neta"]
            for muro in muros
            if muro["tipo"] == tipo
        )


        # ----------------------------------------------------
        # CONCEPTO
        # ----------------------------------------------------

        concepto = conceptos.get(tipo, "").strip()

        if concepto == "":
            concepto = "Sin concepto capturado"


        # ----------------------------------------------------
        # PROTEGER TEXTO PARA HTML
        # ----------------------------------------------------

        tipo_seguro = html.escape(tipo)
        concepto_seguro = html.escape(concepto)


        # ----------------------------------------------------
        # CLAVE
        # ----------------------------------------------------

        clave = f"MU-{indice:02d}"


        # ----------------------------------------------------
        # CATÁLOGO
        # ----------------------------------------------------

        html_catalogo = f"""
<div class="detalle">
<div class="clave">{clave}</div>
<div class="dato"><strong>TIPO</strong><br>{tipo_seguro}</div>
<div class="dato"><strong>CONCEPTO</strong><br>{concepto_seguro}</div>
<div class="dato"><strong>UNIDAD</strong><br>m²</div>
<div class="dato"><strong>CANTIDAD</strong><br>{cantidad_tipo:,.2f} m²</div>
</div>
"""


        st.markdown(
            html_catalogo,
            unsafe_allow_html=True
        )


        if indice < len(tipos_utilizados):

            st.markdown(
                '<div class="linea"></div>',
                unsafe_allow_html=True
            )

# ============================================================
# 05 / MATERIALES
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">05 / Materiales</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Generador de materiales</div>',
    unsafe_allow_html=True
)

st.write(
    "Consulta la composición y cantidad estimada de materiales "
    "asociados a cada sistema constructivo."
)


# ============================================================
# CONFIGURACIÓN DEL SISTEMA DE TABLAROCA
# ============================================================

st.markdown(
    '<div class="seccion-mini">Configuración del sistema</div>',
    unsafe_allow_html=True
)

col_tab1, col_tab2, col_tab3 = st.columns(3)


with col_tab1:

    caras_tablaroca = st.selectbox(
        "Caras de tablaroca",
        [1, 2],
        index=1,
        key="caras_tablaroca",
        help=(
            "1 = una cara de tablaroca. "
            "2 = tablaroca en ambas caras."
        )
    )


with col_tab2:

    separacion_postes = st.selectbox(
        "Separación de postes",
        [0.40, 0.60],
        index=1,
        format_func=lambda x: f"{x:.2f} m",
        key="separacion_postes",
        help="Separación entre postes metálicos."
    )


with col_tab3:

    desperdicio = st.selectbox(
        "Desperdicio",
        [0.00, 0.05, 0.10],
        index=1,
        format_func=lambda x: f"{x * 100:.0f} %",
        key="desperdicio_material",
        help="Porcentaje adicional para cortes y desperdicios."
    )


# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES
# ============================================================

def calcular_materiales_tablaroca(
    muros_tipo,
    caras,
    separacion,
    desperdicio
):

    resultados = []


    # --------------------------------------------------------
    # ÁREA TOTAL
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )


    # --------------------------------------------------------
    # ÁREA DE PLACAS
    # --------------------------------------------------------

    area_placa = (
        area_total
        * caras
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Placa de tablaroca de 12.5 mm",
            "unidad": "m²",
            "cantidad": area_placa,
            "detalle": (
                f"{area_total:.2f} m² × "
                f"{caras} cara(s) + desperdicio"
            )
        }
    )


    # --------------------------------------------------------
    # CANAL METÁLICO
    # --------------------------------------------------------

    canal_total = 0.0

    for muro in muros_tipo:

        # Canal inferior + canal superior
        canal_muro = muro["largo"] * 2

        canal_total += canal_muro


    canal_total *= (1 + desperdicio)


    resultados.append(
        {
            "material": "Canal metálico",
            "unidad": "m",
            "cantidad": canal_total,
            "detalle": "Canal superior e inferior"
        }
    )


    # --------------------------------------------------------
    # POSTES METÁLICOS
    # --------------------------------------------------------

    postes_total = 0.0
    cantidad_postes = 0


    for muro in muros_tipo:

        largo_muro = muro["largo"]

        if largo_muro > 0:

            postes_muro = (
                int(
                    largo_muro
                    / separacion
                )
                + 1
            )

            cantidad_postes += postes_muro

            postes_total += (
                postes_muro
                * muro["alto"]
            )


    postes_total *= (1 + desperdicio)


    resultados.append(
        {
            "material": "Poste metálico",
            "unidad": "m",
            "cantidad": postes_total,
            "detalle": (
                f"{cantidad_postes} postes × altura"
            )
        }
    )


    # --------------------------------------------------------
    # TORNILLOS PARA TABLAROCA
    # --------------------------------------------------------

    tornillos_tablaroca = (
        area_total
        * caras
        * 15
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Tornillo para tablaroca",
            "unidad": "pza",
            "cantidad": tornillos_tablaroca,
            "detalle": "15 tornillos/m² por cara"
        }
    )


    # --------------------------------------------------------
    # TORNILLOS METAL-METAL
    # --------------------------------------------------------

    tornillos_metal = (
        cantidad_postes
        * 4
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Tornillo metal-metal",
            "unidad": "pza",
            "cantidad": tornillos_metal,
            "detalle": "4 tornillos por poste"
        }
    )


    # --------------------------------------------------------
    # CINTA PARA JUNTAS
    # --------------------------------------------------------

    cinta = (
        area_total
        * caras
        * 1.20
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Cinta para juntas",
            "unidad": "m",
            "cantidad": cinta,
            "detalle": "1.20 m/m² por cara"
        }
    )


    # --------------------------------------------------------
    # COMPUESTO PARA JUNTAS
    # --------------------------------------------------------

    compuesto = (
        area_total
        * caras
        * 0.30
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Compuesto para juntas",
            "unidad": "kg",
            "cantidad": compuesto,
            "detalle": "0.30 kg/m² por cara"
        }
    )


    # --------------------------------------------------------
    # ESQUINERO
    # --------------------------------------------------------

    esquinero = 0.0


    for muro in muros_tipo:

        esquinero += (
            muro["alto"]
            * 2
        )


    esquinero *= (1 + desperdicio)


    resultados.append(
        {
            "material": "Esquinero",
            "unidad": "m",
            "cantidad": esquinero,
            "detalle": "2 esquineros verticales por muro"
        }
    )


    return resultados

# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES DE MURO DE BLOCK
# ============================================================

def calcular_materiales_block(muros_tipo, desperdicio):

    resultados = []

    # --------------------------------------------------------
    # ÁREA TOTAL DEL MURO
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )

    # --------------------------------------------------------
    # BLOCK DE CONCRETO
    # --------------------------------------------------------

    cantidad_block = (
        area_total
        * 12.5
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Block de concreto",
            "unidad": "pza",
            "cantidad": cantidad_block,
            "detalle": "12.5 piezas por m²"
        }
    )

    # --------------------------------------------------------
    # MORTERO
    # --------------------------------------------------------

    mortero = (
        area_total
        * 0.020
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Mortero cemento-arena",
            "unidad": "m³",
            "cantidad": mortero,
            "detalle": "0.020 m³ por m² de muro"
        }
    )

    # --------------------------------------------------------
    # CEMENTO
    # --------------------------------------------------------

    cemento = (
        area_total
        * 4.50
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Cemento",
            "unidad": "kg",
            "cantidad": cemento,
            "detalle": "4.50 kg por m² de muro"
        }
    )

    # --------------------------------------------------------
    # ARENA
    # --------------------------------------------------------

    arena = (
        area_total
        * 0.020
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Arena",
            "unidad": "m³",
            "cantidad": arena,
            "detalle": "0.020 m³ por m² de muro"
        }
    )

    return resultados

# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES DE MURO DE LADRILLO
# ============================================================

def calcular_materiales_ladrillo(muros_tipo, desperdicio):

    resultados = []

    # ============================================================
    # ÁREA TOTAL DEL MURO
    # ============================================================

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )

    # ============================================================
    # LADRILLO
    # ============================================================

    cantidad_ladrillo = (
        area_total
        * 16
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Ladrillo",
            "unidad": "pza",
            "cantidad": cantidad_ladrillo,
            "detalle": "16 piezas por m²"
        }
    )

    # ============================================================
    # MORTERO CEMENTO-ARENA
    # ============================================================

    cantidad_mortero = (
        area_total
        * 0.020
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Mortero cemento-arena",
            "unidad": "m³",
            "cantidad": cantidad_mortero,
            "detalle": "0.020 m³ por m² de muro"
        }
    )

    return resultados
   
# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES DE MURO DE CONCRETO
# ============================================================

def calcular_materiales_concreto(muros_tipo, desperdicio):

    resultados = []

    # --------------------------------------------------------
    # ÁREA TOTAL DEL MURO
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )

    # --------------------------------------------------------
    # CONCRETO
    # --------------------------------------------------------

    cantidad_concreto = (
        area_total
        * 0.12
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Concreto",
            "unidad": "m³",
            "cantidad": cantidad_concreto,
            "detalle": "0.12 m³ por m² de muro"
        }
    )

    return resultados

# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES DE MURO DE CONCRETO ARMADO
# ============================================================

def calcular_materiales_concreto_armado(muros_tipo, desperdicio):

    resultados = []

    # --------------------------------------------------------
    # ÁREA TOTAL DEL MURO
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )

    # --------------------------------------------------------
    # CONCRETO
    # --------------------------------------------------------

    cantidad_concreto = (
        area_total
        * 0.15
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Concreto",
            "unidad": "m³",
            "cantidad": cantidad_concreto,
            "detalle": "0.15 m³ por m² de muro"
        }
    )

    # --------------------------------------------------------
    # ACERO DE REFUERZO
    # --------------------------------------------------------

    cantidad_acero = (
        area_total
        * 10.00
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Acero de refuerzo",
            "unidad": "kg",
            "cantidad": cantidad_acero,
            "detalle": "10.00 kg por m² de muro"
        }
    )

    # --------------------------------------------------------
    # ALAMBRE RECOCIDO
    # --------------------------------------------------------

    cantidad_alambre = (
        area_total
        * 0.20
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Alambre recocido",
            "unidad": "kg",
            "cantidad": cantidad_alambre,
            "detalle": "0.20 kg por m² de muro"
        }
    )

    # --------------------------------------------------------
    # CIMBRA
    # --------------------------------------------------------

    cantidad_cimbra = (
        area_total
        * 2.00
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Cimbra",
            "unidad": "m²",
            "cantidad": cantidad_cimbra,
            "detalle": "2.00 m² por m² de muro"
        }
    )

    return resultados

# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES DE MURO DE TABIQUE ROJO RECOCIDO
# ============================================================

def calcular_materiales_tabique_rojo(muros_tipo, desperdicio):

    resultados = []

    # --------------------------------------------------------
    # ÁREA TOTAL DEL MURO
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )

    # --------------------------------------------------------
    # TABIQUE ROJO RECOCIDO
    # --------------------------------------------------------

    cantidad_tabique = (
        area_total
        * 16.00
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Tabique rojo recocido",
            "unidad": "pza",
            "cantidad": cantidad_tabique,
            "detalle": "16.00 piezas por m²"
        }
    )

    # --------------------------------------------------------
    # MORTERO
    # --------------------------------------------------------

    mortero = (
        area_total
        * 0.025
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Mortero cemento-arena",
            "unidad": "m³",
            "cantidad": mortero,
            "detalle": "0.025 m³ por m² de muro"
        }
    )

    # --------------------------------------------------------
    # CEMENTO
    # --------------------------------------------------------

    cemento = (
        area_total
        * 5.00
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Cemento",
            "unidad": "kg",
            "cantidad": cemento,
            "detalle": "5.00 kg por m² de muro"
        }
    )

    # --------------------------------------------------------
    # ARENA
    # --------------------------------------------------------

    arena = (
        area_total
        * 0.025
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Arena",
            "unidad": "m³",
            "cantidad": arena,
            "detalle": "0.025 m³ por m² de muro"
        }
    )

    return resultados
# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES DE MURO DE MAMPOSTERÍA
# ============================================================

def calcular_materiales_mamposteria(muros_tipo, desperdicio):

    resultados = []

    # --------------------------------------------------------
    # ÁREA TOTAL DEL MURO
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )

    # --------------------------------------------------------
    # PIEDRA
    # --------------------------------------------------------

    cantidad_piedra = (
        area_total
        * 0.40
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Piedra",
            "unidad": "m³",
            "cantidad": cantidad_piedra,
            "detalle": "0.40 m³ por m² de muro"
        }
    )

    # --------------------------------------------------------
    # MORTERO CEMENTO-ARENA
    # --------------------------------------------------------

    cantidad_mortero = (
        area_total
        * 0.020
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Mortero cemento-arena",
            "unidad": "m³",
            "cantidad": cantidad_mortero,
            "detalle": "0.020 m³ por m² de muro"
        }
    )

    return resultados

# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES DE MURO DE PIEDRA
# ============================================================

def calcular_materiales_piedra(muros_tipo, desperdicio):

    resultados = []

    # --------------------------------------------------------
    # ÁREA TOTAL DEL MURO
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )

    # --------------------------------------------------------
    # PIEDRA
    # --------------------------------------------------------

    cantidad_piedra = (
        area_total
        * 0.50
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Piedra",
            "unidad": "m³",
            "cantidad": cantidad_piedra,
            "detalle": "0.50 m³ por m² de muro"
        }
    )

    # --------------------------------------------------------
    # MORTERO CEMENTO-ARENA
    # --------------------------------------------------------

    cantidad_mortero = (
        area_total
        * 0.025
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Mortero cemento-arena",
            "unidad": "m³",
            "cantidad": cantidad_mortero,
            "detalle": "0.025 m³ por m² de muro"
        }
    )

    return resultados

# ============================================================
# TIPOS DE MURO UTILIZADOS
# ============================================================

tipos_materiales_utilizados = []


for muro in muros:

    if (
        muro["area_neta"] > 0
        and muro["tipo"] not in tipos_materiales_utilizados
    ):

        tipos_materiales_utilizados.append(
            muro["tipo"]
        )


# ============================================================
# MOSTRAR MENSAJE SI NO HAY MUROS
# ============================================================

if len(tipos_materiales_utilizados) == 0:

    st.info(
        "Captura al menos un muro con un área mayor a "
        "0.00 m² para generar el listado de materiales."
    )


# ============================================================
# GENERAR MATERIALES
# ============================================================

else:

    for tipo in tipos_materiales_utilizados:


        # ----------------------------------------------------
        # MUROS DEL TIPO ACTUAL
        # ----------------------------------------------------

        muros_tipo = [
            muro
            for muro in muros
            if muro["tipo"] == tipo
            and muro["area_neta"] > 0
        ]


        # ----------------------------------------------------
        # ÁREA TOTAL DEL TIPO
        # ----------------------------------------------------

        area_tipo = sum(
            muro["area_neta"]
            for muro in muros_tipo
        )


        # ----------------------------------------------------
        # ENCABEZADO
        # ----------------------------------------------------

        st.markdown(
            f"""
<div class="seccion-mini">
MATERIAL / {html.escape(tipo.upper())}
</div>

<div class="seccion" style="font-size:22px;">
{html.escape(tipo)}
</div>
""",
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
<div class="tarjeta-resultado">

<strong>Área neta cuantificada</strong><br>

<span style="font-size:28px; color:#344238;">
{area_tipo:,.2f} m²
</span>

</div>
""",
            unsafe_allow_html=True
        )
        # ====================================================
        # MATERIALES SEGÚN TIPO DE MURO
        # ====================================================

        materiales = []


        # ====================================================
        # TABLAROCA
        # ====================================================

        if tipo == "Muro de tablaroca":

            materiales = calcular_materiales_tablaroca(
                muros_tipo,
                caras_tablaroca,
                separacion_postes,
                desperdicio
            )


        # ====================================================
        # BLOCK
        # ====================================================

        elif tipo == "Muro de block":

            materiales = calcular_materiales_block(
                muros_tipo,
                desperdicio
            )


        # ====================================================
        # LADRILLO
        # ====================================================

        elif tipo == "Muro de ladrillo":

            materiales = calcular_materiales_ladrillo(
                muros_tipo,
                desperdicio
            )


        # ====================================================
        # CONCRETO
        # ====================================================

        elif tipo == "Muro de concreto":

            materiales = calcular_materiales_concreto(
                muros_tipo,
                desperdicio
            )

        # ============================================================
        # CONCRETO ARMADO
        # ============================================================

        elif tipo == "Muro de concreto armado":

           materiales = calcular_materiales_concreto_armado(
               muros_tipo,
               desperdicio
           )

        # ====================================================
        # TABIQUE ROJO RECOCIDO
        # ====================================================

        elif tipo == "Muro de tabique rojo recocido":

            materiales = calcular_materiales_tabique_rojo(
                muros_tipo,
                desperdicio
            )

        # ============================================================
        # MAMPOSTERÍA
        # ============================================================

        elif tipo == "Muro de mampostería":

           materiales = calcular_materiales_mamposteria(
               muros_tipo,
               desperdicio
           )

        # ============================================================
        # PIEDRA
        # ============================================================

        elif tipo == "Muro de piedra":

           materiales = calcular_materiales_piedra(
               muros_tipo,
               desperdicio
        )

        # ====================================================
        # MOSTRAR MATERIALES
        # ====================================================

        for material in materiales:

            nombre_material = html.escape(
                material["material"]
            )

            unidad_material = html.escape(
                material["unidad"]
            )

            detalle_material = html.escape(
                material["detalle"]
            )

            cantidad_material = material["cantidad"]


            st.markdown(
                f"""
<div class="detalle">

<strong>
{nombre_material}
</strong>

<br><br>

<span style="color:#70766E;">
Unidad: {unidad_material}
</span>

<br>

<span style="color:#70766E;">
Criterio: {detalle_material}
</span>

<br><br>

<strong>
Cantidad estimada:
{cantidad_material:,.2f}
{unidad_material}
</strong>

</div>
""",
                unsafe_allow_html=True
            )


        # ====================================================
        # SEPARADOR ENTRE TIPOS
        # ====================================================

        st.markdown(
            '<div class="linea"></div>',
            unsafe_allow_html=True
        )

# ============================================================
# PREPARAR LIBRO DE EXCEL
# ============================================================

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from io import BytesIO


# ============================================================
# FUNCIÓN PARA DAR FORMATO A LAS HOJAS
# ============================================================

def formatear_hoja(ws):

    # Encabezados
    for cell in ws[1]:

        cell.font = Font(
            bold=True,
            color="FFFFFF"
        )

        cell.fill = PatternFill(
            "solid",
            fgColor="344238"
        )

        cell.alignment = Alignment(
            horizontal="center",
            vertical="center"
        )

    # Bordes
    borde = Border(
        bottom=Side(
            style="thin",
            color="DCD8CA"
        )
    )

    for row in ws.iter_rows():

        for cell in row:

            cell.border = borde
            cell.alignment = Alignment(
                vertical="center"
            )

    # Ajustar columnas
    for columna in ws.columns:

        max_length = 0

        letra = get_column_letter(
            columna[0].column
        )

        for cell in columna:

            if cell.value is not None:

                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        ws.column_dimensions[
            letra
        ].width = min(
            max_length + 3,
            45
        )


# ============================================================
# CREAR LIBRO
# ============================================================

wb = Workbook()


# ============================================================
# HOJA 1 — INFORMACIÓN DEL PROYECTO
# ============================================================

ws_proyecto = wb.active

ws_proyecto.title = "Proyecto"

ws_proyecto.append([
    "Campo",
    "Información"
])

ws_proyecto.append([
    "Nombre del proyecto",
    nombre_proyecto if nombre_proyecto else "Sin capturar"
])

ws_proyecto.append([
    "Ubicación",
    ubicacion_proyecto if ubicacion_proyecto else "Sin capturar"
])

ws_proyecto.append([
    "Plano arquitectónico",
    archivo_plano.name if archivo_plano else "Sin plano cargado"
])

ws_proyecto.append([
    "Sistema",
    "TRAZA | Generadores de Obra"
])

ws_proyecto.append([
    "Generador",
    "Cuantificación de muros"
])

formatear_hoja(ws_proyecto)


# ============================================================
# HOJA 2 — CUADRO DE MUROS
# ============================================================

ws_muros = wb.create_sheet(
    "Cuadro de Muros"
)

ws_muros.append([
    "Clave",
    "Tipo de muro",
    "Largo (m)",
    "Alto (m)",
    "Área bruta (m²)",
    "Descuento vanos (m²)",
    "Área neta (m²)"
])


for muro in muros:

    ws_muros.append([
        f"MU-{muro['numero']:02d}",
        muro["tipo"],
        muro["largo"],
        muro["alto"],
        muro["area_bruta"],
        muro["descuento"],
        muro["area_neta"]
    ])


# TOTAL

ws_muros.append([])

ws_muros.append([
    "TOTAL",
    "",
    "",
    "",
    total_bruto,
    total_descuentos,
    total_muros
])

formatear_hoja(ws_muros)


# ============================================================
# HOJA 3 — CATÁLOGO DE CONCEPTOS
# ============================================================

ws_catalogo = wb.create_sheet(
    "Catálogo"
)

ws_catalogo.append([
    "Clave",
    "Tipo de muro",
    "Concepto",
    "Unidad",
    "Cantidad"
])


for indice, tipo in enumerate(
    tipos_utilizados,
    start=1
):

    cantidad_tipo = sum(
        muro["area_neta"]
        for muro in muros
        if muro["tipo"] == tipo
    )

    concepto = conceptos.get(
        tipo,
        ""
    ).strip()

    if concepto == "":
        concepto = "Sin concepto capturado"

    ws_catalogo.append([
        f"MU-{indice:02d}",
        tipo,
        concepto,
        "m²",
        cantidad_tipo
    ])


formatear_hoja(ws_catalogo)


# ============================================================
# HOJA 4 — MATERIALES
# ============================================================

ws_materiales = wb.create_sheet(
    "Materiales"
)

ws_materiales.append([
    "Tipo de muro",
    "Material",
    "Unidad",
    "Cantidad estimada",
    "Criterio"
])

# ============================================================
# MATERIALES POR TIPO DE MURO
# ============================================================

for tipo in tipos_materiales_utilizados:

    muros_tipo_exportacion = [
        muro
        for muro in muros
        if muro["tipo"] == tipo
        and muro["area_neta"] > 0
    ]

    area_tipo_exportacion = sum(
        muro["area_neta"]
        for muro in muros_tipo_exportacion
    )

    # --------------------------------------------------------
    # TABLAROCA
    # --------------------------------------------------------

    if tipo == "Muro de tablaroca":

        materiales_exportacion = calcular_materiales_tablaroca(
            muros_tipo_exportacion,
            caras_tablaroca,
            separacion_postes,
            desperdicio
        )

        for material in materiales_exportacion:

            ws_materiales.append([
                tipo,
                material["material"],
                material["unidad"],
                material["cantidad"],
                material["detalle"]
            ])

    # --------------------------------------------------------
    # BLOCK
    # --------------------------------------------------------

    elif tipo == "Muro de block":

        materiales_block_exportacion = [

            (
                "Block de concreto",
                "pza",
                area_tipo_exportacion * 12.50,
                "12.50 piezas/m²"
            ),

            (
                "Mortero",
                "m³",
                area_tipo_exportacion * 0.020,
                "0.020 m³/m²"
            ),

            (
                "Cemento",
                "kg",
                area_tipo_exportacion * 4.50,
                "4.50 kg/m²"
            ),

            (
                "Arena",
                "m³",
                area_tipo_exportacion * 0.020,
                "0.020 m³/m²"
            )
        ]

        for material, unidad, cantidad, criterio in materiales_block_exportacion:

            cantidad = cantidad * (1 + desperdicio)

            ws_materiales.append([
                tipo,
                material,
                unidad,
                cantidad,
                criterio
            ])

    # --------------------------------------------------------
    # LADRILLO
    # --------------------------------------------------------

    elif tipo == "Muro de ladrillo":

        materiales_ladrillo_exportacion = [

            (
                "Ladrillo",
                "pza",
                area_tipo_exportacion * 16.00,
                "16.00 piezas/m²"
            ),

            (
                "Mortero",
                "m³",
                area_tipo_exportacion * 0.025,
                "0.025 m³/m²"
            ),

            (
                "Cemento",
                "kg",
                area_tipo_exportacion * 5.00,
                "5.00 kg/m²"
            ),

            (
                "Arena",
                "m³",
                area_tipo_exportacion * 0.025,
                "0.025 m³/m²"
            )
        ]

        for material, unidad, cantidad, criterio in materiales_ladrillo_exportacion:

            cantidad = cantidad * (1 + desperdicio)

            ws_materiales.append([
                tipo,
                material,
                unidad,
                cantidad,
                criterio
            ])

    # --------------------------------------------------------
    # TABIQUE ROJO RECOCIDO
    # --------------------------------------------------------

    elif tipo == "Muro de tabique rojo recocido":

        materiales_tabique_exportacion = [

            (
                "Tabique rojo recocido",
                "pza",
                area_tipo_exportacion * 16.00,
                "16.00 piezas/m²"
            ),

            (
                "Mortero cemento-arena",
                "m³",
                area_tipo_exportacion * 0.025,
                "0.025 m³/m²"
            ),

            (
                "Cemento",
                "kg",
                area_tipo_exportacion * 5.00,
                "5.00 kg/m²"
            ),

            (
                "Arena",
                "m³",
                area_tipo_exportacion * 0.025,
                "0.025 m³/m²"
            )
        ]

        for material, unidad, cantidad, criterio in materiales_tabique_exportacion:

            cantidad = cantidad * (1 + desperdicio)

            ws_materiales.append([
                tipo,
                material,
                unidad,
                cantidad,
                criterio
            ])

        # --------------------------------------------------------
    # CONCRETO
    # --------------------------------------------------------

    elif tipo == "Muro de concreto":

        materiales_concreto_exportacion = [

            (
                "Concreto",
                "m³",
                area_tipo_exportacion * 0.12 * (1 + desperdicio),
                "0.12 m³/m²"
            )
        ]

        for material, unidad, cantidad, criterio in (
            materiales_concreto_exportacion
        ):

            ws_materiales.append([
                tipo,
                material,
                unidad,
                cantidad,
                criterio
            ])

    # --------------------------------------------------------
    # CONCRETO ARMADO
    # --------------------------------------------------------

    elif tipo == "Muro de concreto armado":

        materiales_concreto_armado_exportacion = [

            (
                "Concreto",
                "m³",
                area_tipo_exportacion * 0.15,
                "0.15 m³/m² de muro"
            ),

            (
                "Acero de refuerzo",
                "kg",
                area_tipo_exportacion * 10.00,
                "10.00 kg/m² de muro"
            ),

            (
                "Alambre recocido",
                "kg",
                area_tipo_exportacion * 0.20,
                "0.20 kg/m² de muro"
            ),

            (
                "Cimbra",
                "m²",
                area_tipo_exportacion * 2.00,
                "2.00 m²/m² de muro"
            )
        ]

        for material, unidad, cantidad, criterio in materiales_concreto_armado_exportacion:

            cantidad = cantidad * (1 + desperdicio)

            ws_materiales.append([
                tipo,
                material,
                unidad,
                cantidad,
                criterio
            ])

    # --------------------------------------------------------
    # MAMPOSTERÍA
    # --------------------------------------------------------

    elif tipo == "Muro de mampostería":

        materiales_mamposteria_exportacion = [

            (
                "Piedra",
                "m³",
                area_tipo_exportacion * 0.50,
                "0.50 m³/m² de muro"
            ),

            (
                "Mortero cemento-arena",
                "m³",
                area_tipo_exportacion * 0.020,
                "0.020 m³/m² de muro"
            )
        ]

        for material, unidad, cantidad, criterio in materiales_mamposteria_exportacion:

            cantidad = cantidad * (1 + desperdicio)

            ws_materiales.append([
                tipo,
                material,
                unidad,
                cantidad,
                criterio
            ])

    # --------------------------------------------------------
    # PIEDRA
    # --------------------------------------------------------

    elif tipo == "Muro de piedra":

        materiales_piedra_exportacion = [

            (
                "Piedra",
                "m³",
                area_tipo_exportacion * 0.50,
                "0.50 m³/m² de muro"
            ),

            (
                "Mortero cemento-arena",
                "m³",
                area_tipo_exportacion * 0.025,
                "0.025 m³/m² de muro"
            )
        ]

        for material, unidad, cantidad, criterio in materiales_piedra_exportacion:

            cantidad = cantidad * (1 + desperdicio)

            ws_materiales.append([
                tipo,
                material,
                unidad,
                cantidad,
                criterio
            ])


formatear_hoja(ws_materiales)

# ============================================================
# CREAR ARCHIVO EXCEL EN MEMORIA
# ============================================================

excel_buffer = BytesIO()

wb.save(
    excel_buffer
)

excel_buffer.seek(0)

# ============================================================
# 06 / RESUMEN GENERAL
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">06 / Resumen</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Resumen general del proyecto</div>',
    unsafe_allow_html=True
)

st.write(
    "Vista general de la cuantificación generada por TRAZA."
)


# ============================================================
# DATOS PRINCIPALES
# ============================================================

nombre_resumen = (
    nombre_proyecto.strip()
    if nombre_proyecto.strip()
    else "Sin nombre capturado"
)

ubicacion_resumen = (
    ubicacion_proyecto.strip()
    if ubicacion_proyecto.strip()
    else "Sin ubicación capturada"
)


# ============================================================
# TARJETA PRINCIPAL DEL PROYECTO
# ============================================================

st.markdown(
    f"""
<div class="tarjeta">

<div class="seccion-mini">
INFORMACIÓN DEL PROYECTO
</div>

<div style="
    font-size:26px;
    font-weight:700;
    color:#344238;
    margin-top:8px;
">
{html.escape(nombre_resumen)}
</div>

<div style="
    color:#70766E;
    font-size:15px;
    margin-top:8px;
">
📍 {html.escape(ubicacion_resumen)}
</div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# INDICADORES GENERALES
# ============================================================

col_res1, col_res2, col_res3, col_res4 = st.columns(4)

with col_res1:

    st.metric(
        "Muros cuantificados",
        len(muros)
    )

with col_res2:

    st.metric(
        "Área bruta",
        f"{total_bruto:,.2f} m²"
    )

with col_res3:

    st.metric(
        "Descuentos",
        f"{total_descuentos:,.2f} m²"
    )

with col_res4:

    st.metric(
        "Área neta",
        f"{total_muros:,.2f} m²"
    )


# ============================================================
# TIPOS DE MURO
# ============================================================

st.markdown(
    '<div class="seccion">Sistemas constructivos utilizados</div>',
    unsafe_allow_html=True
)

if len(tipos_utilizados) == 0:

    st.info(
        "Aún no existen tipos de muro con área cuantificada."
    )

else:

    for tipo in tipos_utilizados:

        area_tipo_resumen = sum(
            muro["area_neta"]
            for muro in muros
            if muro["tipo"] == tipo
        )

        cantidad_muros_tipo = sum(
            1
            for muro in muros
            if muro["tipo"] == tipo
        )

        st.markdown(
            f"""
<div class="detalle">

<strong>
{html.escape(tipo)}
</strong>

<br><br>

<span style="color:#70766E;">
Muros: {cantidad_muros_tipo}
</span>

<br>

<span style="color:#70766E;">
Área cuantificada: {area_tipo_resumen:,.2f} m²
</span>

</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# RESUMEN DE MATERIALES
# ============================================================

st.markdown(
    '<div class="seccion">Materiales estimados</div>',
    unsafe_allow_html=True
)

cantidad_tipos_material = len(
    tipos_materiales_utilizados
)

st.markdown(
    f"""
<div class="tarjeta-verde">

<div class="label">
SISTEMAS CON MATERIALES CALCULADOS
</div>

<div class="numero">
{cantidad_tipos_material}
</div>

<div style="
    color:#C8D1C3;
    margin-top:6px;
">
Sistema(s) constructivo(s)
</div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# ESTADO DEL PROYECTO
# ============================================================

st.markdown(
    '<div class="seccion">Estado de la cuantificación</div>',
    unsafe_allow_html=True
)

if len(muros) > 0 and total_muros > 0:

    st.success(
        "✓ Cuantificación de muros generada correctamente."
    )

else:

    st.warning(
        "La cuantificación está pendiente de captura."
    )

# ============================================================
# EXPORTACIÓN
# ============================================================

st.markdown(
    '<div class="seccion-mini">07 / Exportación</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="tarjeta">
<div class="seccion-mini">
ARCHIVO DE CUANTIFICACIÓN
</div>

<div style="
    font-size:18px;
    font-weight:600;
    margin-top:10px;
">
TRAZA_Cuantificacion_Completa.xlsx
</div>

<div style="
    color:#70766E;
    margin-top:14px;
    line-height:1.7;
">
El archivo incluye información del proyecto,
cuadro de muros, catálogo de conceptos
y materiales estimados.
</div>

</div>
""",
    unsafe_allow_html=True
)


st.download_button(
    label="⬇ Descargar cuantificación completa en Excel",
    data=excel_buffer.getvalue(),
    file_name="TRAZA_Cuantificacion_Completa.xlsx",
    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    ),
    use_container_width=True
)


# ============================================================
# RESUMEN DE ARCHIVOS
# ============================================================

st.markdown(
    '<div class="seccion">Contenido del archivo</div>',
    unsafe_allow_html=True
)


col_exp1, col_exp2, col_exp3, col_exp4 = st.columns(4)


with col_exp1:

    st.markdown(
        """
<div class="tarjeta">
<strong>01</strong><br><br>
Información del proyecto
</div>
""",
        unsafe_allow_html=True
    )


with col_exp2:

    st.markdown(
        """
<div class="tarjeta">
<strong>02</strong><br><br>
Cuadro de muros
</div>
""",
        unsafe_allow_html=True
    )


with col_exp3:

    st.markdown(
        """
<div class="tarjeta">
<strong>03</strong><br><br>
Catálogo de conceptos
</div>
""",
        unsafe_allow_html=True
    )


with col_exp4:

    st.markdown(
        """
<div class="tarjeta">
<strong>04</strong><br><br>
Materiales
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# MENSAJE FINAL
# ============================================================

st.success(
    "TRAZA ha generado correctamente el archivo "
    "de cuantificación completa."
)