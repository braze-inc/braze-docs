## Migration granularer Berechtigungen

{% alert important %}
Granulare Berechtigungen befinden sich derzeit in der Early-Access-Phase. Wenn für Ihr Unternehmen eine Migration geplant ist, erhalten Ihre Braze-Administratoren E-Mails und Banner im Dashboard, die sie über die [Migration granularer Berechtigungen]({{site.baseurl}}/granular_permissions_migration/) informieren.
{% endalert %}

Bestehende SCIM-Integrationen und [ältere SCIM-API-Objekte]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api) werden nach der Migration der granularen Berechtigungen Ende April weiterhin funktionieren. 

Es ist nicht erforderlich, dass Sie sofort Maßnahmen ergreifen. Wir empfehlen Ihnen jedoch, Ihre Integrationen auf Berechtigungen zu überprüfen, die granularisiert werden. Wenn Sie derzeit beispielsweise `basic_access` in der API senden, empfehlen wir Ihnen, Ihre Integration nach der Granularisierung zu aktualisieren, um die spezifischen Berechtigungen einzubeziehen (z. B. `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze wird auch nach der Migration der granularen Berechtigungen weiterhin ältere Strings wie `basic_access` akzeptieren, damit bestehende Integrationen weiterhin funktionieren.

## Berechtigungsobjekt

Das Berechtigungsobjekt ist ein Feld, das in einigen Anfragen und Antworten zu finden ist, wenn Sie mit der Nutzerressource über SCIM-ID-Berechtigungen interagieren.

{% alert note %}
App-Gruppen wurden in Braze in Workspaces umbenannt, aber die Schlüssel auf dieser Seite beziehen sich noch auf die alte Terminologie (z. B. `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Ein gültiges Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `companyPermissions` | Optional | Array | Array von [Berechtigungsstrings auf Unternehmensebene]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in über die entsprechende Berechtigung verfügt. |
| `roles` | Optional | Array | Array von [Rollenobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Erforderlich | Array | Array von [Workspace-Berechtigungsobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Workspace-Berechtigungsobjekt

Ein gültiges App-Gruppen-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupName`| Optional | String | Name des Workspace. Wird verwendet, um anzugeben, für welchen Workspace die in diesem Objekt enthaltenen Berechtigungen gelten. | 
| `appGroupId` | Erforderlich, wenn `appGroupName` fehlt | String | ID des Workspace, die als alternative Methode zur Angabe des Workspace dient. |
| `appGroupPermissionSets` | Optional | Array | Array mit einem einzelnen [Workspace-Berechtigungssatz-Objekt]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Erforderlich | Array | Array von Berechtigungsstrings auf Workspace-Ebene aus der Tabelle der [Workspace-Berechtigungsstrings]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für den angegebenen Workspace hat. |
| `team` | Optional | Array | Array von [Team-Berechtigungsobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Workspace-Berechtigungssatz-Objekt {#workspace-permissions-set-object}

Ein gültiges Workspace-Berechtigungssatz-Objekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Optional | String | Name des Workspace-Berechtigungssatzes, der der Nutzer:in für diesen Workspace zugewiesen wird. |
| `appGroupPermissionSetID` | Erforderlich, wenn `appGroupPermissionSetName` fehlt | String | ID des Workspace, die als alternative Methode zur Angabe des Workspace-Berechtigungssatzes dient, der der Nutzer:in für diesen Workspace zugewiesen wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Team-Berechtigungsobjekt

Ein gültiges Team-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `teamName` | Optional | String | Name des Teams, der verwendet werden kann, um anzugeben, für welches Team die Berechtigungen in diesem Objekt gelten. |
| `teamId` | Erforderlich, wenn `teamName` fehlt | String | ID des Teams, die als alternative Methode zur Angabe des Teams dient. |
| `teamPermissions` | Erforderlich | Array | Array von Berechtigungsstrings auf Team-Ebene aus der Tabelle der [Team-Berechtigungsstrings]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für das angegebene Team hat. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Rollenobjekt

Ein gültiges Rollenobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `roleName` | Optional | String | Name der Rolle, die der Nutzer:in zugewiesen wird. |
| `roleId` | Erforderlich, wenn `roleName` fehlt | String | ID der Rolle, die als alternative Methode zur Angabe der Rolle dient. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anhang

### Berechtigungsstrings auf Unternehmensebene {#company}

| Wie in der UI angezeigt | SCIM-API-String |
| --- | --- |
| Administrator | `admin` |
| Unternehmenseinstellungen verwalten | `manage_company_settings` |
| Workspaces erstellen und löschen| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Workspace-Berechtigungsstrings {#workspace-strings}

| Berechtigungsname | SCIM-API-String |
| --- | --- |
| Kampagnen anzeigen | `view_campaigns` |
| Kampagnen bearbeiten | `edit_campaigns` |
| Kampagnen archivieren | `archive_campaigns` |
| Canvase anzeigen | `view_canvases` |
| Canvase bearbeiten | `edit_canvases` |
| Canvase archivieren | `archive_canvases` |
| Frequency-Capping-Regeln anzeigen | `view_frequency_caps` |
| Frequency-Capping-Regeln bearbeiten | `edit_frequency_caps` |
| Nachrichtenpriorisierung anzeigen | `view_message_prioritization` |
| Nachrichtenpriorisierung bearbeiten | `edit_message_prioritization` |
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
| E-Mail-Templates archivieren | `archive_email_templates` |
| Webhook-Templates anzeigen | `view_webhook_templates` |
| Webhook-Templates bearbeiten | `edit_webhook_templates` |
| Webhook-Templates archivieren | `archive_webhook_templates` |
| E-Mail-Link-Templates anzeigen | `view_link_templates` |
| E-Mail-Link-Templates bearbeiten | `edit_link_templates` |
| Mediathek-Assets anzeigen | `view_media_library_assets` |
| Standorte anzeigen | `view_locations` |
| Standorte bearbeiten | `edit_locations` |
| Standorte archivieren | `archive_locations` |
| Aktionscodes anzeigen | `view_promotion_codes` |
| Aktionscodes bearbeiten | `edit_promotion_codes` |
| Aktionscodes exportieren | `export_promotion_codes` |
| Präferenzzentren anzeigen | `view_preference_centers` |
| Präferenzzentren bearbeiten | `edit_preference_centers` |
| Berichte bearbeiten | `edit_reports` |
| Platzierungen anzeigen | `view_placements` |
| Platzierungen bearbeiten | `edit_placements` |
| Platzierungen archivieren | `archive_placements` |
| Banner-Templates anzeigen | `view_banner_templates` |
| Mehrsprachige Einstellungen anzeigen | `view_multi_language_settings` |
| Operator verwenden | `use_operator` |
| Decisioning-Studio-Agenten anzeigen | `view_decisioning_studio_agents` |
| Decisioning-Studio-Zielgruppe anzeigen |`view_decisioning_studio_audience` |
| Decisioning-Studio-Konversions-Event anzeigen | `view_decisioning_studio_conversion_event` |
| Decisioning-Studio-Leitlinien anzeigen | `view_decisioning_studio_guardrails` |
| Kampagnen starten | `launch_campaigns` |
| Canvase starten | `launch_canvases` |
| Dashboard-Nutzer:innen bearbeiten | `edit_dashboard_users` |
| Mediathek-Assets bearbeiten | `edit_media_library_assets` |
| Mediathek-Assets löschen | `delete_media_library_assets` |
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
| Nachrichtenaktivitätsprotokoll anzeigen | `view_message_activity_log` |
| Event-Benutzerprotokoll anzeigen | `view_event_user_log` |
| API-Bezeichner anzeigen | `view_api_identifiers` |
| Dashboard zur API-Nutzung anzeigen | `view_api_usage_dashboard` |
| API-Limits anzeigen | `view_api_limits` |
| API-Nutzungsmeldungen anzeigen | `view_api_usage_alerts` |
| API-Nutzungsmeldungen bearbeiten | `edit_api_usage_alerts` |
| SDK-Debugger anzeigen | `view_sdk_debugger` |
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

| Berechtigungsname | SCIM-API-String |
| --- | --- |
| Kampagnen anzeigen | `view_campaigns` |
| Kampagnen bearbeiten | `edit_campaigns` |
| Kampagnen archivieren | `archive_campaigns` |
| Canvase anzeigen | `view_canvases` |
| Canvase bearbeiten | `edit_canvases` |
| Canvase archivieren | `archive_canvases` |
| Frequency-Capping-Regeln anzeigen | `view_frequency_caps` |
| Frequency-Capping-Regeln bearbeiten | `edit_frequency_caps` |
| Nachrichtenpriorisierung anzeigen | `view_message_prioritization` |
| Nachrichtenpriorisierung bearbeiten | `edit_message_prioritization` |
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
| E-Mail-Templates archivieren | `archive_email_templates` |
| Webhook-Templates anzeigen | `view_webhook_templates` |
| Webhook-Templates bearbeiten | `edit_webhook_templates` |
| Webhook-Templates archivieren | `archive_webhook_templates` |
| E-Mail-Link-Templates anzeigen | `view_link_templates` |
| E-Mail-Link-Templates bearbeiten | `edit_link_templates` |
| Mediathek-Assets anzeigen | `view_media_library_assets` |
| Standorte anzeigen | `view_locations` |
| Standorte bearbeiten | `edit_locations` |
| Standorte archivieren | `archive_locations` |
| Aktionscodes anzeigen | `view_promotion_codes` |
| Aktionscodes bearbeiten | `edit_promotion_codes` |
| Aktionscodes exportieren | `export_promotion_codes` |
| Präferenzzentren anzeigen | `view_preference_centers` |
| Präferenzzentren bearbeiten | `edit_preference_centers` |
| Berichte anzeigen | `view_reports` |
| Berichte erstellen | `create_reports` |
| Berichte bearbeiten | `edit_reports` |
| Banner-Templates anzeigen | `view_banner_templates` |
| Mehrsprachige Einstellungen anzeigen | `view_multi_language_settings` |
| Operator verwenden | `use_operator` |
| Decisioning-Studio-Agenten anzeigen | `view_decisioning_studio_agents` |
| Decisioning-Studio-Konversions-Event anzeigen | `view_decisioning_studio_conversion_event` |
| Kampagnen starten | `launch_campaigns` |
| Canvase starten | `launch_canvases` |
| Dashboard-Nutzer:innen bearbeiten | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Abteilungsstrings

| Wie in der UI angezeigt | SCIM-API-String |
| --- | --- |
| Agentur / Drittanbieter | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finanzen | `finance` |
| Marketing / Redaktion | `marketing` |
| Produktmanagement | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }