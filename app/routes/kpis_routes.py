from datetime import date
from fastapi import APIRouter, Query, HTTPException
from app.services import kpis_service

router = APIRouter(prefix="/kpis", tags=["KPIs"])

# Resumen general
@router.get("/resumen")
def resumen():
    return kpis_service.resumen()


# Métricas por periodo
@router.get("/por-periodo")
def por_periodo():
    return kpis_service.por_periodo()


# Métricas por persona
@router.get("/por-persona")
def por_persona():
    return kpis_service.por_persona()


# Top meses
@router.get("/top-periodos")
def top_periodos():
    return kpis_service.top_periodos()


# Crecimiento mensual
@router.get("/crecimiento-mensual")
def crecimiento_mensual():
    return kpis_service.crecimiento_mensual()


# Métricas por rango de fechas
@router.get("/por-rango-fechas")
def por_rango_fechas(fecha_inicio: date = Query(default=None, description="Fecha inicial en formato Año-Mes-Día"), 
          fecha_fin: date = Query(default=None, description="Fecha final en formato Año-Mes-Día")):
    
    if not fecha_inicio or not fecha_fin:
        raise HTTPException(
            status_code=400,
            detail="Debe enviar fecha_inicio y fecha_fin en formato YYYY-MM-DD"
        )
    
    if fecha_inicio > fecha_fin:
        raise HTTPException(
            status_code=400,
            detail="fecha_inicio no puede ser mayor que fecha_fin"
        )

    return kpis_service.por_rango_fechas(fecha_inicio, fecha_fin)