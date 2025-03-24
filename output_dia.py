import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
from cloud import render_wordcloud
from funciones import extraer_secciones

# Configuración de página
st.set_page_config(
    page_title="Monitor EEUU-LATAM | CEPAL Lab",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargar CSS desde un archivo externo
with open("style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


periodo = "Análisis de Noticias: Impacto de la Administración Trump en América Latina, el Caribe y el Mundo (3-16 de marzo de 2025)"
# Sidebar para navegación
#st.sidebar.title("Contenido")
#st.sidebar.markdown("### Reporte EEUU-LATAM")
#st.sidebar.markdown(periodo)

#pages = {
#    "Resumen Ejecutivo": "Principales hallazgos de la semana",
#    "1. Principales Temas": "Decisiones de EE.UU. con impacto en LATAM",
#    "2. Detalle de Implicancias": "Comercio, inversión, migración y seguridad",
#    "3. Detalle por Países": "Análisis por país y posibles impactos",
#    "4. Áreas Críticas": "Variables para monitoreo futuro"
#}

#for page, description in pages.items():
#    st.sidebar.markdown(f"[{page}](#{page.lower().replace(' ', '-').replace('.', '')})")
#    st.sidebar.markdown(f"<span class='small-text'>{description}</span>", unsafe_allow_html=True)

#st.sidebar.markdown("---")
#st.sidebar.markdown("### Contacto")
#st.sidebar.markdown("lab_cepal@un.org")
#st.sidebar.markdown("Tel: +1 (xxx) xxx-xxxx")

# Encabezado
# CSS personalizado para el encabezado
st.markdown("""

<div class="header-banner">
    <div class="header-slogan">Monitor de noticias EEUU - Latinoamérica</div>
</div>

<div class="navbar">
    <div class="nav-left">
        <div class="nav-item">Análisis de noticias de impacto para la región</div>
        </div>
    <div class="nav-right">
        <div class="nav-item">Semana del 3 al 16 de marzo, 2025</div>
        <div class="nav-item">🌎 CEPAL LAB</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("")
# Cargar el archivo de audio (puede estar en la misma carpeta o una URL)
audio_file = open('resumen_mar_02.mp3', 'rb')
audio_bytes = audio_file.read()

columna1, columna2, columna3, columna4 = st.columns([1,1,1,1])

 
with columna4:
    st.markdown("""
<div style='text-align: left; font-style: italic; font-size: 16px; color: gray;'>
    Resumen en audio (7min)
</div>
""", unsafe_allow_html=True)
    # Mostrar el reproductor
    st.audio(audio_bytes, format='audio/mp3')



# Contenido de la aplicación

# Leer el contenido del archivo markdown
with open("resumen.md", "r", encoding="utf-8") as file:
    resumen_contenido = file.read()
st.markdown("")
st.info("""
## Resumen Ejecutivo
En la semana del 3 al 16 de marzo de 2025, las decisiones de la administración Trump marcaron la agenda global con un fuerte impacto en América Latina y el Caribe. La imposición de aranceles a México, Canadá, la Unión Europea y China desató una guerra comercial en evolución, con represalias y efectos significativos en sectores clave como el automotriz y el acero, especialmente en México y Brasil. Al mismo tiempo, la intención de Trump de “recuperar” el Canal de Panamá y aumentar la presencia militar en la región generó preocupación sobre la soberanía panameña y la creciente rivalidad entre EE.UU. y China. En Venezuela, las nuevas sanciones y la salida de Chevron profundizaron la crisis económica, con efectos colaterales en países vecinos debido a la migración y disputas territoriales.

Por otro lado, las políticas migratorias de Trump endurecieron las deportaciones y redujeron los cruces fronterizos, con implicaciones en varios países de la región receptores de migrantes. En el ámbito político, la elección de Albert Ramdin como secretario general de la OEA abre interrogantes sobre su papel en un contexto de tensiones regionales. Además, se destacan la suspensión de fondos de cooperación de USAID, la expansión del crimen organizado y el conflicto en Ucrania como factores de riesgo adicionales. En conjunto, la semana estuvo marcada por incertidumbre económica, tensiones geopolíticas y desafíos en materia de derechos humanos, configurando un escenario volátil que requiere un seguimiento cercano.
""")

st.header("Principales eventos noticiosos")
st.markdown("Noticias más relevantes durante la semana respecto a las relaciones de Estados Unidos con Latinoamérica.")
secciones = extraer_secciones(resumen_contenido)

for titulo_seccion, contenido_seccion in secciones.items():
    with st.expander(f"**{titulo_seccion}**"):
        st.markdown(contenido_seccion, unsafe_allow_html=True)
        



# Resumen ejecutivo
#st.markdown(resumen_contenido)

###### SECCIÓN 1: PRINCIPALES TEMAS ######
st.header("Temas mas frecuentes")
st.markdown("Los 100 tópicos más recurrentes en las noticias de la semana analizadas")

# Crear datos de ejemplo para el gráfico de principales temas
temas_data = pd.DataFrame({
    'Tema': ['economía', 'aranceles', 'relaciones internacionales', 'política internacional', 'sanciones', 'gobierno', 'petróleo', 'gobierno y política', 'organizaciones internacionales'],
    'Menciones': [16, 15, 11, 11, 9, 9, 8, 7, 7],
    'Impacto Potencial': [9,8.9, 8.8, 8.7, 8.5, 8.3, 8.2, 8, 7.8]
})

col1, col2 = st.columns([2, 1])

with col1:
    render_wordcloud()

with col2:
    st.header("Asuntos clave")
    st.markdown("""
    Sheinbaum y Trump acordaron postergar los **aranceles** de EE.UU. y seguir cooperando en **migración** y **seguridad**. 
    
    Sin embargo, **aranceles** del 25% a todas las importaciones de acero y aluminio a Estados Unidos entraron en vigor generando reacciones de la UE y China.
    
    La **política internacional** de EEUU genera incertidumbre y expectativas a la baja en desempeño de la **economía** mundial.
    """)



###### SECCIÓN 2: DETALLE DE IMPLICANCIAS ######
st.header("Datos relevantes por categoría")

# Crear datos simulados
comercio_data = {
    'Categoría': ['Materias primas', 'Manufacturas', 'Servicios', 'Energía', 'Agricultura'],
    'Cambio % Esperado': [3.5, -1.2, 0.8, 4.7, 2.1]
}

inversion_data = {
    'Temas': ['Petróleo', 'Finanzas', 'Política Económica', 'Inversión extranjera', 'Crecimiento'],
    'Frecuencia': [37, 24, 20, 12, 10],
    'Size': [12, 12, 12, 12, 12]
}

migracion_data = pd.DataFrame({
    'País': ['México', 'Guatemala', 'Honduras', 'El Salvador', 'Colombia', 'Venezuela'],
    'Remesas (MM USD)': [4200, 950, 720, 620, 350, 180],
    'Impacto Migratorio': [8, 9, 9, 7, 6, 10]  # Escala 1-10
})

seguridad_data = pd.DataFrame({
    'Área': ['Narcotráfico', 'Crimen organizado', 'Violencia', 'Seguridad fronteriza', 'Desapariciones'],
    'Índice de Cooperación': [17, 16, 10, 4, 7],  # Escala 1-10
    'Financiamiento US (MM USD)': [17, 16, 10, 4, 4]
})

# Crear tabs para cada categoría
tab1, tab2, tab3, tab4 = st.tabs(["Comercio Internacional", "Economía", "Migración", "Seguridad"])

with tab1:
    #st.subheader("Impacto Comercial")
    
    st.markdown("""
        * El **83,8% de los más de 600.000 millones de dólares** en exportaciones mexicanas fueron hacia Estados Unidos (2024) 
                <a href="https://americaeconomica.com/noticia/mexico/la-presidenta-de-mexico-dice-que-prevalecio-el-dialogo-con-trump-para-postergar-los-aranceles.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>

        * La industria automotriz mexicana aporta la **tercera parte de las exportaciones** a Estados Unidos (2024).<a href="https://americaeconomica.com/noticia/mexico/la-presidenta-de-mexico-dice-que-prevalecio-el-dialogo-con-trump-para-postergar-los-aranceles.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>
        * Los **principales exportadores de acero** a Estados Unidos son Canadá, México, Brasil, Corea del Sur y Japón. La mayor parte de las importaciones estadounidenses de aluminio proceden de Canadá. <a href="https://lancasteronline.com/lavoz/estados-unidos/trump-promete-recuperar-riqueza-robada-al-entrar-en-vigor-aranceles-al-acero-y-aluminio/article_9ffa3ae9-be9e-583e-bb69-ac5a3be3be91.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>
        * La Unión Europea anunció contramedidas, con aranceles por un valor de **26.000 millones de euros** (alrededor de 28.000 millones de dólares) a partir del 1 de abril, afectando a productos de acero, aluminio, textiles, electrodomésticos y productos agrícolas. <a href="https://lancasteronline.com/lavoz/estados-unidos/trump-promete-recuperar-riqueza-robada-al-entrar-en-vigor-aranceles-al-acero-y-aluminio/article_9ffa3ae9-be9e-583e-bb69-ac5a3be3be91.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>
        
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("Datos Económicos")
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        inversion_df = pd.DataFrame(inversion_data)
        fig = px.bar(
            inversion_df,
            x='Temas',
            y='Frecuencia',
            #size='Size',
            color='Size',
            color_continuous_scale='Blues',
            #size_max=50,
            #height=400
        )
        fig.update_layout(
            title='Temas económicos más mencionados',
            plot_bgcolor='white',
            yaxis_title='Frecuencia en noticias',
            xaxis_title='',
            showlegend=False,
            margin=dict(t=50, b=0, l=0, r=0)
        )

        fig.update_coloraxes(showscale=False)  # Esto oculta la barra de colores

        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        #### Cifras de interés
        
        Se estima que de concretarse la imposición de aranceles generales México podría enfrentar una **contracción de más de 1%** del Producto Interno Bruto en 2025.
        
        Suspensión de inversiones de relocalización en México. A la  fecha solo se han confirmado seis proyectos de relocalización por **10.000 millones de dólares**, que representan 6% de los anuncios de inversiones comprometidas.
        
        Chevron, en asociación con Petróleos de Venezuela (Pdvsa), alcanzó una producción de más de **200.000 barriles diarios en 2024**, de acuerdo con datos del Servicio de Investigación del Congreso de EEUU.
                    
        La Autoridad del Canal de Panamá invertirá **$8,000 millones** en la próxima década en el desarrollo de proyectos para mantener la vigencia de la ruta interoceánica.
        
        México y Colombia podrían ver una **ralentización significativa** debido a su alta exposición a EE UU, economías más diversificadas como Chile y Perú podrían mantener un **crecimiento moderado**. Brasil, enfrenta el dilema entre **controlar los precios y mantener la inversión extranjera** en un contexto de volatilidad global.            
        """)

with tab3:
    #st.subheader("Dinámica Migratoria")
       
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Cifras Clave
        
        • En 2024, con más de **64 mil millones de dólares**, las remesas fueron la principal fuente de divisas de la economía mexicana.
        
        • En Honduras las remesas familiares sumaron **$1,597.6 millones** en el primer bimestre de 2025, representando un crecimiento del 21,8% respecto al mismo período de 2024.
        
        • República Dominicana recibió remesas por un total de **1.852 millones de dólares** entre enero y febrero de 2025. Crecimiento de 8.3% respecto a mismo período de 2024.
        """)
    
    with col2:
        st.markdown("""
        #### Movimientos migratorios
        
        El número de migrantes que cruzaron el Tapón del Darién hacia Panamá en enero y febrero cayó un **95,8%** respecto al mismo período en 2024.
        
        El secretario de Estado de EE.UU. confirmó que cerca de **250 miembros del Tren de Aragua** fueron enviados a cárceles de El Salvador. Expertos califican traslados como ilegales.
        
        **348,000** venezolanos protegidos por el TPS (Estatus de Protección Temporal).
        
        Dos tercios de los 38 millones de mexicanos que viven en Estados Unidos, nacieron en ese territorio. 
        """)

with tab4:
    st.subheader("Temas relacionados con seguridad")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.bar(
            seguridad_data,
            x='Área',
            y='Financiamiento US (MM USD)',
            color='Índice de Cooperación',
            color_continuous_scale='Blues',
            text='Financiamiento US (MM USD)',
            height=400
        )
        fig.update_layout(
            #title='Financiamiento e índice de cooperación por área de seguridad',
            plot_bgcolor='white',
            yaxis_title='Cantidad de artículos',
            xaxis_title='',
            coloraxis_colorbar_title='Índice de<br>Cooperación',
            margin=dict(t=50, b=0, l=0, r=0)
        )
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        fig.update_coloraxes(showscale=False)  # Esto oculta la barra de colores
        st.plotly_chart(fig, use_container_width=True)
        
    
    with col2:
        st.markdown("""
        #### Hechos relevantes
        
        • En el marco de la lucha del gobierno de Estados Unidos contra los cárteles de la droga de México, la Red de Control de Delitos Financieros del Departamento del Tesoro (FinCen) comenzó con acciones para interrumpir los flujos financieros ilícitos de estas organizaciones que transiten por el sistema financiero de EEUU.
        
        • La Embajada de Estados Unidos y la Policía colombiana ofrecen un total de $12 millones de dólares por la captura de tres líderes del Tren de Aragua.
        
        • Cerca de 200 de los inmigrantes arrestados en Houston fueron detenidos por delitos relacionados con narcóticos.
        """)

###### SECCIÓN 3: DETALLE POR PAÍSES ######
st.header("Detalle por Países")

# Datos de ejemplo para países
paises_data = pd.DataFrame({
    'País': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 'Dominican Republic', 'Surinam', 'Uruguay', 'Venezuela'],
    'Menciones': [10, 14, 33, 23, 38, 6, 14, 24, 12, 3, 10, 9, 11, 135, 11, 50, 12, 10, 1, 17, 24, 19, 87],
    'Áreas Clave': [['aranceles', 'comercio internacional', 'política comercial', 'desigualdad económica', 'globalización'], ['organizaciones internacionales', 'política internacional', 'gobierno y política', 'diplomacia', 'relaciones internacionales'], ['política internacional', 'organizaciones internacionales', 'diplomacia', 'gobierno y política', 'relaciones internacionales'], ['organizaciones internacionales', 'política internacional', 'diplomacia', 'gobierno', 'gobierno y política'], ['organizaciones internacionales', 'política internacional', 'aranceles', 'gobierno y política', 'relaciones internacionales'], ['política internacional', 'gobierno', 'liderazgo político', 'organizaciones internacionales', 'relaciones internacionales'], ['organizaciones internacionales', 'política internacional', 'relaciones internacionales', 'diplomacia', 'gobierno y política'], ['migración', 'relaciones internacionales', 'política', 'derechos humanos', 'economía'], ['deportación', 'migración', 'derechos humanos', 'política migratoria', 'crimen organizado'], ['deportación', 'inmigración', 'migración', 'diplomacia', 'exiliados'], ['petróleo', 'política internacional', 'sanciones', 'corrupción', 'lobby'], ['economía', 'remesas', 'finanzas', 'inversión extranjera', 'migración'], ['elecciones', 'deportación', 'política', 'gobierno', 'inmigración'], ['aranceles', 'economía', 'comercio internacional', 'relaciones internacionales', 'política'], ['organizaciones internacionales', 'política internacional', 'relaciones internacionales', 'democracia', 'diplomacia'], ['relaciones internacionales', 'seguridad nacional', 'presencia militar', 'geopolítica', 'relaciones bilaterales'], ['política internacional', 'organizaciones internacionales', 'diplomacia', 'gobierno', 'relaciones internacionales'], ['aranceles', 'finanzas', 'negocios', 'Microsoft', 'Windows'], ['corrupción', 'delito', 'falta de ética', 'fiscalización', 'justicia penal'], ['economía', 'remesas', 'finanzas', 'inversión extranjera', 'crecimiento económico'], ['organizaciones internacionales', 'política internacional', 'diplomacia', 'relaciones internacionales', 'gobierno y política'], ['organizaciones internacionales', 'política internacional', 'gobierno', 'relaciones internacionales', 'gobierno y política'], ['petróleo', 'migración', 'sanciones', 'política internacional', 'relaciones internacionales']]
    })

# Mapa interactivo de Latinoamérica
st.markdown('''
Este mapa permite visualizar los países mas mencionados durante la semana. A través del selector por país puede verse en detalle hechos relevantes
            y áreas clave de seguimiento respecto a los países con mayores menciones en los artículos seleccionados.
            ''')
#st.subheader("Menciones por país")

# Crear un mapa de calor para visualizar impacto por país
impact_map = pd.DataFrame({
    'País': paises_data['País'],
    'Menciones': paises_data['Menciones'],
    'Temas': paises_data['Áreas Clave']
})

fig = px.choropleth(
    impact_map,
    locations='País',
    locationmode='country names',
    color='Menciones',
    color_continuous_scale='Blues',
    height=700,
    #title='Mapa de impacto potencial en Latinoamérica',
    # Añadir hover_data para mejorar los popups
    hover_name='País',
    hover_data={'País': False, 'Menciones': True, 'Temas':True}
)

# Ajustar el mapa para mostrar Latinoamérica correctamente
fig.update_geos(
    visible=False,  # Quita el fondo de océanos/tierra
    lataxis_range=[-60, 35],
    lonaxis_range=[-120, -30],
    showcoastlines=True,
    coastlinecolor="darkgray",
    showland=True,
    landcolor="lightgray",
    showcountries=True,
    countrycolor="darkgray",
    framewidth=0  # Elimina el borde alrededor del mapa
)

fig.update_layout(
    margin=dict(t=50, b=0, l=0, r=0),
    coloraxis_colorbar_title='Cantidad de<br>artículos',
    geo=dict(
        showframe=False,  # Elimina el marco
        projection_type='equirectangular'  # Proyección que funciona bien para mostrar países
    ),
    dragmode = False
)

st.plotly_chart(fig, use_container_width=True)

# Tabla de países
#st.subheader("Países mencionados esta semana")
#st.dataframe(
#    paises_data.style.background_gradient(subset=['Impacto'], cmap='Blues')
#    .format({'Impacto': '{:.1f}/10'})
#    .set_properties(**{'text-align': 'left'})
#    .hide_index(),
#    height=300
#)
#======
#Paises seleccionados solo para el ejemplo
paises = ['Mexico','Brasil','Colombia','Chile','Argentina', 'Panamá', 'Venezuela']
# Detalle de países seleccionados
selected_country = st.selectbox("Seleccione un país para más detalles:", paises)#paises_data['País'])

# Datos específicos por país
country_data = {
    'Mexico': {
        'overview': """
*   **Tensiones Comerciales y Aranceles:** La imposición y posterior suspensión temporal de aranceles por parte de Estados Unidos a productos mexicanos (acero, aluminio y otros) ha generado incertidumbre y volatilidad en la economía mexicana. La amenaza de aranceles se utiliza como herramienta de presión en temas de seguridad y migración.
*   **Negociaciones y Diálogo:** A pesar de las tensiones, se observa un esfuerzo por mantener el diálogo entre los presidentes Trump y Sheinbaum, logrando prórrogas en la aplicación de aranceles.
*   **Cooperación en Seguridad:** México ha intensificado medidas para controlar el flujo de fentanilo y la migración irregular hacia Estados Unidos, incluyendo el despliegue de la Guardia Nacional en la frontera y la extradición de narcotraficantes.
*   **Impacto Económico:** La incertidumbre generada por las políticas comerciales de Estados Unidos ha provocado la suspensión de inversiones, la reubicación de empresas y la depreciación del peso mexicano.
*   **Remesas:** Se destaca la importancia de las remesas enviadas por mexicanos en Estados Unidos como fuente clave de divisas para México.
*   **Sector Automotriz:** El sector automotriz mexicano, altamente dependiente de las exportaciones a Estados Unidos, se ve particularmente afectado por las tensiones comerciales.
*   **Apoyo Interno a Sheinbaum:** La presidenta Sheinbaum ha logrado consolidar el apoyo interno a través de una postura firme en defensa de la soberanía y el diálogo con Estados Unidos.
        """,
        'key_areas': """
*   **Comercio Internacional:** La imposición de aranceles y la posible renegociación del T-MEC representan riesgos significativos para la economía mexicana.
*   **Seguridad:** Una posible intervención militar de Estados Unidos en México y la designación de cárteles como organizaciones terroristas podrían generar tensiones y afectar la soberanía nacional.
*   **Migración:** Las políticas migratorias restrictivas de Estados Unidos podrían afectar el flujo de remesas y generar inestabilidad social en México.
*   **Cooperación:** Los recortes en la ayuda estadounidense podrían afectar programas clave en México, como la prevención de la violencia y la atención a víctimas de desaparición forzada.
*   **Economía:** La incertidumbre generada por las políticas de Estados Unidos podría afectar la inversión extranjera y el crecimiento económico de México.
*   **China:** La creciente influencia de China en las importaciones mexicanas podría generar tensiones con Estados Unidos.

    """
    },
    'Brasil': {
        'overview': """
*   **Elección de Albert Ramdin como Secretario General de la OEA:** La elección del candidato surinamés, con el respaldo de Brasil y otros gobiernos de izquierda, pero sin el apoyo explícito de EE.UU., sugiere un posible distanciamiento entre la OEA y la administración Trump. Se anticipan posibles choques, especialmente en temas relacionados con China y la gestión de crisis en países como Venezuela, Cuba y Nicaragua.
*   **Tensiones Comerciales:** La imposición de aranceles al acero y aluminio por parte de EE.UU. afecta significativamente a Brasil, generando tensiones y llamados al respeto mutuo por parte del presidente Lula. Se anticipan negociaciones difíciles para evitar una escalada de la guerra comercial.
*   **Corrupción y Deforestación:** Se destaca la persistencia de la corrupción en la región, con casos emblemáticos como el escándalo SUDAM en Brasil, que involucra la deforestación de la Amazonía. La lucha contra la corrupción y la protección del medio ambiente siguen siendo desafíos importantes.
        """,
        'key_areas': """
*   **Comercio:** Es crucial monitorear de cerca las negociaciones comerciales entre EE.UU. y Brasil, así como el impacto de los aranceles al acero y aluminio en la economía brasileña. Se deben explorar estrategias para diversificar los mercados y reducir la dependencia de EE.UU.
*   **Cooperación:** Es importante evaluar el impacto de los recortes en la financiación de la OEA y buscar fuentes alternativas de financiamiento para programas clave en áreas como derechos humanos, democracia y desarrollo.


    """
    },
    'Colombia': {
        'overview': """
*   **Recortes en la Cooperación de USAID:** La administración Trump ha implementado recortes significativos en la financiación de la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID), afectando programas clave en Colombia dirigidos a comunidades afrocolombianas e indígenas. Estos recortes han provocado el cierre de varias ONG y la suspensión de proyectos de desarrollo, generando preocupación sobre el impacto en la estabilidad social y la lucha contra el narcotráfico.
*   **Elección del Secretario General de la OEA:** La elección de Albert Ramdin como Secretario General de la OEA, con el apoyo de países de izquierda en la región, ha generado expectativas de un enfoque más dialogante y menos confrontacional en la política hemisférica. Sin embargo, también ha suscitado inquietudes en algunos sectores de Estados Unidos, que temen una menor influencia de Washington en la organización.
*   **Reanudación de Deportaciones:** Se ha reportado un acuerdo entre Venezuela y Estados Unidos para reanudar las deportaciones de migrantes venezolanos, lo que ha generado controversia y críticas por parte de analistas y organizaciones de derechos humanos.
*   **Designación del Tren de Aragua como Organización Terrorista:** El gobierno de Estados Unidos ha designado al Tren de Aragua, una banda criminal originaria de Venezuela, como organización terrorista global, lo que ha intensificado la cooperación en materia de seguridad entre Estados Unidos y países como Chile y Colombia.        """,
        'key_areas': """
*   **Impacto de los Recortes en la Cooperación:** Es crucial analizar en detalle el impacto de los recortes de USAID en la estabilidad social, la gobernabilidad y la lucha contra el narcotráfico en países como Colombia. Se deben explorar alternativas de financiación y cooperación para mitigar los efectos negativos de estas medidas.
*   **Gestión de la Migración:** Se requiere un enfoque integral y coordinado para abordar los desafíos de la migración, que incluya políticas de protección de los derechos de los migrantes, programas de desarrollo en los países de origen y una mayor cooperación regional e internacional.
    """
    },
    'Chile': {
        'overview': """
*   **Monitoreo de medidas arancelarias:** El gobierno chileno está monitoreando activamente los posibles impactos de las medidas arancelarias propuestas por Estados Unidos, incluyendo aranceles al cobre y productos agrícolas, así como esfuerzos para disminuir la capacidad económica de China.
*   **Designación del Tren de Aragua como organización terrorista:** Estados Unidos designó al Tren de Aragua, con presencia en Chile, como organización terrorista global. Esto ha llevado a detenciones de miembros de la banda en Chile y a la incautación de armas y drogas.
*   **Elección del Secretario General de la OEA:** Chile, junto con otros países de la región, apoyó la elección de Albert Ramdin como Secretario General de la OEA, quien ha expresado opiniones que difieren de las de Estados Unidos en temas como Venezuela y China.
*   **Propuesta de Alacero a EEUU:** La Asociación Latinoamericana del Acero (Alacero) propuso a Estados Unidos sustituir las importaciones siderúrgicas de China, en lugar de aplicar aranceles.
        """,
        'key_areas': """
*   **Comercio Internacional:** Es crucial monitorear de cerca las políticas comerciales de Estados Unidos, especialmente en relación con el cobre y los productos agrícolas, y evaluar las posibles estrategias de diversificación de mercados para mitigar los riesgos.
*   **Seguridad:** La designación del Tren de Aragua como organización terrorista por parte de Estados Unidos requiere una mayor cooperación en materia de seguridad y el intercambio de información para combatir el crimen organizado transnacional.
*   **Economía y Finanzas:** Se debe prestar especial atención a los posibles efectos del "Efecto Trump" en la economía chilena, incluyendo la devaluación de la moneda, la caída de las remesas y las presiones inflacionarias, y tomar medidas para mitigar estos riesgos.
*   **Cooperación Multilateral:** Se debe seguir de cerca el papel de Chile en la OEA y otras organizaciones multilaterales, y buscar formas de promover la cooperación regional y abordar los desafíos comunes.
    """
    },
    'Argentina': {
        'overview': """
*   **Tensiones Comerciales:** La imposición de aranceles del 25% por parte de Estados Unidos a las importaciones de acero y aluminio desde Argentina ha generado represalias por parte de la Unión Europea y Canadá, lo que indica un posible escalamiento de las tensiones comerciales.
*   **Interés en un Acuerdo Comercial:** Paolo Rocca, CEO de Techint, expresó su deseo de que Estados Unidos lidere una alianza de países para contrarrestar la influencia de China en la industria global, sugiriendo un interés en un acuerdo comercial entre Argentina y Estados Unidos.
*   **Competencia en el Sector Energético:** Se anticipa que Argentina competirá con Estados Unidos en la producción de shale oil de Vaca Muerta, lo que podría generar dinámicas competitivas en el mercado energético.
*   **Propuesta de Sustitución de Importaciones:** Alacero propuso a Estados Unidos sustituir las importaciones de acero chino por producción latinoamericana, incluyendo la argentina, en lugar de aplicar aranceles, lo que podría abrir oportunidades para la industria siderúrgica argentina.
        """,
        'key_areas': """
*   **Riesgos en el Comercio:** Es crucial monitorear el impacto de los aranceles impuestos por Estados Unidos en la economía argentina y evaluar posibles medidas de mitigación.
*   **Oportunidades en el Sector Energético:** Se debe analizar el potencial de Vaca Muerta para competir con la producción estadounidense de shale oil y explorar posibles áreas de colaboración en el sector energético.
*   **Dinámicas Geopolíticas:** Se debe prestar atención a las dinámicas geopolíticas en la región y el papel de Estados Unidos en el equilibrio de poder, especialmente en relación con China.
*   **Impacto de Políticas Estadounidenses:** Es fundamental analizar el impacto de las políticas económicas y comerciales de Estados Unidos en la economía argentina y evaluar posibles estrategias de adaptación.
""",
        
    },
    'Panamá': {
        'overview': """
*   **Amenazas a la Soberanía del Canal:** El presidente de Estados Unidos, Donald Trump, ha expresado en repetidas ocasiones su intención de "recuperar" el Canal de Panamá, generando tensiones diplomáticas y preocupación en Panamá.
*   **Planes Militares de EE.UU.:** La Casa Blanca ha solicitado al Departamento de Defensa de EE.UU. que elabore opciones para aumentar la presencia militar estadounidense en Panamá, incluyendo la posibilidad de tomar el control del Canal por la fuerza.
*   **Negación de Panamá:** El gobierno panameño ha negado cualquier plan o contacto para permitir la presencia militar de EE.UU. en su territorio y ha reafirmado su compromiso con la defensa de su soberanía sobre el Canal.
*   **Venta de Puertos:** La venta de la concesión de los puertos de Balboa y Cristóbal por parte de CK Hutchison Holdings (Hong Kong) a un consorcio estadounidense liderado por BlackRock ha generado controversia y ha sido interpretada como una posible respuesta a las presiones de EE.UU.
*   **Inversiones en Infraestructura:** La Autoridad del Canal de Panamá (ACP) planea invertir $8,000 millones en proyectos de infraestructura en la próxima década, incluyendo la construcción de un gasoducto y un reservorio de agua, para mantener la competitividad de la vía interoceánica.
*   **Migración:** La ofensiva de Trump ha provocado una disminución drástica en el flujo migratorio a través del Tapón del Darién, con un aumento en el número de migrantes que regresan a sus países de origen.
*   **Cooperación en Seguridad:** Existe un acuerdo de colaboración entre las Fuerzas de Operaciones Especiales de EE.UU. y el Ministerio de Seguridad de Panamá para el entrenamiento de las fuerzas de seguridad panameñas.
*   **Multilateralismo:** Ante las amenazas de EE.UU., expertos instan a Panamá a defender el multilateralismo y buscar el apoyo de la comunidad internacional en la OEA y la ONU.
        """,
        'key_areas': """
*   **Soberanía y Neutralidad del Canal:** Es crucial que Panamá defienda su soberanía sobre el Canal y garantice su neutralidad, en cumplimiento de los tratados existentes.
*   **Relaciones Bilaterales con EE.UU.:** Panamá debe mantener un diálogo constructivo con EE.UU. para abordar las preocupaciones sobre la influencia china y garantizar la seguridad de la vía interoceánica, sin ceder a presiones que comprometan su soberanía.
*   **Diversificación Económica:** Panamá debe diversificar su economía y reducir su dependencia del Canal, invirtiendo en otros sectores como el turismo, la logística y la tecnología.
*   **Cooperación Regional:** Panamá debe fortalecer la cooperación regional con otros países de América Latina y el Caribe para hacer frente a los desafíos comunes, como la migración, el crimen organizado y el cambio climático.
*   **Inversión en Seguridad:** Panamá debe invertir en el fortalecimiento de sus fuerzas de seguridad para garantizar la seguridad del Canal y combatir el crimen organizado, sin necesidad de recurrir a la presencia militar de EE.UU.
*   **Impacto de las Políticas Migratorias de EE.UU.:** Es importante monitorear el impacto de las políticas migratorias de EE.UU. en el flujo migratorio a través de Panamá y tomar medidas para proteger los derechos de los migrantes.
*   **Adhesión al Tratado de Neutralidad:** Se debe considerar la posibilidad de sumar adhesiones al Tratado de Neutralidad de 1977, buscando el apoyo de la comunidad internacional para garantizar la seguridad del Canal.
*   **Relación con China:** Panamá debe mantener una relación equilibrada con China, buscando oportunidades de cooperación económica sin comprometer su soberanía ni su relación con EE.UU.
        """
    },
        'Venezuela': {
        'overview': """
*   **Endurecimiento de Sanciones:** La administración Trump ha intensificado la presión sobre el gobierno de Nicolás Maduro mediante la revocación de licencias a empresas estadounidenses como Chevron, obligándolas a cesar operaciones en Venezuela. Esto impacta la producción y exportación de petróleo venezolano, crucial para la economía del país.
*   **Suspensión de Vuelos de Deportación:** En respuesta a las sanciones, el gobierno de Maduro suspendió los vuelos de deportación de migrantes venezolanos desde Estados Unidos, utilizando esta medida como herramienta de negociación.
*   **Acusaciones de Conspiración:** El gobierno venezolano acusa a la petrolera ExxonMobil de conspirar para generar un bloqueo económico contra el país y de influir en la decisión de Estados Unidos de revocar la licencia a Chevron.
*   **Reanudación de Deportaciones:** A pesar de las tensiones iniciales, se reporta un acuerdo para reanudar los vuelos de venezolanos deportados desde EE.UU.
*   **Utilización de la Ley de Enemigos Extranjeros:** La administración Trump invocó la Ley de Enemigos Extranjeros para acelerar las deportaciones de miembros del Tren de Aragua, aunque esta medida fue bloqueada temporalmente por un juez federal.
*   **Cooperación con Rusia e Irán:** Ante la presión de EE.UU., Venezuela busca fortalecer la cooperación con Rusia e Irán en diversos sectores, incluyendo el energético y militar.
*   **Búsqueda de Inversión Extranjera:** Maduro declara una apertura total a la inversión extranjera en el sector petrolero, buscando alternativas ante la salida de Chevron.
*   **Reconfiguración de Flujos Migratorios:** Las políticas de línea dura de Trump están alterando los flujos migratorios, con un aumento de migrantes venezolanos que regresan a su país o buscan nuevos destinos como España y Brasil.
*   **Designación del Tren de Aragua como Organización Terrorista:** Estados Unidos designó al Tren de Aragua como organización terrorista, intensificando la persecución de sus miembros y vinculando al grupo con el gobierno de Maduro.
*   **Elección del Nuevo Secretario General de la OEA:** La elección de Albert Ramdin como Secretario General de la OEA genera expectativas de un enfoque más dialogante hacia Venezuela, aunque enfrenta la presión de Estados Unidos para mantener una postura firme contra el gobierno de Maduro.
        """,
        'key_areas': """
*   **Impacto Económico de las Sanciones:** Es crucial analizar el impacto de las sanciones en la economía venezolana, incluyendo la producción petrolera, la inflación y el bienestar de la población.
*   **Dinámica Migratoria:** Se debe monitorear la evolución de los flujos migratorios venezolanos, incluyendo las deportaciones desde EE.UU. y la búsqueda de nuevos destinos por parte de los migrantes.
*   **Cooperación Internacional:** Es importante analizar las implicaciones de la creciente cooperación entre Venezuela y países como Rusia e Irán, así como su impacto en la relación con Estados Unidos.
*   **Seguridad Regional:** Se debe prestar atención a la situación del Tren de Aragua y su impacto en la seguridad regional, así como a las acusaciones de vínculos entre el grupo y el gobierno de Maduro.
*   **Diálogo y Negociación:** Es fundamental explorar las posibilidades de diálogo y negociación entre Estados Unidos y Venezuela, así como el papel que la OEA y otros actores internacionales pueden desempeñar en este proceso.
*   **Implicaciones para la Industria Petrolera:** Analizar las consecuencias de la salida de Chevron y la posible entrada de nuevas empresas, así como el impacto en la producción y exportación de petróleo venezolano.
*   **Disputa Territorial con Guyana:** Monitorear la evolución de la disputa territorial entre Venezuela y Guyana por el Esequibo, y el papel de las empresas petroleras en esta controversia.
*   **Derechos Humanos y Estado de Derecho:** Evaluar el impacto de las políticas de Estados Unidos y Venezuela en los derechos humanos y el estado de derecho en el país, incluyendo la situación de los presos políticos y la libertad de expresión.
        """
    }
}

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('### Hechos clave observados')
    st.markdown(country_data[selected_country]['overview'])
    
    
with col2:
    st.markdown("### Áreas clave de atención")
    st.markdown(country_data[selected_country]['key_areas'])
        
    

st.markdown("---")
# Añadir análisis final de áreas críticas
st.markdown("""
#### Implicaciones para proyecciones económicas 

Es crucial monitorear y analizar el impacto de las políticas de la administración Trump en la economía de América Latina y el Caribe, incluyendo la devaluación de monedas, la caída de remesas y el aumento de la inflación. Se deben identificar medidas para mitigar los riesgos y aprovechar las oportunidades que puedan surgir.
La evolución de los **precios de commodities** seguirá siendo determinante para los exportadores de materias primas, mientras que las **tensiones comerciales entre EE.UU. y China** podrían crear oportunidades de diversificación para países como México y Brasil.
Las **políticas migratorias** representan un factor de riesgo significativo para economías dependientes de remesas, particularmente en Centroamérica, donde podrían afectar hasta un 20% del PIB de algunos países.
De igual manera, se debe prestar atención a las dinámicas geopolíticas en la región y el papel de Estados Unidos en el equilibrio de poder, especialmente en relación con China.

            
""", unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("""
*Este reporte analiza las noticias de la semana centrándose en el impacto de las decisiones de la administración Trump en América Latina, el Caribe y el mundo. 
Se utiliza un enfoque basado en la frecuencia de las noticias y su potencial impacto, prestando atención a los últimos desenlaces como indicadores de tendencias futuras.
La clasificación de noticias, análisis y reportes automatizados asistidos por Inteligencia Artificial se encuentran en un proceso de desarrollo experimental en el cual
es fundamental la validación experta humana. Por lo tanto los resultados de los análisis deben tomarse con la debida cautela.*"

""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown('<p class="small-text">Reporte preparado por CEPAL Lab para el Trade Emergency Team</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="small-text">Datos actualizados al 17 de marzo, 2025</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="small-text">© Cepal Lab - Versión de prueba </p>', unsafe_allow_html=True)