# Configuración del servidor Braze MCP

> Aprende a configurar el servidor MCP de Braze para poder interactuar con tus datos de Braze mediante lenguaje natural utilizando herramientas como Claude y Cursor. Para obtener información más general, consulta [Servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo | Descripción |
|--------------|-------------|
| Clave de API de Braze | Una clave de API de Braze con los permisos necesarios. Crearás una nueva clave cuando [configures tu servidor Braze MCP](#create-api-key). |
| Cliente MCP | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) y [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) son oficialmente compatibles. Debes tener una cuenta para uno de estos clientes para poder utilizar el servidor MCP de Braze. |
| Terminal | Una aplicación de terminal para que puedas ejecutar comandos e instalar herramientas. Utiliza tu aplicación de terminal preferida o la que venga preinstalada en tu computadora. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuración del servidor Braze MCP

### Paso 1: Instalar `uv`

En primer lugar, instala `uv`—una [herramienta de línea de comandos de Astral](https://docs.astral.sh/uv/getting-started/installation/) para la administración de dependencias y el manejo de paquetes Python.

{% tabs local %}
{% tab MacOS and Linux %}
Abre tu aplicación de terminal, pega el siguiente comando y pulsa <kbd>Intro</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

El resultado es similar al siguiente:

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

El resultado es similar al siguiente:

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

El servidor MCP de Braze admite 38 puntos finales de solo lectura que no devuelven datos de los perfiles de usuario de Braze. Ve a **Configuración** > **API e identificadores** > **Claves de API** y crea una nueva clave de API con algunos o todos los permisos siguientes.

{% details List of read-only, non-PII permissions %}
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
No reutilices una clave de API existente: crea una específicamente para tu cliente MCP. Además, asigna únicamente permisos de solo lectura y no relacionados con la PII, ya que los agentes podrían intentar escribir o eliminar datos en Braze.
{% endalert %}

### Paso 3: Obtén tu identificador y punto final

Cuando configures tu cliente MCP, necesitarás el identificador de tu clave de API y el punto final REST de tu espacio de trabajo. Para obtener estos datos, vuelve a la página **Claves de API** del panel. Mantén esta página abierta para poder consultarla durante [el siguiente paso](#configure-client).

![Las «claves de API» en Braze muestran una clave de API recién creada y el punto final REST del usuario.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Paso 4: Configura tu cliente MCP {#configure-client}

Configura tu cliente MCP utilizando el archivo de configuración proporcionado previamente.

{% tabs %}
{% tab Claude %}
Configura tu servidor MCP utilizando el directorio del conector [Claude Desktop](https://claude.ai/download). 

1. En Claude Desktop, ve a **Configuración** > **Conectores** > **Examinar conectores** > **Extensiones de escritorio** > **Servidor Braze MCP** > **Instalar**.
2. Introduce tu clave de API y la URL base.
3. Guarda la configuración y reinicia Claude Desktop.

{% endtab %}

{% tab Cursor %}
En [Cursor](https://cursor.com/), ve a **Configuración** > **Herramientas e integraciones** > **Herramientas MCP** > **Añadir MCP personalizado** y, a continuación, añade el siguiente fragmento de código:

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

Reemplaza`key-identifier`  y`rest-endpoint`  con los valores correspondientes de la página **Claves de API** en Braze. Tu configuración debería ser similar a la siguiente:

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
{% tab Gemini CLI %}
Gemini CLI lee la configuración del usuario desde `~/.gemini/settings.json`. Si no existe, puedes crearlo ejecutando lo siguiente en tu terminal:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

A continuación, sustituye`yourname`  por la cadena exacta que aparece antes de`@BZXXXXXXXX`  en el indicador de tu terminal. A continuación, sustituye`key-identifier`  y`rest-endpoint`  por los valores correspondientes de la página **Claves de API** de Braze. 

Tu configuración debería ser similar a la siguiente:

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Cuando hayas terminado, guarda la configuración y reinicia Gemini CLI. A continuación, en Gemini, ejecuta los siguientes comandos para verificar que el servidor Braze MCP aparece en la lista y que las herramientas y el esquema están disponibles para su uso:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Deberías ver el`braze`servidor en la lista con las herramientas y el esquema disponibles para su uso.

{% endtab %}
{% endtabs %}

### Paso 5: Enviar una solicitud de prueba

Después de configurar el servidor Braze MCP, intenta enviar una solicitud de prueba a tu cliente MCP. Para ver otros ejemplos y prácticas recomendadas, consulta [Uso del servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![«¿Cuáles son las funciones de Braze que tengo disponibles?», pregunta y respuesta en Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![«¿Cuáles son las funciones disponibles de Braze?» Pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![¿Cuáles son las funciones disponibles de Braze? Pregunta y respuesta en Gemini CLI.]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Solución de problemas

### Errores terminales

#### `uvx` comando no encontrado

Si recibes un error que indica que  no`uvx` se encuentra el comando, vuelve a instalar`uv`  y reinicia tu terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` error

Si recibes un`spawn uvx ENOENT`error, es posible que tengas que actualizar la ruta del archivo en el archivo de configuración de tu cliente. En primer lugar, abre tu terminal y ejecuta el siguiente comando:

```bash
which uvx
```

El comando debería devolver un mensaje similar al siguiente:

```bash
/Users/alex-lee/.local/bin/uvx
```

Copia el mensaje en el portapapeles y abre [el archivo de configuración de tu cliente](#configure-client). Reemplaza`"command": "uvx"`  con la ruta que copiaste y, a continuación, reinicia tu cliente. Por ejemplo:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Error en la instalación del paquete

Si la instalación del paquete falla, intenta instalar una versión específica de Python.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuración del cliente

#### El cliente MCP no puede encontrar el servidor Braze.

1. Verifica que la sintaxis de configuración de tu cliente MCP sea correcta.
2. Reinicia tu cliente MCP después de realizar cambios en la configuración.
3. Comprueba que`uvx`  está en tu sistema `PATH`.

#### Errores de autenticación

1. Verifica que tu`BRAZE_API_KEY`  sea correcto y esté activo.
2. Asegúrate de que`BRAZE_BASE_URL`  coincida con tu instancia de Braze.
3. Comprueba que tu clave de API tiene los [permisos correctos](#create-api-key).

#### Tiempo de espera de conexión agotado o errores de red

1. Verifica que tu`BRAZE_BASE_URL`  sea correcto para tu instancia.
2. Comprueba tu conexión de red y la configuración del cortafuegos.
3. Asegúrate de utilizar HTTPS en tu URL base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
