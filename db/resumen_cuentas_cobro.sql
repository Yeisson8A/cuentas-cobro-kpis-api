CREATE OR REPLACE FUNCTION resumen_cuentas_cobro()
RETURNS TABLE (
    total_cuentas BIGINT,
    total_facturado NUMERIC,
    promedio NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(*) AS total_cuentas,
        COALESCE(SUM(valor), 0) AS total_facturado,
        COALESCE(AVG(valor), 0) AS promedio
    FROM cuentas_cobro;
END;
$$ LANGUAGE plpgsql;