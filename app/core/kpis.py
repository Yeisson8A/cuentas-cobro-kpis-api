from datetime import date
import pandas as pd
from sqlalchemy import text
from app.db.config import engine

# Resumen general
def resumen():
    query = text("""
        SELECT 
            COUNT(*) as total_cuentas,
            SUM(valor) as total_facturado,
            AVG(valor) as promedio
        FROM cuentas_cobro;
    """)

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")[0] if not df.empty else {}
    return result


# Métricas por periodo
def por_periodo():
    query = text("""
        SELECT 
            periodo,
            COUNT(*) as cantidad,
            SUM(valor) as total
        FROM cuentas_cobro
        GROUP BY periodo
        ORDER BY periodo;
    """)

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")
    return result


# Métricas por persona
def por_persona():
    query = text("""
        SELECT 
            nombre,
            identificacion,
            COUNT(*) as cantidad,
            SUM(valor) as total
        FROM cuentas_cobro
        GROUP BY nombre, identificacion
        ORDER BY total DESC;
    """)

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")
    return result


# Top meses
def top_periodos():
    query = text("""
        SELECT 
            periodo,
            SUM(valor) as total
        FROM cuentas_cobro
        GROUP BY periodo
        ORDER BY total DESC
        LIMIT 5;
    """)

    df = pd.read_sql(query, engine)
    result = df.to_dict(orient="records")
    return result


# Crecimiento mensual
def crecimiento_mensual():
    query = """
        SELECT 
            periodo,
            SUM(valor) as total
        FROM cuentas_cobro
        GROUP BY periodo
        ORDER BY periodo;
    """

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
    query = text("""
        SELECT 
            COUNT(*) as total,
            SUM(valor) as total_valor
        FROM cuentas_cobro
        WHERE fecha BETWEEN :inicio AND :fin;
    """)

    df = pd.read_sql(query, engine, params={"inicio": fecha_inicio, "fin": fecha_fin})
    result = df.to_dict(orient="records")[0] if not df.empty else {}
    return result