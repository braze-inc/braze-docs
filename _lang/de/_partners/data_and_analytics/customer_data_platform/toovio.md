---
nav_title: Toovio
article_title: Toovio
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Toovio, einem Unternehmen für Data-as-a-Service, das Ihnen hilft, Ihre verwertbaren Daten zu entdecken und die wichtigsten Elemente zu nutzen, um auf der Grundlage vordefinierter Ziele zusätzliche Ergebnisse zu erzielen."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) ist ein auf künstliche Intelligenz gestützter Data-as-a-Service-Anbieter, der Ihnen hilft, Ihre verwertbaren Daten zu entdecken und die wichtigsten Elemente zu nutzen, um auf der Grundlage vordefinierter Ziele zusätzliche Ergebnisse zu erzielen.

_Diese Integration wird von Toovio gepflegt._

## Über die Integration

Die Partnerschaft zwischen Braze und Toovio ermöglicht das Triggern von Nachrichten nahezu in Echtzeit, die Bereitstellung von Tools zur Steigerung der Performance und den Zugriff auf die fortschrittlichen Tools von Toovio zur Messung von Kampagnen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Toovio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Toovio-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Currents | Braze-Currents ermöglicht es Braze-Clients, Ereignis- oder Verhaltensdaten zu einem Braze-Datenpartner (AWS S3, Google Cloud Storage oder Microsoft Azure Blob Storage) zu streamen, um sie außerhalb der Braze-Plattform zu verarbeiten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die folgende Integration erlaubt es Toovio, Trigger zu generieren, die auf bestimmte Kund:in abzielen und nahezu in Realtime kommunizieren. Von Toovio ermittelte Trigger werden über den [`/users/track`Braze Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) an Braze übermittelt.

### Schritt 1: Daten Partner definieren

Ein Standort für den Currents-Feed muss mit Toovio geteilt werden; dies erlaubt Toovio den Zugriff und die Verarbeitung von Nutzer:innen-Ereignis- und Verhaltensdaten.

### Schritt 2: Eine getriggerte Kampagne einrichten

Erstellen Sie eine über die Braze [API getriggerte Kampagne]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) auf der Grundlage der Kund:in-Events, die Toovio als Targeting verwenden wird. Zusätzlich sollten Targeting Attribute und Werte für Nutzer:innen definiert werden, die die Kampagne triggern sollen.

### Schritt 3: Richten Sie Ihr Toovio-Konto ein

Kontaktieren Sie Toovio unter [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) mit dem Betreff "Anfrage für neue Kund:in", um ein Konto einzurichten. Toovio arbeitet mit den Clients zusammen, um Trigger und die zugrunde liegenden Modelle einzurichten.


