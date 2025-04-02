import streamlit as st
from streamlit_echarts import st_echarts
import random


def render_wordcloud(words):
    def color():
        # Generar colores en el espectro cálido (rojos, naranjas, amarillos)
        r = random.randint(180, 255)  # Valores altos para rojo
        g = random.randint(50, 180)   # Valores medios para verde
        b = random.randint(0, 100)    # Valores bajos para azul
        # Convertir a formato hexadecimal
        return f"#{r:02x}{g:02x}{b:02x}"

    words = words


    data = [{"name": name, "value": value} for name, value in words]
    for item in data:   
        item['textStyle'] = {'color':color()}
    
    wordcloud_option = {
        "tooltip": {},
        "series": [{
        "type": "wordCloud", 
        "data": data,
        "rotationRange": [0, 0],
        "sizeRange": [15,40],
        "gridSize":7,
        "height": '600',
        "shape": 'circle',
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

    