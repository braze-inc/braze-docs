---
nav_title: ActionIQ
article_title: ActionIQ
description: "Este artículo de referencia cubre la integración de Braze y ActionIQ. ActionIQ es una plataforma de datos de los clientes empresariales para especialistas en marketing, analistas y tecnólogos. Esta integración permite a las marcas sincronizar y asignar sus datos de ActionIQ directamente a Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ](https://www.actioniq.com/) es una plataforma de datos de los clientes para marcas empresariales que ofrece a los especialistas en marketing formas fáciles y seguras de activar los datos en cualquier punto de la experiencia del cliente. La arquitectura componible única de ActionIQ significa que los datos pueden permanecer seguros donde viven, y los equipos de marketing sólo utilizan las herramientas que necesitan.

_Esta integración está mantenida por ActionIQ._

## Sobre la integración

La integración de Braze y ActionIQ permite a las marcas sincronizar y mapear sus datos de ActionIQ directamente con Braze, potenciando la entrega de experiencias del cliente extraordinarias basadas en toda la amplitud de sus datos de clientes. Las integraciones disponibles permiten a los usuarios:

- Actualiza los perfiles de usuario en Braze con la información de pertenencia a la audiencia y cualquier atributo directamente desde ActionIQ.
- Reenvíe los eventos rastreados por ActionIQ a Braze en tiempo real para activar campañas personalizadas y específicas.
- Entrega campañas desencadenadas por API en Braze directamente desde puntos de intervención en un trayecto de ActionIQ.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta ActionIQ | Se requiere una cuenta ActionIQ para aprovechar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con los permisos necesarios para la integración correspondiente. Para más detalles, consulta la sección de Requisitos correspondientes. <br><br>Esta clave puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integraciones

### Membresía de la audiencia

Esta integración se utiliza para sincronizar la pertenencia a la audiencia de ActionIQ con Braze mediante la creación de atributos personalizados que indican si un perfil de Braze forma parte de un segmento. Cada público de ActionIQ corresponde a un único atributo booleano personalizado.

La convención de nomenclatura estándar para el atributo personalizado creado es: `AIQ_<Audience ID>_<Split ID>`.

Para crear un segmento de estos usuarios, haz lo siguiente:
1. En Braze, navega hasta **Segmentos**.
2. Crea un nuevo segmento.
3. Selecciona **Atributos personalizados** como filtro.
4. Desde aquí, elige el atributo personalizado de ActionIQ. 
5. Una vez creado el segmento, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

Además, esta integración actualizará cualquier atributo personalizado o estándar de un perfil de usuario de Braze con sus valores de atributo de ActionIQ.

#### Requisitos

Se necesita una clave de API REST de Braze con permisos para `users.track` y `user.export.ids`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**. 

En ActionIQ, configura una conexión Braze proporcionando tu clave de API REST y el punto final REST Braze. 

Para que coincida con los consumidores en la plataforma Braze, se deben incluir los siguientes identificadores en su configuración de activación:
- `braze_id`
- `external_id`

### Eventos

Puedes configurar la plataforma ActionIQ para recibir información de eventos a través de su servicio de ingesta de streaming. Esta opción de integración reenvía estos eventos a Braze para que los especialistas en marketing los utilicen para la orquestación o para desencadenar campañas de marketing. La integración del evento puede enviar atributos ActionIQ adicionales como parte de las propiedades de la carga útil del evento.

#### Requisitos

Se necesita una clave de API REST de Braze con permisos para `users.track` y `user.export.ids`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**. 

La integración de eventos envía la siguiente información a Braze:
- Nombre de evento
- Identificador del consumidor ( `braze_id` o `external_id`)
- Marca de tiempo
- Propiedades de evento, que se rellenan con cualquier atributo adicional en la configuración de exportación

### Campañas activadas

Esta integración desencadenará una campaña en Braze para todos los usuarios de un segmento de ActionIQ. Después de haber configurado la copia de tu campaña, las pruebas multivariantes y las reglas de reelegibilidad, puedes desencadenarla desde cualquier punto de intervención del viaje de ActionIQ añadiendo el ID de campaña de Braze a tu configuración de exportación.

Opcionalmente, puedes incluir cualquier otro atributo de ActionIQ en tu exportación para rellenar la copia de tu campaña. Se envían con el objeto `trigger_properties`.

#### Requisitos

Se necesita una clave de API REST de Braze con permisos para `campaigns.trigger.send` y `campaigns.list`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**.

Los siguientes valores deben enviarse en tu exportación de ActionIQ a Braze:
- Identificador del consumidor ( `braze_id` o `external_id`)
- ID de campaña


