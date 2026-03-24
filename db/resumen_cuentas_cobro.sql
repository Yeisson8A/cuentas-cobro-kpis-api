CREATE OR REPLACE FUNCTION public.resumen_cuentas_cobro(
	)
    RETURNS TABLE(total_cuentas bigint, total_facturado numeric, promedio numeric) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(*) AS total_cuentas,
        COALESCE(SUM(valor), 0) AS total_facturado,
        COALESCE(AVG(valor), 0) AS promedio
    FROM cuentas_cobro;
END;
$BODY$;

ALTER FUNCTION public.resumen_cuentas_cobro()
    OWNER TO postgres;