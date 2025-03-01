---
nav_title: Benachrichtigen Sie
article_title: Benachrichtigen Sie
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Notify, einer Omnichannel-Personalisierungslösung in Echtzeit, die Personalisierung über den gesamten Kundenlebenszyklus hinweg bietet."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Benachrichtigen Sie

> [Notify](https://notifyai.io/) ist eine KI-gesteuerte Softwarelösung, die sich nahtlos in Customer Relationship Management-Tools integrieren lässt, um Marketingstrategien zu verbessern und das Engagement über verschiedene Kanäle hinweg zu erleichtern.

Die Integration von Braze und Notify ermöglicht es Marketingfachleuten, das Engagement über verschiedene Plattformen hinweg effektiv zu steigern. Anstatt sich auf herkömmliche Marketingmethoden zu verlassen, kann eine durch die Braze API ausgelöste Kampagne die Funktionen von Notify nutzen, um personalisierte Nachrichten über mehrere Kanäle zu versenden, darunter E-Mail, SMS, Push-Benachrichtigungen und mehr.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Braze REST API Schlüssel  | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.export.segment` und `campaigns.trigger.send`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| CNAME-Konfiguration | Für das Tracking-Pixel, das in der E-Mail verwendet wird, muss eine Subdomain erstellt werden, damit Notify das Engagement des Benutzers für die Nachrichten verfolgen kann, um das Modell zu verbessern. Geben Sie die URL der Subdomain nach ihrer Erstellung an Notify weiter. |
| Datenbank Opt-in Export | Senden Sie die Kampagnen- und Kaufdaten des letzten Jahres (12 Monate) an Notify. ​Dieser Export wird verwendet, um das Vorhersagemodell von Notify zu trainieren. <br><br> **Felder:** <br><br> **E-Mail:** Ein SHA256-Hash der E-Mail, konvertiert in Kleinbuchstaben und ohne führende oder nachfolgende Leerzeichen.<br><br>**Segment:** Die Segmentinformationen, die den Grad der Aktivität (aktiv oder inaktiv) definieren.<br><br>**Untersegment:** Jede andere relevante Information, wie z.B. die Höhe der Kaufaktivität.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie Ihre Kampagne

Erstellen Sie eine [API-gesteuerte Kampagne](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery) in Braze. Dann teilen Sie die Kampagne `api_identifier` mit Notify.

### Schritt 2: Erstellen Sie Ihr Segment in Braze

Als nächstes erstellen Sie das Nutzersegment, das Sie mit der in [Schritt 1](#step-1-create-your-campaign) erstellten Kampagne ansprechen möchten. Dann teilen Sie die Segment-ID mit Notify.

### Schritt 3: Holen Sie Ihr Segment

Dann exportiert Notify die Benutzer in dem Segment, das der Kampagne zugeordnet ist.

### Schritt 4: Benachrichtigen löst die Kampagne aus

Über den Endpunkt `/campaigns/trigger/send` löst die KI von Notify die in [Schritt 1](#step-1-create-your-campaign) erstellte Braze-Kampagne aus, um sie zu dem Zeitpunkt an die Benutzer zu senden, zu dem sie sich am ehesten engagieren würden.