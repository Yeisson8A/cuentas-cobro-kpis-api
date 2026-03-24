CREATE OR REPLACE FUNCTION public.cuentas_por_persona(
	)
    RETURNS TABLE(nombre character varying, identificacion character varying, cantidad bigint, total numeric) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN
    RETURN QUERY
    SELECT 
        t1.nombre,
        t1.identificacion,
        COUNT(*) AS cantidad,
        COALESCE(SUM(t1.valor), 0) AS total
    FROM cuentas_cobro t1
    GROUP BY t1.nombre, t1.identificacion
    ORDER BY total DESC;
END;
$BODY$;

ALTER FUNCTION public.cuentas_por_persona()
    OWNER TO postgres;