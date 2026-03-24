CREATE OR REPLACE FUNCTION public.total_por_periodo(
	)
    RETURNS TABLE(periodo character varying, total numeric) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN
    RETURN QUERY
    SELECT 
        t1.periodo,
        COALESCE(SUM(t1.valor), 0) AS total
    FROM cuentas_cobro t1
    GROUP BY t1.periodo
    ORDER BY t1.periodo;
END;
$BODY$;

ALTER FUNCTION public.total_por_periodo()
    OWNER TO postgres;