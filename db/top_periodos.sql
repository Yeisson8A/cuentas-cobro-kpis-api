CREATE OR REPLACE FUNCTION top_periodos()
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
    ORDER BY total DESC
    LIMIT 5;
END;
$$ LANGUAGE plpgsql;