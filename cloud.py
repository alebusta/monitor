import streamlit as st
from streamlit_echarts import st_echarts
import random


def render_wordcloud():
    def color():
        # Generar colores en el espectro cálido (rojos, naranjas, amarillos)
        r = random.randint(180, 255)  # Valores altos para rojo
        g = random.randint(50, 180)   # Valores medios para verde
        b = random.randint(0, 100)    # Valores bajos para azul
        # Convertir a formato hexadecimal
        return f"#{r:02x}{g:02x}{b:02x}"

    words = [('aranceles', 100), ('economía', 88), ('relaciones internacionales', 84), ('comercio internacional', 64), ('política', 61), ('política internacional', 47), ('migración', 43), ('política exterior', 39), ('gobierno', 38), ('petróleo', 37), ('comercio exterior', 33), ('diplomacia', 30), ('política migratoria', 29), ('corrupción', 28), ('organizaciones internacionales', 27), ('derechos humanos', 27), ('finanzas', 24), ('sanciones', 24), ('guerra', 21), ('tecnología', 20), ('política comercial', 20), ('política económica', 20), ('remesas', 19), ('seguridad nacional', 19), ('relaciones bilaterales', 18), ('seguridad', 17), ('narcotráfico', 17), ('crimen organizado', 16), ('deportación', 16), ('inmigración', 15), ('gobierno y política', 15), ('elecciones', 15), ('geopolítica', 15), ('energía', 14), ('relaciones comerciales', 14), ('democracia', 13), ('actualizaciones', 12), ('inversión', 12), ('inversión extranjera', 12), ('cooperación internacional', 12), ('guerra comercial', 11), ('conflicto', 11), ('economía global', 11), ('crecimiento económico', 10), ('violencia', 10), ('exportaciones', 10), ('inflación', 10), ('soberanía', 10), ('desarrollo económico', 9), ('presencia militar', 9), ('política energética', 8), ('impacto económico', 8), ('liderazgo', 7), ('negocios', 7), ('sanciones económicas', 7), ('desarrollo sostenible', 7), ('justicia', 7), ('inversiones', 6), ('refugiados', 6), ('canal interoceánico', 6), ('relaciones diplomáticas', 6), ('transparencia', 6), ('proteccionismo', 6), ('producción', 6), ('mercados financieros', 6), ('conflicto territorial', 6), ('política regional', 5), ('industria automotriz', 5), ('deportaciones', 5), ('Canal de Panamá', 5), ('multilateralismo', 5), ('tráfico de drogas', 5), ('infraestructura', 5), ('fronteras', 5), ('globalización', 5), ('soberanía nacional', 5), ('justicia penal', 5), ('amnistía', 4), ('comercio', 4), ('crisis económica', 4), ('liderazgo político', 4), ('desigualdad económica', 4), ('alianzas comerciales', 4), ('producción industrial', 4), ('cultura', 4), ('seguridad fronteriza', 4), ('migración ilegal', 4), ('gasoducto', 4), ('turismo', 4), ('desapariciones', 4), ('educación', 4), ('moneda', 4), ('investigación', 3), ('estabilidad macroeconómica', 3), ('crímenes de lesa humanidad', 3), ('influencia geopolítica', 3), ('frontera', 3)]


    data = [{"name": name, "value": value} for name, value in words]
    for item in data:
        item['textStyle'] = {'color':color()}
    
    wordcloud_option = {
        "tooltip": {},
        "series": [{
        "type": "wordCloud", 
        "data": data,
        "rotationRange": [0, 0],
        #"height": '95%',
        "textStyle": {
            #"color": lambda params: color()
        },
        "emphasis": {
            "focus": 'self',
            "textStyle": {
                "textShadowBlur": 10,
                "textShadowColor": '#333'
            }
        }
        }]
        }
    st_echarts(wordcloud_option)

    # Para que se ejecute automáticamente al llamar el archivo
if __name__ == "__main__":
    render_wordcloud()

    