from datetime import date
from fastapi import APIRouter, Query, HTTPException
from app.responses.response import success_response
from app.services import kpis_service

router = APIRouter(prefix="/kpis", tags=["KPIs"])

# Resumen general
@router.get("/resumen")
def resumen():
    data = kpis_service.resumen()
    return success_response(data)


# Métricas por periodo
@router.get("/por-periodo")
def por_periodo():
    data = kpis_service.por_periodo()
    return success_response(data)


# Métricas por persona
@router.get("/por-persona")
def por_persona():
    data = kpis_service.por_persona()
    return success_response(data)


# Top meses
@router.get("/top-periodos")
def top_periodos():
    data = kpis_service.top_periodos()
    return success_response(data)


# Crecimiento mensual
@router.get("/crecimiento-mensual")
def crecimiento_mensual():
    data = kpis_service.crecimiento_mensual()
    return success_response(data)


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

    data = kpis_service.por_rango_fechas(fecha_inicio, fecha_fin)
    return success_response(data)