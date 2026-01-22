# Einrichten des Braze MCP Servers

> Erfahren Sie, wie Sie den Braze MCP Server einrichten, damit Sie mit Hilfe von Tools wie Claude und Cursor über natürliche Sprache mit Ihren Braze Daten interagieren können. Weitere allgemeine Informationen finden Sie unter [Braze MCP Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|--------------|-------------|
| Braze API-Schlüssel | Ein Braze API-Schlüssel mit den erforderlichen Berechtigungen. Sie erstellen einen neuen Schlüssel, wenn Sie [Ihren Braze MCP Server einrichten](#create-api-key). |
| MCP Client | Derzeit werden nur [Claude](https://claude.ai/) und [Cursor](https://cursor.com/) offiziell unterstützt. Sie benötigen ein Konto für einen dieser Clients, um den Braze MCP Server zu verwenden. |
| Terminal | Eine Terminal App, mit der Sie Befehle ausführen und Tools installieren können. Verwenden Sie Ihre bevorzugte Terminal App oder die App, die auf Ihrem Computer vorinstalliert ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Einrichten des Braze MCP Servers

### Schritt 1: Installieren Sie `uv`

Installieren Sie zunächst `uv`- ein [Kommandozeilen-Tool von Astral](https://docs.astral.sh/uv/getting-started/installation/) für die Verwaltung von Abhängigkeiten und Python-Paketen.

{% tabs local %}
{% tab MacOS und Linux %}
Öffnen Sie Ihr Terminalprogramm, fügen Sie den folgenden Befehl ein und drücken Sie die <kbd>Eingabetaste</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Die Ausgabe sieht in etwa so aus wie die folgende:

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
 Öffnen Sie Windows PowerShell, fügen Sie den folgenden Befehl ein und drücken Sie dann die <kbd>Eingabetaste</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Die Ausgabe sieht in etwa so aus wie die folgende:

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

### Schritt 2: Einen API-Schlüssel erstellen {#create-api-key}

Braze MCP Server unterstützt 38 schreibgeschützte Endpunkte, die keine Daten aus Nutzer:innen-Profilen zurückgeben. Gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel** und erstellen Sie einen neuen Schlüssel mit einigen oder allen der folgenden Berechtigungen.

{% details Liste der Nur-Lese-Berechtigungen, nicht PII %}
#### Kampagnen

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canvas

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Kataloge

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Ingestion von Cloud-Daten

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Content-Blöcke

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Angepasste Attribute

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Events

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPIs

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Nachrichten

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Präferenz-Center

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Käufe

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Segmente

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Sendungen

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### Sitzungen

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### SDK-Authentifizierungsschlüssel

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Abo

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Vorlagen

| Endpunkt | Erforderliche Erlaubnis |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
Verwenden Sie keinen bestehenden API-Schlüssel wieder - erstellen Sie einen speziell für Ihren MCP Client. Vergeben Sie außerdem nur Leseberechtigungen, die keine PII enthalten, da Agenten versuchen könnten, Daten in Braze zu schreiben oder zu löschen.
{% endalert %}

### Schritt 3: Holen Sie sich Ihren Identifikator und Endpunkt

Wenn Sie Ihren MCP Client konfigurieren, benötigen Sie den Bezeichner Ihres API-Schlüssels und den REST-Endpunkt Ihres Workspace. Um diese Details zu erhalten, gehen Sie zurück zur Seite **API-Schlüssel** im Dashboard - lassen Sie diese Seite geöffnet, damit Sie sie im [nächsten Schritt](#configure-client) referenzieren können.

![Die 'API-Schlüssel' in Braze zeigen einen neu erstellten API-Schlüssel und den REST-Endpunkt des Nutzers.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Schritt 4: Konfigurieren Sie Ihren MCP Client {#configure-client}

Konfigurieren Sie Ihren MCP Client mit unserer vorbereiteten Konfigurationsdatei.

{% tabs %}
{% tab Claude %}
Gehen Sie in [Claude Desktop](https://claude.ai/download) zu **Einstellungen** > **Entwickler** > **Konfiguration bearbeiten**, und fügen Sie das folgende Snippet hinzu:

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

Ersetzen Sie `key-identifier` und `rest-endpoint` durch die entsprechenden Werte auf der Seite **API-Schlüssel** in Braze. Ihre Konfiguration sollte in etwa so aussehen wie die folgende:

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

Wenn Sie fertig sind, speichern Sie die Konfiguration und starten Sie Claude Desktop neu.
{% endtab %}

{% tab Cursor %}
Gehen Sie in [Cursor](https://cursor.com/) zu **Einstellungen** > **Tools und Integrationen** > **MCP-Tools** > **Angepassten MCP hinzufügen** und fügen Sie dann das folgende Snippet hinzu:

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

Ersetzen Sie `key-identifier` und `rest-endpoint` durch die entsprechenden Werte auf der Seite **API-Schlüssel** in Braze. Ihre Konfiguration sollte in etwa so aussehen wie die folgende:

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

Wenn Sie fertig sind, speichern Sie die Konfiguration und starten Sie Cursor neu.
{% endtab %}
{% endtabs %}

### Schritt 5: Senden Sie eine Testaufforderung

Nachdem Sie nun den Braze MCP Server eingerichtet haben, versuchen Sie, eine Testaufforderung an Ihren MCP Client zu senden. Weitere Beispiele und bewährte Verfahren finden Sie unter [Verwendung des Braze MCP Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![Die Frage 'Welche Braze-Funktionen stehen mir zur Verfügung?' wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage 'Welche Funktionen sind in Braze verfügbar?' wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Fehlersuche

### Terminal-Fehler

#### `uvx` Befehl nicht gefunden

Wenn Sie die Fehlermeldung `uvx` command not found erhalten, installieren Sie `uv` neu und starten Sie Ihr Terminal neu.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` Fehler

Wenn Sie eine `spawn uvx ENOENT` Fehlermeldung erhalten, müssen Sie möglicherweise den Dateipfad in der Konfigurationsdatei Ihres Clients aktualisieren. Öffnen Sie zunächst Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
which uvx
```

Der Befehl sollte eine Nachricht ähnlich der folgenden zurückgeben:

```bash
/Users/alex-lee/.local/bin/uvx
```

Kopieren Sie die Nachricht in Ihre Zwischenablage und öffnen Sie [die Konfigurationsdatei Ihres Clients](#configure-client). Ersetzen Sie `"command": "uvx"` durch den Pfad, den Sie kopiert haben, und starten Sie dann Ihren Client neu. Zum Beispiel:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Paketinstallation schlägt fehl

Wenn Ihre Paketinstallation fehlschlägt, versuchen Sie stattdessen, eine bestimmte Python-Version zu installieren.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Client-Konfiguration

#### MCP-Client kann den Braze Server nicht finden

1. Überprüfen Sie, ob die Syntax Ihrer MCP Client-Konfiguration korrekt ist.
2. Starten Sie Ihren MCP Client nach Konfigurationsänderungen neu.
3. Überprüfen Sie, ob `uvx` in Ihrem System enthalten ist `PATH`.

#### Authentifizierungsfehler

1. Überprüfen Sie, ob Ihre `BRAZE_API_KEY` korrekt und aktiv ist.
2. Stellen Sie sicher, dass Ihre `BRAZE_BASE_URL` mit Ihrer Braze-Instanz übereinstimmt.
3. Überprüfen Sie, ob Ihr API-Schlüssel die [richtigen Berechtigungen](#create-api-key) hat.

#### Zeitüberschreitungen bei der Verbindung oder Netzwerkfehler

1. Überprüfen Sie, ob Ihre `BRAZE_BASE_URL` für Ihre Instanz korrekt ist.
2. Überprüfen Sie Ihre Netzwerkverbindung und Ihre Firewall-Einstellungen.
3. Stellen Sie sicher, dass Sie HTTPS in Ihrer Basis-URL verwenden.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
