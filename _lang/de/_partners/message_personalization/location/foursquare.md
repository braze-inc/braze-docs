---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Foursquare, einer Plattform für Standortdaten, die das Triggern von Ereignissen in Echtzeit auf der Grundlage des Standorts ermöglicht."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) ist eine Plattform für Standortdaten, die das Targeting von Standortdaten in Ihren Kampagnen ermöglicht. Verwenden Sie das Pilgrim SDK von Foursquare für iOS- und Android-Apps, um Ereignisse in Realtime auf der Grundlage des Standorts zu triggern. So können Sie die leistungsstarken Geo-Targeting-Funktionen von Foursquare nutzen, um relevante, personalisierte Nachrichten mit Braze zu versenden.

_Diese Integration wird von Foursquare gepflegt._

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Foursquare Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein Foursquare-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Workspace und App IDs | Die Workspace- und App-IDs von Braze finden Sie in der [Entwicklungskonsole]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Um die beiden Plattformen zu integrieren, müssen Sie die beiden SDKs integrieren und die passenden Nutzer:innen-Felder abbilden. Nach der Integration des Pilgrim SDK erhalten Sie Standort-Ereignisse auf dem Gerät oder an einen Webhook. 

### Schritt 1: Abbildung der Nutzer:in-Felder

Um die Felder zwischen den beiden SDKs korrekt abzubilden, setzen Sie in beiden Systemen dieselbe Nutzer:in ID mit der [Methode`changeUser` ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) im Braze SDK und der Methode `setUserId` von [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) im Pilgrim SDK.

### Schritt 2: Pilgrim-Konsole konfigurieren
![Ein Bild der Pilgrim-Konsole, die nach der Gruppen-ID, der Android App ID und der iOS App ID fragt.][2]{: style="float:right;max-width:40%;margin-left:15px;"}

Suchen Sie die Workspace- und App IDs in der Braze Entwickler:in-Konsole. Als nächstes geben Sie Ihren Braze REST API-Schlüssel und Ihre App IDs in der Foursquare Pilgrim-Konsole ein.

Sobald Sie die Pilgrim-Konsole konfiguriert haben, zeichnet das Pilgrim SDK Standort-Events auf und leitet sie an Braze weiter, was ein Retargeting und eine Segmentierung qualifizierter Kund:in zulässig macht. Weitere Informationen finden Sie auf der [Entwickler:in-Seite von Foursquare](https://developer.foursquare.com/).

{% alert important %}
Das Pilgrim SDK setzt voraus, dass Sie die Standortdienste aktivieren.
{% endalert %}

## Triggern von Nachrichten

Sobald die Integration eingerichtet ist, können Sie eine Kampagne oder ein Canvas einrichten, das auf Standort-Ereignisse reagiert, die vom Pilgrim SDK generiert werden. Diese Integration ist ideal für Messaging in Realtime, direkt nachdem Nutzer:innen einen Ort von Interesse betreten haben, oder für eine verzögerte Nachkommunikation, nachdem sie ihn verlassen haben, wie z.B. eine Danksagung oder eine Erinnerung.

So senden Sie eine Kampagne, die Nachrichten auf der Grundlage eines bestimmten Standorts versendet:
- Erstellen Sie eine Braze-Kampagne oder ein Braze-Canvas, das mit **aktionsbasierter Zustellung** versendet wird.
- Verwenden Sie für Ihren Trigger ein angepasstes Event von `arrival` mit einem Filter für die Event-Eigenschaften von `locationType`, wie im folgenden Screenshot gezeigt.

![Eine aktionsbasierte Kampagne im Schritt der Zustellung, bei der "Ankunft" als Option "angepasstes Event durchführen" ausgewählt wurde, wobei "locationType" gleich "home" ist.]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Retargeting

Um Ihre Nutzer:innen erneut zu retargeten, verwenden Sie das Pilgrim SDK, um ein angepasstes Attribut `last_location` auf den Nutzerprofilen Ihrer Nutzer:innen zu setzen. Sie können dann den `matches regex` Vergleich verwenden, um Nutzer:innen zu retargeten, die einen bestimmten Standort in der realen Welt aufgesucht haben, z.B. alle Nutzer:innen zu segmentieren, die kürzlich in einer Pizzeria waren.

![Eine aktionsbasierte Kampagne im Schritt Zielgruppe zusammenstellen, bei der "last_location" gleich "Pizza Place" ist.]({% image_buster /assets/img_archive/last-location-segment.png %})

Sie können in Braze auch Nutzer:innen segmentieren, die in einem bestimmten Zeitfenster eine bestimmte Art von Veranstaltungsort auf der Grundlage von Foursquare `primaryCategoryId` besucht haben. Um diesen Datenpunkt für Ihre Retargeting-Anwendungsfälle zu nutzen, protokollieren Sie `primaryCategoryId` als Event-Eigenschaft während Ihrer Segmentierung der Zielgruppe. Um die Nutzer:innen und Eigenschaften zu identifizieren, die von der Foursquare API und dem Pilgrim SDK verwendet werden, besuchen Sie die [Entwickler:in von Foursquare](https://developer.foursquare.com/).


[1]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[2]: {% image_buster /assets/img_archive/pilgrim-dev-console.png %}