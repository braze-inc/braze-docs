---
nav_title: loplat
article_title: loplat
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und loplat, einer Offline-Plattform für standortbasiertes Marketing, die es Ihnen ermöglicht, Proximity Marketing-Kampagnen durch Hinzufügen von Standortkontext durchzuführen."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat][1] ist die führende offline ortsbezogene Plattform. Nutzen Sie das loplat SDK, um die Besucherzahlen in Ihrem Geschäft intelligent zu erhöhen und Marketingkampagnen durchzuführen, die zum Kauf im Geschäft anregen. Nach Beendigung der Kampagne können Sie die Leistung des Geschäfts durch eine Analyse der Besucherzahlen messen.

Die Integration von Braze und loplat ermöglicht es Ihnen, die Standortdienste von loplat (POI speichern und benutzerdefinierte Geofence) zu nutzen, um geokontextbezogene Marketingkampagnen auszulösen und benutzerdefinierte Ereignisse mit Offline-Segmentierung zu erstellen. Wenn Nutzer den von Ihnen in loplat X festgelegten Zielort besuchen, werden die Kampagnen- und Standortinformationen sofort an Braze gesendet.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| loplat X Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein loplat X-Konto.<br><br>Senden Sie eine E-Mail an [support@loplat.com][3], um ein loplat X-Konto anzufordern. |
| loplat SDK | loplat SDK erkennt die Besuche von Nutzern in Geschäften, verarbeitet Standortereignisse und unterscheidet, ob Nutzer an einem Ort bleiben oder umziehen. Sie können das loplat SDK verwenden, um die Besucherzahlen Ihres Geschäfts zu analysieren, Push-Nachrichten zu senden, wenn Benutzer Ihr Geschäft betreten, usw.<br><br>Beachten Sie, dass das SDK nur für Android und iOS verfügbar ist. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die von loplat bereitgestellten benutzerdefinierten Informationen zum Veranstaltungsort können in Ihren Kampagnen verwendet werden, um z.B. folgende Zwecke zu erfüllen:

- [Duty-Free-Aktionsalarm][2]
    - Senden Sie Duty-Free-Shop-Rabattcoupons an die Benutzer, die sich in der Nähe der Boarding-Gates am Flughafen befinden.
- Standort für Ladestationen für Elektrofahrzeuge (EV) Push
    - Richten Sie Geofences um Ladestationen ein und benachrichtigen Sie die Nutzer, wenn sie sich in der Nähe der Station befinden, um sie zum Laden zu ermutigen.

## Integration

### Schritt 1: Integrieren Sie die SDKs

Integrieren Sie das loplat SDK und das Braze SDK in Ihre App anhand der in der [loplat-Braze-Integrationsdokumentation][4] beschriebenen Schritte.

### Schritt 2: Synchronisieren Sie die Dashboards von Braze und loplat X und erstellen Sie eine Kampagne

Erstellen Sie einen neuen API-Schlüssel im Braze Dashboard. Kopieren Sie den API-Schlüssel und fügen Sie ihn unter **Einstellungen > API-Einstellungen** im Dashboard von loplat X ein. Weitere Einzelheiten finden Sie im [Benutzerhandbuch zu loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25).

#### API-gesteuerte Lieferung

1. Erstellen Sie eine Braze-Kampagne oder ein Canvas, das mit **API-gesteuerter Zustellung** versendet, und kopieren Sie die Kampagnen-ID.
2. Starten Sie die Kampagne in Braze, nachdem Sie alle Schritte abgeschlossen haben.
3. Gehen Sie zu loplat X und erstellen Sie eine Kampagne gemäß den Anweisungen im [loplat X Benutzerhandbuch][5].
4. Fügen Sie die Braze-Kampagnen-ID unter den **Einstellungen für die Kampagnennachrichten** ein und starten Sie die Kampagne.

![][7]

#### Aktionsbasierte Lieferung

Mit der Integration können Sie Standortbedingungen anwenden, indem Sie Geofence-Informationen, die Region, den Markennamen oder den Namen des Geschäfts senden. Außerdem können Sie Segmente hinzufügen oder die Konvertierung mit dem von Ihnen erstellten benutzerdefinierten Ereignis zuweisen.
1. Erstellen Sie eine loplat X-Kampagne gemäß den Anweisungen im [loplat X-Benutzerhandbuch][6].
2. Fügen Sie ein benutzerdefiniertes Ereignis unter den **Einstellungen für Kampagnennachrichten** hinzu und starten Sie die Kampagne.
3. Gehen Sie zum Braze Dashboard und erstellen Sie eine Kampagne oder ein Canvas, das mit **Action-Based Delivery** versendet wird.
4. Wählen Sie das benutzerdefinierte Ereignis, das Sie in loplat X erstellt haben, um eine Aktion zum Auslösen des Standorts festzulegen.

![][8]

[1]: https://www.loplat.com/
[2]: https://www.loplat.com/loplat-x#usecase
[3]: mailto:support@loplat.com
[4]: https://developers.loplat.com/braze/
[5]: https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb
[6]: https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598
[7]: {% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %}
[8]: {% image_buster /assets/img/loplat/loplat_action_based_delivery.png %}