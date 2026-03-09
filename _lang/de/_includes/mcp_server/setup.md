# Einrichtung des Braze MCP-Servers

> Erfahren Sie, wie Sie den Braze MCP-Server einrichten, um mit Ihren Braze-Daten über natürliche Sprache mithilfe von Tools wie Claude und Cursor zu interagieren. Weitere allgemeine Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}.{{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/){% endif %}

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|--------------|-------------|
| Braze-API-Schlüssel | Ein Braze-API-Schlüssel mit den erforderlichen Berechtigungen. Sie erstellen einen neuen Schlüssel, wenn Sie [Ihren Braze MCP-Server einrichten.](#create-api-key) |
| MCP-Client | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) und [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) werden offiziell unterstützt. Sie benötigen ein Konto für einen dieser Clients, um den Braze MCP-Server nutzen zu können. |
| Terminal | Eine Terminal-App, mit der Sie Befehle ausführen und Tools installieren können. Bitte verwenden Sie Ihre bevorzugte Terminal-App oder die auf Ihrem Computer vorinstallierte App. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Einrichtung des Braze MCP-Servers

### Schritt 1: Installieren `uv`

Installieren Sie zunächst`uv` —ein [Befehlszeilentool von Astral](https://docs.astral.sh/uv/getting-started/installation/) für die Abhängigkeitsverwaltung und die Handhabung von Python-Paketen.

{% tabs local %}
{% tab MacOS and Linux %}
Öffnen Sie bitte Ihre Terminal-Anwendung, fügen Sie den folgenden Befehl ein und drücken Sie <kbd>die Eingabetaste</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Die Ausgabe sieht in etwa wie folgt aus:

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
 Öffnen Sie Windows PowerShell, fügen Sie den folgenden Befehl ein und drücken Sie <kbd>die Eingabetaste</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Die Ausgabe sieht in etwa wie folgt aus:

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

### Schritt 2: Erstellen Sie einen API-Schlüssel. {#create-api-key}

Der Braze MCP-Server unterstützt 38 schreibgeschützte Endpunkte, die keine Daten aus Braze-Nutzerprofilen zurückgeben. Bitte navigieren Sie zu **„Einstellungen“** > **„APIs und Bezeichner“** > **„API-Schlüssel“** und erstellen Sie einen neuen Schlüssel mit einigen oder allen der folgenden Berechtigungen.

{% details List of read-only, non-PII permissions %}
#### Kampagnen

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canvas

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Kataloge

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Ingestion von Cloud-Daten

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Content-Blöcke

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Angepasste Attribute

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Events

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### KPIs

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Nachrichten

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Präferenz-Center

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Käufe

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Segmente

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Sendungen

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### Sitzungen

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### SDK-Authentifizierungsschlüssel

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Abo

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Vorlagen

| Endpunkt | Erforderliche Genehmigung |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
Bitte verwenden Sie keinen bereits vorhandenen API-Schlüssel wieder, sondern erstellen Sie einen neuen Schlüssel speziell für Ihren MCP-Client. Bitte weisen Sie ausschließlich schreibgeschützte, nicht PII-bezogene Berechtigungen zu, da Agenten möglicherweise versuchen könnten, Daten in Braze zu schreiben oder zu löschen.
{% endalert %}

### Schritt 3: Bitte holen Sie sich Ihren Bezeichner und Ihren Endpunkt ein.

Bei der Konfiguration Ihres MCP-Clients benötigen Sie den Bezeichner Ihres API-Schlüssels und den REST-Endpunkt Ihres Workspaces. Um diese Informationen zu erhalten, kehren Sie bitte zur Seite **„API-Schlüssel“** im Dashboard zurück. Bitte lassen Sie diese Seite geöffnet, damit Sie im[ nächsten Schritt](#configure-client) darauf referenzieren können.

![Die „API-Schlüssel“ in Braze zeigen einen neu erstellten API-Schlüssel und den REST-Endpunkt der Nutzer:innen an.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Schritt 4: Bitte konfigurieren Sie Ihren MCP-Client. {#configure-client}

Bitte konfigurieren Sie Ihren MCP-Client mithilfe der bereitgestellten Konfigurationsdatei.

{% tabs %}
{% tab Claude %}
Richten Sie Ihren MCP-Server mithilfe des [Claude Desktop](https://claude.ai/download)-Konnektors ein. 

1. Bitte gehen Sie in Claude Desktop zu **„Einstellungen“** > **„Konnektoren“** > **„Konnektoren durchsuchen“** > **„Desktop-Erweiterungen“** > **„Braze MCP Server**“ > **„Installieren**“.
2. Bitte geben Sie Ihren API-Schlüssel und Ihre Basis-URL ein.
3. Bitte speichern Sie die Konfiguration und starten Sie Claude Desktop neu.

{% endtab %}

{% tab Cursor %}
Bitte gehen Sie in [Cursor](https://cursor.com/) zu **„Einstellungen“** > **„Tools und Integrationen“** > **„MCP-Tools“** > **„Angepasstes MCP hinzufügen**“ und fügen Sie anschließend das folgende Snippet hinzu:

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

Ersetzen Sie`key-identifier`  und`rest-endpoint`  durch die entsprechenden Werte von der Seite **„API-Schlüssel“** in Braze. Ihre Konfiguration sollte in etwa wie folgt aussehen:

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

Wenn Sie fertig sind, speichern Sie bitte die Konfiguration und starten Sie Cursor neu.
{% endtab %}
{% tab Gemini CLI %}
Gemini CLI liest die Einstellungen der Nutzer:innen aus `~/.gemini/settings.json`. Sollte dies nicht vorhanden sein, können Sie es erstellen, indem Sie Folgendes in Ihrem Terminal ausführen:

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

Ersetzen Sie anschließend in Ihrer `yourname``@BZXXXXXXXX`Terminal-Eingabeaufforderung  durch den genauen String vor . Ersetzen Sie anschließend`key-identifier`  und`rest-endpoint`  durch die entsprechenden Werte von der Seite **„API-Schlüssel“** in Braze. 

Ihre Konfiguration sollte in etwa wie folgt aussehen:

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

Wenn Sie fertig sind, speichern Sie bitte die Konfiguration und starten Sie Gemini CLI neu. Führen Sie anschließend in Gemini die folgenden Befehle aus, um zu überprüfen, ob der Braze MCP-Server aufgeführt ist und die Tools und das Schema zur Verwendung verfügbar sind:

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Sie sollten den`braze`Server mit den verfügbaren Tools und Schemata aufgelistet sehen.

{% endtab %}
{% endtabs %}

### Schritt 5: Bitte senden Sie eine Testanweisung.

Nachdem Sie den Braze MCP-Server eingerichtet haben, senden Sie bitte eine Testnachricht an Ihren MCP-Client. Weitere Beispiele und bewährte Verfahren finden Sie unter [Verwendung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![„Welche Braze-Funktionen stehen mir zur Verfügung?“ – diese Frage wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage „Welche Braze-Funktionen stehen mir zur Verfügung?“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![Welche Funktionen von Braze stehen mir zur Verfügung? Diese Frage wird in Gemini CLI gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Fehlersuche

### Terminalfehler

#### `uvx` Befehl nicht gefunden

Sollten Sie eine Fehlermeldung erhalten, dass`uvx`der Befehl nicht gefunden wurde, installieren Sie bitte erneut`uv`und starten Sie Ihr Terminal neu.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` Fehler

Sollten Sie Fehlermeldungen`spawn uvx ENOENT` erhalten, ist es möglicherweise erforderlich, den Dateipfad in der Konfigurationsdatei Ihres Clients zu aktualisieren. Bitte öffnen Sie zunächst Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
which uvx
```

Der Befehl sollte eine Nachricht ähnlich der folgenden zurückgeben:

```bash
/Users/alex-lee/.local/bin/uvx
```

Bitte kopieren Sie die Nachricht in Ihre Zwischenablage und öffnen Sie [die Konfigurationsdatei Ihres Clients](#configure-client). Ersetzen Sie dies`"command": "uvx"`durch den kopierten Pfad und starten Sie anschließend Ihren Client neu. Zum Beispiel:

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### Die Installation des Pakets ist fehlgeschlagen.

Sollte die Installation Ihres Pakets fehlschlagen, versuchen Sie bitte, stattdessen eine bestimmte Python-Version zu installieren.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Client-Konfiguration

#### Der MCP-Client kann den Braze-Server nicht finden.

1. Bitte überprüfen Sie, ob die Syntax Ihrer MCP-Clientkonfiguration korrekt ist.
2. Bitte starten Sie Ihren MCP-Client nach Konfigurationsänderungen neu.
3. Bitte überprüfen Sie, ob`uvx`sich in Ihrem System befindet`PATH`.

#### Authentifizierungsfehler

1. Bitte überprüfen Sie, ob `BRAZE_API_KEY`Ihre Angaben korrekt und aktiv sind.
2. Bitte stellen Sie sicher, dass Ihre Konfiguration`BRAZE_BASE_URL` mit Ihrer Braze-Instanz übereinstimmt.
3. Bitte überprüfen Sie, ob Ihr API-Schlüssel über die [erforderlichen Berechtigungen](#create-api-key) verfügt.

#### Zeitüberschreitungen bei der Verbindung oder Netzwerkfehler

1. Bitte überprüfen Sie, ob Ihre Angaben für Ihre `BRAZE_BASE_URL`Instanz korrekt sind.
2. Bitte überprüfen Sie Ihre Netzwerkverbindung und Ihre Firewall-Einstellungen.
3. Bitte stellen Sie sicher, dass Sie HTTPS in Ihrer Basis-URL verwenden.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
