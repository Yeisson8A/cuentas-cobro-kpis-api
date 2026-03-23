from datetime import date
from unittest.mock import patch
from app.services import kpis_service


@patch("app.core.kpis.resumen")
def test_resumen(mock_func):
    mock_func.return_value = {"total": 100}

    result = kpis_service.resumen()

    mock_func.assert_called_once()
    assert result == {"total": 100}


@patch("app.core.kpis.por_periodo")
def test_por_periodo(mock_func):
    mock_func.return_value = [{"periodo": "2026-02"}]

    result = kpis_service.por_periodo()

    mock_func.assert_called_once()
    assert isinstance(result, list)


@patch("app.core.kpis.por_persona")
def test_por_persona(mock_func):
    mock_func.return_value = [{"nombre": "Test"}]

    result = kpis_service.por_persona()

    mock_func.assert_called_once()
    assert result[0]["nombre"] == "Test"


@patch("app.core.kpis.top_periodos")
def test_top_periodos(mock_func):
    mock_func.return_value = [{"total": 2000}]

    result = kpis_service.top_periodos()

    mock_func.assert_called_once()
    assert result[0]["total"] == 2000


@patch("app.core.kpis.crecimiento_mensual")
def test_crecimiento_mensual(mock_func):
    mock_func.return_value = [{"crecimiento": 10}]

    result = kpis_service.crecimiento_mensual()

    mock_func.assert_called_once()
    assert "crecimiento" in result[0]


@patch("app.core.kpis.por_rango_fechas")
def test_por_rango_fechas(mock_func):
    mock_func.return_value = [{"total": 500}]

    fecha_inicio = date(2026, 2, 1)
    fecha_fin = date(2026, 2, 28)

    result = kpis_service.por_rango_fechas(fecha_inicio, fecha_fin)

    mock_func.assert_called_once_with(fecha_inicio, fecha_fin)
    assert result == [{"total": 500}]