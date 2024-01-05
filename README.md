[English](#english)    

## Contenedor Docker para Python - Proyecto de prueba 

### Descripción
Este repositorio contiene los archivos necesarios para editar y probar una app de python, usando contenedores docker.

### Archivos
- app (carpeta)  
    es la carpeta para la aplicación en Python  
- Dockerfile  
    con este archivo se puede hacer la imagen de Python  
    Para hacer este proyecto trabaje en en windows 10 pro, con Docker Desktop instalado, con un entorno Ubuntu (WSL), en este entorno linux, en una terminal de comando, y dentro de la carpeta donde se encuentra este archivo ejecutamos el siguiente comando:
  
        docker build -t python-app
  
    luego con este otro comando levanto el contenedor, conecto ambas carpetas (en ubuntu y en contenedor)
  
        docker run -it -v /home/lean/learning/docker/python/app:/app python-app  


<a name="english"></a>
## Docker container for Python- Test project 

### Description
This repository contains the files necessary to edit and test a python app, using docker containers.  

### Files
- app (folder)  
    This is the folder for the Python app  
- Dockerfile  
    with this file we can create the Python image  
    To do this project, I worked on Windows 10 Pro, with Docker Desktop installed, with an Ubuntu environment (WSL), in this Linux environment, in a command terminal, and inside the folder where this file is located, we execute the following command:
  
        docker build -t python-app
  
    then with this other command raise the container, connect both folders (in ubuntu and in container)
  
        docker run -it -v /home/lean/learning/docker/python/app:/app python-app  
