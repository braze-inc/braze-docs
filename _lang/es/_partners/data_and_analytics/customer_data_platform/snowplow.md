---
nav_title: Snowplow
article_title: Snowplow
description: "Este artículo de referencia describe la asociación entre Braze y Snowplow, una plataforma de recopilación de datos de código abierto, que permite reenviar eventos de Snowplow a Braze a través del etiquetado del lado del servidor de Google Tag Manager."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplowanalytics.com) es una plataforma escalable de código abierto para la recopilación de datos ricos, de alta calidad y baja latencia. Está diseñado para recopilar datos de comportamiento completos y de alta calidad para las empresas.

_Esta integración está mantenida por Snowplow._

## Sobre la integración

La integración de Braze y Snowplow permite a los usuarios reenviar eventos de Snowplow a Braze a través del etiquetado del lado del servidor de Google Tag Manager. La etiqueta Braze del Quitanieves te permite enviar eventos a Braze y te ofrece flexibilidad y control adicionales:
- Visibilidad total de todas las transformaciones de los datos
- Capacidad para evolucionar en sofisticación con el tiempo
- Todos los datos permanecen en tu nube privada hasta que decidas reenviarlos
- Facilidad de configuración gracias a las numerosas bibliotecas de etiquetas y a la conocida interfaz de usuario de Google Tag Manager.

Aproveche los ricos datos de comportamiento de Snowplow para impulsar potentes interacciones centradas en el cliente en Braze y enviar mensajes personalizados en tiempo real.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Tubería quitanieves | Hay que poner en marcha una tubería quitanieves. |
| Google Tag Manager en el servidor | Es necesario desplegar GTM-SS y configurar el [cliente Snowplow para GTM-SS](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/). |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

### Entrega personalizada y basada en la acción
Utilice cualquiera de los numerosos eventos enriquecidos que Snowplow recopila por defecto o defina sus propios eventos personalizados para dar forma a recorridos del cliente aún más granulares que tengan sentido para su negocio. Aproveche los ricos datos de comportamiento de Snowplow para diseñar embudos de clientes y desbloquear valor para sus equipos de marketing y producto, ayudándoles a maximizar la conversión y el uso del producto a través de Braze.

### Segmentación dinámica
Cree audiencias dinámicas en Braze basadas en los datos de comportamiento de alta calidad de Snowplow: A medida que los usuarios realizan acciones en su producto, aplicación o sitio web, puede aprovechar los datos de comportamiento en tiempo real que Snowplow recopila para añadir o eliminar automáticamente usuarios de los segmentos relevantes en Braze.

## Integración

### Paso 1: Instalación de plantillas

#### Instalación manual

1. Descarga el [`template.tpl`](https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl) archivo de plantilla.
2. Cree una nueva etiqueta en la sección **Plantillas** de un contenedor de servidor de Google Tag Manager.
3. Haga clic en el menú **Más acciones** de la esquina superior derecha y seleccione **Importar**.
4. Importe el archivo de plantilla descargado y guárdelo.

#### Galería del administrador de etiquetas

Próximamente. Esta etiqueta está pendiente de aprobación para ser incluida en la galería GTM.

### Paso 2: Configuración de la etiqueta Braze

Con la plantilla instalada, añada la etiqueta Braze a su contenedor GTM-SS.

1. En la pestaña **Etiqueta**, seleccione **Nueva** y, a continuación, seleccione la **etiqueta Braze** como configuración de etiqueta.
2. Seleccione el desencadenante deseado para los eventos que desea reenviar a Braze.
3. Introduzca los parámetros necesarios y configure su etiqueta (encontrará más detalles en la siguiente sección Personalización).
4. Haga clic en **Guardar**.

## Personalización

### Parámetros obligatorios de la etiqueta

La siguiente tabla enumera los parámetros de etiqueta necesarios que debe incluir en la configuración de su etiqueta Braze.

| Parámetro | Descripción |
| --------- | ----------- |
| Punto final de la API REST Braze | Establece la URL de tu [punto final]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) REST Braze. |
| Clave API Braze | Establece tu [clave de API]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) Braze que se incluirá en cada solicitud. |
| Braze `external_id` | Establezca esta clave en la propiedad de evento de cliente que corresponda a la dirección `external_id` de sus usuarios y que se utilizará como [identificador de usuario Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Asignación de eventos

La siguiente tabla enumera las opciones de mapeo de eventos relativas al evento Quitanieves según lo reclamado por el [cliente Quitanieves](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/).

| Opción de asignación | Descripción |
| --------- | ----------- |
| Incluir autodescripción del evento | Activado por defecto. Indica si los datos del evento autodescriptivo Snowplow se incluirán en los objetos de propiedades del evento enviados a Braze. |
| Reglas de contexto del evento quitanieves | Describe cómo la etiqueta Braze utilizará las entidades de contexto adjuntas a un evento Quitanieves. |
| Extraer la entidad de la matriz si se trata de un solo elemento | Las entidades quitanieves siempre están en matrices, ya que se pueden adjuntar varias de la misma entidad a un evento. Esta opción seleccionará el único elemento de la matriz si ésta sólo contiene un único elemento. |
| Incluir todas las entidades en el objeto de evento | Activado por defecto. Incluye todas las entidades de un evento dentro del objeto de propiedades del evento Braze. Desactive esta opción para seleccionar entidades individuales para su inclusión. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mapeado avanzado de eventos

#### Reglas de propiedad de los eventos

Si desea incluir otras propiedades del evento cliente y asignarlas al evento Braze, haga referencia a las reglas de la tabla siguiente: 

| Reglas de propiedad de los eventos | Descripción |
| --------- | ----------- |
| Incluir propiedades de eventos comunes | Activada por defecto, esta opción establece si se incluyen automáticamente las propiedades de evento de la [definición de evento común](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data) en las propiedades del evento Braze. |
| Reglas adicionales de asignación de propiedades de usuario y propiedades de evento | Especifique la clave de propiedad del evento cliente y la clave de objeto de las propiedades a las que desea asignarla (o deje la clave asignada en blanco para mantener el mismo nombre). Aquí puede utilizar la notación de ruta clave (por ejemplo, `x-sp-tp2.p` para una plataforma de eventos Snowplow o `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` para un id de vista de página de eventos Snowplow (en el índice 0 de la matriz) o elegir propiedades que no sean Snowplow si utiliza un cliente alternativo.<br><br>Las reglas de asignación de propiedades de eventos rellenan el objeto de propiedades de eventos Braze.|
| Incluir propiedades comunes de los usuarios| Activada por defecto, esta opción establece si se incluyen las propiedades `user_data` de la definición de evento común en el objeto de atributos de usuario Braze.|
| Propiedad de la hora del evento | Esta opción le permite especificar la propiedad del evento cliente para rellenar la hora del evento (en formato ISO-8601) o dejarla vacía para utilizar la hora actual (comportamiento por defecto). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Asignación de entidades

Usando la tabla de mapeo de entidades de Snowplow, las entidades pueden ser remapeadas para tener diferentes nombres en Braze e incluidas en propiedades de eventos, u objetos de atributos de usuario. 

La entidad puede especificarse en dos formatos diferentes:
- Coincidencia de versión principal: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1` donde `com_snowplowanalytics_snowplow` es el proveedor del evento, `web_page` es el nombre del esquema y `1` es el número de versión principal. `x-sp-` también puede omitirse si se desea.
- Coincidencia de esquema completa: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| Opción de asignación de entidades | Descripción |
| --------- | ----------- |
| Incluir entidades no mapeadas en el evento | Al remapear o mover algunas entidades a atributos de usuario con la personalización anterior, esta opción permite garantizar que todas las entidades no mapeadas (como cualquier entidad que no se encuentre en las [reglas de propiedades del evento](#event-property-rules)) se incluirán en el objeto de propiedades del evento Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


