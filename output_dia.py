import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import base64
from cloud import render_wordcloud
from funciones import extraer_secciones

# Configuración de página
st.set_page_config(
    page_title="Monitor EEUU-LATAM | CEPAL Lab",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Función para codificar la imagen en base64
def get_base64_of_bin_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Cargar CSS desde un archivo externo
with open("style.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Codificar la imagen
img_base64 = get_base64_of_bin_file("assets/22130.jpg")
st.markdown(f"""
    <style>
    .header-banner {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
    }}
    </style>
""", unsafe_allow_html=True)

periodo = "Análisis de Noticias: Impacto de la Administración Trump en América Latina, el Caribe y el Mundo (3-16 de marzo de 2025)"

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
        <div class="nav-item">Semana del 17 al 23 de marzo, 2025</div>
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
with open("resumen_02.md", "r", encoding="utf-8") as file:
    resumen_contenido = file.read()
st.markdown("")
st.info("""
## Resumen Ejecutivo
Durante la semana del 17 al 23 de marzo de 2025, las decisiones de la administración Trump marcaron fuertemente la agenda regional, con especial énfasis en la imposición de aranceles y el endurecimiento de la política migratoria. La escalada de tensiones comerciales con México, Canadá, la Unión Europea y China derivó en una creciente incertidumbre económica, particularmente para América Latina y el Caribe, donde se teme un impacto directo en sectores clave, como el caso de México que podría entrar en recesión. Paralelamente, las represalias comerciales de la Unión Europea y la posibilidad de flexibilización en algunos casos mantuvieron el tema en constante evolución. En el ámbito migratorio, la deportación de migrantes venezolanos a prisiones en El Salvador generó alarma regional por posibles violaciones a los derechos humanos, mientras Estados Unidos intensificaba sus advertencias y sanciones contra gobiernos que se niegan a cooperar.

En paralelo, se consolidan otras dinámicas estratégicas en la región, como el fortalecimiento de la cooperación en defensa entre Estados Unidos, Argentina y Ecuador, lo que abre la discusión sobre la instalación de bases militares estadounidenses. También se destacan temas de alto interés como la elección de Albert Ramdin como nuevo secretario general de la OEA, los recortes de Estados Unidos a programas de salud global y la creciente disputa entre Washington y Beijing por el control de minerales críticos en el “triángulo del litio”. Frente a este escenario, la próxima semana será clave para monitorear la evolución de las políticas arancelarias y migratorias de Estados Unidos, la respuesta regional ante posibles sanciones, y el rumbo que tome la OEA bajo su nuevo liderazgo.
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
#st.header("Temas mas frecuentes")


# Crear datos de ejemplo para el gráfico de principales temas
temas_data = pd.DataFrame({
    'Tema': ['economía', 'aranceles', 'relaciones internacionales', 'política internacional', 'sanciones', 'gobierno', 'petróleo', 'gobierno y política', 'organizaciones internacionales'],
    'Menciones': [16, 15, 11, 11, 9, 9, 8, 7, 7],
    'Impacto Potencial': [9,8.9, 8.8, 8.7, 8.5, 8.3, 8.2, 8, 7.8]
})

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Temas más frecuentes")
    render_wordcloud()

with col2:
    st.header("Asuntos clave")
    st.markdown("""
    - Ante las amenazas arancelarias de Trump, la OCDE revisó a la baja sus previsiones de crecimiento mundial para 2025, 
                previendo una recesión en la economía mexicana. BMW desafía los aranceles de Trump y protege sus precios en México. 
                La UE busca acercarse a Latinoamérica tras las amenazas arancelarias de Trump.
    - Trump ha implementado tácticas drásticas para reducir los cruces fronterizos, incluyendo la detención indefinida del asilo, el despliegue de soldados y la presión a gobiernos latinoamericanos.
    - Se estima una eventual recesión en Estados Unidos debido a la guerra comercial y las políticas arancelarias de Trump.
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
        * Intercambio comercial entre Estados Unidos y México está valorado en **839 mil millones de dólares anuales**.
                <a href="https://americaeconomica.com/noticia/mexico/la-presidenta-de-mexico-dice-que-prevalecio-el-dialogo-con-trump-para-postergar-los-aranceles.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>

        * Se estima que construir una casa en Estados Unidos cuesta $9,000 más debido a los aranceles de Trump.<a href="https://americaeconomica.com/noticia/mexico/la-presidenta-de-mexico-dice-que-prevalecio-el-dialogo-con-trump-para-postergar-los-aranceles.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>
        * 50% es el arancel que impuso la Unión Europea sobre el whisky estadounidense, una medida que impacta directamente a la industria de bebidas espirituosas, la cual genera más de 200.000 millones de dólares en actividad económica y emplea a aproximadamente 1,7 millones de personas en los sectores de producción, distribución y venta. <a href="https://lancasteronline.com/lavoz/estados-unidos/trump-promete-recuperar-riqueza-robada-al-entrar-en-vigor-aranceles-al-acero-y-aluminio/article_9ffa3ae9-be9e-583e-bb69-ac5a3be3be91.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>
        * China respondió con aranceles de hasta 15% sobre productos agrícolas estadounidenses. <a href="https://lancasteronline.com/lavoz/estados-unidos/trump-promete-recuperar-riqueza-robada-al-entrar-en-vigor-aranceles-al-acero-y-aluminio/article_9ffa3ae9-be9e-583e-bb69-ac5a3be3be91.html" target="_blank" style="text-decoration:none; background-color:#f0f0f0; border-radius:50%; display:inline-block; width:75px; height:16px; line-height:16px; font-size:11px; text-align:center;">Ir a fuente</a>
        * El canal mueve el 5% del comercio marítimo mundial. 
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
        
        El índice de precios al productor aumentó un 3.2% en febrero.
        
        La OCDE reduce el pronóstico del PIB mundial del 3,3 % al 3,1 % para el presente año. 
        
        Se estima que un aumento del 10 % en los aranceles sobre todas las importaciones en Estados Unidos podría generar un incremento de 0,4 puntos porcentuales en la inflación global durante los próximos tres años.
                    
        América Latina: Proyecto Global Gateway implica un programa de inversión europea por U$S 45 mil millones
        
        Se estima en Venezuela un impacto acumulado de 3,8 mil millones de dólares en el PIB por la salida de Chevron.            
        """)

with tab3:
    #st.subheader("Dinámica Migratoria")
       
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Cifras Clave
        
        • Durante 2024 las remesas recibidas en México fueron de $64,745 millones, representando el 3.8% del PIB nacional y el 44% del total de ingreo de divisas al país. El 96,6% provienen de Estados Unidos.
        
        • El envío de remesas a El Salvador alcanzó $1,406.4 millones, un crecimiento de 14.2% (enero-febrero 2025).
        
        • Los envíos de remesas a México podrían disminuir entre 1.2% y 2.9% debido a políticas migratorias de Estados Unidos.
                    
        • Remesas alcanzaron los US$3 mil 638 millones en el primer bimestre de 2025 en Guatemala.
    
        """)
    
    with col2:
        st.markdown("""
        #### Movimientos migratorios
        
        Más de 530,000 cubanos, haitianos, nicaragüenses y venezolanos ingresaron legalmente a EEUU bajo el permiso humanitario de residencia temporal (“parole”) y el CBP One podrían perder su estatus migratorio.
        
        $6 millonespagará EEUU a El Salvador por la detención "terroristas extranjeros".
        
        Más de 850,000 migrantes cubanos han llegado a Estados Unidos desde 2022 a septiembre de 2024.
        
        8,347 personas fueron detenidas intentando cruzar ilegalmente la frontera de EEUU en febrero de 2025. 
                    
        8 millones de venezolanos han huido de la agitación económica y emigrado a EE.UU. y otros países de Latinoamérica .
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
        
        • Seis cárteles mexicanos designados como organizaciones terroristas extranjeras por el Registro Federal de Estados Unidos.
        
        • 7 millas (11 kilómetros) adicionales de muro fronterizo a construirse en Arizona.
        
        • 200 millones de dólares cuesta mantener el sistema carcelario de El Salvador.
        """)

###### SECCIÓN 3: DETALLE POR PAÍSES ######
st.header("Detalle por Países")

# Datos de ejemplo para países
paises_data = pd.DataFrame({
    'País': ['Antigua y Barbuda', 'Argentina', 'Belize', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 'República Dominicana', 'Surinam', 'Uruguay', 'Venezuela'],
    'Menciones': [1, 32, 1, 3, 8, 18, 2, 15, 17, 28, 4, 7, 91, 1, 36, 4, 3, 3, 8, 2, 3, 102],
    'Áreas Clave': [['desarrollo económico', 'economía', 'inclusión', 'integración regional', 'resiliencia'], ['gobierno', 'corrupción', 'sanciones', 'política', 'justicia'], ['gobierno', 'noticias de América Latina', 'política exterior', 'política internacional', 'relaciones diplomáticas'], ['Netflix', 'acuerdos comerciales', 'adquisiciones', 'cine', 'cooperación internacional'], ['cooperación internacional', 'desarrollo regional', 'economía', 'gobierno', 'gobierno migratorio'], ['música', 'política', 'economía', 'elecciones', 'gira musical'], ['gobierno', 'OEA', 'accidentes aéreos', 'desastres naturales', 'justicia'], ['migración', 'política migratoria', 'gobierno', 'inmigración', 'refugiados'], ['política', 'gobierno', 'diplomacia', 'elecciones', 'relaciones internacionales'], ['política migratoria', 'deportación', 'migración', 'inmigración', 'gobierno'], ['migración', 'seguridad fronteriza', 'tráfico de personas', 'conflicto comercial', 'corrupción'], ['economía', 'política migratoria', 'remesas', 'finanzas internacionales', 'migración'], ['economía', 'migración', 'aranceles', 'comercio internacional', 'moneda'], ['gobiernos autoritarios', 'libertad de prensa', 'medio ambiente', 'minería ilegal', 'periodismo'], ['relaciones internacionales', 'fútbol', 'política exterior', 'política internacional', 'comercio internacional'], ['política exterior', 'relaciones internacionales', 'conflicto internacional', 'guerra', 'historia'], ['aranceles', 'billetera digital', 'comercio internacional', 'criptomoneda', 'desastres naturales'], ['arte', 'autonomía', 'comunidad puertorriqueña', 'cultura', 'diáspora'], ['economía', 'espionaje', 'gobierno', 'inflación', 'moneda'], ['gobierno', 'organizaciones internacionales', 'OEA', 'deportación', 'política de la región'], ['Netflix', 'ataques cibernéticos', 'ciberataque', 'cine', 'confidencialidad'], ['petróleo', 'migración', 'gobierno', 'política migratoria', 'política energética']]
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
paises = ['Mexico','El Salvador','Colombia','Ecuador','Argentina', 'Panamá', 'Venezuela']
# Detalle de países seleccionados
selected_country = st.selectbox("Seleccione un país para más detalles:", paises)#paises_data['País'])

# Datos específicos por país
country_data = {
    'Mexico': {
        'overview': """
*   **Amenazas Arancelarias:** El presidente de Estados Unidos, Donald Trump, continúa utilizando la amenaza de imponer aranceles a productos mexicanos como herramienta de presión en temas de migración, seguridad y comercio. Se ha concedido una prórroga hasta el 2 de abril, pero la incertidumbre persiste.
*   **Alerta de Viaje:** El Departamento de Estado de EE. UU. ha emitido una alerta de viaje de "Nivel 4: No viajar" para varios estados de México debido a la violencia y el crimen organizado, lo que podría afectar el turismo y la inversión.
*   **Deportaciones y Remesas:** Las políticas migratorias de Trump, incluyendo el aumento de deportaciones, podrían impactar negativamente el flujo de remesas hacia México, aunque la magnitud de la disminución es incierta.
*   **Designación de Cárteles como Terroristas:** La designación de cárteles mexicanos como organizaciones terroristas extranjeras (FTOs) por parte de EE.UU. podría afectar el crédito a empresas mexicanas y generar mayor vigilancia en las instituciones financieras.
*   **Inversión y Nearshoring:** A pesar de las tensiones comerciales, se anuncian nuevas inversiones en México, especialmente en el norte del país, en sectores como fertilizantes y centros digitales. El nearshoring sigue siendo una tendencia importante, con empresas trasladando fábricas de China a México.
*   **Protección Consular:** El gobierno mexicano está reforzando la protección legal y la asistencia a sus connacionales en Estados Unidos ante las políticas migratorias restrictivas.
*   **Comercio Automotriz:** Trump insiste en que las plantas automotrices se construyan en Estados Unidos y no en México ni Canadá, lo que podría afectar la producción y las exportaciones mexicanas.
*   **Cooperación en Seguridad:** A pesar de las tensiones, existe cooperación en materia de seguridad, como el decomiso de armas provenientes de EE.UU. y la detención de líderes criminales.
*   **TV Migrante:** México lanza TV Migrante, un canal público para “dar voz a la migración”
        """,
        'key_areas': """
*   **Comercio:** Monitorear de cerca las negociaciones comerciales y la posible imposición de aranceles, así como buscar alternativas para diversificar los mercados y reducir la dependencia de EE.UU.
*   **Migración:** Evaluar el impacto de las políticas migratorias de EE.UU. en el flujo de remesas y en la situación de los migrantes mexicanos, y fortalecer los programas de apoyo y protección consular.
*   **Seguridad:** Intensificar la cooperación en materia de seguridad para combatir el crimen organizado y el tráfico de drogas, pero también abordar las causas estructurales de la violencia y la inseguridad en México.
*   **Inversión:** Promover la inversión extranjera directa en sectores estratégicos y diversificar las fuentes de inversión, aprovechando el nearshoring y las oportunidades que ofrecen otros mercados como los BRICS.
*   **Diplomacia:** Mantener un diálogo constructivo con el gobierno de EE.UU. para abordar los desafíos comunes y buscar soluciones mutuamente beneficiosas, pero también defender los intereses y la soberanía de México.
*   **Economía:** Analizar el impacto de las políticas de EE.UU. en la economía mexicana y tomar medidas para mitigar los riesgos y aprovechar las oportunidades, como el fortalecimiento del mercado interno y la diversificación de las exportaciones.

    """
    },
    'El Salvador': {
        'overview': """
*   **Deportaciones Masivas:** EE.UU. ha deportado a El Salvador a cientos de personas, principalmente venezolanos, acusados de pertenecer a la banda criminal "Tren de Aragua" y a la MS-13. Estas deportaciones se realizaron bajo la Ley de Enemigos Extranjeros de 1798.
*   **Acuerdo Bilateral:** Existe un acuerdo entre los gobiernos de EE.UU. y El Salvador, liderados por Trump y Bukele respectivamente, para que El Salvador reciba a estos deportados en su Centro de Confinamiento del Terrorismo (CECOT). EE.UU. está pagando a El Salvador por el alojamiento de estos individuos.
*   **Cuestionamientos Legales y de Derechos Humanos:** Las deportaciones han generado controversia y desafíos legales en EE.UU., con un juez federal bloqueando temporalmente las deportaciones. Organizaciones de derechos humanos han expresado preocupación por la falta de debido proceso y la posible criminalización injusta de migrantes.
*   **Reacciones Políticas:** El gobierno venezolano ha calificado las deportaciones como un "crimen de lesa humanidad" y ha solicitado la intervención de la ONU. Dentro de EE.UU., hay debate sobre la legalidad y la ética de las deportaciones, así como sobre la evidencia que vincula a los deportados con actividades criminales.
*   **Remesas:** Se observa un aumento en el envío de remesas a El Salvador, posiblemente debido al temor de los salvadoreños en el exterior ante las políticas migratorias de EE.UU.
*   **TPS:** Activistas urgen a salvadoreños a renovar el Estatus de Protección Temporal (TPS) ante las buenas relaciones entre Trump y Bukele.
        """,
        'key_areas': """
*   **Debido Proceso y Derechos Humanos:** Es crucial monitorear el trato que reciben los deportados en El Salvador, asegurando el respeto a sus derechos humanos y el acceso a un debido proceso legal. Se debe investigar la veracidad de las acusaciones que vinculan a los deportados con actividades criminales.
*   **Impacto en la Relación Bilateral:** Analizar cómo estas acciones impactan la relación bilateral entre EE.UU. y El Salvador a largo plazo, considerando las implicaciones para la cooperación en otras áreas como comercio, inversión y seguridad.
*   **Estabilidad Económica de El Salvador:** Evaluar el impacto del aumento de las remesas en la economía salvadoreña, así como los posibles riesgos asociados a la dependencia de estos flujos financieros.
*   **Cooperación en Seguridad:** Examinar la efectividad de la cooperación entre EE.UU. y El Salvador en la lucha contra el crimen organizado transnacional, asegurando que se respeten los derechos humanos y el estado de derecho.
*   **Implicaciones Regionales:** Analizar las implicaciones de estas políticas para la migración y la seguridad en la región, incluyendo el papel de Venezuela y otros países afectados por el crimen organizado transnacional.
*   **Transparencia:** Es fundamental que tanto EE.UU. como El Salvador hagan pública la lista de las personas detenidas y los delitos por los que son investigadas.


    """
    },
    'Colombia': {
        'overview': """
*   **Migración:** Se observa un flujo constante de migrantes colombianos que regresan desde Estados Unidos y México, lo que sugiere posibles dificultades económicas o cambios en las políticas migratorias en esos países. También se menciona el caso de colombianos deportados desde Estados Unidos después de vivir allí por décadas.
*   **Remesas:** Las remesas desde Estados Unidos representan una fuente importante de ingresos para Colombia, con un crecimiento constante aunque a un ritmo decreciente. Se anticipa que las remesas podrían convertirse en la principal fuente de divisas del país, superando incluso al petróleo.
*   **Documentos Desclasificados:** La desclasificación de documentos relacionados con el asesinato de Kennedy revela planes de Estados Unidos con el expresidente colombiano Alberto Lleras Camargo, lo que indica una relación histórica de cooperación y posible intervención en asuntos internos.
*   **Reforma Laboral:** El hundimiento de la reforma laboral en el Congreso colombiano genera tensión política interna y podría tener implicaciones en las relaciones con Estados Unidos, especialmente si se considera que la reforma podría afectar la inversión extranjera.
*   **Cooperación en Seguridad:** Expertos internacionales visitan Colombia para analizar la situación de seguridad, lo que sugiere un interés en la cooperación en este ámbito.

""",
        'key_areas': """
*   **Impacto de las políticas migratorias de EE.UU.:** Es crucial monitorear las políticas migratorias de Estados Unidos y su impacto en el flujo de migrantes colombianos que regresan al país, así como en el envío de remesas.
*   **Oportunidades y riesgos en el comercio:** Se debe analizar el impacto de las políticas arancelarias de Estados Unidos en la economía colombiana y las oportunidades para fortalecer el comercio bilateral.
*   **Cooperación en seguridad:** Es importante evaluar las oportunidades para fortalecer la cooperación en seguridad con Estados Unidos, especialmente en la lucha contra el crimen organizado y el narcotráfico.
*   **Implicaciones políticas internas:** Se debe analizar cómo la situación política interna en Colombia, incluyendo el hundimiento de la reforma laboral y la propuesta de consulta popular, podría afectar las relaciones con Estados Unidos.
*   **Diversificación de relaciones:** Es importante considerar la estrategia de Colombia de diversificar sus relaciones internacionales, incluyendo el acercamiento a China y la posible entrada a los BRICS, y cómo esto podría afectar su relación con Estados Unidos.

    """
    },
    'Ecuador': {
        'overview': """
*   **Interés en fortalecer la relación bilateral:** El gobierno de Ecuador, bajo la administración de Daniel Noboa, está tomando medidas concretas para fortalecer la relación con Estados Unidos. Esto incluye el nombramiento de un nuevo embajador en EE.UU., la contratación de una consultora para acercar a Noboa con el presidente estadounidense Donald Trump, y la solicitud formal a EE.UU. para que declare a grupos criminales ecuatorianos como organizaciones terroristas.
*   **Cooperación en seguridad:** Existe un interés mutuo en la cooperación en materia de seguridad. Ecuador ha expresado interés en albergar una base militar estadounidense y ha anunciado una "alianza estratégica" con Erik Prince, fundador de Blackwater, para asesorar en la lucha contra el narcoterrorismo y la protección marítima.
*   **Acuerdo comercial:** Ecuador está siguiendo los pasos de Argentina en la búsqueda de un acuerdo comercial con Estados Unidos.
*   **Política Migratoria:** Se observa preocupación por las deportaciones masivas de migrantes ecuatorianos desde Estados Unidos.
*   **Influencia de EE.UU. en la política interna:** Se menciona la influencia de Estados Unidos en el proceso político ecuatoriano, con apoyo a la candidatura de Noboa.
        """,
        'key_areas': """
*   **Implicaciones de la cooperación en seguridad:** Es crucial analizar las implicaciones de la cooperación en seguridad con EE.UU., incluyendo la posible instalación de bases militares y la participación de empresas privadas como Blackwater. Se deben evaluar los riesgos y beneficios de estas acciones, considerando la soberanía nacional y la posible escalada de la violencia.
*   **Oportunidades y desafíos del acuerdo comercial:** Se debe analizar el potencial impacto de un acuerdo comercial con EE.UU. en la economía ecuatoriana, identificando oportunidades para el crecimiento y diversificación de las exportaciones, así como los posibles desafíos para sectores sensibles.
*   **Impacto de las políticas migratorias de EE.UU.:** Es importante monitorear y analizar el impacto de las políticas migratorias de EE.UU. en la población ecuatoriana, incluyendo las deportaciones y las restricciones a la migración. Se deben explorar mecanismos para proteger los derechos de los migrantes ecuatorianos y facilitar su reintegración en caso de retorno.
*   **Riesgos de la polarización política:** Se debe prestar atención a la polarización política en Ecuador y la posible influencia de actores externos, incluyendo EE.UU. Es importante promover el diálogo y la búsqueda de consensos para garantizar la estabilidad política y social del país.
*   **Impacto de la designación de grupos criminales como terroristas:** Analizar las implicaciones de la designación de grupos criminales ecuatorianos como organizaciones terroristas por parte de EE.UU., incluyendo el impacto en la cooperación en seguridad y la posible aplicación de sanciones económicas.
    """
    },
    'Argentina': {
        'overview': """
*   **Sanciones de EEUU a Cristina Kirchner y Julio De Vido:** El gobierno de Donald Trump sancionó a la expresidenta Cristina Fernández de Kirchner y al exministro Julio De Vido, prohibiéndoles el ingreso a Estados Unidos a ellos y a sus familiares directos, debido a su participación en actos de corrupción durante su gestión. Esta medida se basa en la Sección 7031(c) de la Ley de Asignaciones del Departamento de Estado.
*   **Cooperación en Defensa:** Se observa un fortalecimiento de la cooperación en materia de defensa entre Argentina y Estados Unidos, con la realización de entrenamientos conjuntos entre las fuerzas armadas de ambos países.
*   **Interés en Inversión:** A pesar de la crisis industrial, una multinacional estadounidense realizó una inversión multimillonaria en Argentina.
*   **Reacciones Políticas:** La sanción a Cristina Kirchner generó diversas reacciones políticas en Argentina, incluyendo el respaldo de algunos sectores y la crítica de otros, así como la ironía del presidente Javier Milei.
*   **Elogios a la Política Económica:** Expertos latinoamericanos elogiaron el rumbo de la economía argentina bajo la administración de Javier Milei, destacando el equilibrio fiscal y la oportunidad de atraer inversiones.
        """,
        'key_areas': """
*   **Implicaciones de las Sanciones:** Analizar el impacto de las sanciones impuestas por Estados Unidos a Cristina Kirchner y Julio De Vido en la política interna argentina y en las relaciones bilaterales.
*   **Oportunidades en Defensa:** Evaluar las oportunidades y riesgos de la cooperación en materia de defensa entre Argentina y Estados Unidos, considerando los intereses y prioridades de ambos países.
*   **Clima de Inversión:** Monitorear el clima de inversión en Argentina y las perspectivas de nuevas inversiones estadounidenses, teniendo en cuenta los desafíos económicos y políticos del país.
*   **Política Económica:** Analizar la sostenibilidad de la política económica implementada por el gobierno de Javier Milei y su impacto en la relación con Estados Unidos, especialmente en materia de comercio e inversión.
*   **Relación Bilateral:** Evaluar el estado general de la relación bilateral entre Argentina y Estados Unidos, considerando los diferentes temas de interés mutuo y los posibles puntos de tensión.
""",
        
    },
    'Panamá': {
        'overview': """
*   **Amenazas a la Soberanía del Canal:** El expresidente Trump ha expresado públicamente su deseo de "recuperar" el Canal de Panamá, generando tensiones bilaterales y preocupación en Panamá sobre su soberanía.
*   **Investigación de EE.UU. sobre el Canal:** La Comisión Marítima Federal (FMC) de EE.UU. ha iniciado una investigación sobre posibles restricciones en el Canal de Panamá que podrían afectar el comercio internacional, lo que podría derivar en sanciones.
*   **Presencia China en el Canal:** Existe preocupación en EE.UU. sobre la influencia china en la operación del Canal, particularmente en relación con la empresa de Hong Kong CK Hutchison, que administra puertos clave. La venta de activos portuarios de CK Hutchison a la empresa estadounidense BlackRock ha generado controversia y escrutinio.
*   **Cooperación en Seguridad:** A pesar de las tensiones, la cooperación en seguridad entre EE.UU. y Panamá continúa, incluyendo ejercicios militares conjuntos, asistencia humanitaria y cooperación cibernética. El Comando Sur de EE.UU. ha enviado helicópteros y aviones de transporte a Panamá para programas de asistencia humanitaria y ejercicios de seguridad.
*   **Visitas de Congresistas:** Delegaciones bipartidistas del Congreso de EE.UU. han visitado Panamá para discutir temas de interés mutuo, incluyendo la gestión del Canal y la presencia china.
*   **Preocupaciones Económicas:** La calificadora Moody's ha expresado su preocupación por las tensiones entre Panamá y EE.UU., así como por el litigio con Minera Panamá, que podrían afectar la economía panameña.
*   **Interés en Infraestructura Portuaria:** El presidente de Panamá ha anunciado planes para construir un megapuerto en el Pacífico, complementando los negocios del Canal.
        
""",
        'key_areas': """
*   **Soberanía del Canal:** Es crucial monitorear de cerca las acciones y declaraciones de EE.UU. con respecto al Canal de Panamá y defender la soberanía panameña sobre la vía acuática.
*   **Relaciones Comerciales:** La investigación de la FMC y la posible imposición de sanciones podrían tener un impacto significativo en el comercio internacional y la economía panameña. Es importante evaluar los riesgos y oportunidades en este ámbito.
*   **Influencia China:** La creciente presencia económica y política de China en Panamá es un tema de preocupación para EE.UU. Es necesario analizar las implicaciones de esta influencia en la relación bilateral y en la seguridad regional.
*   **Cooperación en Seguridad:** A pesar de las tensiones, la cooperación en seguridad entre EE.UU. y Panamá es importante para abordar desafíos comunes como el crimen organizado transnacional, la migración ilegal y la seguridad del Canal.
*   **Estabilidad Económica:** Las tensiones con EE.UU. y el litigio con Minera Panamá podrían afectar la estabilidad económica de Panamá. Es importante implementar políticas fiscales sólidas y diversificar la economía para mitigar estos riesgos.
*   **Diplomacia y Diálogo:** Es fundamental mantener un diálogo abierto y constructivo con EE.UU. para abordar las preocupaciones mutuas y fortalecer la relación bilateral.

        """
    },
        'Venezuela': {
        'overview': """
*   **Política Migratoria Restrictiva:** La administración Trump ha intensificado las deportaciones de venezolanos, invocando la Ley de Enemigos Extranjeros y enviando a algunos a prisiones en El Salvador, generando controversia y denuncias de violaciones de derechos humanos. Se observa una narrativa que vincula a los migrantes venezolanos con la banda criminal Tren de Aragua, aunque informes de inteligencia contradicen la conexión directa con el gobierno de Maduro.
*   **Sanciones Económicas y Petroleras:** Se mantiene la política de sanciones económicas contra Venezuela, con la revocación de licencias a empresas petroleras como Chevron, lo que impacta la producción y exportación de crudo. Sin embargo, se evalúa una posible extensión de la licencia de Chevron, posiblemente condicionada a la aceptación de vuelos de deportación y al destino de los ingresos petroleros.
*   **Tensiones Diplomáticas:** Las relaciones bilaterales se caracterizan por la tensión y la desconfianza, con acusaciones mutuas de injerencia y violaciones de derechos humanos. Estados Unidos amenaza con nuevas sanciones si Venezuela no acepta los vuelos de deportación, mientras que Venezuela denuncia el trato a sus migrantes y la injerencia de ExxonMobil en la controversia por el territorio de la Guayana Esequiba.
*   **Confiscación de Bienes:** Estados Unidos busca la confiscación de bienes vinculados al gobierno de Maduro, como el avión presidencial, alegando violaciones de las leyes de sanciones y lavado de dinero.
*   **Reacciones Internas:** La situación genera divisiones internas en Venezuela, con la oposición criticando la política migratoria de EE.UU. y el gobierno denunciando un "secuestro" de migrantes.
        """,
        'key_areas': """
*   **Impacto Humanitario de las Sanciones:** Es crucial evaluar el impacto de las sanciones económicas en la población venezolana, especialmente en el acceso a bienes esenciales y servicios básicos.
*   **Protección de los Derechos de los Migrantes:** Se debe monitorear de cerca la situación de los migrantes venezolanos en Estados Unidos, garantizando el debido proceso y evitando la criminalización injusta.
*   **Estabilidad Política y Económica:** Es importante analizar las implicaciones de las políticas de EE.UU. en la estabilidad política y económica de Venezuela, considerando el impacto en la producción petrolera, la inversión extranjera y la gobernabilidad.
*   **Influencia de Actores Externos:** Se debe evaluar la influencia de otros actores externos, como China y Rusia, en la economía y la política venezolana, y su impacto en la relación con Estados Unidos.
*   **Posibles Escenarios de Negociación:** Es necesario analizar los posibles escenarios de negociación entre Estados Unidos y Venezuela, considerando los intereses en juego y las condiciones para un diálogo constructivo.
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

El análisis de los hechos noticiosos presentados revela varias implicaciones económicas para América Latina y el Caribe, que la CEPAL deberá considerar en sus proyecciones. La imposición de aranceles por parte de EE.UU., especialmente si se extienden a México y otros socios comerciales, podría frenar el crecimiento regional y aumentar la inflación. La OCDE ya prevé una recesión en México debido a estas políticas. La CEPAL deberá evaluar el impacto de estas medidas en el comercio intrarregional y en la competitividad de las exportaciones latinoamericanas.
Las políticas migratorias restrictivas de EE.UU. impactan el flujo de remesas, crucial para economías como Honduras, donde representan un 25% del PIB. Si bien inicialmente las remesas pueden aumentar por envíos precautorios, a largo plazo la reducción de migrantes empleados en EE.UU. podría disminuir estos ingresos. La CEPAL deberá analizar la vulnerabilidad de las economías dependientes de remesas ante estos cambios. 
La disputa entre EE.UU. y China por el control de recursos estratégicos como el litio y el Canal de Panamá genera incertidumbre en la región. La CEPAL deberá monitorear cómo estas tensiones geopolíticas afectan la inversión extranjera directa y las oportunidades de diversificación económica para los países latinoamericanos.

            
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
