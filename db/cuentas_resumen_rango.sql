CREATE OR REPLACE FUNCTION cuentas_resumen_rango(
    fecha_inicio DATE,
    fecha_fin DATE
)
RETURNS TABLE (
    total BIGINT,
    total_valor NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(*) AS total,
        COALESCE(SUM(valor), 0) AS total_valor
    FROM cuentas_cobro
    WHERE fecha BETWEEN fecha_inicio AND fecha_fin;
END;
$$ LANGUAGE plpgsql;