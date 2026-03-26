---
nav_title: Solución de problemas
article_title: Solución de problemas en segmentos
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Este artículo de referencia cubre los pasos para solucionar problemas y las consideraciones a tener en cuenta al utilizar segmentos."
---

# Solución de problemas en segmentos

## Errores

### La audiencia objetivo es demasiado compleja para lanzarla

Este error poco frecuente se produce si tu audiencia objetivo contiene demasiados valores de regex, valores de regex excesivamente largos, filtros excesivamente detallados (como «es cualquiera de los 30 000 códigos postales») o demasiados filtros. Esto incluye todos los filtros de una campaña o audiencia de Canvas, tanto si los filtros se encuentran dentro de los segmentos referenciados como si se añaden como filtros en el paso **Audiencia objetivo**.

![Error para una audiencia objetivo que alcanza el umbral de complejidad.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Cuando añades filtros de segmento a una campaña o Canvas, esos filtros se traducen en consultas en Braze (el recuento de caracteres de estas consultas no es 1:1 con respecto al número de caracteres que ve un usuario del panel de control). Cuando Braze envía una campaña o Canvas, ejecutamos una consulta que combina todos los filtros de la audiencia objetivo. Aplicamos un límite al número de caracteres en la consulta resultante para una audiencia objetivo. Para una campaña o Canvas determinados, sumamos el recuento de caracteres de todos los segmentos a los que se hace referencia, incluidos todos los filtros adicionales. Para un segmento determinado, sumamos el recuento de caracteres de todos los filtros y valores de filtro.

Tu panel mostrará un error cuando una campaña, Canvas o segmento supere el límite y no se pueda lanzar. Si recibes este error, simplifica tu audiencia objetivo antes de volver a lanzar, incluyendo:

- Si tu audiencia hace referencia a varios segmentos, asegúrate de que los segmentos no tengan redundancias, como los mismos filtros que aparecen en varios segmentos.
- Asegúrate de no hacer referencia a datos obsoletos en los filtros de segmentos. Por ejemplo, un filtro obsoleto podría buscar usuarios que no hayan recibido un determinado paso en Canvas en la última semana, aunque Canvas lleve meses sin funcionar.
- Los segmentos que son solo listas de ID de usuario o correos electrónicos (que a menudo utilizan un filtro regex) se pueden convertir a una [importación CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) y simplificarse en un único filtro CSV.
- Si tienes CDI, es posible que puedas crear un segmento CDI que extraiga el grupo directamente de tu almacén de datos.

También puedes [ponerte en contacto con el servicio de asistencia]({{site.baseurl}}/braze_support/) para obtener más ayuda con la optimización de los filtros.

{% alert note %}
Comenzamos a limitar el número de caracteres en abril de 2025. Las campañas y los lienzos que se lanzaron antes de abril de 2025 quedaron exentos, lo que significa que pueden seguir superando el límite, mientras que las campañas y los lienzos recién creados no pueden superarlo. Si editas o clonas una campaña o Canvas con derechos adquiridos, **no** **podrás** lanzarla hasta que la audiencia se actualice por debajo del límite.
{% endalert %}

### Las campañas activas o detenidas o los lienzos superan el umbral de complejidad de la audiencia.

Este banner aparece en la parte superior de una campaña o lista de Canvas siempre que las campañas o Canvas activos o detenidos tengan audiencias que superen el umbral de complejidad de la audiencia. Selecciona el banner para filtrar la lista y mostrar solo las campañas o lienzos que superan el umbral y, a continuación, sigue los pasos de solución de problemas que se indican en [El audiencia objetivo es demasiado compleja para lanzarla](#target-audience-is-too-complex-to-launch).

![Banner de error que indica que 4 lienzos activos o detenidos superan el umbral de complejidad de la audiencia.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### El filtro supera los 10 000 bytes o es demasiado largo para guardarlo.

Braze limita los filtros de segmentos individuales a un máximo de 10 000 bytes, lo que equivale a 10 000 caracteres en inglés o 3333 caracteres en japonés. Aparece una advertencia cada vez que un filtro individual supera los 10 000 bytes, tanto si el filtro se encuentra dentro de un segmento como si se ha añadido directamente a la campaña o a Canvas. 

![Banner de error para un filtro cuyo valor supera los 10 000 caracteres.]({% image_buster /assets/img/segment/filter_error.png %})

![Error en un filtro de atributos personalizados,`menu_item`,cuyo valor de atributo supera los 10 000 caracteres.]({% image_buster /assets/img/segment/segment_filter_error.png %})


Este error ocurre muy raramente, pero cuando ocurre, suele ser con filtros regex que apuntan a una lista de ID de usuario o direcciones de correo electrónico. En ese caso, puedes seguir estos pasos para convertir los filtros a un archivo CSV:

1. Exporta los usuarios del segmento afectado o del filtro regex específico. 
2. Limpia el CSV según sea necesario. Necesitas el ID de Braze o el ID de Appboy, pero puedes eliminar todas las demás columnas si no son necesarias. También recomendamos revisar tus datos para confirmar que sean recientes (por ejemplo, eliminar usuarios a los que ya no deseas dirigirte).
3. [Importa]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) de nuevo el archivo CSV, que agrupa automáticamente a los usuarios en un único filtro basado en CSV altamente eficiente.

## Comportamiento de los usuarios

### El usuario ya no está en un segmento

Si un usuario no está disponible mientras se crea un segmento, sus datos de usuario que determinan su elegibilidad para el segmento podrían haber cambiado como resultado de su propia actividad o de otras campañas y Canvases con los que haya interactuado anteriormente. Si la reelección está activada, su perfil de usuario mostrará los últimos datos de la campaña recibida.

### Aparece información de los usuarios de otras aplicaciones cuando filtro una aplicación específica.

Los usuarios pueden tener varias aplicaciones, por lo que la selección de una aplicación específica en la sección **Aplicaciones utilizadas** de la página de segmentación arrojará resultados para los usuarios que al menos tengan esa aplicación. El filtro no arroja resultados para los usuarios que tienen exclusivamente esa app.

## Filtrado

### Opciones de filtrado modificadas

Tus opciones de filtrado están relacionadas con el formato (tipo de datos) que pasas a Braze para tu atributo personalizado. Para revisar el tipo de datos que Braze reconoce para tus atributos personalizados, ve a **Configuración de datos** > **Atributos personalizados**.

Si tus opciones de filtrar han cambiado, es una indicación de que tus datos se están pasando a Braze en un formato (tipo de datos) diferente al anterior. Para obtener descripciones detalladas de los distintos tipos de datos y sus opciones de filtrado, consulta los [tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

Ten en cuenta que cambiar el tipo de datos de un atributo personalizado en el panel rechazará los datos que se envíen a Braze en un formato diferente.

## Análisis e informes

### El *mensaje enviado* o los *destinatarios únicos* en Campaign Analytics no coinciden con el recuento de segmentos 

Si el recuento de su análisis de campaña para *Mensajes enviados* o *Destinatarios únicos* no coincide con el número de usuarios del filtro de segmento `Has received message from campaign X`, puede deberse a dos motivos:

1. **Los usuarios pueden haber sido archivados, huérfanos o eliminados desde el lanzamiento de la campaña.**<br><br>Por ejemplo, supongamos que 1000 usuarios reciben una campaña y haces una exportación CSV el mismo día. Verás 1.000 usuarios reportados. Durante el mes siguiente, 50 de esos 1.000 usuarios son eliminados (por ejemplo, por el endpoint `users/delete` ). Cuando realice otra exportación CSV, verá 950 usuarios registrados, mientras que el recuento de *destinatarios únicos* en **Campaign Analytics** sigue siendo de 1.000.<br><br>En otras palabras, la métrica de *destinatarios únicos* es un recuento incremental, mientras que el segmentador y la exportación CSV proporcionan un recuento de los usuarios existentes actualmente.<br><br>

2. **La campaña tiene configurada la reelegibilidad, por lo que los usuarios pueden volver a entrar en la campaña varias veces**<br><br>Por ejemplo, supongamos que una campaña de correo electrónico tiene la reelegibilidad establecida en cero minutos (los usuarios pueden volver a entrar en la campaña siempre que cumplan los requisitos del segmento de audiencia), y la campaña lleva en marcha más de un mes. El número de *mensajes enviados* en **Campaign Analytics** no coincidiría con el número del segmento porque este campo incluiría mensajes enviados a usuarios duplicados.<br><br>Esto se debe a que Braze cuenta los usuarios únicos como *Destinatarios Únicos Diarios*, o el número de usuarios que recibieron un mensaje concreto en un día. Esto significa que los usuarios que vuelvan a cumplir los requisitos serán contabilizados más de una vez como destinatarios únicos, ya que la ventana "única" sólo dura un día. Esto puede dar lugar a que el número de *Destinatarios Únicos Diarios* sea superior al número de perfiles de usuario en la exportación CSV. Los perfiles de usuario del archivo CSV serán realmente únicos.

### Se asigna al usuario a dos aplicaciones a pesar de haber iniciado sesión en una sola aplicación.

Al crear un segmento, puedes dirigirte a usuarios que hayan [utilizado aplicaciones específicas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform). Un usuario debe haber iniciado sesión en una aplicación específica para que se le asigne a esa aplicación; sin embargo, hay dos casos en los que un usuario puede ser asignado a una aplicación específica sin haber iniciado sesión en ella. 

El primer escenario es si el`app_id`campo se rellena al utilizar el`/users/track`punto final, concretamente al utilizar un [objeto]({{site.baseurl}}/api/objects_filters/purchase_object/) [de evento]({{site.baseurl}}/api/objects_filters/event_object/) o [compra]({{site.baseurl}}/api/objects_filters/purchase_object/), como en este ejemplo:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

El segundo escenario se da si el`app_id`campo se rellena al utilizar el`/users/track`punto final para la migración de tickets push, como en este ejemplo: 

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
