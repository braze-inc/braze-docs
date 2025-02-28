---
nav_title: Airbyte
article_title: Airbyte
description: "Dieser Referenzartikel behandelt die Integration von Braze und Airbyte. Airbyte ist eine Open-Source-Datenintegrations-Engine, die Sie bei der Konsolidierung Ihrer Daten in Ihren Data Warehouses, Seen und Datenbanken unterstützt und Echtzeit-Ereignisse von Airbyte an Braze weiterleitet."
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/) ist eine Open-Source-Datenintegrations-Engine, die Sie bei der Konsolidierung Ihrer Daten in Ihren Data Warehouses, Seen und Datenbanken unterstützt.

Die Integration von Braze und Airbyte ermöglicht es Benutzern, eine Datenpipeline zu erstellen, um Braze-Daten zu sammeln und zu analysieren, indem alle Ihre Anwendungen und Datenbanken mit einem zentralen Warehouse verbunden werden. Nachdem die Daten im zentralen Warehouse gesammelt wurden, können Datenteams die Daten von Braze mit ihren bevorzugten Business Intelligence-Tools effektiv untersuchen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Airbyte Cloud-Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein [Airbyte Cloud-Konto](https://cloud.airbyte.io/workspaces). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

1. Navigieren Sie in Ihrem Airbyte Cloud-Konto zu **Quellen > + Neue Quelle > Einrichten der Quelle**.
2. Geben Sie "Braze" als Quellennamen ein und wählen Sie **Braze** aus der Quellen-Dropdown-Liste.
3. Geben Sie Ihre Endpunkt-URL, den Braze REST API-Schlüssel und das Startdatum an. Klicken Sie auf **Quelle einrichten**.

### Unterstützte Sync-Modi

Der Braze-Quellanschluss von Airbyte unterstützt die folgenden [Synchronisationsmodi](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):
- **Vollständige Aktualisierung | Überschreiben**: Synchronisieren Sie alle Datensätze der Quelle und ersetzen Sie die Daten im Ziel, indem Sie sie überschreiben.
- **Inkrementelle Synchronisierung | Anhängen**: Synchronisieren Sie neue Datensätze von der Quelle und fügen Sie sie dem Ziel hinzu, ohne Daten zu löschen.

### Unterstützte Streams

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
Die Ratengrenzen sind je nach Stream unterschiedlich. Weitere Informationen finden Sie in der [Tabelle der Tarifgrenzen](https://www.braze.com/docs/api/api_limits/#rate-limits-by-request-type).
{% endalert %}
