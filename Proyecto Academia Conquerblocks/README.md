
## ESP:

# Proyecto de Pagina Web de la academia Conquerblocks (Internacionalizado) 📚

Esta es una página web sencilla sin estilos con varias vistas y funcionalidades como logearse, ver cursos si estas logieado (vistas protegidas), ver noticias destacas desde la Home Page.... Todo realizado con **HTML** y **Django**. La página web cuenta con una versión en español y otra en inglés. Podemos cambiar la versión con tan solo darle a un botón gracias a Django Rosetta. El proyecto también cuenta con vistas protegidas.

## 🎯 Objetivo del Proyecto

El objetivo de este proyecto es crear una página web con funcionalidades y desde el admin crear las diversas noticias y cursos que queramos. Primeros acercamientos al Backend

## 👁️ Vista previa del proyecto

<img src="images/captura1.png" width=1200>
<img src="images/captura2.png" width=1200>
<img src="images/captura3.png" width=1200>
<img src="images/captura4.png" width=1200>
<img src="images/captura5.png" width=1200>


## 🛠️ Estructura del Proyecto

El proyecto está organizado en varias carpetas y archivos para facilitar su mantenimiento y expansión:

Una carpeta **blog** que corresponderá a la app de las noticias:
- **admin.py**: Fichero donde registramos y personalizamos nuestros modelos para que aparezcan en el admin de Django.
- **models.py**: Fichero donde creamos nuestro modelo de post.
- **urls.py**: Fichero donde definimos y conectamos nuestras urls de post.
- **views.py**: Fichero donde creamos nuestras vistas de post.
- **translation.py**: Fichero donde traducimos nuestro modelo para que en el admin aparezca un campo en español y otro en ingles para que sea traducible.

Una carpeta **conquerblocks** que corresponderá a la app principal:
- Una carpeta **static** que contendrá las imagenes principales para el proyecto
- Una carpeta **templates** donde se crearan todas las plantillas HTMLs de nuestro proyecto
- **urls.py**: Fichero donde definimos nuestras URLs principales.
- **settings**: Fichero donde pondremos todas las configuraciones del proyecto, como INSTALLED_APPS, MIDDLEWARES...

Una carpeta **core** que corresponderá a una subapp con modelos core, que sería como los modelos y vistas principales del proyecto.
- **admin.py**: Fichero donde registramos y personalizamos nuestros modelos para que aparezcan en el admin de Django.
- **models.py**: Fichero donde creamos nuestro modelo de contact.
- **urls.py**: Fichero donde definimos y conectamos nuestras urls de home, login, register, logout, contact, about_us, avisoslegales.
- **views.py**: Fichero donde creamos nuestras vistas de home, login, register, logout, contact, about_us y avisoslegales.
- **forms.py**: Fichero donde creamos nuestros formularios de contacto, login y register

Una carpeta **courses** que corresponderá a la app de cursos:
- **admin.py**: Fichero donde registramos y personalizamos nuestros modelos para que aparezcan en el admin de Django.
- **models.py**: Fichero donde creamos nuestro modelo de cursos.
- **urls.py**: Fichero donde definimos y conectamos nuestras urls de cursos.
- **views.py**: Fichero donde creamos nuestras vistas de cursos.
- **translation.py**: Fichero donde traducimos nuestro modelo para que en el admin aparezca un campo en español y otro en ingles para que sea traducible.

Una carpeta **images** con capturas del proyecto para mostrar una vista previa del mismo en este README

Una carpeta **locale** que será la encargada de internacionalizar el proyecto gracias a las traducciones hechas con Django Rosetta

Una carpeta **media** que servirá para que desde el admin podamos seleccionar que archivos pdf queremos descargar en las vistas de cursos y también para poner portadas a cursos y blogs

Una carpeta **static** con varias herramientas de django instaladas como django debug toolbar, ckeditor para mejorar el textarea base de Django...

**manage.py**: Fichero que recoge las funcionalidades y manejo de django.

**requirements.txt**: Fichero que recoge los requerimientos que hacen falta para que el proyecto funcione adecuadamente. Se deberán instalar en un nuevo entorno virtual


## 🚀 Funcionalidades y uso

- **Registro**: La página cuenta con un formulario para registrar usuarios que quedarán guardados en la base de datos. Es muy importante registrarse para
  poder utilizar al 100% la página, ya que se requiere un usuario para ver la vista Cursos.
  
- **Iniciar sesión**: Podrás logearte con tu usuario registrado previamente.

- **Posibilidad de contacto**: El proyecto cuenta con un formulario de contacto el cual está conectado a mi correo, por lo cual se puede contactar conmigo también de esta manera

- **Internacionalización**: El proyecto cuenta con traducción al inglés. Solo debemos utilizar el desplegable para llevar a cabo el cambio. Están traducidas
  todas las vistas del proyecto y todos los modelos, así como su información.

- **Vistas protegidas**: Los usuarios que no estén logeados no podrán consultar los cursos.

- **Uso del admin**: Si te registras, puedes utilizar el admin de django con ese usuario poniendo /admin en el enlace y crear nuevos cursos y noticias con CKEDITOR

- **Errores en formularios**: Los formularios cuentan con mensajes de apoyo para cuando el usuario introduce mal algún dato. También existen campos 
  obligatorios que deberán rellenarse si o si


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
