---
nav_title: Sendbird
article_title: Sendbird
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Sendbird, einer führenden In-App-Messaging-Lösung, die es Benutzern ermöglicht, In-App-Benachrichtigungen auf der Sendbird-Plattform zu empfangen."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird][4] Notifications bietet Marketingfachleuten und Produktmanagern einen leistungsstarken neuen Kanal für die In-App-Kommunikation mit ihren Kunden in Form von dauerhaften, interaktiven One-Way-Nachrichten. Diese Nachrichten können für jede Art von Kommunikation verwendet werden und werden am häufigsten für Werbe- und Transaktionszwecke eingesetzt.

Die Integration von Braze und Sendbird ermöglicht es Braze-Benutzern:
* Nutzen Sie die Segmentierungs- und Auslösungsfunktionen von Braze, um personalisierte In-App-Benachrichtigungen auszulösen.
* Erstellen Sie maßgeschneiderte In-App-Benachrichtigungen auf der Sendbird Notifications Plattform, die dann innerhalb der App-Umgebung ausgeliefert werden und so das Engagement der Nutzer erhöhen.

Durch die Nutzung der gemeinsamen Fähigkeiten von Braze und Sendbird Notifications können Unternehmen die Kundenbindung erhöhen und durch effektive In-App-Benachrichtigungsstrategien höhere Konversionsraten erzielen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sendbird-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Sendbird-Konto. |
| Sendbird UIKit | Sie müssen das Sendbird UIKit in Ihrer [iOS-][2] oder [Android-App][3] installiert haben. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

![][13]

Die Integration von Braze und Sendbird Notifications bietet eine Reihe von Anwendungsfällen, um das Kundenengagement zu steigern und eine außergewöhnliche Benutzererfahrung zu bieten:

- **Marketing**: Verbessern Sie gezielte Kampagnen mit personalisierten Angeboten und Empfehlungen, die auf die Vorlieben der Nutzer zugeschnitten sind, wie z. B. exklusive Rabatte auf der Grundlage des Surfverhaltens oder früherer Einkäufe.
- **Transaktionsbezogen**: Verbessern Sie die Kundenkommunikation durch Echtzeit-Updates zu Bestellungen, Lieferungen, Rechnungen und Zahlungen, einschließlich Benachrichtigungen über den Bestellstatus, Versanddetails und voraussichtliche Lieferzeiten.

## Integration

### Schritt 1: Eine Benachrichtigungsvorlage erstellen

Mit [Sendbird-Vorlagen][7] können Sie personalisierte In-App-Benachrichtigungen versenden, indem Sie mehrere Vorlagen für jeden Kanal erstellen und verwenden. Vorlagen können im Sendbird Dashboard erstellt und angepasst werden, ohne dass Sie Code schreiben müssen.

![][10]

### Schritt 2: Einrichten der Braze-Integration im Sendbird-Dashboard

Wählen Sie im **Sendbird Dashboard** Ihre Anwendung aus, navigieren Sie zu **Benachrichtigungen > Integrationen** und klicken Sie unter dem Abschnitt **Braze** auf **Hinzufügen**. Hier benötigen Sie Ihren Braze REST API-Schlüssel und den Braze REST-Endpunkt.

Sobald Sie alle Felder ausgefüllt haben, klicken Sie auf **Speichern**, um die Integration abzuschließen und auf die Integrationsendpunkte und das API-Token zuzugreifen.

### Schritt 3: Sendbird Notification Builder installieren

Als nächstes müssen Sie [Sendbird Notification Builder][6] installieren. Mit dieser Google Chrome-Erweiterung können Sie über Sendbird auf dem Braze Dashboard individuelle Benachrichtigungen versenden.

![][12]

#### Fügen Sie die Sendbird-Anmeldeinformationen zur Erweiterung hinzu

Sobald die Erweiterung installiert ist, klicken Sie auf das Sendbird-Symbol in der Symbolleiste Ihres Browsers und wählen Sie **Einstellungen**. Geben Sie hier Ihre App-ID und Ihr API-Token an, die Sie im **Sendbird Notification Builder** gefunden haben.

### Schritt 4: Sendbird-Benutzer-ID der Braze-Benutzer-ID zuordnen

Eine Sendbird-Benutzer-ID muss als [benutzerdefiniertes Attribut][5] zu einem Braze-Benutzerprofil hinzugefügt werden, damit die Integration genutzt werden kann. Sie können Benutzerprofile über CSV-Dateien von der Seite [Benutzerimport][8] hochladen und aktualisieren. Alternativ können Sie auch die Braze-Benutzer-ID als Sendbird-Benutzer-ID verwenden.

### Schritt 5: Einrichten Ihrer Webhook-Vorlage

Gehen Sie in Braze unter **Vorlagen & Medien** zu **Webhook-Vorlagen** und wählen Sie die **Sendbird Webhook-Vorlage**. Beachten Sie, dass diese Vorlage nur verfügbar ist, wenn Sie die Sendbird Notification Builder Erweiterung installiert haben.

{% raw %}
1. Geben Sie einen Vorlagennamen an und fügen Sie bei Bedarf Teams und Tags hinzu.
2. Kopieren Sie einen Echtzeit- oder Batch-Endpunkt aus dem Sendbird-Dashboard in die **Webhook-URL**.
3. Klicken Sie im Feld **Empfänger** auf das Symbol <i class="fas fa-plus"></i> und fügen Sie das Benutzerattribut ein, das der Sendbird-Benutzer-ID zugeordnet ist.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` wenn Sie ein benutzerdefiniertes Attribut `sendbird_id` als Sendbird-Benutzer-ID verwenden.
    - `{{ '{{' }}${user_id}}}` wenn Sie die Braze-Benutzer-ID als Sendbird-Benutzer-ID verwenden.
4. Ersetzen Sie auf der Registerkarte **Einstellungen** `SENDBIRD_API_TOKEN` durch das Benachrichtigungs-API-Token aus dem Sendbird-Dashboard.
5. Speichern Sie die Vorlage.
{% endraw %}

## Mit dieser Integration

### Kampagnen

1. Klicken Sie im Braze Dashboard auf der Seite **Kampagnen** auf **Kampagne erstellen** > **Webhook**.
2. Wählen Sie die Webhook-Vorlage, die Sie oben erstellt haben. Es wird dringend empfohlen, den Batch-Endpunkt für Kampagnen zu verwenden.
3. Passen Sie die Vorlage an, indem Sie ihre Variablen auf der Registerkarte **Verfassen** bearbeiten.

### Canvas

1. Fügen Sie aus einem neuen oder bestehenden Canvas eine **Nachrichtenkomponente** hinzu. 
2. Öffnen Sie die Komponente und wählen Sie **Webhook** aus den **Messaging-Kanälen**.
3. Wählen Sie die Webhook-Vorlage, die Sie oben erstellt haben. Es wird dringend empfohlen, den Echtzeit-Endpunkt für Canvases zu verwenden.
4. Passen Sie die Vorlage an, indem Sie ihre Variablen auf der Registerkarte **Verfassen** bearbeiten.

## Anpassung

### Verfolgen Sie Lieferung und offenen Status

Um die Zustellung und den Öffnungsstatus der Benachrichtigungen in die Konversionsmetrik einer Kampagne zu integrieren, fügen Sie ein benutzerdefiniertes Ereignis auf dem Braze Dashboard hinzu.

1. Gehen Sie im Braze-Dashboard zu **Einstellungen > Einstellungen verwalten > Benutzerdefinierte Ereignisse**, und klicken Sie auf **\+ Benutzerdefiniertes Ereignis hinzufügen**.
2. Nachdem Sie ein benutzerdefiniertes Ereignis erstellt haben, klicken Sie auf **Eigenschaften verwalten**, fügen eine Eigenschaft namens "Status" hinzu und wählen "String" als Eigenschaftstyp.
3. Wenn Sie eine Benachrichtigung in Kampagnen oder Canvases verfassen, geben Sie den Namen des benutzerdefinierten Ereignisses in das Feld **Ereignisname** ein.

Dieses benutzerdefinierte Ereignis wird für jede Benachrichtigung zweimal ausgelöst: wenn eine Nachricht gesendet wird und wenn ein Benutzer die Nachricht öffnet.
- Wenn eine Nachricht gesendet wird, wird ein benutzerdefiniertes Ereignis mit dem Status `SENT` ausgelöst.
- Wenn eine Nachricht gelesen wird, wird ein benutzerdefiniertes Ereignis mit dem Status `READ` ausgelöst.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit
[3]: https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit
[4]: https://sendbird.com/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[6]: https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji
[7]: https://sendbird.com/docs/notifications/v1/templates
[8]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[10]: {% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %}
[11]: {% image_buster /assets/img/sendbird/sendbird-dashboard-integrations.png %}
[12]: {% image_buster /assets/img/sendbird/sendbird-notification-builder.png %}
[13]: {% image_buster /assets/img/sendbird/use-cases.png %}