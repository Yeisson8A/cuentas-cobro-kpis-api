from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


@patch("app.services.kpis_service.resumen")
def test_resumen(mock_resumen):
    mock_resumen.return_value = {"total": 100}

    response = client.get("/kpis/resumen")

    body = response.json()

    assert response.status_code == 200
    assert body["success"] is True
    assert body["data"] == {"total": 100}
    assert body["message"] == "OK"


@patch("app.services.kpis_service.por_periodo")
def test_por_periodo(mock_func):
    mock_func.return_value = [{"periodo": "2026-02", "total": 1000}]

    response = client.get("/kpis/por-periodo")
    body = response.json()

    assert response.status_code == 200
    assert body["success"] is True
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@patch("app.services.kpis_service.por_persona")
def test_por_persona(mock_func):
    mock_func.return_value = [{"nombre": "Test", "total": 500}]

    response = client.get("/kpis/por-persona")
    body = response.json()

    assert response.status_code == 200
    assert body["data"][0]["nombre"] == "Test"


@patch("app.services.kpis_service.top_periodos")
def test_top_periodos(mock_func):
    mock_func.return_value = [{"periodo": "2026-02", "total": 2000}]

    response = client.get("/kpis/top-periodos")
    body = response.json()

    assert response.status_code == 200
    assert body["data"][0]["total"] == 2000


@patch("app.services.kpis_service.crecimiento_mensual")
def test_crecimiento_mensual(mock_func):
    mock_func.return_value = [{"periodo": "2026-02", "crecimiento": 10}]

    response = client.get("/kpis/crecimiento-mensual")
    body = response.json()

    assert response.status_code == 200
    assert "crecimiento" in body["data"][0]


@patch("app.services.kpis_service.por_rango_fechas")
def test_por_rango_fechas_ok(mock_func):
    mock_func.return_value = [{"total": 1000}]

    response = client.get(
        "/kpis/por-rango-fechas?fecha_inicio=2026-02-01&fecha_fin=2026-02-28"
    )

    body = response.json()

    assert response.status_code == 200
    assert body["success"] is True
    assert body["data"] == [{"total": 1000}]


def test_por_rango_fechas_missing_params():
    response = client.get("/kpis/por-rango-fechas")

    assert response.status_code == 400
    assert "Debe enviar fecha_inicio" in response.json()["error"]["message"]


def test_por_rango_fechas_invalid_date():
    response = client.get(
        "/kpis/por-rango-fechas?fecha_inicio=2026-02-30&fecha_fin=2026-02-28"
    )

    assert response.status_code == 422
    assert response.json()["error"]["type"] == "validation_error"


def test_por_rango_fechas_wrong_order():
    response = client.get(
        "/kpis/por-rango-fechas?fecha_inicio=2026-03-01&fecha_fin=2026-02-01"
    )

    assert response.status_code == 400
    assert "no puede ser mayor" in response.json()["error"]["message"]