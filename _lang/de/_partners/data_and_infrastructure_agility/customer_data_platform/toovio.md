---
nav_title: Toovio
article_title: Toovio
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Toovio, einem Data-as-a-Service-Unternehmen, das Ihnen hilft, Ihre verwertbaren Daten zu entdecken und die wichtigsten Elemente zu nutzen, um auf der Grundlage vordefinierter Ziele zusätzliche Ergebnisse zu erzielen."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) ist ein auf künstlicher Intelligenz basierendes Data-as-a-Service-Unternehmen, das Ihnen hilft, Ihre verwertbaren Daten zu entdecken und die wichtigsten Elemente zu nutzen, um auf der Grundlage vordefinierter Ziele zusätzliche Ergebnisse zu erzielen.

Die Partnerschaft zwischen Braze und Toovio ermöglicht die Auslösung von Nachrichten nahezu in Echtzeit, die Bereitstellung von Tools zur Steigerung der Leistung und den Zugriff auf die fortschrittlichen Tools von Toovio zur Messung von Kampagnen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Toovio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Toovio-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Lötende Ströme | Mit Braze Currents können Braze-Clients Ereignis- oder Verhaltensdaten an einen Braze-Datenpartner (AWS S3, Google Cloud Storage oder Microsoft Azure Blob Storage) zur Verarbeitung außerhalb der Braze-Plattform streamen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Mit der folgenden Integration kann Toovio Auslöser generieren, die auf bestimmte Kunden abzielen und nahezu in Echtzeit kommunizieren. Von Toovio festgelegte Auslöser werden über den [Endpunkt][3] Braze [`/users/track` an Braze übermittelt.][3]

### Schritt 1: Datenpartner definieren

Ein Ablageort für den Currents-Feed muss mit Toovio geteilt werden. Dies ermöglicht Toovio den Zugriff und die Verarbeitung von Benutzerereignissen und Verhaltensdaten.

### Schritt 2: Eine ausgelöste Kampagne einrichten

Erstellen Sie eine [durch die Braze-API ausgelöste Kampagne][4] auf der Grundlage der Kundenereignisse, auf die Toovio abzielen wird. Außerdem sollten Sie die Zielbenutzerattribute und -werte definieren, die die Kampagne auslösen sollen.

### Schritt 3: Richten Sie Ihr Toovio-Konto ein

Kontaktieren Sie Toovio unter [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) mit dem Betreff "New Customer Request", um ein Konto einzurichten. Toovio arbeitet mit Kunden zusammen, um Auslöser und zugrunde liegende Modelle einzurichten.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/
[2]: {{site.baseurl}}/api/api_key/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
