---
nav_title: ActionIQ
article_title: ActionIQ
description: "Este artículo de referencia cubre la integración de Braze y ActionIQ. ActionIQ es una plataforma empresarial de datos de clientes para profesionales del marketing, analistas y tecnólogos. Esta integración permite a las marcas sincronizar y asignar sus datos de ActionIQ directamente a Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ][2] pone orden en el caos de la experiencia del cliente. El centro de experiencia del cliente (CX) de ActionIQ ofrece a todos los equipos un acceso de autoservicio directo pero controlado a los datos de los clientes para descubrir audiencias y orquestar experiencias a escala.

La integración de Braze y ActionIQ permite a las marcas sincronizar y asignar sus datos de ActionIQ directamente a Braze, potenciando la entrega de experiencias de cliente extraordinarias basadas en toda la amplitud de sus datos de cliente. La integración permite a los usuarios:
- Asigne segmentos de audiencia o atributos personalizados a Braze directamente desde ActionIQ
- Reenvíe los eventos rastreados por ActionIQ a Braze en tiempo real para activar campañas personalizadas y específicas.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta ActionIQ | Se requiere una cuenta ActionIQ para aprovechar esta integración. |
| Clave REST API de Braze | Una clave de API REST Braze con permisos `users.track` y `user.export.ids`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST][1]. Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Membresía de la audiencia

Esta integración se utiliza para sincronizar la pertenencia a la audiencia de ActionIQ con Braze mediante la creación de atributos personalizados que indican si un perfil de Braze forma parte de un segmento. Cada público de ActionIQ corresponde a un único atributo booleano personalizado.

La convención de nomenclatura estándar para el atributo personalizado creado es: `AIQ_<Audience ID>_<Split ID>`.

Para crear un segmento de estos usuarios, en Braze, vaya a **Segmentos**, cree un nuevo segmento y seleccione **Atributos personalizados** como filtro. Desde aquí, puede elegir el atributo personalizado ActionIQ. Una vez creado el segmento, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

#### Requisitos

En ActionIQ, configura una conexión Braze proporcionando tu clave de API REST y el punto final REST Braze. 

Para que coincida con los consumidores en la plataforma Braze, se deben incluir los siguientes identificadores en su configuración de activación:
- `braze_id`
- `external_id`

Una vez conectada tu integración, la información empezará a enviarse a Braze.

### Eventos

La plataforma ActionIQ puede configurarse para recibir información de eventos a través de su servicio de ingesta de streaming. Esta otra opción de integración reenvía estos Eventos a Braze, para que los profesionales del marketing los utilicen para la orquestación o la activación de campañas de marketing.

La integración de eventos puede enviar atributos ActionIQ adicionales como parte de las propiedades dentro de la carga útil del evento.

#### Requisitos

La integración de eventos envía la siguiente información a Braze:
- Nombre de evento
- Identificador del consumidor ( `braze_id` o `external_id`)
- Marca de tiempo
- Propiedades de evento, que se rellenan con cualquier atributo adicional en la configuración de exportación


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/