CREATE OR REPLACE FUNCTION cuentas_por_periodo()
RETURNS TABLE (
    periodo TEXT,
    cantidad BIGINT,
    total NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        periodo,
        COUNT(*) AS cantidad,
        COALESCE(SUM(valor), 0) AS total
    FROM cuentas_cobro
    GROUP BY periodo
    ORDER BY periodo;
END;
$$ LANGUAGE plpgsql;