CREATE SEQUENCE IF NOT EXISTS public.cuentas_cobro_id_cuenta_cobro_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.cuentas_cobro_id_cuenta_cobro_seq
    OWNER TO postgres;