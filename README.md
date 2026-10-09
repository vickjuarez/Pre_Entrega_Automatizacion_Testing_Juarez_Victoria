# Pre-Entrega: Automatización de Pruebas con Selenium y Pytest

Este proyecto es una automatización de pruebas end-to-end para la página SauceDemo. Está desarrollado utilizando el patrón de diseño **POM** para mantener el código ordenado y con los test organizados de manera aislada , con el objetivo de no dañar el progreso de otra prueba si es que alguna falla 

## Propósito del Proyecto
Validar de forma automatizada flujos ESCENCIALES de la plataforma (inicio de sesión, validación de títulos de inventario y gestión de productos en el carrito).

## Tecnologías Utilizadas
* Python como lenguaje principal
* Pytest para estructura de testing
* Selenium WebDriver para automatización
* Git y GitHub para control de versiones
* pip install selenium pytest pytest-html
  
## Cómo correr las pruebas  

1. Abrir el proyecto en Visual Studio Code.
2. Hacer clic en el ícono del tubo de ensayo ubicado en la barra lateral izquierda.
3. Para ejecutar todas las pruebas juntas, hacer clic en el botón de reproducción general en la esquina superior derecha del panel.
4. Para ejecutar una prueba individual, posicionarse sobre el archivo de test deseado.
5. Al pasar el cursor sobre el test específico, hacer clic en el botón de reproducción, que aparece a la derecha para correr únicamente esa prueba.

## Estructura del Proyecto
* `Test/`: Contiene los archivos de prueba con pytest.
* `Utils/`: Contiene los archivos auxiliares y Page Object Model.
* `Reports/`: Almacena el reporte HTML generado.

## Cómo generar el reporte HTML
Para ejecutar las pruebas y generar el reporte en la carpeta `Reports/`, utilizá el siguiente comando en la terminal:
```bash
python -m pytest --html=Reports/reporte_HTML.html --self-contained-html

## Cómo instalar las dependencias

Escribir la siguiente línea en la terminal:
```bash
pip install selenium pytest pytest-html

