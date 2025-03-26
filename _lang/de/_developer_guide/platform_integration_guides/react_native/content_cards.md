---
nav_title: Content-Cards
article_title: Inhaltskarten für React Native
platform: React Native
page_order: 3
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie mit Content-Cards für React Native-Apps beginnen können."
channel: content cards

---

# Integration von Inhaltskarten

> Dieser Artikel beschreibt, wie Sie Content-Cards für React Native einrichten.

Die Braze SDKs enthalten einen Standard-Kartenfeed, der Ihnen den Einstieg in die Arbeit mit Content-Cards erleichtert. Sie können den Kartenfeed mit der Methode `Braze.launchContentCards()` anzeigen. Der im Braze SDK enthaltene Standard-Kartenfeed verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content-Cards.

## Anpassung

Um Ihre eigene Benutzeroberfläche zu erstellen, können Sie eine Liste der verfügbaren Karten abrufen und auf Aktualisierungen der Karten warten:

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
Wenn Sie Ihre eigene Benutzeroberfläche zur Anzeige von Karten erstellen möchten, müssen Sie `logContentCardImpression` aufrufen, um Analysen für diese Karten zu erhalten. Dies gilt auch für Karten des Typs `control`, die nachverfolgt werden müssen, auch wenn sie dem Nutzer nicht angezeigt werden.
{% endalert %}

Mit diesen zusätzlichen Methoden können Sie einen angepassten Content-Card-Feed in Ihrer App erstellen:

| Methode                                   | Beschreibung                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Startet das UI-Element Inhaltskarten.                                                                 |
| `requestContentCardsRefresh()`           | Fordert die neuesten Inhaltskarten vom Braze SDK-Server an. Die sich daraus ergebende Liste der Karten wird an jeden der zuvor registrierten [Inhaltskarten-Ereignis-Hörer](#customization) weitergegeben. |
| `getContentCards()`                      | Ruft Inhaltskarten aus dem Braze SDK ab. Dies gibt ein Versprechen zurück, das mit der neuesten Liste der Karten vom Server aufgelöst wird. |
| `getCachedContentCards()`                | Liefert das aktuellste Array der Inhaltskarten aus dem Cache.                                            |
| `logContentCardClicked(cardId)`          | Protokolliert einen Klick für die angegebene Content Card ID. Diese Methode wird nur zu Analysezwecken verwendet. Rufen Sie zum Ausführen der Klick-Aktion zusätzlich `processContentCardClickAction(cardId)` auf.                                                        |
| `logContentCardImpression(cardId)`       | Protokolliert einen Abdruck für die angegebene Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Protokolliert eine Ausblendung für die angegebene Content-Card-ID.                                                        |
| `processContentCardClickAction(cardId)`  | Führen Sie die Aktion einer bestimmten Karte aus.                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Test mit Anzeige der Beispiel-Inhaltskarte

Gehen Sie zum Testen einer Beispiel-Content-Card wie folgt vor.

1. Richten Sie einen aktiven Nutzer in der React-Anwendung ein, indem Sie die Methode [`Braze.changeUser('your-user-id')`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) aufrufen.
2. Gehen Sie zu **Kampagnen** und folgen Sie [dieser Anleitung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create), um eine neue Content Card Kampagne zu erstellen.
3. Erstellen Sie Ihre Test-Inhaltskarten-Kampagne und gehen Sie auf die Registerkarte **Test**. Fügen Sie die gleiche `user-id` wie der Testbenutzer hinzu und klicken Sie auf **Test senden**. In Kürze sollten Sie in der Lage sein, eine Content-Card auf Ihrem Gerät zu starten.

![Eine Braze Content Card Kampagne, bei der Sie Ihre eigene Benutzer-ID als Testempfänger hinzufügen können, um Ihre Content Card zu testen.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

Für weitere Integrationen folgen Sie bitte den [Anleitungen zur Android-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) oder [zur iOS-Integration](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui), je nach Ihrer Plattform.

Eine Beispielimplementierung hierfür finden Sie in BrazeProject innerhalb des [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk).

## Datenmodell der Inhaltskarte

Das Content-Card-Datenmodell ist im React Native SDK verfügbar. Eine vollständige Referenz des Content-Card-Datenmodells finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)\- und der [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

Das Braze React Native SDK verfügt über drei Typen von Content-Cards, die ein gemeinsames Basismodell haben: **Nur Bild**, **Bildunterschrift** und **Klassisch**.

Es gibt auch einen speziellen **Kontrollkartentyp**, der an Benutzer zurückgegeben wird, die sich in der Kontrollgruppe für eine bestimmte Karte befinden.

Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell und hat die folgenden zusätzlichen Eigenschaften.

### Eigenschaften des Basisinhaltskartenmodells

Das Basiskartenmodell bietet grundlegende Verhaltensweisen für alle Karten.

|Eigenschaft      | Beschreibung                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | Die ID der Karte wurde von Braze festgelegt.                                                                                            |
|`created`     | Der UNIX-Zeitstempel der Erstellungszeit der Karte von Braze.                                                             |
|`expiresAt`   | Der UNIX-Zeitstempel des Verfallszeitpunkts der Karte. Wenn der Wert kleiner als 0 ist, bedeutet dies, dass die Karte nie abläuft.      |
|`viewed`      | Ob die Karte vom Benutzer gelesen oder ungelesen ist. Damit werden keine Analysen protokolliert.                                           |
|`clicked`     | Ob die Karte vom Benutzer angeklickt wurde.                                                                         |
|`pinned`      | Ob die Karte angeheftet ist.                                                                                            |
|`dismissed`   | Ob der Benutzer diese Karte abgelehnt hat. Wenn Sie eine Karte als abgewiesen markieren, die bereits abgewiesen wurde, ist das ein No-op. |
|`dismissible` | Ob die Karte vom Nutzer ausgeblendet werden kann.                                                                           |
|`url`         | (Optional) Die URL-Zeichenfolge, die mit der Kartenklickaktion verknüpft ist.                                                       |
|`openURLInWebView` | Ob URLs für diese Karte in Braze's WebView geöffnet werden sollen oder nicht.                                            |
|`isControl`   | Ob diese Karte eine Kontrollkarte ist. Kontrollkarten sollten dem Benutzer nicht angezeigt werden.                                |
|`extras`      | Die Karte der Key-Value-Extras für diese Karte.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz der Basiskarte finden Sie in der [Android-](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) und [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Eigenschaften von Content-Cards des Typs "Nur Bild"

Nur-Bild-Karten sind anklickbare Bilder in voller Größe.

|Eigenschaft           | Beschreibung                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | Der Typ der Inhaltskarte, `IMAGE_ONLY`.                                                                              |
|`image`            | Die URL des Bildes der Karte.                                                                                      |
|`imageAspectRatio` | Das Seitenverhältnis des Bildes der Karte. Es soll als Hinweis dienen, bevor der Ladevorgang des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz zu Karten des Typs "Nur Bild" finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)\- bzw. [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct)-Dokumentation.

### Bild mit Beschriftung Inhalt Kartenmodelleigenschaften

Bildunterschriftenkarten sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

|Eigenschaft           | Beschreibung                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | Der Typ der Inhaltskarte, `CAPTIONED`.                                                                               |
|`image`            | Die URL des Bildes der Karte.                                                                                      |
|`imageAspectRatio` | Das Seitenverhältnis des Bildes der Karte. Es soll als Hinweis dienen, bevor der Ladevorgang des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
|`title`            | Der Titeltext für die Karte.                                                                                      |
|`cardDescription`  | Der Beschreibungstext für die Karte.                                                                                |
|`domain`           | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz zu Karten des Typs "Bildunterschrift" finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)\- bzw. [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct)-Dokumentation.

### Eigenschaften des klassischen Inhaltskartenmodells

Klassische Karten haben einen Titel, eine Beschreibung und ein optionales Bild auf der linken Seite des Textes.

|Eigenschaft           | Beschreibung                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | Der Typ der Inhaltskarte, `CLASSIC`.                                                                                 |
|`image`            | (Optional) Die URL des Bildes der Karte.                                                                           |
|`title`            | Der Titeltext für die Karte.                                                                                      |
|`cardDescription`  | Der Beschreibungstext für die Karte.                                                                                |
|`domain`           | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz der klassischen Inhaltskarte (Textanzeige) finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Eine vollständige Referenz der klassischen Bildkarte (Kurznachrichten) finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

### Eigenschaften von Content-Cards des Typs "Control"

Kontrollkarten enthalten alle Basiseigenschaften, mit einigen wichtigen Unterschieden. Das Wichtigste:

- Die Eigenschaft `isControl` ist garantiert `true`.
- Die Eigenschaft `extras` ist garantiert leer.

Eine vollständige Referenz der Kontrollkarte finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html)\- bzw. [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct)-Dokumentation.

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/content_cards.md %}

