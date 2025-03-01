---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Foursquare, einer Plattform für Standortdaten, die die Auslösung von Ereignissen in Echtzeit auf der Grundlage des Standorts ermöglicht."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) ist eine Plattform für Standortdaten, mit der Sie Ihre Braze-Kampagnen auf Standortdaten ausrichten können. Verwenden Sie das Pilgrim SDK von Foursquare für iOS- und Android-Apps, um Ereignisse in Echtzeit auf der Grundlage Ihres Standorts auszulösen. So können Sie die leistungsstarken Geo-Targeting-Funktionen von Foursquare nutzen, um mit Braze relevante, personalisierte Nachrichten zu versenden.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Foursquare-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein Foursquare-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Arbeitsbereich und App IDs | Den Braze-Arbeitsbereich und die App-IDs finden Sie in der [Entwicklerkonsole]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Um die beiden Plattformen zu integrieren, müssen Sie die beiden SDKs integrieren und die passenden Benutzerfelder zuordnen. Nachdem Sie das Pilgrim SDK integriert haben, erhalten Sie Standort-Ereignisse auf dem Gerät oder über einen Webhook. 

### Schritt 1: Felder der Benutzer-ID zuordnen

Um Felder zwischen den beiden SDKs korrekt zuzuordnen, setzen Sie in beiden Systemen dieselbe Benutzer-ID mit der [Methode`changeUser` ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) im Braze SDK und der Methode `setUserId` von [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) im Pilgrim SDK.

### Schritt 2: Pilgrim-Konsole konfigurieren
![Ein Bild der Pilgrim-Konsole, die nach der Gruppen-ID, der Android-App-ID und der iOS-App-ID fragt.][2]{: style="float:right;max-width:40%;margin-left:15px;"}

Suchen Sie den Arbeitsbereich und die App-IDs in der Braze-Entwicklerkonsole. Als nächstes geben Sie Ihren Braze REST API-Schlüssel und Ihre App-IDs in der Foursquare Pilgrim-Konsole ein.

Sobald Sie die Pilgrim-Konsole konfiguriert haben, zeichnet das Pilgrim-SDK Standortereignisse auf und leitet sie an Braze weiter, so dass Sie qualifizierte Kunden erneut ansprechen und segmentieren können. Weitere Informationen finden Sie auf der [Foursquare-Entwicklerseite](https://developer.foursquare.com/).

{% alert important %}
Das Pilgrim SDK erfordert, dass Sie die Standortdienste aktivieren.
{% endalert %}

## Auslösende Nachrichten

Sobald die Integration eingerichtet ist, können Sie eine Kampagne oder ein Canvas einrichten, die bzw. das auf die vom Pilgrim SDK generierten Standort-Ereignisse reagieren wird. Dieser Weg der Integration ist ideal für Echtzeit-Nachrichten direkt nach dem Betreten eines interessanten Ortes oder für eine verzögerte Folgekommunikation nach dem Verlassen des Ortes, wie z.B. ein Dankesschreiben oder eine Erinnerung.

Zum Versenden einer Kampagne, die Nachrichten auf der Grundlage eines bestimmten Standorts versendet:
- Erstellen Sie eine Braze-Kampagne oder ein Canvas, das mit **Action-Based Delivery** versendet wird.
- Verwenden Sie für Ihren Auslöser ein benutzerdefiniertes Ereignis von `arrival` mit einem Ereignis-Eigenschaftsfilter für `locationType`, wie im folgenden Screenshot gezeigt.

![Eine aktionsbasierte Kampagne im Zustellungsschritt, bei der "Ankunft" als Option "benutzerdefiniertes Ereignis durchführen" ausgewählt wurde, wobei "locationType" gleich "home" ist.]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Neuausrichtung

Um Ihre Benutzer erneut anzusprechen, verwenden Sie das Pilgrim SDK, um ein benutzerdefiniertes Attribut `last_location` in den Benutzerprofilen Ihrer Braze-Benutzer zu setzen. Sie können dann den `matches regex` Vergleich verwenden, um Nutzer erneut anzusprechen, die einen bestimmten Ort in der realen Welt aufgesucht haben, z. B. alle Nutzer, die kürzlich in einer Pizzeria waren.

![Eine aktionsbasierte Kampagne im Schritt "Zielbenutzer" zeigt, dass "last_location" gleich "Pizza Place" ist.]({% image_buster /assets/img_archive/last-location-segment.png %})

Sie können in Braze auch Benutzer segmentieren, die in einem bestimmten Zeitfenster eine bestimmte Art von Veranstaltungsort auf der Grundlage von Foursquare `primaryCategoryId` besucht haben. Um diesen Datenpunkt für Ihre Retargeting-Anwendungsfälle zu nutzen, protokollieren Sie `primaryCategoryId` als eine Ereigniseigenschaft während Ihres Zielgruppensegmentierungsprozesses. Um die von der Foursquare-API und dem Pilgrim SDK verwendeten Benutzer und Eigenschaften zu identifizieren, besuchen Sie die [Foursquare-Entwicklerseite](https://developer.foursquare.com/).

[1]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[2]: {% image_buster /assets/img_archive/pilgrim-dev-console.png %}