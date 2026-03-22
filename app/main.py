from fastapi import FastAPI
from app.handlers.error_handlers import register_exception_handlers
from app.routes import kpis_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="KPI API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"  # Angular
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar handlers globales
register_exception_handlers(app)

# Registrar rutas
app.include_router(kpis_routes.router)