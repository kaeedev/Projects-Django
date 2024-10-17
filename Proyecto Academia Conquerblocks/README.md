
## ESP:

# Proyecto de Pagina Web de la academia Conquerblocks (Internacionalizado) 📚

Esta es una página web sencilla sin estilos con varias vistas y funcionalidades como logearse, ver cursos si estas logieado (vistas protegidas), ver noticias destacas desde la Home Page.... Todo realizado con **HTML** y **Django**. La página web cuenta con una versión en español y otra en inglés. Podemos cambiar la versión con tan solo darle a un botón gracias a Django Rosetta. El proyecto también cuenta con vistas protegidas.

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es crear una página web con funcionalidades y desde el admin crear las diversas noticias y cursos que queramos. Primeros acercamientos al Backend

## 👁️ Vista previa del proyecto
<img src="images/FireShot%Capture%029%-%Página%Home%-%127.0.0.1.png" width=1200>
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

---
## EN:

# Library Website Project (Internationalized) 📚

This is a simple, unstyled website with several views and functionalities such as logging in, registering, adding books, authors, or publishers, editing them, deleting them, and a search bar. Everything is done using HTML and Django. The website has both a Spanish and English version. We can switch between versions with just a click, thanks to Django Rosetta. The project also includes protected views.

## 🎯 Project Objective

The objective of this project is to create a website with functionalities and a database to store created data and users. This is a first approach to backend development.

## 👁️ Project Preview

<img src="images/Captura%20de%20pantalla%202024-10-12%20143052.png" width=1200> <img src="images/Captura%20de%20pantalla%202024-10-12%20143106.png" width=1200> <img src="images/Captura%20de%20pantalla%202024-10-12%20143125.png" width=1200> <img src="images/Captura%20de%20pantalla%202024-10-12%20143204.png" width=1200>

## 🛠️ Project Structure

The project is organized into several folders and files for easy maintenance and expansion:

A biblioteca folder corresponds to the main "app":

- A templates folder, which contains all the project's HTML files with corresponding views for authors, publishers, books, general views, and error pages.
- admin.py: File where we register and customize our models for the Django admin.
- context_processor.py: File where we define context processors.
- settings.py: File that contains all the project settings to make it functional.
- models.py: File where we create our main models.
- urls.py: File where we define and connect our main URLs.
- views.py: File where we create the project's main views.

A books folder corresponds to a "sub-app" within the library:

- A forms folder, where independent forms are created as needed.
- A models folder, where author, publisher, and book models are created.
- A urls folder, where the URLs for author, publisher, and book are defined.
- A views folder, where we create views for authors, publishers, and books.
- admin.py: File where we register our models so they can be used in the admin.
- custom_middleware.py: File where we create custom middleware.
- decorators.py: File where we create custom decorators.
- An images folder contains some project screenshots for visual reference.

A locale folder is used for the project's internationalization. This project only includes translations from Spanish to English.

create_data.py: An old file used to create models automatically. It was only used for testing purposes. 
manage.py: File that handles Django's functionalities and management. 
requirements.txt: File that lists the necessary dependencies for the project to work properly. These should be installed in a new virtual environment.

## 🚀 Features and Usage

- Register: The page has a form to register users, who will be saved in the database. It’s important to register to use all project features since there are protected views and functions.

- Login: You can log in with your user account.

- Add authors/books/publishers: If you're logged in, you can create new authors, books, or publishers with any information you want. The project already includes some example authors, books, and publishers.

- Edit/Delete authors/books/publishers: If you're logged in, you can also edit and delete existing authors, books, or publishers. Note: models are protected and can only be edited or deleted if you are the CREATOR of the models. If you're not the creator, you'll be redirected to a page informing you that you don't have permission to perform these actions.

- Contact form: The project includes a contact form connected to my email, allowing you to get in touch with me this way.

- Search bar: The project includes a search bar to find authors, books, and publishers.

- Internationalization: The project has an English translation. You can use the dropdown menu to switch the language. All project views and models, as well as their information, are translated.

- Protected views: Users who are not logged in won't be able to perform functions such as creating, editing, or deleting data. If they try, they'll be redirected to the login page.

- Admin usage: If you register, you can use Django's admin interface by adding /admin to the URL.

- Context processors: There are messages in the project to provide context to the user, such as informational or success messages.

. Form errors: The forms include support messages for when the user inputs incorrect data. There are also required fields that must be filled in.

- Counter: A counter shows the total number of books, authors, and publishers registered on the site. When you add a new model, the count increases, and when you delete one, it decreases.

## 🛠️ Installation and Running

1. Clone this repository:
   ```bash
   https://github.com/kaeedev/Projects-Django.git

2. Create a virtual environment to install the necessary dependencies:
   ```bash
   python3 -m venv venv
   
   ```
   or
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the project: You'll need to run a local server:
   Deberás runear un servidor local
   ```bash
   python manage.py runserver
   ```

6. Use the django admin if you wish:
   ```bash
   Add /admin to the end of the local server URL
   
## 📝 License

This project is available for educational and learning purposes only.

### Conditions:

The source code of this project can be used, modified, and distributed for educational purposes only.
If you have any questions or want to use any resource from this project, feel free to contact me.
