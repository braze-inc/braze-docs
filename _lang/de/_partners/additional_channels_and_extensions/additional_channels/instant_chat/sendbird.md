---
nav_title: Sendbird
article_title: Sendbird
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Sendbird, einer führenden Lösung für In-App Messaging, die es Nutzern:in erlaubt, In-App-Nachrichten auf der Sendbird-Plattform zu empfangen."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications bietet Marketern und Produktmanagern einen leistungsstarken neuen Kanal zur Kommunikation mit ihren Kunden in der App mit persistenten, interaktiven Einweg-Nachrichten. Diese Nachrichten können für jede Art von Kommunikation verwendet werden und werden am häufigsten für Werbe- und Transaktionszwecke eingesetzt.

_Diese Integration wird von Sendbird gepflegt._

## Über die Integration

Die Integration von Braze und Sendbird lässt Nutzer:innen von Braze zu:
* Nutzen Sie die Segmentierungs- und Triggerfunktionen von Braze, um personalisierte In-App-Benachrichtigungen zu initiieren.
* Erstellen Sie auf der Sendbird Notifications Plattform maßgeschneiderte In-App-Benachrichtigungen, die dann innerhalb der App-Umgebung zugestellt werden und das Engagement der Nutzer:innen erhöhen.

Durch die Nutzung der gemeinsamen Fähigkeiten von Braze und Sendbird Notifications können Unternehmen das Customer-Engagement erhöhen und die Konversionsrate durch effektive In-App-Benachrichtigungsstrategien steigern.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sendbird-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Sendbird-Konto. |
| Sendbird UIKit | Sie müssen das Sendbird UIKit in Ihrer [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) oder [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit) App installiert haben. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

![]({% image_buster /assets/img/sendbird/use-cases.png %})

Die Integration von Braze und Sendbird Notifications bietet eine Reihe von Anwendungsfällen, um das Customer-Engagement zu steigern und ein außergewöhnliches Nutzer:innen-Erlebnis zuzustellen:

- **Marketing**: Verbessern Sie zielgerichtete Kampagnen mit personalisierten Aktionen und Empfehlungen, die auf die Vorlieben der Nutzer:innen zugeschnitten sind, wie z.B. exklusive Rabatte auf der Grundlage des Verlaufs des Surfens oder früherer Einkäufe.
- **Transaktionen**: Verbessern Sie die Kommunikation mit Ihren Kund:in durch Realtime Updates zu Bestellungen, Lieferungen, Rechnungen und Zahlungen, einschließlich Benachrichtigungen über Bestellstatus, Versanddetails und geschätzte Zustellungszeiten.

## Integration

### Schritt 1: Erstellen Sie eine Template für Benachrichtigungen

[Sendbird Templates](https://sendbird.com/docs/notifications/v1/templates) erlauben es Ihnen, personalisierte In-App-Benachrichtigungen zu versenden, indem Sie mehrere Templates für jeden Kanal erstellen und verwenden. Templates können auf dem Sendbird Dashboard erstellt und angepasst werden, ohne dass Sie Code schreiben müssen.

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Schritt 2: Einrichten der Braze-Integration im Sendbird-Dashboard

Wählen Sie im **Sendbird Dashboard** Ihre Anwendung aus, navigieren Sie zu **Benachrichtigungen > Integrationen** und klicken Sie unter dem Abschnitt **Braze** auf **Hinzufügen**. Hier benötigen Sie Ihren Braze REST API-Schlüssel und den Braze REST-Endpunkt.

Sobald Sie alle Felder ausgefüllt haben, klicken Sie auf **Speichern**, um die Integration abzuschließen und auf die Endpunkte der Integration und das API-Token zuzugreifen.

### Schritt 3: Sendbird Notification Builder installieren

Als nächstes müssen Sie [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji) installieren. Mit dieser Google Chrome-Erweiterung können Sie angepasste Benachrichtigungen über Sendbird an das Braze-Dashboard senden.

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Fügen Sie die Zugangsdaten von Sendbird zur Erweiterung hinzu

Sobald die Erweiterung installiert ist, klicken Sie auf das Sendbird-Symbol in der Symbolleiste Ihres Browsers und wählen Sie **Einstellungen**. Geben Sie hier Ihre App ID und Ihr API Token aus dem **Sendbird Notification Builder** an.

### Schritt 4: Abbildung der Sendbird Nutzer:innen ID auf die Braze Nutzer:innen ID

Eine Sendbird ID muss als [angepasstes Attribut]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) zu einem Braze Nutzerprofil hinzugefügt werden, damit die Integration genutzt werden kann. Sie können Nutzerprofile über CSV-Dateien von der Seite [Nutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) hochladen und aktualisieren. Alternativ können Sie auch die Braze Nutzer:innen ID als Sendbird Nutzer:innen verwenden.

### Schritt 5: Richten Sie Ihr Webhook Template ein

Gehen Sie in Braze unter **Templates und Medien** zu **Webhook-Vorlagen** und wählen Sie die **Sendbird Webhook-Vorlage**. Beachten Sie, dass dieses Template nur verfügbar ist, wenn Sie die Sendbird Notification Builder Erweiterung installiert haben.

{% raw %}
1. Geben Sie einen Template-Namen an und fügen Sie Teams und Tags nach Bedarf hinzu.
2. Kopieren Sie einen Realtime- oder Batch-Endpunkt aus dem Sendbird Dashboard in die **Webhook-URL**.
3. Klicken Sie im Feld **Empfänger** auf das Symbol <i class="fas fa-plus"></i> und fügen Sie das Attribut des Nutzers ein, das der Nutzer:innen-ID von Sendbird zugeordnet ist.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` wenn Sie ein angepasstes Attribut `sendbird_id` als Sendbird Nutzer:innen ID verwenden.
    - `{{ '{{' }}${user_id}}}` wenn Sie die Braze Nutzer:innen ID als Sendbird Nutzer:innen ID verwenden.
4. Ersetzen Sie auf dem Tab **Einstellungen** `SENDBIRD_API_TOKEN` durch das Token für die Benachrichtigungs-APIs aus dem Sendbird Dashboard.
5. Speichern Sie die Vorlage.
{% endraw %}

## Verwendung dieser Integration

### Kampagnen

1. Klicken Sie im Braze-Dashboard auf der Seite **Kampagnen** auf **Kampagne erstellen** > **Webhook**.
2. Wählen Sie das Webhook Template aus, das Sie oben erstellt haben. Es wird dringend empfohlen, den Endpunkt Batch für Kampagnen zu verwenden.
3. Passen Sie das Template an, indem Sie seine Variablen auf dem Tab **Verfassen** bearbeiten.

### Canvas

1. Fügen Sie aus einem neuen oder bestehenden Canvas eine Komponente **Nachricht** hinzu. 
2. Öffnen Sie die Komponente und wählen Sie **Webhook** aus den **Messaging-Kanälen**.
3. Wählen Sie das Webhook Template aus, das Sie oben erstellt haben. Es wird dringend empfohlen, den Realtime Endpunkt für Canvase zu verwenden.
4. Passen Sie das Template an, indem Sie seine Variablen auf dem Tab **Verfassen** bearbeiten.

## Anpassung

### Tracking der Zustellung und des Status der Öffnung

Um die Zustellung und den Öffnungsstatus der Benachrichtigungen in die Konversions-Metrik einer Kampagne zu integrieren, fügen Sie ein angepasstes Event auf dem Braze-Dashboard hinzu.

1. Gehen Sie auf dem Braze-Dashboard zu **Einstellungen > Einstellungen verwalten > Angepasste Events**, und klicken Sie auf **\+ Angepasstes Event hinzufügen**.
2. Nachdem Sie ein angepasstes Event erstellt haben, klicken Sie auf **Eigenschaften verwalten**, fügen eine Eigenschaft namens "Status" hinzu und wählen als Eigenschaftstyp "String".
3. Wenn Sie eine Benachrichtigung in Kampagnen oder Canvase verfassen, geben Sie den Namen des angepassten Events in das Feld **Event Name** ein.

Dieses angepasste Event wird für jede Benachrichtigung zweimal ausgelöst, wenn eine Nachricht gesendet wird und wenn ein Nutzer:innen die Nachricht öffnet.
- Wenn eine Nachricht gesendet wird, wird ein angepasstes Event mit dem Status `SENT` ausgelöst.
- Wenn eine Nachricht gelesen wird, wird ein angepasstes Event mit dem Status `READ` getriggert.


