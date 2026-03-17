## Migración de permisos granulares

{% alert important %}
Los permisos granulares se encuentran en fase de acceso anticipado. Cuando se planifique la migración para tu empresa, los administradores de Braze recibirán correos electrónicos y banners en el panel de control notificándoles la [migración]({{site.baseurl}}/granular_permissions_migration/) de [permisos granulares]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

Las integraciones SCIM existentes y [los objetos API SCIM heredados]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api) seguirán funcionando después de la migración de permisos granulares a finales de abril. 

No es necesario que tomes ninguna medida inmediata. Sin embargo, te recomendamos que revises tus integraciones para ver si hay permisos que vayan a ser granularizados. Por ejemplo, si actualmente estás enviando`basic_access`  en la API, te sugerimos que actualices tu integración después de la granularización para incluir los permisos específicos (por ejemplo, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze seguirá aceptando cadenas heredadas, como `basic_access`, después de la migración de permisos granulares, para que las integraciones existentes no se vean afectadas.

## Objeto permisos

El objeto permisos es un campo que se encuentra en algunas de las peticiones y respuestas cuando se interactúa con el recurso usuario a través de los permisos de ID SCIM.

{% alert note %}
Los grupos de aplicaciones han pasado a llamarse espacios de trabajo en Braze, pero las claves de esta página siguen haciendo referencia a la terminología antigua (por ejemplo, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Un objeto de permisos válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `companyPermissions` | Opcional | Matriz | Matriz de [cadenas de permisos a nivel de empresa]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente. |
| `roles` | Opcional | Matriz | Matriz de [objetos de rol]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Obligatoria | Matriz | Matriz de [objetos de permiso del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de permisos del espacio de trabajo

Un objeto de permiso de grupo de aplicaciones válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupName`| Opcional | Cadena | Nombre del espacio de trabajo. Sirve para especificar a qué espacio de trabajo corresponden los permisos contenidos en este objeto. | 
| `appGroupId` | Obligatorio si falta `appGroupName`  | Cadena | ID del espacio de trabajo, que sirve como método alternativo para especificar el espacio de trabajo. |
| `appGroupPermissionSets` | Opcional | Matriz | Matriz con un único [objeto del conjunto de permisos del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel del espacio de trabajo de la tabla de [cadenas de permisos del espacio]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings) de trabajo, en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el espacio de trabajo especificado. |
| `team` | Opcional | Matriz | Matriz de [objetos de permiso del equipo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de configuración de permisos del espacio de trabajo {#workspace-permissions-set-object}

Un objeto válido del conjunto de permisos del espacio de trabajo es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | Cadena | Nombre del conjunto de permisos del espacio de trabajo que se está asignando al usuario para este espacio de trabajo. |
| `appGroupPermissionSetID` | Obligatorio si falta `appGroupPermissionSetName`  | Cadena | ID del espacio de trabajo, que sirve como método alternativo para especificar el conjunto de permisos del espacio de trabajo asignado al usuario para este espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de permisos del equipo

Un objeto de permiso de equipo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `teamName` | Opcional | Cadena | Nombre del equipo, que puede utilizarse para especificar a qué equipo corresponden los permisos de este objeto. |
| `teamId` | Obligatorio si falta `teamName`  | Cadena | ID del equipo, que sirve como método alternativo para especificar el equipo. |
| `teamPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel de equipo de la tabla [de cadenas de permisos de equipos]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el equipo especificado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Objeto de rol

Un objeto de rol válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `roleName` | Opcional | Cadena | Nombre del rol que se está asignando al usuario. |
| `roleId` | Obligatorio si falta `roleName`  | Cadena | ID del rol, que sirve como método alternativo para especificar el rol. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anexo

### Cadenas de permisos de empresa {#company}

| Como se muestra en la IU | Cadena API SCIM |
| --- | --- |
| Administrador | `admin` |
| Administrar la configuración de la empresa | `manage_company_settings` |
| Crear y eliminar espacios de trabajo| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Cadenas de permisos del espacio de trabajo {#workspace-strings}

| Nombre del permiso | Cadena API SCIM |
| --- | --- |
| Ver campañas | `view_campaigns` |
| Editar campañas | `edit_campaigns` |
| Archivar campañas | `archive_campaigns` |
| Ver Canvas | `view_canvases` |
| Editar Canvas | `edit_canvases` |
| Archivar Canvas | `archive_canvases` |
| Ver las reglas de limitación de frecuencia | `view_frequency_caps` |
| Editar reglas de limitación de frecuencia | `edit_frequency_caps` |
| Ver priorización de mensajes | `view_message_prioritization` |
| Editar priorización de mensajes | `edit_message_prioritization` |
| Ver bloques de contenido | `view_content_blocks` |
| Editar bloque de contenido | `edit_content_blocks` |
| Archivar bloques de contenido | `archive_content_blocks` |
| Ver las feature flags | `view_feature_flags` |
| Editar conmutador de características | `edit_feature_flags` |
| Archiva feature flags | `archive_feature_flags` |
| Ver segmentos | `view_segments` |
| Editar segmentos | `edit_segments` |
| Archivar segmentos | `archive_segments` |
| Ver grupo de control global | `view_global_control_group` |
| Editar grupo de control global | `edit_global_control_group` |
| Ver plantillas IAM | `view_iam_templates` |
| Editar plantillas IAM | `edit_iam_templates` |
| Archivar plantillas IAM | `archive_iam_templates` |
| Ver plantillas de correo electrónico | `view_email_templates` |
| Editar plantilla de correo electrónico | `edit_email_templates` |
| Archivar plantillas de correo electrónico | `archive_email_templates` |
| Ver plantillas webhook | `view_webhook_templates` |
| Editar plantillas webhook | `edit_webhook_templates` |
| Archivar plantillas webhook | `archive_webhook_templates` |
| Ver plantillas de enlaces | `view_link_templates` |
| Editar plantillas de enlaces | `edit_link_templates` |
| Ver activos de la biblioteca de medios | `view_media_library_assets` |
| Ver ubicaciones | `view_locations` |
| Editar ubicaciones | `edit_locations` |
| Ubicación de los archivos | `archive_locations` |
| Ver códigos promocionales | `view_promotion_codes` |
| Editar códigos promocionales | `edit_promotion_codes` |
| Códigos promocionales de las exportaciones | `export_promotion_codes` |
| Ver centros de preferencia | `view_preference_centers` |
| Editar centros de preferencia | `edit_preference_centers` |
| Editar informes | `edit_reports` |
| Ver Colocaciones | `view_placements` |
| Editar ubicaciones | `edit_placements` |
| Archivar colocaciones | `archive_placements` |
| Ver plantillas de banners | `view_banner_templates` |
| Ver configuración multilingüe | `view_multi_language_settings` |
| Utilizar operador | `use_operator` |
| Ver agentes de Decisioning Studio | `view_decisioning_studio_agents` |
| Ver Audiencia de Decisioning Studio |`view_decisioning_studio_audience` |
| Ver evento de conversión de Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Ver protecciones de Decisioning Studio | `view_decisioning_studio_guardrails` |
| Lanzar campañas | `launch_campaigns` |
| Lanzar Canvas | `launch_canvases` |
| Editar usuarios del panel | `edit_dashboard_users` |
| Editar activos de la biblioteca de medios | `edit_media_library_assets` |
| Eliminar activos de la biblioteca de medios | `delete_media_library_assets` |
| Ver Importar usuarios | `view_import_users` |
| Importar usuarios	| `import_users` |
| Editar datos de usuario | `edit_user_data` |
| Ver registros de fusión de usuarios | `view_user_merge_records` |
| Fusionar usuarios duplicados | `merge_duplicate_users` |
| Ver las claves de API | `view_api_keys` |
| Editar claves de API | `edit_api_keys` |
| Ver grupos internos | `view_internal_user_groups` |
| Editar grupos internos | `edit_internal_user_groups` |
| Eliminar grupos internos | `delete_internal_user_groups` |
| Ver registro de actividad de mensajes | `view_message_activity_log` |
| Ver registro de usuarios del evento | `view_event_user_log` |
| Ver identificadores de la API | `view_api_identifiers` |
| Ver panel de uso de la API | `view_api_usage_dashboard` |
| Ver límites de la API | `view_api_limits` |
| Ver alertas de uso de la API | `view_api_usage_alerts` |
| Editar alertas de uso de la API | `edit_api_usage_alerts` |
| Ver depurador de SDK | `view_sdk_debugger` |
| Editar depurador de SDK | `edit_sdk_debugger` |
| Lanzar bloques de contenido | `launch_content_blocks` |
| Editar la ingesta de datos en la nube | `edit_cloud_data_ingestion` |
| Ver configuración de la aplicación | `view_app_settings` |
| Editar configuración de la aplicación | `edit_app_settings` |
| Ver configuración push | `view_push_settings` |
| Editar configuración push | `edit_push_settings` |
| Ver equipos | `view_teams` |
| Modificar equipos | `edit_teams` |
| Archivar equipos | `archive_teams` |
| Ver atributos personalizados | `view_custom_attributes` |
| Editar atributos personalizados | `edit_custom_attributes` |
| Atributos personalizados de la lista de bloqueo | `blocklist_custom_attributes` |
| Eliminar atributos personalizados | `delete_custom_attributes` |
| Exportar atributos personalizados | `export_custom_attributes` |
| Ver eventos personalizados	 | `view_custom_events` |
| Editar eventos personalizados | `edit_custom_events` |
| Eventos personalizados de la lista de bloqueo | `blocklist_custom_events` |
| Eliminar eventos personalizados | `delete_custom_events` |
| Exportar eventos personalizados | `export_custom_events` |
| Editar segmentación de propiedades de eventos personalizados | `edit_custom_event_property_segmentation` |
| Ver productos | `view_products` |
| Editar productos	 | `edit_products` |
| Productos de la lista de bloqueo | `blocklist_products` |
| Editar segmentación de propiedades de compra | `edit_purchase_property_segmentation` |
| Ver etiquetas | `view_tags` |
| Editar etiquetas | `edit_tags` |
| Borrar etiquetas | `delete_tags` |
| Ver configuración del correo electrónico	| `view_email_settings` |
| Editar configuración de correo electrónico | `edit_email_settings` |
| Ver catálogos | `view_catalogs` |
| Editar catálogos	 | `edit_catalogs` |
| Exportar catálogos | `export_catalogs` |
| Eliminar catálogos | `delete_catalogs` |
| Ver configuración de Whatsapp | `view_whatsapp_settings` |
| Editar socios tecnológicos | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Cadenas de permiso del equipo {#team}

| Nombre del permiso | Cadena API SCIM |
| --- | --- |
| Ver campañas | `view_campaigns` |
| Editar campañas | `edit_campaigns` |
| Archivar campañas | `archive_campaigns` |
| Ver Canvas | `view_canvases` |
| Editar Canvas | `edit_canvases` |
| Archivar Canvas | `archive_canvases` |
| Ver las reglas de limitación de frecuencia | `view_frequency_caps` |
| Editar reglas de limitación de frecuencia | `edit_frequency_caps` |
| Ver priorización de mensajes | `view_message_prioritization` |
| Editar priorización de mensajes | `edit_message_prioritization` |
| Ver bloques de contenido | `view_content_blocks` |
| Ver las feature flags | `view_feature_flags` |
| Editar conmutador de características | `edit_feature_flags` |
| Archiva feature flags | `archive_feature_flags` |
| Ver segmentos | `view_segments` |
| Editar segmentos | `edit_segments` |
| Editar grupo de control global | `edit_global_control_group` |
| Ver plantillas IAM | `view_iam_templates` |
| Editar plantillas IAM | `edit_iam_templates` |
| Archivar plantillas IAM | `archive_iam_templates` |
| Ver plantillas de correo electrónico | `view_email_templates` |
| Editar plantilla de correo electrónico | `edit_email_templates` |
| Archivar plantillas de correo electrónico | `archive_email_templates` |
| Ver plantillas webhook | `view_webhook_templates` |
| Editar plantillas webhook | `edit_webhook_templates` |
| Archivar plantillas webhook | `archive_webhook_templates` |
| Ver plantillas de enlaces | `view_link_templates` |
| Editar plantillas de enlaces | `edit_link_templates` |
| Ver activos de la biblioteca de medios | `view_media_library_assets` |
| Ver ubicaciones | `view_locations` |
| Editar ubicaciones | `edit_locations` |
| Ubicación de los archivos | `archive_locations` |
| Ver códigos promocionales | `view_promotion_codes` |
| Editar códigos promocionales | `edit_promotion_codes` |
| Códigos promocionales de las exportaciones | `export_promotion_codes` |
| Ver centros de preferencia | `view_preference_centers` |
| Editar centros de preferencia | `edit_preference_centers` |
| Ver informes | `view_reports` |
| Crear informes | `create_reports` |
| Editar informes | `edit_reports` |
| Ver plantillas de banners | `view_banner_templates` |
| Ver configuración multilingüe | `view_multi_language_settings` |
| Utilizar operador | `use_operator` |
| Ver agentes de Decisioning Studio | `view_decisioning_studio_agents` |
| Ver evento de conversión de Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Lanzar campañas | `launch_campaigns` |
| Lanzar Canvas | `launch_canvases` |
| Editar usuarios del panel | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Cadenas del departamento

| Como se muestra en la IU | Cadena API SCIM |
| --- | --- |
| Agencia / Proveedor externo | `agency` |
| BI / Análisis | `bi` |
| Alta dirección | `c_suite` |
| Ingeniería | `engineering` |
| Finanzas | `finance` |
| Marketing / Editorial | `marketing` |
| Administración de producto | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }