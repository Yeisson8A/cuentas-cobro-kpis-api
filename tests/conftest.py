import pandas as pd
import pytest

@pytest.fixture
def mock_df_resumen():
    return pd.DataFrame([{
        "total_cuentas": 10,
        "total_facturado": 1000,
        "promedio": 100
    }])

@pytest.fixture
def mock_df_por_periodo():
    return pd.DataFrame([
        {"periodo": "2026-01", "cantidad": 2, "total": 500},
        {"periodo": "2026-02", "cantidad": 3, "total": 800},
    ])

@pytest.fixture
def mock_df_por_persona():
    return pd.DataFrame([
        {"nombre": "Juan", "identificacion": "123", "cantidad": 2, "total": 500}
    ])

@pytest.fixture
def mock_df_top_periodos():
    return pd.DataFrame([
        {"periodo": "2026-02", "total": 2000}
    ])

@pytest.fixture
def mock_df_crecimiento_mensual():
    return pd.DataFrame([
        {"periodo": "2026-01", "total": 100},
        {"periodo": "2026-02", "total": 200},
        {"periodo": "2026-03", "total": 100},
    ])

@pytest.fixture
def mock_df_por_rango_fechas():
    return pd.DataFrame([{
        "total": 5,
        "total_valor": 1000
    }])