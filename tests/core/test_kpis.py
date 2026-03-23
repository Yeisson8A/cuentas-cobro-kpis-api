import pandas as pd
from datetime import date
from unittest.mock import patch
from app.core import kpis


@patch("app.core.kpis.pd.read_sql")
def test_resumen(mock_read_sql, mock_df_resumen):
    mock_read_sql.return_value = mock_df_resumen

    result = kpis.resumen()

    assert result["total_cuentas"] == 10
    assert result["total_facturado"] == 1000


@patch("app.core.kpis.pd.read_sql")
def test_resumen_empty(mock_read_sql):
    mock_read_sql.return_value = pd.DataFrame()

    result = kpis.resumen()

    assert result == {}


@patch("app.core.kpis.pd.read_sql")
def test_por_periodo(mock_read_sql, mock_df_por_periodo):
    mock_read_sql.return_value = mock_df_por_periodo

    result = kpis.por_periodo()

    assert len(result) == 2
    assert result[0]["periodo"] == "2026-01"


@patch("app.core.kpis.pd.read_sql")
def test_por_persona(mock_read_sql, mock_df_por_persona):
    mock_read_sql.return_value = mock_df_por_persona

    result = kpis.por_persona()

    assert result[0]["nombre"] == "Juan"


@patch("app.core.kpis.pd.read_sql")
def test_top_periodos(mock_read_sql, mock_df_top_periodos):
    mock_read_sql.return_value = mock_df_top_periodos

    result = kpis.top_periodos()

    assert result[0]["total"] == 2000


@patch("app.core.kpis.pd.read_sql")
def test_crecimiento_mensual(mock_read_sql, mock_df_crecimiento_mensual):
    mock_read_sql.return_value = mock_df_crecimiento_mensual

    result = kpis.crecimiento_mensual()

    assert result[0]["crecimiento"] == 0  # primer mes
    assert result[1]["crecimiento"] == 100.0  # (200-100)/100
    assert result[2]["crecimiento"] == -50.0  # (100-200)/200


@patch("app.core.kpis.pd.read_sql")
def test_crecimiento_mensual_empty(mock_read_sql):
    mock_read_sql.return_value = pd.DataFrame()

    result = kpis.crecimiento_mensual()

    assert result == []


@patch("app.core.kpis.pd.read_sql")
def test_por_rango_fechas(mock_read_sql, mock_df_por_rango_fechas):
    mock_read_sql.return_value = mock_df_por_rango_fechas

    fecha_inicio = date(2026, 2, 1)
    fecha_fin = date(2026, 2, 28)

    result = kpis.por_rango_fechas(fecha_inicio, fecha_fin)

    mock_read_sql.assert_called_once()
    assert result["total"] == 5


@patch("app.core.kpis.pd.read_sql")
def test_por_rango_fechas_empty(mock_read_sql):
    mock_read_sql.return_value = pd.DataFrame()

    result = kpis.por_rango_fechas(date(2026, 1, 1), date(2026, 1, 31))

    assert result == {}