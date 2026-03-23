CREATE OR REPLACE FUNCTION total_por_periodo()
RETURNS TABLE (
    periodo TEXT,
    total NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        periodo,
        COALESCE(SUM(valor), 0) AS total
    FROM cuentas_cobro
    GROUP BY periodo
    ORDER BY periodo;
END;
$$ LANGUAGE plpgsql;