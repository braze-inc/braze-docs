## Migration granularer Berechtigungen

{% alert important %}
Granulare Berechtigungen befinden sich derzeit in der Early-Access-Phase. Wenn für Ihr Unternehmen eine Migration geplant ist, erhalten Ihre Braze-Administratoren E-Mails und Banner im Dashboard, die sie über die [Migration der]({{site.baseurl}}/granular_permissions_migration/) [detaillierten Berechtigungen]({{site.baseurl}}/granular_permissions_migration/) informieren.
{% endalert %}

Bestehende SCIM-Integrationen und [ältere SCIM-API-Objekte]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api) werden nach der Migration der granularen Berechtigungen Ende April weiterhin funktionieren. 

Es ist nicht erforderlich, dass Sie sofort Maßnahmen ergreifen. Wir empfehlen Ihnen jedoch, Ihre Integrationen auf Berechtigungen zu überprüfen, die granularisiert werden. Wenn Sie derzeit beispielsweise in der `basic_access`API senden, empfehlen wir Ihnen, Ihre Integration nach der Granularisierung zu aktualisieren, um die spezifischen Berechtigungen (z. B. `"appGroupPermissions":["view_campaigns","edit_campaigns"]`) einzubeziehen. Braze wird auch`basic_access` nach der Migration der granularen Berechtigungen weiterhin ältere Strings akzeptieren, damit bestehende Integrationen weiterhin funktionieren.

## Objekt Berechtigungen

Das Berechtigungsobjekt ist ein Feld, das in einigen Anfragen und Antworten zu finden ist, wenn Sie mit der Benutzerressource über SCIM-ID-Berechtigungen interagieren.

{% alert note %}
App-Gruppen wurden in Braze in Workspaces umbenannt, aber die angegebenen Tastaturbefehle beziehen sich noch auf die alte Terminologie (zum Beispiel `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Ein gültiges Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Werte-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `companyPermissions` | Optional | Array | String-Array von [Berechtigungs-Strings auf Unternehmensebene]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), wobei das Vorhandensein der String-Zeichenfolge bedeutet, dass die Nutzer:in über die entsprechende Berechtigung verfügt. |
| `roles` | Optional | Array | Array von [Rollenobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Erforderlich | Array | Array mit [Objekten für Arbeitsbereichsberechtigungen]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Workspace-Berechtigungen

Ein gültiges Appgruppen-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupName`| Optional | String | Workspace-Name Wird verwendet, um anzugeben, für welchen Arbeitsbereich die in diesem Objekt enthaltenen Berechtigungen gelten. | 
| `appGroupId` | Erforderlich, wenn `appGroupName` fehlt | String | ID des Workspace als dessen alternative Bezeichnung |
| `appGroupPermissionSets` | Optional | Array | Array mit einem einzelnen [Objekt der Arbeitsbereichsberechtigungen]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Erforderlich | Array | Array von Berechtigungsstrings auf Arbeitsbereichsebene aus der Tabelle [der Arbeitsbereichsberechtigungsstrings]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), wobei das Vorhandensein des Strings bedeutet, dass der Benutzer die entsprechende Berechtigung für den angegebenen Arbeitsbereich hat. |
| `team` | Optional | Array | Array von [Team-Berechtigungsobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objekt Workspace-Berechtigungssatz {#workspace-permissions-set-object}

Ein gültiges Objekt für den Workspace-Berechtigungssatz ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Optional | String | Name der Arbeitsbereich-Berechtigungsgruppe, die dem Benutzer für diesen Arbeitsbereich zugewiesen wird. |
| `appGroupPermissionSetID` | Erforderlich, wenn `appGroupPermissionSetName` fehlt | String | ID des Workspace als dessen alternative Bezeichnung des nutzerspezifischen Workspace-Berechtigungssatzes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objekt "Teamberechtigungen

Ein gültiges Team-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `teamName` | Optional | String | Name des Teams, der verwendet werden kann, um anzugeben, für welches Team die Berechtigungen in diesem Objekt gelten. |
| `teamId` | Erforderlich, wenn `teamName` fehlt | String | ID des Teams, die als alternative Methode zur Spezifizierung des Teams dient. |
| `teamPermissions` | Erforderlich | Array | Array mit Berechtigungsstrings auf Teamebene aus der Tabelle [Teams Permission Strings]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), in der das Vorhandensein des Strings bedeutet, dass der Benutzer die entsprechende Berechtigung für das angegebene Team hat. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Rollenobjekt

Ein gültiges Rollenobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `roleName` | Optional | String | Name der Rolle, die dem Benutzer zugewiesen wird. |
| `roleId` | Erforderlich, wenn `roleName` fehlt | String | ID der Rolle, die als alternative Methode zur Spezifizierung der Rolle dient. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anhang

### Erlaubnisstränge des Unternehmens {#company}

| Wie in UI angezeigt | SCIM API Zeichenfolge |
| --- | --- |
| Administrator | `admin` |
| Unternehmenseinstellungen verwalten | `manage_company_settings` |
| Workspaces erstellen und löschen| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Arbeitsbereichsberechtigungsstrings {#workspace-strings}

| Berechtigungsname | SCIM API Zeichenfolge |
| --- | --- |
| Kampagnen anzeigen | `view_campaigns` |
| Kampagnen bearbeiten | `edit_campaigns` |
| Kampagnen archivieren | `archive_campaigns` |
| Canvase anzeigen | `view_canvases` |
| Canvase bearbeiten | `edit_canvases` |
| Canvase archivieren | `archive_canvases` |
| Frequency-Capping-Regeln anzeigen | `view_frequency_caps` |
| Frequency-Capping-Regeln bearbeiten | `edit_frequency_caps` |
| Priorisierung von Nachrichten anzeigen | `view_message_prioritization` |
| Priorisierung von Nachrichten bearbeiten | `edit_message_prioritization` |
| Content-Blöcke anzeigen | `view_content_blocks` |
| Content-Blöcke bearbeiten | `edit_content_blocks` |
| Content-Blöcke archivieren | `archive_content_blocks` |
| Feature-Flags anzeigen | `view_feature_flags` |
| Feature-Flags bearbeiten | `edit_feature_flags` |
| Feature-Flags archivieren | `archive_feature_flags` |
| Segmente anzeigen | `view_segments` |
| Segmente bearbeiten | `edit_segments` |
| Segmente archivieren | `archive_segments` |
| Globale Kontrollgruppe anzeigen | `view_global_control_group` |
| Globale Kontrollgruppe bearbeiten | `edit_global_control_group` |
| IAM-Templates anzeigen | `view_iam_templates` |
| IAM-Templates bearbeiten | `edit_iam_templates` |
| IAM-Templates archivieren | `archive_iam_templates` |
| E-Mail-Templates anzeigen | `view_email_templates` |
| E-Mail-Templates bearbeiten | `edit_email_templates` |
| E-Mail Templates archivieren | `archive_email_templates` |
| Webhook-Templates anzeigen | `view_webhook_templates` |
| Webhook-Templates bearbeiten | `edit_webhook_templates` |
| Webhook-Templates archivieren | `archive_webhook_templates` |
| Link-Templates anzeigen | `view_link_templates` |
| Link-Templates bearbeiten | `edit_link_templates` |
| Mediathek Assets ansehen | `view_media_library_assets` |
| Standorte anzeigen | `view_locations` |
| Standorte bearbeiten | `edit_locations` |
| Standorte archivieren | `archive_locations` |
| Aktionscodes anzeigen | `view_promotion_codes` |
| Aktionscodes bearbeiten | `edit_promotion_codes` |
| Exportförderungsaktionscodes | `export_promotion_codes` |
| Präferenzzentren anzeigen | `view_preference_centers` |
| Präferenzzentren bearbeiten | `edit_preference_centers` |
| Berichte bearbeiten | `edit_reports` |
| Platzierungen ansehen | `view_placements` |
| Platzierungen bearbeiten | `edit_placements` |
| Platzierungen archivieren | `archive_placements` |
| Banner-Templates anzeigen | `view_banner_templates` |
| Mehrsprachige Einstellungen anzeigen | `view_multi_language_settings` |
| Operator verwenden | `use_operator` |
| Entscheidungsstudio-Agenten anzeigen | `view_decisioning_studio_agents` |
| Decisioning Studio-Zielgruppe anzeigen |`view_decisioning_studio_audience` |
| Entscheidungsstudio-Konversions-Event anzeigen | `view_decisioning_studio_conversion_event` |
| Leitlinien von Decisioning Studio anzeigen | `view_decisioning_studio_guardrails` |
| Kampagnen starten | `launch_campaigns` |
| Canvase starten | `launch_canvases` |
| Dashboard-Nutzer:innen bearbeiten | `edit_dashboard_users` |
| Assets der Medienbibliothek bearbeiten | `edit_media_library_assets` |
| Assets der Medienbibliothek löschen | `delete_media_library_assets` |
| Importierte Nutzer:innen anzeigen | `view_import_users` |
| Nutzer:innen importieren	| `import_users` |
| Nutzerdaten bearbeiten | `edit_user_data` |
| Zusammengeführte Nutzerdatensätze anzeigen | `view_user_merge_records` |
| Doppelte Nutzer:innen zusammenführen | `merge_duplicate_users` |
| API-Schlüssel anzeigen | `view_api_keys` |
| API-Schlüssel bearbeiten | `edit_api_keys` |
| Interne Gruppen anzeigen | `view_internal_user_groups` |
| Interne Gruppen bearbeiten | `edit_internal_user_groups` |
| Interne Gruppen löschen | `delete_internal_user_groups` |
| Nachrichten-Aktivitätsprotokoll anzeigen | `view_message_activity_log` |
| Event-Nutzerprotokoll anzeigen | `view_event_user_log` |
| API-Bezeichner anzeigen | `view_api_identifiers` |
| Dashboard zur API-Nutzung anzeigen | `view_api_usage_dashboard` |
| API-Limits anzeigen | `view_api_limits` |
| API-Nutzungsmeldungen anzeigen | `view_api_usage_alerts` |
| API-Nutzungsmeldungen bearbeiten | `edit_api_usage_alerts` |
| SDK Debugger anzeigen | `view_sdk_debugger` |
| SDK-Debugger bearbeiten | `edit_sdk_debugger` |
| Content-Blöcke starten | `launch_content_blocks` |
| Cloud-Datenaufnahme bearbeiten | `edit_cloud_data_ingestion` |
| App-Einstellungen anzeigen | `view_app_settings` |
| App-Einstellungen bearbeiten | `edit_app_settings` |
| Push-Einstellungen anzeigen | `view_push_settings` |
| Push-Einstellungen bearbeiten | `edit_push_settings` |
| Teams anzeigen | `view_teams` |
| Teams bearbeiten | `edit_teams` |
| Teams archivieren | `archive_teams` |
| Angepasste Attribute anzeigen | `view_custom_attributes` |
| Angepasste Attribute bearbeiten | `edit_custom_attributes` |
| Sperrliste für angepasste Attribute | `blocklist_custom_attributes` |
| Angepasste Attribute löschen | `delete_custom_attributes` |
| Angepasste Attribute exportieren | `export_custom_attributes` |
| Angepasste Events anzeigen	 | `view_custom_events` |
| Angepasste Events bearbeiten | `edit_custom_events` |
| Sperrliste für angepasste Events | `blocklist_custom_events` |
| Angepasste Events löschen | `delete_custom_events` |
| Angepasste Events exportieren | `export_custom_events` |
| Segmentierung von angepassten Event-Eigenschaften bearbeiten | `edit_custom_event_property_segmentation` |
| Produkte anzeigen | `view_products` |
| Produkte bearbeiten	 | `edit_products` |
| Sperrliste für Produkte | `blocklist_products` |
| Segmentierung von Kaufeigenschaften bearbeiten | `edit_purchase_property_segmentation` |
| Tags anzeigen | `view_tags` |
| Tags bearbeiten | `edit_tags` |
| Tags löschen | `delete_tags` |
| E-Mail-Einstellungen anzeigen	| `view_email_settings` |
| E-Mail-Einstellungen bearbeiten | `edit_email_settings` |
| Kataloge anzeigen | `view_catalogs` |
| Kataloge bearbeiten	 | `edit_catalogs` |
| Kataloge exportieren | `export_catalogs` |
| Kataloge löschen | `delete_catalogs` |
| WhatsApp-Einstellungen anzeigen | `view_whatsapp_settings` |
| Technologiepartner bearbeiten | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Team-Berechtigungsstrings {#team}

| Berechtigungsname | SCIM API Zeichenfolge |
| --- | --- |
| Kampagnen anzeigen | `view_campaigns` |
| Kampagnen bearbeiten | `edit_campaigns` |
| Kampagnen archivieren | `archive_campaigns` |
| Canvase anzeigen | `view_canvases` |
| Canvase bearbeiten | `edit_canvases` |
| Canvase archivieren | `archive_canvases` |
| Frequency-Capping-Regeln anzeigen | `view_frequency_caps` |
| Frequency-Capping-Regeln bearbeiten | `edit_frequency_caps` |
| Priorisierung von Nachrichten anzeigen | `view_message_prioritization` |
| Priorisierung von Nachrichten bearbeiten | `edit_message_prioritization` |
| Content-Blöcke anzeigen | `view_content_blocks` |
| Feature-Flags anzeigen | `view_feature_flags` |
| Feature-Flags bearbeiten | `edit_feature_flags` |
| Feature-Flags archivieren | `archive_feature_flags` |
| Segmente anzeigen | `view_segments` |
| Segmente bearbeiten | `edit_segments` |
| Globale Kontrollgruppe bearbeiten | `edit_global_control_group` |
| IAM-Templates anzeigen | `view_iam_templates` |
| IAM-Templates bearbeiten | `edit_iam_templates` |
| IAM-Templates archivieren | `archive_iam_templates` |
| E-Mail-Templates anzeigen | `view_email_templates` |
| E-Mail-Templates bearbeiten | `edit_email_templates` |
| E-Mail Templates archivieren | `archive_email_templates` |
| Webhook-Templates anzeigen | `view_webhook_templates` |
| Webhook-Templates bearbeiten | `edit_webhook_templates` |
| Webhook-Templates archivieren | `archive_webhook_templates` |
| Link-Templates anzeigen | `view_link_templates` |
| Link-Templates bearbeiten | `edit_link_templates` |
| Mediathek Assets ansehen | `view_media_library_assets` |
| Standorte anzeigen | `view_locations` |
| Standorte bearbeiten | `edit_locations` |
| Standorte archivieren | `archive_locations` |
| Aktionscodes anzeigen | `view_promotion_codes` |
| Aktionscodes bearbeiten | `edit_promotion_codes` |
| Exportförderungsaktionscodes | `export_promotion_codes` |
| Präferenzzentren anzeigen | `view_preference_centers` |
| Präferenzzentren bearbeiten | `edit_preference_centers` |
| Berichte anzeigen | `view_reports` |
| Erstellen Sie Berichte | `create_reports` |
| Berichte bearbeiten | `edit_reports` |
| Banner-Templates anzeigen | `view_banner_templates` |
| Mehrsprachige Einstellungen anzeigen | `view_multi_language_settings` |
| Operator verwenden | `use_operator` |
| Entscheidungsstudio-Agenten anzeigen | `view_decisioning_studio_agents` |
| Entscheidungsstudio-Konversions-Event anzeigen | `view_decisioning_studio_conversion_event` |
| Kampagnen starten | `launch_campaigns` |
| Canvase starten | `launch_canvases` |
| Dashboard-Nutzer:innen bearbeiten | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Abteilungsstrings

| Wie in UI angezeigt | SCIM API Zeichenfolge |
| --- | --- |
| Agentur/Dritte Partei | `agency` |
| BI / Analytik | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finanzen | `finance` |
| Marketing / Redaktion | `marketing` |
| Produktmanagement | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }