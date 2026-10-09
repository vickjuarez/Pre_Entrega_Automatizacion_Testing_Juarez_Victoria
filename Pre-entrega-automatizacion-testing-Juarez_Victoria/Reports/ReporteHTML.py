# Para reemplazar escribir el codigo en la terminal que es este #pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html#
#genere el reporte de manera automatica, ademas de que me permite tener un control de errores y mostrar mensajes claros 
# al usuario sobre el estado de la ejecucion

import subprocess #con el módulo subprocess puedo ejecutar comandos de la terminal desde Python

def generar_reporte_html():
    print("Iniciando la ejecución de las pruebas y generación del reporte...")
    comando = [
        "python", 
        "-m", 
        "pytest", 
        "--html=reporte_HTML.html", 
        "--self-contained-html"
    ]
    
    try:
        resultado = subprocess.run(comando, check=True)
        print("\n ¡Éxito! El reporte 'reporte_HTML.html' se generó correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"\n Hubo un error al ejecutar las pruebas. Código de error: {e}")

# Este bloque me asegura que el script se vaya a ejecutar al correrlo
if __name__ == "__main__":
    generar_reporte_html()

 