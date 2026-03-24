CREATE OR REPLACE FUNCTION public.top_periodos(
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
    ORDER BY total DESC
    LIMIT 5;
END;
$BODY$;

ALTER FUNCTION public.top_periodos()
    OWNER TO postgres;