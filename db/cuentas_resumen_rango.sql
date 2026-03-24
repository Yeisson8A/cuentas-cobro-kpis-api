CREATE OR REPLACE FUNCTION public.cuentas_resumen_rango(
	fecha_inicio date,
	fecha_fin date)
    RETURNS TABLE(total bigint, total_valor numeric) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(*) AS total,
        COALESCE(SUM(valor), 0) AS total_valor
    FROM cuentas_cobro
    WHERE fecha BETWEEN fecha_inicio AND fecha_fin;
END;
$BODY$;

ALTER FUNCTION public.cuentas_resumen_rango(date, date)
    OWNER TO postgres;