from datetime import date

from app.core import kpis

# Resumen general
def resumen():
    return kpis.resumen()


# Métricas por periodo
def por_periodo():
    return kpis.por_periodo()


# Métricas por persona
def por_persona():
    return kpis.por_persona()


# Top meses
def top_periodos():
    return kpis.top_periodos()


# Crecimiento mensual
def crecimiento_mensual():
    return kpis.crecimiento_mensual()


# Métricas por rango de fechas
def por_rango_fechas(fecha_inicio: date, fecha_fin: date):
    return kpis.por_rango_fechas(fecha_inicio, fecha_fin)