---
nav_title: "Objetos de la API SCIM y Apéndice"
article_title: Objetos de la API SCIM y Apéndice
page_order: 8
page_type: reference
description: "En este artículo se explican los diferentes objetos de la API SCIM y el apéndice."
hidden: true
permalink: "/scim_api_appendix/"
---

# Objetos y apéndice de la API SCIM

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
| `companyPermissions` | Opcional | Matriz | Matriz de cadenas de permisos a nivel de empresa de la tabla [Cadenas de permisos de empresa](#company), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente. |
| `roles` | Opcional | Matriz | Matriz de [objetos de rol](#role-object). |
| `appGroup` | Obligatoria | Matriz | Matriz de [objetos de permiso del espacio de trabajo](#workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de permisos del espacio de trabajo {#workspace-permission-object}

Un objeto de permiso de grupo de aplicaciones válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupName`| Opcional | Cadena | Nombre del espacio de trabajo. Sirve para especificar a qué espacio de trabajo corresponden los permisos contenidos en este objeto. | 
| `appGroupId` | Obligatorio si falta `appGroupName`  | Cadena | ID del espacio de trabajo, que sirve como método alternativo para especificar el espacio de trabajo. |
| `appGroupPermissionSets` | Opcional | Matriz | Matriz con un único [objeto del conjunto de permisos del espacio de trabajo](#workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel del espacio de trabajo de la tabla de [cadenas de permisos del espacio](#workspace-strings) de trabajo, en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el espacio de trabajo especificado. |
| `team` | Opcional | Matriz | Matriz de [objetos de permiso del equipo](#team-permissions-object). |
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
| `teamPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel de equipo de la tabla [de cadenas de permisos de equipos](#team), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el equipo especificado. |
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
| Puede administrar la configuración de empresa | `manage_company_settings` |
| Puede añadir/eliminar espacios de trabajo| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Cadenas de permisos del espacio de trabajo {#workspace-strings}

| Nombre del permiso | Cadena API SCIM |
| --- | --- |
| Administrador | `admin` |
| Campañas de Acceso, Lonas, Tarjetas, Segmentos, Mediateca | `basic_access` |
| Aprobar y denegar Canvas | `approve_deny_campaigns` |
| Enviar campañas, Canvas | `send_campaigns_canvases` |
| Publicar tarjetas | `publish_cards` |
| Editar segmentos | `edit_segments` |
| Exportar datos de usuario | `export_user_data` |
| Ver PII | `view_pii` |
| Ver perfiles de usuarios que cumplen las reglas de PII | `view_user_profile` |
| Administrar usuarios del dashboard | `manage_dashboard_users` |
| Administrar activos de biblioteca de medios | `manage_media_library` |
| Ver datos de consumo | `view_usage_data` |
| Importar y actualizar datos de usuario | `import_update_user_data` |
| Ver datos de facturación | `view_billing_details` |
| Acceso a la consola para desarrolladores | `dev_console` |
| Lanzar bloques de contenido | `launch_content_blocks` |
| Administrar integraciones externas | `manage_external_integrations` |
| Administrar aplicaciones | `manage_apps` |
| Gestionar equipos | `manage_teams` |
| Administrar eventos, atributos, compras | `manage_events_attributes_purchases` |
| Gestionar etiquetas | `manage_tags` |
| Administrar configuración del correo electrónico | `manage_email_settings` |
| Administrar grupos de suscripción | `manage_subscription_groups` |
| Administrar configuración de aprobación | `manage_approval_settings` |
| Administrar permisos para el dashboard de catálogos | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Cadenas de permiso del equipo {#team}

| Nombre del permiso | Cadena API SCIM |
| --- | --- |
| Administrador | `admin` |
| Campañas de Acceso, Lonas, Tarjetas, Segmentos, Mediateca | `basic_access` |
| Aprobar y denegar Canvas | `approve_deny_campaigns` |
| Enviar campañas, Canvas | `send_campaigns_canvases` |
| Publicar tarjetas | `publish_cards` |
| Editar segmentos | `edit_segments` |
| Exportar datos de usuario | `export_user_data` |
| Visualizar perfil de usuario | `view_user_profile` |
| Administrar usuarios del dashboard | `manage_dashboard_users` |
| Administrar activos de biblioteca de medios | `manage_media_library` |
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
