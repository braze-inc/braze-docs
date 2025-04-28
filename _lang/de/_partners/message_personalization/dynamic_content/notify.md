---
nav_title: Benachrichtigen Sie
article_title: Benachrichtigen Sie
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Notify, einer Realtime Omnichannel-Personalisierungslösung, die Personalisierung über den gesamten Kundenlebenszyklus bietet."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Benachrichtigen Sie

> [Notify](https://fr.notify-group.com/) ist eine KI-gesteuerte Softwarelösung, die sich nahtlos in Management-Tools für Kundenbeziehungen integrieren lässt, um Marketing-Strategien zu verbessern und das Engagement über mehrere Kanäle hinweg zu erleichtern.

Die Integration von Braze und Notify ermöglicht es Marketern, das Engagement über verschiedene Plattformen hinweg effektiv zu fördern. Anstatt sich auf herkömmliche Marketing-Methoden zu verlassen, kann eine durch die Braze API ausgelöste Kampagne die Möglichkeiten von Notify nutzen, um personalisiertes Messaging über mehrere Kanäle zuzustellen, einschließlich E-Mail, SMS, Push-Benachrichtigungen und mehr.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.export.segment` und `campaigns.trigger.send`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| CNAME-Konfiguration | Für das Tracking-Pixel, das in der E-Mail für Notify verwendet wird, um das Engagement der Nutzer:innen beim Messaging zu verfolgen, muss eine Subdomain erstellt werden, um das Modell weiter zu informieren. Geben Sie die URL der Subdomain nach ihrer Erstellung an Notify weiter. |
| Datenbank Opt-in Export | Senden Sie die Kampagnen- und Kaufdaten des vergangenen Jahres (12 Monate) an Notify. ​Dieser Export wird verwendet, um das Notify Vorhersagemodell zu trainieren. <br><br> **Felder:** <br><br> **E-Mail:** Ein SHA256-Hash der E-Mail, konvertiert in Kleinbuchstaben und ohne führende oder nachfolgende Leerzeichen.<br><br>**Segmente:** Die Segmentinformationen, die den Grad der Aktivität (aktiv oder inaktiv) definieren.<br><br>**Untersegmente:** Jede andere relevante Information, wie z.B. die Höhe der Kaufaktivität.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Kampagne erstellen

Erstellen Sie eine [API-getriggerte Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery) in Braze. Dann teilen Sie die Kampagne `api_identifier` mit Notify.

### Schritt 2: Erstellen Sie Ihr Segment in Braze

Als nächstes erstellen Sie das Segment der Nutzer:innen, die Sie mit der in [Schritt 1](#step-1-create-your-campaign) erstellten Kampagne ansprechen möchten. Dann teilen Sie die ID des Segments mit Notify.

### Schritt 3: Holen Sie Ihr Segment

Dann exportiert Notify die Nutzer:innen des Segments, das der Kampagne zugeordnet ist.

### Schritt 4: Notify triggert die Kampagne

Über den Endpunkt `/campaigns/trigger/send` triggert die KI von Notify die in [Schritt 1](#step-1-create-your-campaign) erstellte Kampagne von Braze, um sie zu dem Zeitpunkt an die Nutzer:innen zu senden, zu dem sie sich am ehesten engagieren würden.
