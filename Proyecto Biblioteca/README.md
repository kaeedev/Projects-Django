## ESP:

# Proyecto de Pagina Web de una Biblioteca (Internacionalizado) 📚

Esta es una página web sencilla sin estilos con varias vistas y funcionalidades como logearse, registrarse, registrar libros, autores o editoriales, editarlos, borrarlos, barra de busqueda.... Todo realizado con **HTML** y **Django**. La página web cuenta con una versión en español y otra en inglés. Podemos cambiar la versión con tan solo darle a un botón gracias a Django Rosetta. El proyecto también cuenta con vistas protegidas

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es crear una página web con funcionalidades y con una base de datos donde guardar los datos creados y los usuarios creados. Primer acercamiento al Backend

## 👁️ Vista previa del proyecto
<img src="images/Captura%20de%20pantalla%202024-10-12%20143052.png" width=1200>
<img src="images/Captura%20de%20pantalla%202024-10-12%20143106.png" width=1200>
<img src="images/Captura%20de%20pantalla%202024-10-12%20143125.png" width=1200>
<img src="images/Captura%20de%20pantalla%202024-10-12%20143204.png" width=1200>

## 🛠️ Estructura del Proyecto

El proyecto está organizado en varias carpetas y archivos para facilitar su mantenimiento y expansión:

Una carpeta **biblioteca** que corresponderá a la "app" principal:
- Una carpeta **templates** donde recoge todos los HTMLs del proyecto con sus vistas correspondientes para autores, editoriales, libros, vistas generales y     para errores.
- **admin.py**: Fichero donde registramos y personalizamos nuestros modelos para que aparezcan en el admin de Django.
- **context_processor.py**: Fichero donde definimos procesadores de contexto.
- **settings.py**: Fichero que recoge todos los ajustes del proyecto para poder funcionar.
- **models.py**: Fichero donde creamos nuestros modelos principales.
- **urls.py**: Fichero donde definimos y conectamos nuestras urls principales.
- **views.py**: Fichero donde creamos nuestras vistas principales del proyecto.
- **game.py**: Maneja el flujo del juego y toda su lógica principal.

Una carpeta **books** que corresponderá a una "subapp" de biblioteca:
- Una carpeta **forms** donde se crean los formularios independientes para lo que se necesite.
- Una carpeta **models** donde se crean los modelos de autor, editorial y libro.
- Una carpeta **urls** donde se definen las urls de autor, editorial y libro.
- Una carpeta **views** donde creamos las vistas de autor, editorial y libro.
- **admin.py**: Fichero donde registramos nuestros modelos para que puedan ser utilizados en el admin.
- **custom_middleware.py**: Fichero donde creamos middlewares personalizados.
- **decorators.py**: Fichero donde creamos decoradores personalizados.

Una carpeta **images** que contiene algunas capturas del proyecto para su visualización

Una carpeta **locale** que es utilizada para la internacionalización del proyecto. Este proyecto solo cuenta con traducciones del español al inglés

**create_data.py**: Antiguo fichero para crear modelos de forma automatizada. Servia para testear solamente.
**manage.py**: Fichero que recoge las funcionalidades y manejo de django.
**requirements.txt**: Fichero que recoge los requerimientos que hacen falta para que el proyecto funcione adecuadamente. Se deberán instalar en un nuevo entorno virtual


## 🚀 Funcionalidades y uso

- **Registro**: La página cuenta con un formulario para registrar usuarios que quedarán guardados en la base de datos. Es muy importante registrarse para
  poder utilizar todas las funcionalidades del proyecto, ya que el proyecto tiene vistas protegidas y funciones protegidas.
  
- **Iniciar sesión**: Podrás logearte con tu usuario
  
- **Agregar autores/libros/editoriales**: Si estás logeado con un usuario, puedes crear nuevos autores, libros o editoriales con la información que tu       
  quieras. El proyecto de base ya cuenta con algunos autores, libros y editoriales a modo de ejemplo

- **Editar/Borrar autores/libros/editoriales**: Si estás logeado, también puedes editar y borrar los autores, libros o editoriales existentes. **¡OJO!** los
  modelos también cuentan con protección y solo podrán ser editables o borrables si eres **CREADOR** de esos modelos. Si no eres creador, te redireccionará a   una página que te dirá que no tienes permiso para llevar a cabo dichas acciones.

- **Posibilidad de contacto**: El proyecto cuenta con un formulario de contacto el cual está conectado a mi correo, por lo cual se puede contactar conmigo       también de esta manera

- **Barra de busqueda**: El proyecto cuenta con una barra de busqueda para buscar autores, libros y editoriales.

- **Internacionalización**: El proyecto cuenta con traducción al inglés. Solo debemos utilizar el desplegable para llevar a cabo el cambio. Están traducidas
  todas las vistas del proyecto y todos los modelos, así como su información.

- **Vistas protegidas**: Los usuarios que no estén logeados no podrán realizar funciones como crear, editar o borrar datos. Si lo intentan se les         
  redireccionará al login

- **Uso del admin**: Si te registras, puedes utilizar el admin de django con ese usuario poniendo /admin en el enlace

- **Procesadores de contexto**: En el proyecto existen mensajes para brindar contexto al usuario. Mensajes de información y de éxito.

- **Errores en formularios**: Los formularios cuentan con mensajes de apoyo para cuando el usuario introduce mal algún dato. También existen campos 
  obligatorios que deberán rellenarse si o si

- **Contador**: Existe un contador de cuantos libros, autores y editoriales hay registrados en la página. Al añadir un nuevo modelo se incrementa y al borrar
  disminuye


## 🛠️ Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   https://github.com/kaeedev/Projects-Django.git

2. Crea un entorno virtual en el proyecto para instalar las dependencias necesarias:
   ```bash
   python3 -m venv venv
   
   ```
 o
   ```bash
   python -m venv venv
   ```

3. Inicia el entorno virtual que has creado:
   ```bash
   source venv/bin/activate

4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta el programa:
   Deberás runear un servidor local
   ```bash
   python manage.py runserver
   ```

6. Usar el admin de django si lo deseas:
   ```bash
   Añadir /admin al final del enlace del servidor local

## 📝 Licencia

Este proyecto está disponible únicamente para uso **docente** y con fines de aprendizaje.

### Condiciones:
- El código fuente de este proyecto puede ser usado, modificado y distribuido solo con fines educativos.

Si tienes alguna duda o quieres utilizar algún recurso de este proyecto, por favor contacta conmigo.
