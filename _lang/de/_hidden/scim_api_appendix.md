---
nav_title: "SCIM-API-Objekte und Anhang"
article_title: SCIM-API-Objekte und Anhang
page_order: 8
page_type: reference
description: "Dieser Artikel erklärt die verschiedenen SCIM-API-Objekte und den Anhang."
hidden: true
permalink: "/scim_api_appendix/"
---

# SCIM-API-Objekte und Anhang

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
| `companyPermissions` | Optional | Array | Array von Berechtigungsstrings auf Unternehmensebene aus der Tabelle [Company permission strings](#company), in der das Vorhandensein des Strings dem Benutzer entspricht, der die entsprechende Berechtigung hat. |
| `roles` | Optional | Array | Array von [Rollenobjekten](#role-object). |
| `appGroup` | Erforderlich | Array | Array mit [Objekten für Arbeitsbereichsberechtigungen](#workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objekt Arbeitsbereich-Berechtigungen {#workspace-permission-object}

Ein gültiges Appgruppen-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupName`| Optional | String | Workspace-Name Wird verwendet, um anzugeben, für welchen Arbeitsbereich die in diesem Objekt enthaltenen Berechtigungen gelten. | 
| `appGroupId` | Erforderlich, wenn `appGroupName` fehlt | String | ID des Workspace als dessen alternative Bezeichnung |
| `appGroupPermissionSets` | Optional | Array | Array mit einem einzelnen [Objekt der Arbeitsbereichsberechtigungen](#workspace-permissions-set-object). |
| `appGroupPermissions` | Erforderlich | Array | Array von Berechtigungsstrings auf Arbeitsbereichsebene aus der Tabelle [der Arbeitsbereichsberechtigungsstrings](#workspace-strings), wobei das Vorhandensein des Strings bedeutet, dass der Benutzer die entsprechende Berechtigung für den angegebenen Arbeitsbereich hat. |
| `team` | Optional | Array | Array von [Team-Berechtigungsobjekten](#team-permissions-object). |
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
| `teamPermissions` | Erforderlich | Array | Array mit Berechtigungsstrings auf Teamebene aus der Tabelle [Teams Permission Strings](#team), in der das Vorhandensein des Strings bedeutet, dass der Benutzer die entsprechende Berechtigung für das angegebene Team hat. |
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
| Kann die Unternehmenseinstellungen verwalten | `manage_company_settings` |
| Kann Arbeitsbereiche hinzufügen/entfernen| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Arbeitsbereichsberechtigungsstrings {#workspace-strings}

| Berechtigungsname | SCIM API Zeichenfolge |
| --- | --- |
| Admin | `admin` |
| Zugang zu Kampagnen, Leinwänden, Karten, Segmenten, Mediathek | `basic_access` |
| Canvase genehmigen und ablehnen | `approve_deny_campaigns` |
| Kampagnen versenden, Leinwände | `send_campaigns_canvases` |
| Karten veröffentlichen | `publish_cards` |
| Segmente bearbeiten | `edit_segments` |
| Benutzerdaten exportieren | `export_user_data` |
| PII ansehen | `view_pii` |
| Benutzerprofile anzeigen PII-konform | `view_user_profile` |
| Dashboard-Benutzer verwalten | `manage_dashboard_users` |
| Assets der Mediathek verwalten | `manage_media_library` |
| Nutzungsdaten anzeigen | `view_usage_data` |
| Benutzerdaten importieren und aktualisieren | `import_update_user_data` |
| Rechnungsdetails anzeigen | `view_billing_details` |
| Dev-Konsole öffnen | `dev_console` |
| Content-Blöcke starten | `launch_content_blocks` |
| Externe Integrationen verwalten | `manage_external_integrations` |
| Apps verwalten | `manage_apps` |
| Teams verwalten | `manage_teams` |
| Ereignisse, Attribute und Einkäufe verwalten | `manage_events_attributes_purchases` |
| Tags verwalten | `manage_tags` |
| E-Mail-Einstellungen verwalten | `manage_email_settings` |
| Abonnementgruppen verwalten | `manage_subscription_groups` |
| Genehmigungseinstellungen verwalten | `manage_approval_settings` |
| Kataloge verwalten Dashboard Berechtigung | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Team-Berechtigungsstrings {#team}

| Berechtigungsname | SCIM API Zeichenfolge |
| --- | --- |
| Admin | `admin` |
| Zugang zu Kampagnen, Leinwänden, Karten, Segmenten, Mediathek | `basic_access` |
| Canvase genehmigen und ablehnen | `approve_deny_campaigns` |
| Kampagnen versenden, Leinwände | `send_campaigns_canvases` |
| Karten veröffentlichen | `publish_cards` |
| Segmente bearbeiten | `edit_segments` |
| Benutzerdaten exportieren | `export_user_data` |
| Benutzerprofil ansehen | `view_user_profile` |
| Dashboard-Benutzer verwalten | `manage_dashboard_users` |
| Assets der Mediathek verwalten | `manage_media_library` |
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
