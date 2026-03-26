CREATE TABLE IF NOT EXISTS public.cuentas_cobro
(
    id_cuenta_cobro integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    periodo character varying(10) COLLATE pg_catalog."default",
    identificacion character varying(20) COLLATE pg_catalog."default",
    nombre character varying(200) COLLATE pg_catalog."default",
    fecha date,
    concepto character varying COLLATE pg_catalog."default",
    valor numeric(12,0),
    CONSTRAINT cuentas_cobro_pkey PRIMARY KEY (id_cuenta_cobro),
    CONSTRAINT "IX_unique_periodo_identificacion" UNIQUE (periodo, identificacion)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cuentas_cobro
    OWNER to postgres;