from datetime import date
import pandas as pd
from app.config.config import engine

# Resumen general
def resumen():
    query = "SELECT * FROM resumen_cuentas_cobro();"

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")[0] if not df.empty else {}
    return result


# Métricas por periodo
def por_periodo():
    query = "SELECT * FROM cuentas_por_periodo();"

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")
    return result


# Métricas por persona
def por_persona():
    query = "SELECT * FROM cuentas_por_persona();"

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")
    return result


# Top meses
def top_periodos():
    query = "SELECT * FROM top_periodos();"

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")
    return result


# Crecimiento mensual
def crecimiento_mensual():
    query = "SELECT * FROM total_por_periodo();"

    df = pd.read_sql(query, engine)

    if df.empty:
        return []

    # Asegurar orden correcto
    df = df.sort_values("periodo")

    # Calcular crecimiento
    df["crecimiento"] = df["total"].pct_change() * 100

    # Limpiar NaN (primer mes no tiene anterior)
    df["crecimiento"] = df["crecimiento"].fillna(0)
    # Redondear valores
    df["crecimiento"] = df["crecimiento"].round(2)
    result = df.to_dict(orient="records")
    return result


# Métricas por rango de fechas
def por_rango_fechas(fecha_inicio: date, fecha_fin: date):
    query = "SELECT * FROM cuentas_resumen_rango(%(inicio)s, %(fin)s);"

    df = pd.read_sql(query, engine, params={"inicio": fecha_inicio, "fin": fecha_fin})
    result = df.to_dict(orient="records")[0] if not df.empty else {}
    return result