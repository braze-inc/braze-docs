---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Este artículo de referencia describe la asociación entre Braze y Looker, una plataforma de análisis de inteligencia empresarial y big data."
page_type: partner
search_tag: Partner

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> [Looker](https://looker.com/), una plataforma de análisis de inteligencia empresarial y big data, te permite explorar, analizar y compartir análisis empresariales en tiempo real fácilmente.

La integración de Braze y Looker permite a los usuarios de Braze aprovechar [los bloques de Looker](#looker-blocks) y las [acciones de Looker](#looker-actions) de los usuarios a través de la API REST. Estos usuarios marcados pueden añadirse a segmentos para [orientar](#segment-users) futuras campañas Braze o Lienzos. Para utilizar Looker con Braze, te recomendamos que envíes tus datos Braze a un [almacén de datos utilizando Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/), y que después utilices Braze Looker Blocks para modelar y visualizar rápidamente tus datos Braze en Looker.

## Requisitos previos

| Requisito | Descripción |
|---|---|
|Cuenta Looker | Se necesita una [cuenta Looker](https://looker.com/) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Limitaciones

- Este proceso sólo funciona con datos que no hayan sido pivotados.
- La API procesa un máximo de 100.000 filas a la vez.
- El recuento final de la bandera de un usuario puede ser inferior debido a duplicados o a no usuarios.

## Integración

### Bloques de Looker

Nuestros bloques de Looker ayudan a los clientes de Braze a acceder rápidamente a una vista de los datos granulares que ofrecemos a través de [Currents]({{site.baseurl}}/partners/braze_currents/about/). Nuestros bloques proporcionan visualizaciones y modelos prediseñados para los datos de Currents, de modo que los clientes de Braze puedan implementar fácilmente patrones analíticos como la retención, evaluar la capacidad de entrega de mensajes, echar un vistazo más detallado al comportamiento del usuario y mucho más.

Para implementar los bloques de Looker, sigue las instrucciones de los archivos README del código de GitHub.
- [Bloque de análisis de interacción de mensajes README](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [Bloque de análisis del comportamiento del usuario README](https://github.com/llooker/braze_retention_block/blob/master/README.md)

Ambas integraciones suponen que tu [integración inicial de Braze]({{site.baseurl}}/user_guide/onboarding_with_braze/integration/), así como tu integración de Braze con un [almacén de datos](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) compatible con Looker, está configurada adecuadamente para capturar y enviar los datos necesarios.


{% alert important %}
Braze ha construido nuestros bloques de Looker utilizando [Snowflake](https://www.snowflake.com/) como almacén de datos. Aunque nuestro objetivo es que nuestros Bloques funcionen con el mayor número posible de almacenes de datos, algunas funciones SQL pueden diferir en disponibilidad, sintaxis o comportamiento entre dialectos.
{% endalert %}

{% alert warning %}
¡Ten en cuenta las diferentes convenciones de nomenclatura! Los nombres personalizados pueden causar incongruencias en los datos, a menos que cambies todos los nombres correspondientes. Si has personalizado algún nombre de Vista/tabla o modelo, renombra cada uno de ellos en el LookML con el nombre que hayas seleccionado.
{% endalert %}

#### Bloques disponibles

| Bloquear | Descripción |
|---|---|
| Bloque de análisis de interacción de mensajes | Este bloque incluye datos sobre push, correo electrónico, mensajes dentro de la aplicación, webhook, conversión, entrada en Canvas y eventos de inscripción en el grupo de control de la campaña. <br><br>Obtén más información sobre este [bloque de Looker](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) o consulta el [código de GitHub](https://github.com/llooker/braze_message_engagement_block). |
| Bloque de análisis del comportamiento del usuario | Este bloque incluye datos sobre eventos personalizados, compras, sesiones, eventos de ubicación y desinstalaciones.<br><br>Obtén más información sobre este [bloque de Looker](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) o consulta el [código de GitHub](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Acciones de Looker

Las acciones de Looker te permiten marcar usuarios dentro de Braze a través del punto final de la API REST desde un Look de Looker. Las acciones requieren que una dimensión esté etiquetada con `braze_id`. La Acción añadirá el valor marcado al atributo personalizado `looker_export` del usuario.

{% alert important %}
Solo se marcarán los usuarios existentes. No puedes utilizar Looks pivotados al marcar datos en Braze.
{% endalert %}

#### Paso 1: Configurar una acción Braze Looker

Configura una acción de Looker de Braze con tu clave de API REST de Braze y tu punto final REST.

![La página de configuración de Looker Braze. Aquí puedes encontrar campos para la clave de API de Braze y el punto final de API REST de Braze.]({% image_buster /assets/img/braze-looker-action.png %})

#### Paso 2: Configurar Looker Develop

Dentro de Looker Develop, selecciona las vistas adecuadas. Añade `braze_id` a la etiqueta de dimensiones y confirma los cambios.
Esta etiqueta `braze_id` se utiliza para determinar qué campo es la clave única.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Asegúrate de confirmar los cambios. Las acciones de Looker sólo funcionarán con la configuración de producción.**

#### Paso 3: Establecer atributos de usuario en etiquetas

Opcionalmente, se puede establecer cualquier atributo utilizando una etiqueta `braze[]` con el nombre del atributo entre paréntesis. Por ejemplo, si quisieras que se enviara un atributo personalizado `user_segment`, la etiqueta sería `braze[user_segment]`.

Ten en cuenta las siguientes limitaciones:
- Los atributos sólo se enviarán si se **incluyen como campo dentro de la apariencia**.
- Los tipos admitidos son `Strings`, `Boolean`, `Numbers` y `Dates`.
- Los nombres de los atributos distinguen entre mayúsculas y minúsculas.
- También se pueden establecer atributos estándar, siempre que coincidan exactamente con los nombres de [perfil de usuario estándar]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields).
- La etiqueta completa debe ir entre comillas. Por ejemplo, `tags: ["braze[first_name]"]`. También se pueden asignar otras etiquetas, pero se ignorarán.
- Puedes encontrar información adicional en [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Paso 4: Enviar la acción Looker

1. Dentro de un Look con una dimensión `braze_id` seleccionada, haz clic en el engranaje de configuración ( <i class="fas fa-cog"></i> ) de la parte superior derecha, y selecciona **Enviar....**
2. Selecciona la Acción Braze personalizada.
3. En **Clave única**, proporciona la clave de mapeado de usuario principal para la cuenta Braze (`external_id` o `braze_id`).
4. Dale un nombre a la exportación. Si no se indica ninguno, se utilizará `LOOKER_EXPORT`.
5. En **Opciones avanzadas**, selecciona **Resultados en tabla** o **Todos los resultados** y, a continuación, **Enviar**.<br><br>![]({% image_buster /assets/img/send-looker-action.png %})<br><br>Si la exportación se envió correctamente, entonces `LOOKER_EXPORT` debería aparecer en el perfil de usuario como un atributo personalizado con el valor que introdujiste en la acción.<br><br>![]({% image_buster /assets/img/custom-attributes-looker.png %})

##### Ejemplo de API saliente

A continuación se muestra un ejemplo de llamada saliente a la API, que se enviará al [punto final`/users/track/` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

###### Encabezado
```
Authorization: Bearer [API_KEY]
```

###### Cuerpo
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Segmentar usuarios en Braze {#segment-users}

En Braze, para crear un segmento de estos usuarios marcados, navega a **Segmentos** en **Interacción**, asigna un nombre a tu segmento y selecciona **Looker_Export** como filtro. A continuación, utiliza la opción "incluye valor" y proporciona la bandera del atributo personalizado que asignaste en Looker.

![En el constructor de segmentos Braze, el filtro "looker_export" se establece en "includes_value" y "Looker".]({% image_buster /assets/img/braze_segments.png %})

Una vez guardado, puede hacer referencia a este segmento durante la creación de Canvas o campañas en el paso de segmentación de usuarios.

## Solución de problemas
Si tienes problemas con la acción Looker, añade un usuario de prueba a [los grupos internos]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/) y comprueba lo siguiente:

* La clave de API tiene los permisos `users.track`.
* Se introduce el punto final REST correcto, como `https://rest.iad-01.braze.com`.
* Se establece una etiqueta `braze_id` en la vista de dimensión.
* Tu consulta incluye la dimensión o atributo ID como columna.
* Los resultados de Looker no están pivotados.
* La clave única está correctamente seleccionada. Por lo general, la `external_id`.
* `braze_id` en la dimensión es diferente de `braze_id` en la API. `braze_id` en la dimensión se utiliza para indicar que es el campo `id` para la API de Braze. Para la mayoría de los propósitos, al enviar `external_id` es la clave primaria.
* El usuario `external_id` existe en la plataforma Braze.
* El campo `looker_export` está configurado como `Automatically Detect` en `Braze Platform > Settings > Manage Settings > Custom Attributes`.
* Los cambios se comprometen con la producción. Las acciones de Looker funcionan en la configuración de producción.

