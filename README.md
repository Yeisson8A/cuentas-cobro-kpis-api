# Api para KPIs de Cuentas de Cobro en FastAPI y PostgreSQL contenerizada
Proyecto de desarrollo de una API para el cálculo de KPIs con base en información de cuentas de cobro, cuyo origen se encuentra en una automatización con **n8n**. Esta API se encuentra desarrollada en Python, usando las librerías Uvicorn, SQL Alchemy y FastAPI, además teniendo como base de datos **PostgreSQL**; todo esto contenerizado mediante **Docker**.

## Requisitos
- Docker y Docker Compose
- Python 3.8+

# Environment
- **DB_HOST:** Host del servidor de base de datos, o del contenedor en Docker, por ejemplo: postgresql
- **DB_PORT:** Puerto del servidor de base de datos, para PostgreSQL el puerto por defecto es 5432
- **DB_NAME:** Nombre de la base de datos
- **DB_USER:** Usuario del servidor de base de datos
- **DB_PASSWORD:** Contraseña del usuario del servidor de base de datos

### Crear la red Docker (una sola vez)
`docker network create cuentas-cobro-net`

### Conectar el contenedor PostgreSQL a la red
`docker network connect cuentas-cobro-net postgresql`

### Construir la imagen
`docker-compose build`

### Levantar todo
`docker-compose up -d`

## Acceso
- **API**: `http://localhost:8001`
- **Swagger**: `http://localhost:8001/docs`
- **PostgreSQL**: `localhost:5432`

## Ejecución de pruebas unitarias

### Ejecutar pruebas unitarias
`python -m pytest .`

### Visualizar cobertura
Carpeta `htmlcov` en la raiz del proyecto, y abrir en el navegador el archivo `index.html`

## Scripts de funciones SQL
Carpeta `db` en la raiz del proyecto, y dentro se encuentran cada uno de los scripts de las funciones utilizadas para la generación de los KPIs

## Workflow para automatización de carga de datos **n8n**
<img width="1043" height="266" alt="image" src="https://github.com/user-attachments/assets/cfb7f51c-531f-4075-ab7b-095e6b7625a8" />

Dentro de la carpeta `automation` en la raiz del proyecto, se encuentra el archivo `json` correspondiente a este flujo de procesos, con el nombre **Automatizacion_Cuentas_Cobro.json**

### Importación del Workflow:

- Localiza el archivo `Automatizacion_Cuentas_Cobro.json` en la carpeta `automation` de la raíz del proyecto.
- En la interfaz de n8n, crea un nuevo flujo.
- Haz clic en el menú (tres puntos) en la esquina superior derecha y selecciona **"Import from File"**.
- Selecciona el archivo `.json` mencionado.

### Configuración de Nodos:
Tras importar, se deberá actualizar las credenciales del nodo PostgreSQL:

- Haz clic en el nodo y selecciona **"Create New Credential"**.
- Ingresa los datos de conexión al servidor PostgreSQL tal y como se configuraron en el archivo `.env`, indicando:
    - **Host**: Corresponde al nombre del host del servidor donde se encuentra la base de datos a consultar.
    - **Base de datos**: Corresponde al nombre de la base de datos a utilizar.
    - **Usuario**: Corresponde al usuario de conexión al servidor de base de datos, el usuario por defecto de PostgreSQL es `postgres`.
    - **Contraseña**: Corresponde a la contraseña asociada a dicho usuario para conectarse al servidor de base de datos.
    - **Puerto**: Corresponde al puerto de conexión del servidor de base de datos, el puerto por defecto de PostgreSQL es `5432`.
