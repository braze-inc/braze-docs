---
nav_title: Solución de problemas
article_title: Segmentos de solución de problemas
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Este artículo de referencia cubre los pasos para la solución de problemas y las consideraciones a tener en cuenta al utilizar segmentos."
---

# Segmentos de solución de problemas

## Errores

### La audiencia objetivo es demasiado compleja para lanzarla

Este raro error se produce si tu audiencia objetivo contiene demasiados valores regex, valores regex excesivamente largos, filtros excesivamente detallados (como "es cualquiera de los 30.000 códigos postales") o demasiados filtros. Esto incluye todos los filtros de audiencia de una campaña o de Canvas, tanto si los filtros se encuentran dentro de los segmentos referenciados como si se añaden como filtros en el paso en Canvas **Audiencia objetivo**.

Cuando añades filtros de segmento a una campaña o Canvas, esos filtros se traducen en consultas en Braze (el recuento de caracteres de estas consultas no es 1:1 respecto al número de caracteres que ve un usuario del panel). Cuando Braze envía una campaña o Canvas, ejecutamos una consulta que combina todos los filtros de la audiencia objetivo. Aplicamos un umbral que limita el número de caracteres de la consulta resultante para una audiencia objetivo. Para una determinada campaña o Canvas, sumamos el recuento de caracteres en todos los segmentos referenciados, incluyendo todos los filtros adicionales. Para un segmento determinado, sumamos el recuento de caracteres de todos los filtros y valores de filtrado.

Tu panel mostrará un error cuando una campaña, Canvas o segmento supere el umbral y no se pueda lanzar. Si recibes este error, simplifica tu audiencia objetivo antes de volver a lanzarlo, incluyendo:

- Si tu audiencia hace referencia a varios segmentos, asegúrate de que los segmentos no tengan redundancias, como que los mismos filtros aparezcan en varios segmentos.
- Asegúrate de que no estás haciendo referencia a datos obsoletos en los filtros de segmento. Por ejemplo, un filtro anticuado podría buscar usuarios que no hayan recibido un determinado paso en Canvas en la última semana, aunque el Canvas lleve meses parado.
- Los segmentos que son sólo listas de ID de usuario o correos electrónicos (que a menudo utilizan un filtro regex) pueden convertirse en una [importación CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) y simplificarse en un único filtro CSV.
- Si tienes CDI, puedes crear un segmento CDI que extraiga el grupo directamente de tu almacén de datos.

También puedes [ponerte en contacto con el servicio de asistencia]({{site.baseurl}}/braze_support/) para obtener más ayuda sobre la optimización de los filtros.

{% alert note %}
Empezamos a limitar el número de caracteres en abril de 2025. Las campañas y los lienzos lanzados antes de abril de 2025 están protegidos, lo que significa que pueden seguir superando el límite, mientras que las campañas y los lienzos de nueva creación no pueden superar el límite. Si editas o clonas una campaña o Canvas con derechos adquiridos, **no** podrás lanzarla hasta que se actualice la audiencia para que esté por debajo del límite.
{% endalert %}

### X campañas o Lienzos activos o parados superan el umbral de complejidad de la audiencia

Este banner se muestra en la parte superior de la lista de una campaña o Canvas siempre que las campañas o Canvas activos o parados tengan audiencias que superen el umbral de complejidad de audiencia. Selecciona el banner para filtrar la lista sólo a las campañas o Lienzos que superen el umbral, y luego sigue los pasos de solución de problemas en [La audiencia objetivo es demasiado compleja para lanzarla](#target-audience-is-too-complex-to-launch).

### El filtro supera los 10.000 caracteres o es demasiado largo para guardarlo

Braze limita los filtros de segmentos individuales a un máximo de 10.000 caracteres. Aparece una advertencia cada vez que un filtro individual supera los 10.000 caracteres, tanto si el filtro está dentro de un segmento como si se añade directamente a la campaña o al Canvas. 

Este error se produce muy raramente, pero cuando ocurre, suele ser con filtros regex que tienen como objetivo una lista de ID de usuario o direcciones de correo electrónico. En ese caso, puedes seguir estos pasos para convertir los filtros a un CSV:

1. Exporta los usuarios del segmento afectado o del filtro regex específico. 
2. Limpia el CSV según sea necesario. Necesitas el ID de Braze o el ID de Appboy, pero puedes eliminar todas las demás columnas si no son necesarias. También te recomendamos que revises tus datos para confirmar que son recientes (por ejemplo, elimina los usuarios a los que ya no intentas dirigirte).
3. Vuelve a [importar]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) el archivo CSV, que agrupa automáticamente a los usuarios en un único filtro basado en CSV muy eficaz.

## Comportamiento del usuario

### El usuario ya no está en un segmento

Si un usuario no está disponible al crear un segmento, sus datos de usuario que determinan su elegibilidad para el segmento podrían haber cambiado como resultado de su propia actividad o de otras campañas y Canvases con los que haya interactuado anteriormente. Si la reelegibilidad está activada, su perfil de usuario mostrará los últimos datos de la campaña recibida.

### Aparece información para usuarios de otras aplicaciones cuando filtro por una aplicación concreta

Los usuarios pueden tener varias aplicaciones, por lo que seleccionar una aplicación concreta en la sección **Aplicaciones utilizadas** de la página de segmentación arrojará resultados para los usuarios que al menos tengan esa aplicación. El filtro no da resultados para los usuarios que tienen exclusivamente esa aplicación.

## Filtrar

### Opciones de filtrado modificadas

Tus opciones de filtrado están relacionadas con el formato (tipo de datos) que pasas a Braze para tu atributo personalizado. Para revisar el tipo de datos que Braze reconoce para tus atributos personalizados, ve a **Configuración de datos** > **Atributos** personalizados **.**

Si tus opciones de filtrar han cambiado, es una indicación de que tus datos se están pasando a Braze en un formato (tipo de datos) diferente al anterior. Para obtener descripciones detalladas de los distintos tipos de datos y sus opciones de filtrado, consulta los [tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

Ten en cuenta que cambiar el tipo de datos de un atributo personalizado en el panel rechazará los datos que se envíen a Braze en un formato diferente.

## Análisis e informes

### El *mensaje enviado* o los *destinatarios únicos* en los análisis de campaña no coinciden con el recuento de segmentos 

Si el recuento del análisis de tu campaña para *Mensajes enviados* o *Destinatarios únicos* no coincide con el número de usuarios del filtro de segmentos `Has received message from campaign X`, puede deberse a dos motivos:

1. **Los usuarios pueden haber sido archivados, huérfanos o eliminados desde el lanzamiento de la campaña**<br><br>Por ejemplo, supongamos que 1.000 usuarios reciben una campaña y haces una exportación CSV el mismo día. Verás que se informa de 1.000 usuarios. Durante el mes siguiente, 50 de esos 1.000 usuarios son eliminados (por ejemplo, por el punto final `users/delete` ). Cuando realices otra exportación CSV, verás que se informa de 950 usuarios, mientras que el recuento de *destinatarios* únicos en **Análisis de campaña** sigue siendo de 1.000.<br><br>En otras palabras, la métrica *Destinatarios únicos* es un recuento incremental, mientras que el segmentador y la exportación CSV proporcionan un recuento de los usuarios existentes actualmente.<br><br>

2. **La campaña tiene configurada la reelegibilidad, por lo que los usuarios pueden volver a entrar en la campaña varias veces**<br><br>Por ejemplo, supongamos que una campaña de correo electrónico tiene la reelegibilidad establecida en cero minutos (los usuarios pueden volver a entrar en la campaña siempre que cumplan los requisitos del segmento de audiencia), y la campaña lleva en marcha más de un mes. El número de *mensajes enviados* en **Análisis de campaña** no coincidiría con el número del segmento porque este campo incluiría mensajes enviados a usuarios duplicados.<br><br>Esto se debe a que Braze cuenta a los usuarios únicos como *Destinatarios Únicos Diarios*, o el número de usuarios que recibieron un mensaje concreto en un día. Esto significa que los usuarios que vuelvan a ser elegibles se contarán más de una vez como destinatarios únicos, porque la ventana "única" sólo dura un día. Esto puede hacer que el número de *Destinatarios diarios únicos* sea superior al número de perfiles de usuario de la exportación CSV. Los perfiles de usuario del archivo CSV serán realmente únicos.

### Se asigna un usuario a dos aplicaciones a pesar de registrar una sesión en una sola aplicación

Al crear un segmento, puedes dirigirte a usuarios que hayan [utilizado aplicaciones específicas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform). Un usuario necesita haber tenido una sesión en una aplicación específica para ser asignado a esa aplicación; sin embargo, hay dos escenarios en los que un usuario puede ser asignado a una aplicación específica sin haber tenido sesiones en la aplicación. 

El primer escenario es si el campo `app_id` se rellena cuando se utiliza el punto final `/users/track`, concretamente cuando se utiliza un [objeto de]({{site.baseurl}}/api/objects_filters/purchase_object/) [evento]({{site.baseurl}}/api/objects_filters/event_object/) o de [compra]({{site.baseurl}}/api/objects_filters/purchase_object/), como en este ejemplo:

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

El segundo escenario es si el campo `app_id` se rellena al utilizar el endpoint `/users/track` para migrar tickets push, como en este ejemplo: 

```json
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
```
