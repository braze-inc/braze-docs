---
nav_title: loplat
article_title: loplat
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und loplat, einer Offline-Plattform für standortbasiertes Marketing, die es Ihnen erlaubt, Kampagnen im Bereich Proximity Marketing durchzuführen, indem Sie den Standortkontext hinzufügen."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat][1] ist die führende Offline-Plattform für Standorte. Nutzen Sie das loplat SDK, um die Besucherzahlen Ihres Shops intelligent zu erhöhen und Marketing Kampagnen durchzuführen, die zum Kauf im Laden anregen. Sie können die Performance des Shops durch eine Analyse der Besucherzahlen nach Abschluss der Kampagne messen.

_Diese Integration wird von Loplat gepflegt._

## Über die Integration

Die Integration von Braze und loplat erlaubt es Ihnen, die Standortdienste von loplat (POI speichern und Geofence anpassen) zu nutzen, um kontextuelle Marketing-Kampagnen auszulösen und angepasste Events mit Offline-Segmentierung zu erstellen. Wenn Nutzer:innen den von Ihnen in loplat X festgelegten Targeting-Standort besuchen, werden die Kampagnen- und Standortinformationen sofort an Braze gesendet.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| loplat X Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein loplat X-Konto.<br><br>Mailen Sie an [support@loplat.com][3], um ein loplat X-Konto anzufordern. |
| loplat SDK | loplat SDK erkennt die Besuche von Nutzer:innen in Geschäften, verarbeitet Standort-Ereignisse und unterscheidet, ob Nutzer:innen an einem Ort bleiben oder umziehen. Sie können loplat SDK verwenden, um die Besucherzahlen Ihres Shops zu analysieren, Push Nachrichten zu senden, wenn Nutzer:innen Ihren Shop betreten, usw.<br><br>Beachten Sie, dass das SDK nur für Android und iOS verfügbar ist. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die von loplat zur Verfügung gestellten Informationen über angepasste Event Standorte können in Ihren Kampagnen verwendet werden, um Anwendungsfälle wie diese zu realisieren:

- [Alarm für Duty-Free-Aktionen][2]
    - Senden Sie den Nutzern:innen, die sich in der Nähe der Boarding-Gates am Flughafen befinden, Rabattcoupons für Duty-Free-Shops.
- Push für Standorte von Ladestationen für Elektrofahrzeuge (EV)
    - Legen Sie Geoofences um Ladestationen fest und benachrichtigen Sie die Nutzer:innen, wenn sie sich in der Nähe der Station befinden und ermutigen Sie sie zum Laden.

## Integration

### Schritt 1: Integration der SDKs

Integrieren Sie das loplat SDK und das Braze SDK in Ihre App anhand der Schritte, die in der Dokumentation zur [loplat-Braze-Integration][4] beschrieben sind.

### Schritt 2: Synchronisieren Sie die Dashboards von Braze und loplat X und erstellen Sie eine Kampagne

Erstellen Sie einen neuen API-Schlüssel auf dem Braze-Dashboard. Kopieren Sie den API-Schlüssel und fügen Sie ihn unter **Einstellungen > API-Einstellungen** auf dem Dashboard von loplat X ein. Weitere Einzelheiten finden Sie im [Nutzer:innen-Handbuch von loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25).

#### API-getriggerte Zustellung

1. Erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas, das mit **API-getriggerter Zustellung** versendet, und kopieren Sie die ID der Kampagne.
2. Starten Sie die Kampagne in Braze, nachdem Sie alle Schritte abgeschlossen haben.
3. Gehen Sie zu loplat X und erstellen Sie eine Kampagne gemäß den Anweisungen im [Handbuch für Nutzer:innen von loplat X.][5]
4. Fügen Sie die ID der Braze-Kampagne unter den **Einstellungen für die Nachrichten der Kampagne** ein, und starten Sie die Kampagne.

![][7]

#### Aktionsbasierte Zustellung

Mit der Integration können Sie Standortbedingungen anwenden, indem Sie Geofence-Informationen, die Region, den Markennamen oder den Namen des Shops senden. Außerdem können Sie Segmente hinzufügen oder die Konversion mit dem angepassten Event zuordnen, das Sie erstellt haben.
1. Erstellen Sie eine loplat X Kampagne gemäß den Anweisungen im [Handbuch für Nutzer:innen von loplat X.][6]
2. Fügen Sie ein angepasstes Event unter den **Einstellungen für Messaging-Kampagnen** hinzu und starten Sie die Kampagne.
3. Rufen Sie das Braze-Dashboard auf und erstellen Sie eine Kampagne oder ein Canvas, das mit **aktionsbasierter Zustellung** versendet wird.
4. Wählen Sie das angepasste Event aus, das Sie in loplat X erstellt haben, um eine Standort triggernde Aktion festzulegen.

![][8]


[1]: https://www.loplat.com/
[2]: https://www.loplat.com/loplat-x#usecase
[3]: mailto:support@loplat.com
[4]: https://developers.loplat.com/braze/
[5]: https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb
[6]: https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598
[7]: {% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %}
[8]: {% image_buster /assets/img/loplat/loplat_action_based_delivery.png %}