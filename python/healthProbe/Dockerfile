FROM registry.access.redhat.com/ubi9/python-311:1-45

# Copiamos el código fuente al directorio de trabajo del contenedor
COPY --chown=1001:1001 . /app

# Instalamos las dependencias necesarias
RUN pip install Flask

# Definimos el directorio de trabajo
WORKDIR /app
#RUN chmod 777 -R /app

# Ejecutamos el script cuando se inicie el contenedor
CMD ["python", "app.py"]
