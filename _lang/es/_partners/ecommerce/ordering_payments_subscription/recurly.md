---
nav_title: Recurly
article_title: Recurly
description: "Recurly es la plataforma líder de gestión de suscripciones y facturación para marcas de venta directa al consumidor que buscan aumentar sus suscripciones e ingresos recurrentes."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) es una plataforma de gestión de suscripciones y facturación. La plataforma integrada Recurly simplifica la automatización del ciclo de vida de la suscripción a escala, habilitando a los equipos para que gestionen y optimicen la experiencia del suscriptor, desde la prueba de nuevos planes, ofertas y promociones hasta la gestión de métodos de pago, integraciones e información.

_Esta integración está mantenida por Recurly._

## Sobre la integración

La integración entre Recurly y Braze simplifica el proceso de compartir datos de suscripción con Braze, habilitando la comunicación personalizada con los clientes.

- Aprovecha los eventos del ciclo de vida de la suscripción de Recurly (por ejemplo, renovaciones, pausas o cancelaciones de la suscripción) en Braze para desencadenar campañas y comunicaciones personalizadas.
- Aprovecha los datos de suscripción de Recurly (por ejemplo, planes de suscripción, complementos o estado) para crear y gestionar usuarios, segmentos y Canvas de Braze para ejecutar campañas y comunicaciones específicas de cohorte.
- Envía los datos de Recurly directamente a Braze, habilitando casos de uso adicionales de mensajería y reduciendo los costes generales de desarrollo.

Puedes encontrar más información sobre el uso de Recurly con Braze en [los documentos de Recurly](https://docs.recurly.com/docs/braze-integration).

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Recurly | Se requiere un plan de suscripción Elite [Recurly](https://recurly.com/) con el Conmutador de características de Braze habilitado para aprovechar esta asociación. También es necesaria la activación de las facturas de crédito en tu plataforma Recurly.|
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. Dado que Recurly sólo utiliza el punto final `users.track`, recomendamos aprovisionar una clave específica de Recurly sólo con este permiso. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |

## Integración

Antes de empezar, asegúrate de que tienes cuentas activas tanto en Braze como en Recurly.

### Conecta Recurly a Braze

1. En Recurly, ve a **Integraciones** > **Braze**. Cuando navegues por primera vez a la página de configuración de la integración Braze en Recurly, la interfaz te pedirá que conectes los dos sistemas.

2. Proporciona las siguientes credenciales:

- **URL de la instancia:** El punto final REST de Braze de la instancia a la que estás aprovisionado.
- **Clave de API (identificador):** La clave de API REST de Braze que Recurly debe utilizar al enviar solicitudes a Braze.

Recuerda copiar la URL de tu instancia de Braze. Por ejemplo, tu URL podría ser así 

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3\. Después de introducir tus credenciales, haz clic en **Conectar**.

## Uso de esta integración

### Identificadores admitidos

Recurly utiliza la dirección `account_code` de una cuenta como `external_id` en Braze. Por ello, la dirección `account_code` de tus cuentas de Recurly debe coincidir con la de tu usuario de Braze `external_id`.

### Eventos personalizados

Para una interacción eficaz con los clientes, debes [configurar eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) en Braze para recibir eventos desencadenados por Recurly. Asegúrate de incluir cada evento de Recurly para una integración de datos completa. Estos eventos también pueden ser objeto de seguimiento en [los análisis Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics). Una vez configurados, estos eventos personalizados pueden utilizarse para segmentar a los usuarios o personalizar la mensajería. 

| Evento personalizado Braze| Evento recurrente |
| ----------- | ----------- |
| Nueva suscripción a Recurly              | Se desencadena cuando se crea una suscripción                            |
| Suscripción renovada a Recurly          | Se desencadena cuando se renueva una suscripción                                |
| Suscripción actualizada a Recurly          | Se desencadena cuando cambian los atributos de una suscripción (cambio de plan, cambio de precio o cambio de cantidad) |
| Suscripción cancelada de Recurly         | Se desencadena cuando se cancela una suscripción                           |
| Suscripción reactivada a Recurly      | Se desencadena cuando se reactiva una suscripción cancelada               |
| Suscripción a Recurly pausada           | Se desencadena cuando una suscripción se pone en pausa                   |
| Reanudación de la suscripción a Recurly          | Se desencadena cuando se reanuda una suscripción                              |
| Suscripción a Recurly caducada          | Se desencadena cuando caduca una suscripción                               |
| Factura Recurly creada               | Se desencadena cuando se crea una factura                                |
| Pago Recurrente Exitoso            | Se desencadena cuando se cobra correctamente una factura                 |
| Reembolso Recurrido Emitido                 | Se desencadena cuando se emite un reembolso                                   |
| Pago periódico fallido      | Se desencadena cuando falla una factura de renovación de una suscripción          |

### Dosificación y límite de velocidad

Dado que Recurly utiliza el punto final Braze `/users/track`, la integración está sujeta a los límites de velocidad estándar de Braze de 50.000 solicitudes por minuto.

Recurly agrupa determinados eventos del ciclo de vida de la suscripción como llamadas únicas a la API de Braze para reducir el número de llamadas realizadas.

- La creación de varias suscripciones al mismo tiempo se agrupa por lotes y se envía a Braze como una única solicitud.
- Cuando se renuevan varias suscripciones al mismo tiempo para una cuenta, cada una de esas renovaciones se agrupa en una única solicitud.
- Los eventos del ciclo de vida de la suscripción al mismo modelo se envían como una única solicitud. Por ejemplo, una factura recién creada con un pago enviaría una única solicitud API con los eventos personalizados `Recurly Invoice Created` y `Recurly Successful Payment`.

Los lotes se envían a Braze en grupos de hasta 75 eventos a la vez. Por ejemplo, si se crearan 100 suscripciones a la vez, Recurly haría dos peticiones API a Braze. Para más detalles, consulta la opción [de agrupar solicitudes de seguimiento de usuarios]({{site.baseurl}}/api/api_limits/#batch-user-track).


