---
nav_title: Treasure Data
article_title: Treasure Data
description: "Este artículo de referencia describe la asociación entre Braze y Treasure Data, una plataforma de datos de clientes empresariales que permite escribir resultados de trabajos directamente en Braze."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> [Treasure Data](https://www.treasuredata.com/) es una plataforma de datos de clientes (CDP) que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en su pila de marketing.

La integración de Braze y Treasure Data te permite escribir los resultados de los trabajos de Treasure Data directamente en Braze, permitiéndote:
* **Asignar identificadores externos**: Asigne ID a la cuenta de usuario Braze desde su sistema CRM. 
* **Gestionar la exclusión voluntaria**: Cuando un usuario final actualiza su consentimiento eligiendo no participar.
* **Cargue su seguimiento de eventos, compras o atributos de perfil personalizados**. Esta información puede ayudarle a crear segmentos de clientes precisos que mejoren la experiencia del usuario en sus campañas.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta de Treasure Data | Se necesita una [cuenta de Treasure Data](https://www.treasuredata.com/custom-demo/) para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST Braze con permisos `users.track`, `users.delete`, `users.alias.new`, `users.identify`.<br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Casos prácticos

Puede sincronizar sus perfiles de cliente consolidados de Treasure Data en Braze para crear segmentos objetivo. Treasure Data admite datos de cookies propios, ID de móviles, sistemas de terceros como tu CRM, y muchos más.

## Integración

### Paso 1: Crear una nueva conexión

En Treasure Data, ve al **Catálogo** en el **Hub de Integraciones** y busca y selecciona **Braze**. 

En el mensaje **Nueva autenticación** que aparece, asigne un nombre a la conexión e indique la clave de la API REST Braze y el punto final REST. Seleccione **Hecho** cuando haya terminado.

![]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### Paso 2: Definir tu consulta

En Treasure Data, ve a **Consultas** en tu **Banco de Trabajo de Datos** y selecciona una consulta cuyos datos quieras exportar. Ejecute esta consulta para validar el conjunto de resultados.

{% alert note %}
Para los usuarios que utilicen HIVE para crear consultas, HIVE requiere que cualquier columna o tabla que comience con un guión bajo vaya entre comillas. Por ejemplo, `_merge_objects`.
{% endalert %}

A continuación, seleccione **Exportar resultados** y seleccione una autenticación de integración existente.

![]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

Defina parámetros adicionales de exportación de resultados como se indica en la siguiente [sección de personalización](#customization). En el contenido de su integración de exportación, revise los parámetros de integración.

![La página "Exportar resultados". En esta página hay campos para "modo", "tipo de seguimiento" y "campos preformateados". Para este ejemplo, "Usuario-Seguimiento" y "Eventos personalizados" se establecen en estos campos, respectivamente.]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

Por último, seleccione **Hecho**, ejecute la consulta y compruebe que los datos se han transferido a Braze.

### Personalización

Los parámetros de los resultados de exportación se incluyen en la siguiente tabla:

| Parámetro                 | Valores | Descripción |
|---------------------------|---|---|
| `mode`                    | Usuario - Nuevo Alias<br>Usuario - Identificación<br>Usuario - Seguimiento<br>Usuario - Borrar | Modo conector |
| `pre_formatted_fields`    | Cadena | Usar para columnas array o JSON para mantener el formato. |
| `track_record_type`       | Eventos personalizados<br>Compras<br>Atributos del perfil de usuario| Tipo de registro para el **usuario - Modo de seguimiento**  |
| `skip_on_invalid_records` | Booleano | Si está activada, continúa e ignora cualquier registro no válido para la columna JSON. <br> De lo contrario, el trabajo se detiene. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Visite [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) para obtener más información sobre campos preformateados, consultas de ejemplo, detalles de parámetros y programación de trabajos de exportación de consultas.
{% endalert %}

## Webhooks

Los usuarios de Treasure Data pueden ingerir datos a través de la API REST pública. Puedes utilizar Treasure Data para crear webhooks personalizados en tus datos. Para más información, visita [Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API)

