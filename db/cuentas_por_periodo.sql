CREATE OR REPLACE FUNCTION public.cuentas_por_periodo(
	)
    RETURNS TABLE(periodo character varying, cantidad bigint, total numeric) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN
    RETURN QUERY
    SELECT 
        t1.periodo,
        COUNT(*) AS cantidad,
        COALESCE(SUM(t1.valor), 0) AS total
    FROM cuentas_cobro t1
    GROUP BY t1.periodo
    ORDER BY t1.periodo;
END;
$BODY$;

ALTER FUNCTION public.cuentas_por_periodo()
    OWNER TO postgres;