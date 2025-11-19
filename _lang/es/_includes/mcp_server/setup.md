# Configuración del servidor Braze MCP

> Aprende a configurar el servidor Braze MCP, para que puedas interactuar con tus datos Braze mediante lenguaje natural utilizando herramientas como Claude y Cursor. Para más información general, consulta [Servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "desarrollador" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo | Descripción |
|--------------|-------------|
| Clave de API Braze | Una clave de API Braze con los permisos necesarios. Crearás una nueva clave cuando [configures tu servidor Braze MCP](#create-api-key). |
| Cliente MCP | Actualmente, sólo [Claude](https://claude.ai/) y [Cursor](https://cursor.com/) son compatibles oficialmente. Necesitarás una cuenta de uno de estos clientes para utilizar el servidor Braze MCP. |
| Terminal | Una aplicación de terminal para que puedas ejecutar comandos e instalar herramientas. Utiliza la aplicación de terminal que prefieras o la que esté preinstalada en tu computadora. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuración del servidor Braze MCP

### Paso 1: Instala `uv`

En primer lugar, instala `uv`-una [herramienta de línea de comandos de Astral](https://docs.astral.sh/uv/getting-started/installation/) para la administración de dependencias y la gestión de paquetes de Python.

{% tabs local %}
{% tab MacOS y Linux %}
Abre tu aplicación de terminal, pega el siguiente comando y pulsa <kbd>Intro</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

El resultado será similar al siguiente

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Windows %}
 Abre Windows PowerShell, pega el siguiente comando y pulsa <kbd>Intro</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

El resultado será similar al siguiente

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### Paso 2: Crear una clave de API {#create-api-key}

El servidor Braze MCP admite 38 puntos finales de sólo lectura que no devuelven datos de los perfiles de usuario Braze. Ve a **Configuración** > **API e identificadores** > **Claves de API** y crea una nueva clave con algunos o todos los permisos siguientes.

{% details Lista de permisos de sólo lectura, no PII %}
#### Campañas

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canvas

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Catálogos

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Ingesta de datos de Cloud

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Bloques de contenido

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Atributos personalizados

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Eventos

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPI

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Mensajes

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Centro de preferencias

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Compras

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Segmentos

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Envíos

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### Sesiones

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Claves de autenticación SDK

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Suscripción

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Plantillas

| Punto de conexión | Permiso necesario |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
No reutilices una clave de API existente: crea una específica para tu cliente MCP. Además, asigna sólo permisos de sólo lectura, no PII, ya que los agentes pueden intentar escribir o borrar datos en Braze.
{% endalert %}

### Paso 3: Obtén tu identificador y punto final

Cuando configures tu cliente MCP, necesitarás el identificador de tu clave de API y el punto final REST de tu espacio de trabajo. Para obtener estos detalles, vuelve a la página **Claves de API** del panel; mantén esta página abierta para poder consultarla en [el siguiente paso](#configure-client).

![Las "Claves de API" en Braze muestran una clave de API recién creada y el punto final REST del usuario.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Paso 4: Configura tu cliente MCP {#configure-client}

Configura tu cliente MCP utilizando nuestro archivo de configuración preproporcionado.

{% tabs %}
{% tab Claude %}
En [Claude Desktop](https://claude.ai/download), ve a **Configuración** > **Desarrollador** > **Editar configuración**, y añade el siguiente fragmento de código:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "key-identifier",
        "BRAZE_BASE_URL": "rest-endpoint"
      }
    }
  }
}
```

Sustituye `key-identifier` y `rest-endpoint` por los valores correspondientes de la página **Claves de API** en Braze. Tu configuración debe ser similar a la siguiente

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Cuando hayas terminado, guarda la configuración y reinicia Claude Desktop.
{% endtab %}

{% tab Cursor %}
En [Cursor](https://cursor.com/), ve a **Configuración** > **Herramientas e integraciones** > **Herramientas MCP** > **Añadir MCP personalizado**, y añade el siguiente fragmento de código:

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

Sustituye `key-identifier` y `rest-endpoint` por los valores correspondientes de la página **Claves de API** en Braze. Tu configuración debe ser similar a la siguiente

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Cuando hayas terminado, guarda la configuración y reinicia Cursor.
{% endtab %}
{% endtabs %}

### Paso 5: Enviar un aviso de prueba

Ahora que ya has configurado el servidor MCP Braze, intenta enviar un aviso de prueba a tu cliente MCP. Para otros ejemplos y buenas prácticas, consulta [Uso del servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "desarrollador" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![Pregunta "¿Cuáles son mis funciones Braze disponibles?" y responde en Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Cuáles son mis funciones Braze disponibles' se pregunta y se responde en Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Solución de problemas

### Errores de terminal

#### `uvx` comando no encontrado

Si recibes un error que indica que no se encuentra el comando `uvx`, reinstala `uv` y reinicia tu terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` error

Si recibes un error `spawn uvx ENOENT`, puede que tengas que actualizar la ruta del archivo en el archivo de configuración de tu cliente. Primero, abre tu terminal y ejecuta el siguiente comando:

```bash
which uvx
```

El comando debería devolver un mensaje similar al siguiente:

```bash
/Users/alex-lee/.local/bin/uvx
```

Copia el mensaje en el portapapeles y abre [el archivo de configuración de tu cliente](#configure-client). Sustituye `"command": "uvx"` por la ruta que has copiado y, a continuación, reinicia tu cliente. Por ejemplo:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Falla la instalación del paquete

Si falla la instalación del paquete, prueba a instalar una versión concreta de Python.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuración del cliente

#### El cliente MCP no encuentra el servidor Braze

1. Comprueba que la sintaxis de configuración de tu cliente MCP es correcta.
2. Reinicia tu cliente MCP tras los cambios de configuración.
3. Comprueba que `uvx` está en tu sistema `PATH`.

#### Errores de autenticación

1. Comprueba que tu `BRAZE_API_KEY` es correcto y está activo.
2. Asegúrate de que tu `BRAZE_BASE_URL` coincide con tu instancia de Braze.
3. Comprueba que tu clave de API tiene los [permisos correctos](#create-api-key).

#### Tiempos de conexión o errores de red

1. Comprueba que tu `BRAZE_BASE_URL` es correcto para tu instancia.
2. Comprueba tu conexión de red y la configuración del cortafuegos.
3. Asegúrate de que utilizas HTTPS en tu URL base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
