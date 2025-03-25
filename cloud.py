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

    words = [('economía', 101), ('gobierno', 101), ('relaciones internacionales', 86), ('política migratoria', 69), ('migración', 64), ('política', 57), ('política internacional', 50), ('política exterior', 47), ('derechos humanos', 46), ('aranceles', 45), ('petróleo', 41), ('comercio internacional', 41), ('corrupción', 39), ('sanciones', 34), ('inmigración', 34), ('deportación', 31), ('desarrollo económico', 26), ('justicia', 25), ('política económica', 24), ('diplomacia', 24), ('negocios', 23), ('inversión', 22), ('finanzas', 22), ('política energética', 22), ('energía', 19), ('política comercial', 19), ('seguridad', 18), ('remesas', 16), ('seguridad nacional', 16), ('conflicto', 15), ('cooperación internacional', 14), ('relaciones comerciales', 14), ('guerra', 14), ('refugiados', 14), ('tecnología', 13), ('conflicto internacional', 13), ('violencia', 12), ('seguridad pública', 12), ('crimen organizado', 12), ('moneda', 12), ('organizaciones internacionales', 11), ('economía global', 11), ('elecciones', 10), ('inflación', 10), ('relaciones bilaterales', 10), ('trabajo', 10), ('detención', 9), ('crecimiento económico', 9), ('seguridad marítima', 9), ('migración forzada', 9), ('mercado financiero', 8), ('guerra comercial', 8), ('infraestructura', 8), ('geopolítica', 8), ('inversión extranjera', 8), ('producción', 7), ('empresas', 7), ('democracia', 7), ('gobierno federal', 7), ('seguridad fronteriza', 7), ('viajes', 7), ('medios de comunicación', 7), ('recursos naturales', 7), ('defensa', 7), ('desarrollo regional', 7), ('comercio marítimo', 6), ('medio ambiente', 6), ('independencia', 6), ('mercados financieros', 6), ('prisiones', 6), ('terrorismo', 6), ('recortes presupuestarios', 6), ('delincuencia', 6), ('estrategia geopolítica', 6), ('proteccionismo', 6), ('integración regional', 6), ('negociaciones', 6), ('industria automotriz', 6), ('investigación', 6), ('Venezuela', 6), ('relaciones diplomáticas', 5), ('relocalización', 5), ('gobierno migratorio', 5), ('producción industrial', 5), ('periodismo', 5), ('relaciones geopolíticas', 5), ('competición deportiva', 5), ('deportaciones', 5), ('canal de Panamá', 5), ('crisis', 5), ('gasto público', 5), ('innovación', 5), ('legislación', 5), ('política monetaria', 5), ('competencia económica', 5), ('comercio', 5), ('criptomoneda', 5)]


    data = [{"name": name, "value": value} for name, value in words]
    for item in data:
        item['textStyle'] = {'color':color()}
    
    wordcloud_option = {
        "tooltip": {},
        "series": [{
        "type": "wordCloud", 
        "data": data,
        "rotationRange": [0, 0],
        "height": '95%',
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

    