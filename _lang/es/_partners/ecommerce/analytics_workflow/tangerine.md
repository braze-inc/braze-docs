---
nav_title: Mandarina
article_title: Mandarina
description: "Este artículo describe la asociación entre Braze y Tangerine Store360, una plataforma omnicanal que conecta las tiendas físicas con las tiendas en línea para ofrecer experiencias superiores en tienda a los consumidores y a los empleados de las tiendas. A través de esta integración, los datos brutos de campaña e impresiones de Braze están disponibles en Store360 a través de Snowflake Secure Data Sharing, y las marcas pueden medir cómo sus campañas afectan a la participación en tienda y al tráfico en tienda."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine diseña, construye y opera una plataforma omnicanal llamada Store360. Store360 es una plataforma habilitadora omnicanal que conecta las tiendas físicas con las tiendas online para mejorar la experiencia del consumidor y del empleado en la tienda. Store360 rastrea y analiza el tráfico de visitas a las tiendas físicas, incluidos los usuarios de la aplicación móvil de los minoristas y su participación en la tienda.

La integración de Braze y Tangerine le permite integrar datos sin procesar de campañas e impresiones de Braze en Store360 a través de Snowflake Secure Data Sharing. Ahora las marcas pueden medir el impacto de estas campañas en las visitas a las tiendas físicas y en la participación en las mismas.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Store360 | Se necesita una cuenta Store360 para beneficiarse de esta asociación. |
| ID de cuenta Braze | Tu ID de grupo de la aplicación Braze. |
| Coincidencia de identificadores de usuario | Los datos de sus clientes en Store360 y Braze deben tener ID de usuario coincidentes en las dos plataformas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

### Analizar el impacto de la campaña en la visita a la tienda física

Las marcas utilizan Braze para enviar mensajes de campaña a los consumidores con el fin de aumentar las visitas a las tiendas. Durante la campaña, Store360 captura las visitas de usuarios de aplicaciones móviles identificados por ID de usuario.

Gracias a la capacidad analítica de Store360 Insight, las marcas pueden visualizar los detalles del impacto de la campaña, desde los mensajes enviados y leídos (datos de Braze) hasta quiénes y cuántos destinatarios visitaron las tiendas físicas (datos de Store360).

## Integración

### Paso 1: Habilitar el intercambio seguro de datos Snowflake

Trabaja con tu equipo Braze para habilitar y configurar Snowflake Secure Data Share.

### Paso 2: Configurar Store360 para obtener Datos Braze

Configure el ID de grupo de su aplicación Braze con su cuenta de servicio Store360 mediante la consola web del administrador de Store360. Esto solicitará al equipo de administración de Tangerine que sincronice los datos de Braze con Store360 mediante el uso compartido de datos Snowflake.

### Paso 3: Integrar los SDK de Store360 en la aplicación móvil

Para realizar un seguimiento y analizar las visitas a la tienda de los usuarios de la aplicación móvil y las actividades en la tienda junto con los datos de campañas e impresiones de Braze, debe integrar el SDK Store360 en su aplicación móvil siguiendo los pasos que se indican en la documentación de instalación del SDK Store360. Esta documentación le será facilitada tras la firma de un contrato de cliente entre Tangerine Store 360.

## Analizar datos Braze en Store360

Benefíciese del intercambio seguro de datos Snowflake para compartir sus datos brutos de campaña e impresiones Braze con los análisis Store360 Insight, que proporcionan una imagen completa del ciclo de vida y las actividades de los usuarios, desde online a offline.

Como referencia, aquí están todos los [campos Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) disponibles para ser incorporados en los análisis de Store360. Los detalles de este paso son muy específicos del cliente y requieren configuraciones especiales. Hable con su gestor de cuenta Store360 o support@tangerine.io para obtener más información.

## Información importante y limitaciones

### Disponibilidad del servicio

Actualmente, el servicio Store360 está disponible comercialmente en Japón e Indonesia.

Tangerine tiene previsto lanzar el producto Store360 en los siguientes países en 2023.
- Estados Unidos de América
- Tailandia
- Singapur
- Vietnam
- Corea

### Retención de datos

Existe una política de retención de dos años de tus datos de Braze para compartirlos con Snowflake.

### Retraso al rellenar los datos de eventos Braze

Los eventos Braze se procesan con tecnología de streaming y están disponibles casi en tiempo real. Generalmente, los eventos están disponibles a los 30 minutos de producirse.
