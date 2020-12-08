# Notas-SAIA-Scrapping
Pequeño script para ver las notas de saia.psm.edu.ve/ sin necesidad de entrar a la página.

# Instrucciones

1.- Instalar Python 3.8.x (ignorar este paso si ya lo tienes instalado)

2.- Clonar el Repositorio en tu directorio

3.- Una vez clonado instala las dependencias de la siguiente manera:
    
    $ pip3 install requirements.txt

4.- Una vez instaladas dirígete al archivo "scrape_notas.py" y edita el diccionario USER_INFO:
  
    USER_INFO = {
    "username": "Tu nombre de usuario SAIA va aqui",
    "password": "Tu contraseña va aqui"
    }

5.- Una vez configurado tu usuario puedes ejecutar el script y observar tis notas

6.- (OBSERVACIÓN): para cambiar las materias que quieres visualizar debes de editar una línea del código:

    example = scrape_course_data(materias.<AQUÍ_VA_LA_MATERIA>, USER_INFO, SAIA_URLS)
    
    Las opciones (materias) disponibles son:
    
    materias.BASE_DE_DATOS
    materias.ESTRUCTURA_DE_DATOS
    materias.ORG_COMPUTADOR
    materias.ING_ECONOMICA
    materias.DISEÑO_DE_SISTEMAS
    materias.ANALISIS_NUMERICO
    materias.TEORIA_DE_ORGANIZACION
