def extraer_secciones(contenido_md):
    """
    Extrae secciones de un archivo markdown basadas en los encabezados de nivel 2 (##).
    Retorna un diccionario con los títulos de sección y su contenido.
    """
    secciones = {}
    lineas = contenido_md.split('\n')
    seccion_actual = None
    contenido_seccion = []
    
    for linea in lineas:
        if linea.startswith('## '):
            # Si encontramos un nuevo encabezado, guardamos la sección anterior
            if seccion_actual is not None:
                secciones[seccion_actual] = '\n'.join(contenido_seccion)
                contenido_seccion = []
            # Actualizamos la sección actual
            seccion_actual = linea[3:].strip()
        elif seccion_actual is not None:
            contenido_seccion.append(linea)
    
    # Guardamos la última sección si existe
    if seccion_actual is not None and contenido_seccion:
        secciones[seccion_actual] = '\n'.join(contenido_seccion)
    
    return secciones



