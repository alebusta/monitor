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


# Encabezado
# CSS personalizado para el encabezado
st.markdown("""

<div class="header-banner">
    <div class="header-slogan">Monitor de tendencias EEUU - Latinoamérica</div>
</div>

<div class="navbar">
    <div class="nav-left">
        <div class="nav-item">Análisis de noticias de impacto para la región</div>
        </div>
    <div class="nav-right">
        <div class="nav-item">Semana del 23 al 30 de marzo, 2025</div>
        <div class="nav-item">🌎 CEPAL LAB</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("")
# Cargar el archivo de audio (puede estar en la misma carpeta o una URL)
audio_file = open('resumen_mar_04.mp3', 'rb')
audio_bytes = audio_file.read()

# Función para crear un enlace a PDF
def get_pdf_link(pdf_file):
    with open(pdf_file, "rb") as file:
        pdf_bytes = file.read()
    
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    return f'<a href="data:application/pdf;base64,{base64_pdf}" download="resumen.pdf" style="font-size:16px; text-align: right; color:gray;">📄 versión para imprimir</a>'


columna1, columna2, columna3 = st.columns([3,1,1])

with columna1:
    st.header("Principales eventos noticiosos")
    st.markdown("Noticias más relevantes durante la semana respecto a las relaciones de Estados Unidos con Latinoamérica.")
    
 
with columna2:

    # Ruta a tu archivo PDF - ajusta esta ruta según sea necesario
    pdf_file = "monitor_mar_w4.pdf"
    
    try:
        # Mostrar el enlace para PDF
        pdf_link = get_pdf_link(pdf_file)
        st.markdown(pdf_link, unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown("📄 <span style='color:#999;font-size:12px;'>PDF no disponible</span>", unsafe_allow_html=True)

with columna3:
    
    st.markdown("""
<div style='text-align: left; font-style: italic; font-size: 16px; color: gray;'>
    Resumen en audio (6min)
</div>
""", unsafe_allow_html=True)
    # Mostrar el reproductor
    st.audio(audio_bytes, format='audio/mp3')


# Contenido de la aplicación

# Leer el contenido del archivo markdown
with open("resumen.md", "r", encoding="utf-8") as file:
    resumen_contenido = file.read()


secciones = extraer_secciones(resumen_contenido)

for titulo_seccion, contenido_seccion in secciones.items():
    with st.expander(f"**{titulo_seccion}**"):
        st.markdown(contenido_seccion, unsafe_allow_html=True)
        


# Crear datos de ejemplo para el gráfico de principales temas
temas_data = pd.DataFrame({
    'Tema': ['economía', 'aranceles', 'relaciones internacionales', 'política internacional', 'sanciones', 'gobierno', 'petróleo', 'gobierno y política', 'organizaciones internacionales'],
    'Menciones': [16, 15, 11, 11, 9, 9, 8, 7, 7],
    'Impacto Potencial': [9,8.9, 8.8, 8.7, 8.5, 8.3, 8.2, 8, 7.8]
})

col1, col2 = st.columns([1, 1])

with col1:
    st.header("Temas más frecuentes")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    words = [('comercio internacional', 121), ('aranceles', 118), ('relaciones internacionales', 115), ('economía', 96), ('gobierno', 81), ('migración', 68), ('política exterior', 56), ('política migratoria', 52), ('petróleo', 51), ('política internacional', 45), ('política económica', 42), ('diplomacia', 39), ('relaciones comerciales', 30), ('inmigración', 30), ('seguridad', 29), ('seguridad nacional', 29), ('política', 28), ('derechos humanos', 26), ('desarrollo económico', 26), ('deportación', 25), ('energía', 24), ('relaciones bilaterales', 22), ('industria automotriz', 21), ('remesas', 21), ('cooperación internacional', 20), ('política comercial', 20), ('inversión', 20), ('sanciones', 19), ('economía global', 19), ('corrupción', 17), ('seguridad fronteriza', 16), ('finanzas', 15), ('crimen organizado', 14), ('elecciones', 13), ('refugiados', 13), ('salud pública', 12), ('política energética', 12), ('conflicto geopolítico', 12), ('moneda', 12), ('narcotráfico', 12), ('crecimiento económico', 12), ('justicia', 11), ('organizaciones internacionales', 11), ('política electoral', 11), ('exportación', 10), ('conflicto internacional', 10), ('violencia', 10), ('sanciones económicas', 10), ('alianzas geopolíticas', 10), ('proteccionismo', 10), ('guerra comercial', 9), ('comercio', 9), ('liderazgo político', 9), ('empleo', 9), ('negocios', 8), ('integración regional', 8), ('seguridad pública', 8), ('democracia', 8), ('tecnología', 8), ('seguridad regional', 8), ('inversión extranjera', 8), ('relocalización', 8), ('liderazgo', 7), ('inflación', 7), ('globalización', 7), ('conflicto', 7), ('gas', 6), ('trabajo', 6), ('alianzas militares', 6), ('seguridad internacional', 6), ('estabilidad económica', 6), ('relaciones económicas', 6), ('reuniones diplomáticas', 6), ('guerra', 6), ('defensa', 5), ('mercados financieros', 5), ('transparencia', 5), ('gobierno y política', 5), ('gobierno autoritario', 5), ('política de seguridad', 5), ('alianzas', 5), ('ayuda humanitaria', 5), ('relaciones geopolíticas', 5), ('mercado financiero', 5), ('geopolítica', 5), ('libre comercio', 5), ('inmigración ilegal', 5), ('recesión', 4), ('institucionalidad', 4), ('tráfico de drogas', 4), ('soberanía', 4), ('terrorismo', 4), ('legislación', 4), ('partidos políticos', 4), ('transporte', 4)]
    render_wordcloud(words)

with col2:
    st.header("Detalle por Países")
    
    # Datos de ejemplo para países
    paises_data = pd.DataFrame({
        'País': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Guyana', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 'Dominican Republic', 'Surinam', 'Uruguay', 'Venezuela'],
        'Menciones': [7, 1, 5, 7, 26, 1, 23, 25, 19, 7, 5, 9, 1, 127, 5, 33, 4, 2, 2, 7, 2, 3, 98],
        'Áreas Clave': [['economía', 'política internacional', 'aranceles', 'comercio internacional', 'conflicto político'], ['gobierno', 'liderazgo político', 'movimientos políticos', 'política', 'política internacional'], ['aranceles', 'comercio internacional', 'política internacional', 'relaciones comerciales', 'relaciones internacionales'], ['desarrollo económico', 'comercio internacional', 'integración regional', 'cooperación internacional', 'corrupción'], ['migración', 'cooperación internacional', 'gobierno', 'diplomacia', 'narcotráfico'], ['desarrollo económico', 'gobierno digital', 'innovación pública', 'inteligencia artificial', 'transformación tecnológica'], ['relaciones internacionales', 'derechos humanos', 'migración', 'política exterior', 'economía'], ['gobierno', 'relaciones internacionales', 'diplomacia', 'política electoral', 'política exterior'], ['migración', 'deportación', 'política migratoria', 'gobierno', 'derechos humanos'], ['corrupción', 'desarrollo económico', 'economía', 'migración', 'remesas'], ['relaciones geopolíticas', 'amenaza militar', 'conflicto internacional', 'defensa territorial', 'política internacional'], ['economía', 'inmigración', 'remesas', 'migración', 'café'], ['gobiernos regionales', 'petróleo', 'política internacional', 'relaciones geopolíticas'], ['aranceles', 'comercio internacional', 'economía', 'relaciones internacionales', 'gobierno'], ['derechos humanos', 'diplomacia', 'gobierno', 'organizaciones internacionales', 'refugiados'], ['relaciones internacionales', 'gobierno', 'política exterior', 'seguridad regional', 'bases militares'], ['acuerdos comerciales', 'alianzas comerciales', 'comercio internacional', 'conflicto internacional', 'conflicto regional'], ['estabilidad económica', 'comercio internacional', 'contingencia', 'guerra comercial', 'política económica'], ['deportación', 'economía', 'migración', 'políticas migratorias', 'remesas'], ['economía', 'crecimiento económico', 'deportación', 'migración', 'políticas migratorias'], ['diplomacia', 'gobierno', 'gobiernos regionales', 'organizaciones internacionales', 'petróleo'], ['ciberseguridad', 'crecimiento empresarial', 'delincuencia cibernética', 'desarrollo económico', 'economía global'], ['petróleo', 'aranceles', 'comercio internacional', 'relaciones internacionales', 'energía']]
        })


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
        height=500,
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




#======
st.header("Temas por países más mencionados")
#Paises seleccionados solo para el ejemplo
paises = ['Mexico','El Salvador','Colombia','Ecuador','Cuba', 'Panamá', 'Venezuela']
# Detalle de países seleccionados
selected_country = st.selectbox("Seleccione un país:", paises)#paises_data['País'])

# Datos específicos por país
country_data = {
    'Mexico': {
        'overview': """
*   **Amenaza Arancelaria:** La imposición de aranceles del 25% por parte de Estados Unidos a vehículos no fabricados en su territorio, programada para el 2 de abril, genera incertidumbre y tensión comercial. Esta medida, impulsada por el presidente Trump, busca presionar a las empresas automotrices para trasladar su producción a EE.UU.
*   **Reunión de Seguridad:** La Secretaria de Seguridad Nacional de EE.UU., Kristi Noem, visitó México para reunirse con la presidenta Claudia Sheinbaum, abordando temas de migración, seguridad fronteriza y combate al narcotráfico, especialmente el fentanilo. Se acordó reforzar la coordinación en estas áreas.
*   **Impacto Migratorio:** Se proyecta una posible caída en las remesas dirigidas a México debido a las deportaciones de migrantes mexicanos desde Estados Unidos. Escenarios con 200,000 y 300,000 deportaciones podrían resultar en disminuciones del 1.3% y 3% en el flujo de remesas, respectivamente.
*   **Reacción Mexicana:** Ante la amenaza arancelaria, el gobierno mexicano ha adoptado una postura cautelosa, buscando un "trato preferencial" con EE.UU. y evitando la confrontación directa. Se han anunciado medidas arancelarias y no arancelarias en respuesta, priorizando la defensa de las empresas nacionales y extranjeras que operan en México.
*   **Desplazamiento de Inversión:** Algunas empresas chinas están reconsiderando sus inversiones en México debido a las tensiones comerciales y las políticas proteccionistas de EE.UU., buscando alternativas en otros países de Latinoamérica.
*   **Cumplimiento del TMEC:** Se destaca que el 91% de la producción automotriz mexicana cumple con las reglas del T-MEC, lo que podría mitigar el impacto de los aranceles estadounidenses. Sin embargo, la incertidumbre persiste sobre el futuro del acuerdo comercial.
        """,

    },
    'El Salvador': {
        'overview': """
*   **Deportaciones y Encarcelamiento:** Estados Unidos ha deportado a El Salvador a cientos de venezolanos acusados de pertenecer a la banda criminal "Tren de Aragua", quienes fueron inmediatamente encarcelados en una prisión de máxima seguridad. Esta acción se basa en un acuerdo bilateral y la invocación de la Ley de Enemigos Extranjeros por parte de EE.UU.
*   **Cooperación en Seguridad:** La Secretaria de Seguridad Nacional de EE.UU., Kristi Noem, visitó El Salvador para evaluar la cooperación en materia de seguridad y discutir el aumento de vuelos de deportación. Su visita incluyó una inspección del Centro de Confinamiento del Terrorismo (CECOT), donde están recluidos los deportados.
*   **Impacto en Remesas:** Existe preocupación sobre el impacto de las políticas migratorias de EE.UU. en las remesas que El Salvador recibe, dado que una parte significativa proviene de salvadoreños indocumentados en EE.UU. Un estudio indica que El Salvador es el segundo país más vulnerable en Latinoamérica en este aspecto.
*   **Lista Engel:** Funcionarios salvadoreños han sido incluidos en la "Lista Engel" de EE.UU., lo que les prohíbe la entrada a ese país por presuntos actos de corrupción.
        """,

    },
    'Colombia': {
        'overview': """
*   **Cooperación en Seguridad y Migración:** Se observa un fortalecimiento de la cooperación entre Estados Unidos y Colombia en materia de seguridad y control migratorio, evidenciado por la reunión entre el Presidente Petro y la Secretaria de Seguridad Nacional de EE.UU., Kristi Noem, y la firma de una declaración de intención para la cooperación biométrica. Este acuerdo busca facilitar el intercambio de datos para identificar criminales y prevenir su tránsito fronterizo.
*   **Tensiones Diplomáticas y Comerciales:** A pesar de la cooperación, existen tensiones latentes entre ambos países, como se refleja en la disputa diplomática y arancelaria previa por la deportación de colombianos. La visita de Noem se produce en un contexto de roces entre los presidentes Trump y Petro.
*   **Rol de Colombia en la Política Migratoria de EE.UU.:** Se discute el papel de Colombia en la crisis migratoria americana, especialmente en la región del Urabá, como punto de partida de migrantes hacia el Darién. EE.UU. busca que Colombia actúe como barrera operativa para contener la migración irregular.
*   **Lucha contra el Narcotráfico:** La lucha contra el narcotráfico sigue siendo un tema central en la relación bilateral, con discusiones sobre estrategias de erradicación de cultivos ilícitos.
*   **Preocupación por la Injerencia de EE.UU.:** Existe preocupación por la injerencia de EE.UU. en asuntos internos de Colombia, especialmente en el ámbito electoral, como se menciona en relación con posibles acciones de Elon Musk en Brasil.

""",

    },
    'Ecuador': {
        'overview': """
*   **Reanudación de Proyectos de Seguridad:** Estados Unidos ha reanudado proyectos de seguridad con Ecuador, a través de la Oficina de Asuntos Internacionales de Narcóticos y Aplicación de la Ley (INL), que estaban en pausa. Estos proyectos incluyen la construcción de una base de interdicción marítima, donación de botes patrulleros, remodelación de la escuela de poligrafistas, donación de vehículos y remodelación de la clínica veterinaria de la unidad canina para la Policía.
*   **Reunión Noboa-Trump:** El presidente de Ecuador, Daniel Noboa, se reunió con el presidente de Estados Unidos, Donald Trump, en Mar-a-Lago, Florida. Los temas discutidos incluyeron seguridad, migración y comercio bilateral.
*   **Cooperación en Seguridad:** Noboa busca apoyo internacional en la lucha contra los carteles de la droga y ha gestionado la posibilidad de recibir fuerzas especiales de otros países o establecer bases militares extranjeras. Planteó al Congreso la eliminación de la prohibición de establecer bases militares extranjeras en la Constitución.
*   **Migración:** Noboa conversó con Trump sobre migración en favor de los ecuatorianos en Estados Unidos. El Ejecutivo estadounidense ha sacado a Ecuador de la lista de prioridad de deportaciones.
*   **Comercio:** Se discutió un trato justo en materia comercial entre ambos países. Estados Unidos es el principal socio comercial de Ecuador.
*   **Lucha contra el Crimen Organizado:** Noboa ha solicitado públicamente al Gobierno de Trump que incluya en la lista de grupos terroristas a los grupos armados irregulares en su país.

        """,

    },
    'Cuba': {
        'overview': """
*   **Tensiones Migratorias:** Se observa un incremento en las deportaciones de cubanos desde Estados Unidos, generando críticas por parte del gobierno cubano, quien acusa a figuras políticas estadounidenses de promover estas medidas. A pesar de las tensiones, Cuba manifiesta su disposición a mantener el diálogo con EE.UU. en materia migratoria.
*   **Sanciones Económicas:** Las sanciones económicas impuestas por Estados Unidos, particularmente durante la administración Trump, continúan impactando la economía cubana. Bancos internacionales, como PostFinance, cierran cuentas de clientes cubanos por temor a sanciones estadounidenses. Las restricciones en el envío de remesas persisten, afectando a familias que dependen de estos ingresos.
*   **Diplomacia y Derechos Humanos:** Estados Unidos nomina a la disidente cubana Rosa María Payá como miembro de la Comisión Interamericana de Derechos Humanos (CIDH), lo que refleja el interés de EE.UU. en la situación de los derechos humanos en Cuba. El gobierno cubano critica las políticas de EE.UU. hacia los cubanos, pero es criticado por su historial de violaciones de derechos humanos.
*   **Acusaciones y Retórica:** El gobierno cubano acusa a Estados Unidos de chantaje e intimidación contra sus naciones, utilizando herramientas económicas y políticas punitivas. Se critica el uso de la Base Naval de Guantánamo para encarcelar migrantes.
        """,
        
    },
    'Panamá': {
        'overview': """
*   **Tensiones Bilaterales:** Existe una tensión latente entre Estados Unidos y Panamá, exacerbada por las declaraciones del expresidente Trump sobre la posible "recuperación" del Canal de Panamá y las insinuaciones sobre la injerencia china en la gestión de la vía interoceánica.
*   **Presencia Militar:** El gobierno panameño ha reiterado su rechazo a la instalación de bases militares estadounidenses en su territorio, reafirmando su compromiso con la soberanía del Canal. Sin embargo, se mantienen ejercicios militares conjuntos y cooperación en seguridad.
*   **Influencia China:** La creciente influencia de China en Panamá, especialmente en el ámbito portuario y tecnológico, es un tema de preocupación para Estados Unidos. La nominación de Kevin Cabrera como embajador de EE.UU. en Panamá refleja esta preocupación, con un enfoque en contrarrestar la influencia china.
*   **Transacciones Portuarias:** La posible venta de los puertos de Balboa y Cristóbal, operados por una empresa de Hong Kong (CK Hutchison), a un consorcio estadounidense liderado por BlackRock, ha generado controversia y la intervención del regulador antimonopolio chino. Estados Unidos ha expresado su satisfacción por esta posible "recuperación" de la vía interoceánica.
*   **Cooperación en Seguridad:** A pesar de las tensiones, existe cooperación bilateral en temas de seguridad, incluyendo el combate al narcotráfico, la migración irregular y la seguridad cibernética. El Comando Sur de EE.UU. realiza operaciones de asistencia humanitaria y seguridad en coordinación con el gobierno panameño.
*   **Migración:** Panamá y Colombia buscan estrategias conjuntas para abordar las deportaciones de migrantes, especialmente venezolanos, desde Estados Unidos.
*   **Sanciones:** Panamá ha cancelado el registro de 107 barcos sancionados internacionalmente, atendiendo a las denuncias de Estados Unidos sobre la permisividad en el registro de buques.
        
""",

    },
        'Venezuela': {
        'overview': """
*   **Imposición de Aranceles:** EE.UU. impuso un arancel del 25% a los países que compren petróleo o gas a Venezuela, efectivo a partir del 2 de abril de 2025. Esta medida busca presionar al gobierno de Nicolás Maduro y restringir sus ingresos por exportaciones de hidrocarburos.
*   **Revocación de Licencias:** EE.UU. revocó las licencias que permitían a empresas petroleras extranjeras, incluyendo Repsol, Eni y Chevron, operar y exportar petróleo venezolano. Se les ha dado un plazo hasta finales de mayo para liquidar sus operaciones.
*   **Deportaciones:** Se reanudaron los vuelos de deportación de venezolanos desde EE.UU. a Venezuela, con la particularidad de que algunos deportados fueron enviados a una cárcel en El Salvador, generando controversia y acusaciones de violaciones de derechos humanos.
*   **Tensiones Bilaterales:** Las relaciones entre EE.UU. y Venezuela se mantienen tensas, con acusaciones mutuas de hostilidad y desestabilización. EE.UU. justifica sus acciones con argumentos de seguridad nacional y lucha contra el crimen, mientras que Venezuela denuncia injerencia y violaciones del derecho internacional.
*   **Reacciones Internacionales:** China ha criticado las sanciones de EE.UU. y ha exigido el fin de los aranceles al petróleo venezolano. México también ha expresado su desacuerdo con las sanciones económicas.
*   **Disputa Territorial con Guyana:** EE.UU. ha prometido una respuesta firme si Venezuela ataca a Guyana, en medio de una disputa territorial que incluye importantes reservas de petróleo y gas.
        """,
 
    }
}

st.markdown('### Noticias clave')
st.markdown(country_data[selected_country]['overview'])
  
        
    


# Pie de página
st.markdown("---")
st.markdown("""
*Este reporte analiza las noticias de la semana centrándose en el impacto de las decisiones de la administración Trump en América Latina, el Caribe y el mundo. 
Se utiliza un enfoque basado en la frecuencia de las noticias y su potencial impacto, prestando atención a los últimos desenlaces como indicadores de tendencias futuras.
La clasificación de noticias, análisis y reportes automatizados de texto y audio asistidos por Inteligencia Artificial se encuentran en un proceso de desarrollo experimental en el cual
es fundamental la validación experta humana. Por lo tanto los resultados de los análisis deben tomarse con la debida cautela.*

""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown('<p class="small-text">Reporte preparado por CEPAL Lab para el Trade Emergency Team</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="small-text">Datos actualizados al 30 de marzo, 2025</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="small-text">© Cepal Lab - Versión demo </p>', unsafe_allow_html=True)
