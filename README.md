# Entrega Intermedia de Proyecto Final (Coderhouse Python 31090)
## _Wine Store_

## Miembros del equipo

- Lucía Gómez Salinas
- Manuel Florez
- Luis Pablo Segovia


| Nombre | LinkedIn | GitHub | Email |
| ------ | ------ | ------ | ------ |
| Lucía Gomez Salinas | https://www.linkedin.com/in/luciadgsalinas/| https://github.com/luciadgsalinas | luciag.salinas92@gmail.com | 
| Manuel Florez | https://www.linkedin.com/in/manuel14mds/ | https://github.com/manuel14mds | manuel14mds@gmail.com | 
| Luis Pablo Segovia | https://www.linkedin.com/in/luispablosegovia/ | https://github.com/manoloacademia| luispablosegovia@icloud.com | 


## Proyecto: Vinos

El proyecto se basa en un e-commerce de vinos.
En él se pueden encontrar 3 clases de modelos:

- Vinos (Wines)
- Bodegas (Wineries)
- Variedades (Varietal)

Además, se pueden agregar nuevas instancias de estos modelos a la base de datos.

## Navegación y tipos de usuario

Se puede acceder a las distintas opciones de la navbar dependiendo del tipo de usuario:
- Usuario no logueado
- Usuario logueado
- Usuario administrador

En caso de ser un "usuario no logueado" las opciones son:
- Home
- All wines
- Varietal
- Winery
- About Us
- Login
- Register
- Search

En caso de ser un "usuario logueado" las opciones son las mismas opciones +:
- Log out
- Create Profile 
- Profile
- Update profile
- Shop

En caso de ser un "usuario administrador" tiene todas la opciones que un usuario logueado:
- Add Wine
- Add varietal
- Add winery
- Crud Wines

## Video de Navegación por el proyecto
### Hacer click en la imagen del vino:

[![Watch the video](https://media.istockphoto.com/photos/detail-of-pouring-red-wine-into-glass-picture-id1191927537?k=20&m=1191927537&s=612x612&w=0&h=-0PFgiUFJyHDBPl3UZnmQSYtMU20IhtD_ESJelfRdes=)](https://www.youtube.com/watch?v=2-M1FfZu5y8) 

## Tecnologías

| TECNOLOGÍA | VERSIÓN | DESCRIPCIÓN |
| ------ | ------ | ------ |
| Python | v3.9.6 | Lenguaje de programación |
| Bootstrap | v4.6 | Diseño y estilos |
| Django | v4.1 | Framework de python |
| django-crispy-form | v1.14.0 | Imágenes del formulario |
| Pillow | v9.2.0 | Imágenes de modelos  |
| HTML | v5 | Web |
| CSS | v3 | Estilos  |

## Instalación

Se debe crear un virtual environment en el cual se pueda instalar django y todas las dependencias para correr el programa.
Para hacerlo de forma más simple se puede acceder al archivo requirements.txt que se encuentra en el repositorio.
Para hacer la instalación, una vez creado el virtual environment, acceder con:

```
pip install -r requirements.txt
```

Una vez instalados todos los requerimientos, es necesario iniciar el servidor con el comando:

```
python manage.py runserver
```

Una vez que el runserver este corriendo, podemos acceder al local host que nos brinda la terminal.

```
http://127.0.0.1:8000/
```


## License

MIT

**Free Software, Hell Yeah!**
