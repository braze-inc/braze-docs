---
nav_title: Nube de ventas Salesforce
article_title: Gestión de clientes potenciales con Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Aprende a utilizar los webhooks Braze para crear y actualizar clientes potenciales en Salesforce Sales Cloud a través del punto final Salesforce sobjects/Lead."
---

# Gestión de clientes potenciales con Salesforce Sales Cloud

> [Salesforce](https://www.salesforce.com/) es una de las principales plataformas de gestión de relaciones con los clientes (CRM) en la nube del mundo, diseñada para ayudar a las empresas a gestionar todo su proceso de ventas, incluida la generación de prospectos, el seguimiento de oportunidades y la administración de cuentas.<br><br>Esta página muestra cómo utilizar webhooks Braze para crear y actualizar clientes potenciales en Salesforce Sales Cloud mediante una integración enviada por la comunidad.

{% alert important %}
Se trata de una integración enviada por la comunidad y no está soportada directamente por Braze. Sólo las plantillas oficiales de webhook proporcionadas por Braze son compatibles con Braze.
{% endalert %}

## Cómo funciona

La integración de Braze y Salesforce Sales Cloud utiliza webhooks Braze para crear y actualizar clientes potenciales en Salesforce Sales Cloud a través del punto final Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html).

Braze ofrece actualmente dos integraciones con Salesforce Sales Cloud para los siguientes casos de uso:
1. [Crear un cliente potencial en Salesforce Sales Cloud](#creating-lead)
2. [Actualizar un cliente potencial en Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Esta integración es puramente para actualizar Salesforce desde Braze como parte de tus esfuerzos de captación y nutrición de clientes potenciales. Para sincronizar datos de Salesforce con Braze, consulta el [modelo de datos B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) o ponte en contacto con uno de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home/).
{% endalert %}

## Requisitos previos

Esta integración requiere que crees una aplicación conectada en Salesforce Sales Cloud siguiendo los pasos de la documentación de Salesforce: [Configura una aplicación conectada para el flujo de credenciales de cliente OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

Cuando configures los ajustes OAuth necesarios para la aplicación conectada, mantén todos los ajustes OAuth con sus valores y selecciones predeterminados, excepto los siguientes:
1. Selecciona **Habilitar para** el flujo de **dispositivos**. Puedes dejar **la URL de devolución de llamada** en blanco, ya que estará predeterminada a un marcador de posición.
2. Para **los Ámbitos OAuth** seleccionados, añade **Administrar datos de usuario a través de API (api)**.
3. Selecciona **Habilitar flujo de credenciales de cliente**.

## Crear un cliente potencial en Salesforce Sales Cloud {#creating-lead}

Como plataforma de interacción con los clientes, Braze puede generar nuevos clientes potenciales basándose en los flujos de usuarios, como rellenar un formulario en una página de destino. Cuando eso ocurra, puedes utilizar un webhook Braze Salesforce Sales Cloud para crear un cliente potencial correspondiente en Salesforce.

### Paso 1: Recoge tu `client_id` y `client_secret`

1. En Salesforce, ve a **Herramientas de la plataforma** > **Aplicaciones** > Administrador de aplicaciones.
2. Busca tu aplicación Braze recién creada y selecciona **Ver**.
3. En **Clave y secreto del consumidor**, selecciona **Gestionar detalles del consumidor**.
4. En la página resultante, toma nota de tu **Clave de Consumidor** y de tu **Secreto de Consumidor**. La **Clave del Consumidor** es tu `client_id`, y el **Secreto del Consumidor** es tu `client_secret`.

### Paso 2: Configura tu plantilla webhook

Utiliza plantillas para reutilizar rápidamente este webhook en toda la plataforma Braze. 

1. En Braze, ve a **Plantillas**, selecciona **Plantillas de webhook** y, a continuación, **\+ Crear plantilla de webhook**.
2. Proporciona un nombre para la plantilla, como "Salesforce Sales Cloud > Crear cliente potencial".
3. En la pestaña **Redactar**, introduce los siguientes datos:

#### Componer webhook 

| Campo | Detalles |
| --- | --- |
| URL del webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| Método HTTP | `POST` |
| Cuerpo de la solicitud | Pares clave-valor JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valores clave de la propiedad del cuerpo

Selecciona **\+ Añadir nueva propiedad de cuerpo** para cada uno de los pares clave-valor que quieras mapear de Braze a Salesforce. Puedes mapear sobre cualquier campo que desees, por lo que la tabla siguiente es sólo un ejemplo.

| Clave | Valor |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| apellido | {% raw %}`{{${last_name}}}`{% endraw %} |
| correo electrónico | {% raw %}`{{${email_address}}}`{% endraw %} |
| empresa | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Encabezados de solicitud

Selecciona **\+ Añadir nuevo encabezado** para cada uno de los siguientes encabezados de solicitud.

| Clave | Valor |
| --- | --- |
| Autorización | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Tipo de contenido | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4\. Selecciona **Guardar plantilla**.

Una plantilla webhook rellenada para crear un cliente potencial.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Actualizar un cliente potencial en Salesforce Sales Cloud {#updating-lead}

Para configurar un webhook Braze Salesforce Sales Cloud que actualice los clientes potenciales en Salesforce, necesitas un identificador común entre Salesforce Sales Cloud y Braze. El ejemplo siguiente utiliza el `lead_id` de Salesforce como el `external_id` de Braze, pero también puedes conseguirlo utilizando un `user_alias`. Para más detalles, consulta [Datos B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models)

Este ejemplo muestra específicamente cómo actualizar la etapa de un cliente potencial a "MQL" (cliente potencial cualificado para marketing) después de que un cliente potencial supere un determinado umbral de clientes potenciales. Se trata de una parte esencial de nuestro caso de uso [de flujo de trabajo de puntuación de clientes potenciales B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/).

### Paso 1: Recoge tu `client_id` y `client_secret`

1. En Salesforce, ve a **Herramientas de la plataforma** > **Aplicaciones** > Administrador de aplicaciones.
2. Busca tu aplicación Braze recién creada y selecciona **Ver**.
3. En **Clave y secreto del consumidor**, selecciona **Gestionar detalles del consumidor**.
4. En la página resultante, toma nota de tu **Clave de Consumidor** y de tu **Secreto de Consumidor**.
    - La **Clave del Consumidor** es tu `client_id`, y el **Secreto del Consumidor** es tu `client_secret`.

### Paso 2: Configura tu plantilla webhook

1. En Braze, ve a **Plantillas**, selecciona **Plantillas de webhook** y, a continuación, **\+ Crear plantilla de webhook**.
2. Proporciona un nombre para la plantilla, como "Salesforce Sales Cloud > Actualizar cliente potencial a MQL".
3. En la pestaña **Redactar**, introduce los siguientes datos:

#### Componer webhook 

| Campo | Detalles |
| --- | --- |
|URL del webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| Método HTTP | `PATCH` |
| Cuerpo de la solicitud | Pares clave-valor JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valores clave de la propiedad del cuerpo

Selecciona **\+ Añadir nueva propiedad del cuerpo** para el siguiente par clave-valor. Nota que `Lead_Stage__c` es un nombre de ejemplo. El campo personalizado que utilizas para realizar el seguimiento de los MQL en Salesforce puede tener un nombre diferente, así que asegúrate de que coinciden.

| Clave | Valor |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Encabezados de solicitud

Selecciona **\+ Añadir nuevo encabezado** para cada uno de los siguientes encabezados de solicitud.

| Clave | Valor |
| --- | --- |
| Autorización | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Tipo de contenido | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4\. Selecciona **Guardar plantilla**.

Una plantilla webhook rellenada para actualizar un cliente potencial.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Utilizar estos webhooks en un flujo de trabajo operativo

Puedes añadir rápidamente tus plantillas a tus flujos de trabajo operativos en Braze, por ejemplo:

1. Parte de una [campaña de nuevo usuario](#new-lead) que crea un cliente potencial en Salesforce
2. Parte de un [Canvas de puntuación de clientes potenciales](#lead-scoring) que actualiza los usuarios que han superado tu umbral de MQL a "MQL", y que actualiza Salesforce Sales Cloud con la misma información

### Nueva campaña principal {#new-lead}

Para crear un cliente potencial en Salesforce cuando un usuario proporcione su dirección de correo electrónico, puedes crear una campaña que utilice la plantilla de webhook "Actualizar cliente potencial" y que se desencadene cuando un usuario añada su dirección de correo electrónico (por ejemplo, cuando rellene un formulario Web).

Paso 2 de la creación de una campaña basada en acciones y con la acción desencadenante "Añadir una dirección de correo electrónico".]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Lead scoring Canvas para superar el umbral de Lead Cualificado en Marketing (MQL) {#lead-scoring}

Este webhook se trata en el caso de uso de la puntuación de [clientes potenciales]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff), pero también puedes comprobar los MQL y actualizar directamente Salesforce dentro del Canvas de puntuación de clientes potenciales (en lugar de crear una campaña de webhook independiente): 

Añade un paso posterior a tu actualización de usuarios para comprobar si un usuario ha superado el umbral MQL que hayas definido. Si se han cruzado, actualiza el estado del usuario a "MQL", y luego actualiza Salesforce con el mismo estado "MQL" utilizando esta plantilla webhook. Salesforce se encarga del resto, enrutando este cliente potencial a los equipos de ventas adecuados mediante las reglas de enrutamiento de clientes potenciales que hayas definido.  

#### Añadir paso en Canvas para comprobar los usuarios que han superado el umbral MQL 

1. Añade un paso de **Ruta de audiencia** con dos grupos: "Umbral MQL" y "Todos los demás".
2. En el grupo "Umbral de MQL", busca a los usuarios que actualmente no tengan un estado de "MQL" (por ejemplo, `lead_stage` es igual a "Lead"), pero que tengan una puntuación de lead superior al umbral que hayas definido (por ejemplo, `lead_score` mayor de 50). Si es así, avanzan al siguiente paso, si no, salen.

\![El grupo de la ruta de audiencia "Umbral MQL" con filtros para un `lead_stage` igual a "Lead" y un `lead_score` superior a "50".]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3\. Añade un paso de **Actualización de Usuario** que actualice el valor del atributo `lead_stage` del usuario a "MQL".

\![El paso de actualización de usuario "Actualizar a MQL" que actualiza el atributo `lead_stage` para que tenga el valor "MQL".]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4\. Añade un paso webhook que actualice Salesforce con la nueva etapa MQL.

El paso webhook "Actualizar Salesforce" con los detalles completados.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

¡Ahora tu flujo Canvas actualizará a los usuarios que hayan cruzado tu umbral de MQL!

\![Un paso en Canvas de actualización de usuarios que comprueba si un usuario supera el umbral MQL y, si lo supera, actualiza Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Solución de problemas

Estos flujos de trabajo tienen una capacidad de depuración limitada dentro de Salesforce, por lo que recomendamos consultar el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log) Braze para averiguar por qué ha fallado un Webhook y si se ha producido algún error.

Por ejemplo, un error causado por una URL no válida utilizada para la recuperación del token oAuth se mostraría como `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

Un cuerpo de respuesta de error que indica que la URL no es válida.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})

