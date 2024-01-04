[English](#english)    

## Contenedor Docker para Python - Proyecto de prueba 

### Descripción
Este repositorio contiene los archivos necesarios para editar y probar una app de python, usando contenedores docker.

### Lista de elementos
- app (carpeta)
    es la carpeta para la aplicación en Python
- Dockerfile
    con este archivo se puede hacer la imagenes de Python
    Para hacer este proyecto trabaje en en windows 10 pro, con Docker Desktop instalado, con un entorno Ubuntu (WSL), en este entorno linux, en una terminal de comando, y dentro de la carpeta donde se encuentra este archivo ejecutamos el siguiente comando:  
    docker run -it -v /app:/app python-app
    luego con este otro comando levanto el contenedor, conecto ambas carpetas (en ubuntu y en contenedor)  
    docker run -it -v /home/lean/learning/docker/python/app:/app python-app


<a name="english"></a>
## Docker - Proyecto de prueba 

### Descripción
Este repositorio contiene los archivos necesarios para ver como funciona una aplicación, en este caso una app Node JS conectada a una base de datos Mongo, usando contenedores docker.

### Lista de elementos
- app (carpeta)
    es la carpeta para la aplicación en Node JS
- .gitignore
   este archivo no se usa debido a la ausencia de datos sensibles como claves, nombres de usuario...
- Dockerfile
    con este archivo se pueden hacer las imagenes de node, mongo y mongoexpress
- mongo.yaml
    este archivo usado con docker-compose contiene la configuración para iniciar los contenedores y el volúmen 
