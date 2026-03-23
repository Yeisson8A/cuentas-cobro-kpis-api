CREATE OR REPLACE FUNCTION cuentas_por_persona()
RETURNS TABLE (
    nombre TEXT,
    identificacion TEXT,
    cantidad BIGINT,
    total NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        nombre,
        identificacion,
        COUNT(*) AS cantidad,
        COALESCE(SUM(valor), 0) AS total
    FROM cuentas_cobro
    GROUP BY nombre, identificacion
    ORDER BY total DESC;
END;
$$ LANGUAGE plpgsql;