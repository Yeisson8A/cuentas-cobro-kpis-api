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