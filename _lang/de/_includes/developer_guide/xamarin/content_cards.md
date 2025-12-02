## Über .NET MAUI Content-Cards

Das Braze .NET MAUI SDK enthält einen Standard-Card-Feed, um Ihnen den Einstieg in Content-Cards zu erleichtern. Der im Braze SDK enthaltene Standard-Kartenfeed verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content-Cards.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Kartentypen und Eigenschaften

Das Braze .NET MAUI SDK verfügt über drei eindeutige Content-Cards-Kartentypen, die sich ein Basismodell teilen: [Banner](#xamarin_banner), [Bildunterschrift](#xamarin_captioned-image) und [Klassisch](#xamarin_classic). Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell und hat die folgenden zusätzlichen Eigenschaften.

### Basis-Kartenmodell

|Eigenschaft           | Beschreibung                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | Die ID der Karte wurde von Braze festgelegt.                                                                                            |
|`created`          | Der UNIX-Zeitstempel der Erstellungszeit der Karte von Braze.                                                             |
|`expiresAt`        | Der UNIX-Zeitstempel des Verfallszeitpunkts der Karte. Wenn der Wert kleiner als 0 ist, bedeutet dies, dass die Karte nie abläuft.      |
|`viewed`           | Ob die Karte vom Benutzer gelesen oder ungelesen ist. Damit werden keine Analysen protokolliert.                                           |
|`clicked`          | Ob die Karte vom Benutzer angeklickt wurde.                                                                         |
|`pinned`           | Ob die Karte angeheftet ist.                                                                                            |
|`dismissed`        | Ob der Benutzer diese Karte abgelehnt hat. Wenn Sie eine Karte als abgewiesen markieren, die bereits abgewiesen wurde, ist das ein No-op. |
|`dismissible`      | Ob die Karte vom Nutzer ausgeblendet werden kann.                                                                           |
|`urlString`        | (Optional) Der URL String, der mit der Kartenklick-Aktion verknüpft ist.                                                       |
|`openUrlInWebView` | Ob die URLs für diese Karte in der Braze WebView geöffnet werden sollen oder nicht.                                                 |
|`isControlCard`    | Ob diese Karte eine Kontrollkarte ist. Kontrollkarten sollten dem Benutzer nicht angezeigt werden.                                |
|`extras`           | Die Karte der Key-Value-Extras für diese Karte.                                                                             |
|`isTest`           | Ob diese Karte eine Testkarte ist.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz der Basiskarte finden Sie in der [Android-](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) und [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Banner

Bannerkarten sind anklickbare Bilder in voller Größe.

|Eigenschaft           | Beschreibung                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | Die URL des Bildes der Karte.                                                                                      |
|`imageAspectRatio` | Das Seitenverhältnis des Bildes der Karte. Es soll als Hinweis dienen, bevor der Ladevorgang des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz der Bannerkarte finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (jetzt umbenannt in Nur Bild).

### Bildunterschrift

Bildunterschriftenkarten sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

|Eigenschaft           | Beschreibung                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | Die URL des Bildes der Karte.                                                                                      |
|`imageAspectRatio` | Das Seitenverhältnis des Bildes der Karte. Es soll als Hinweis dienen, bevor der Ladevorgang des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
|`title`            | Der Titeltext für die Karte.                                                                                      |
|`cardDescription`  | Der Beschreibungstext für die Karte.                                                                                |
|`domain`           | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz zu Karten des Typs "Bildunterschrift" finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)\- bzw. [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct)-Dokumentation.

### Klassisch

Klassische Karten haben einen Titel, eine Beschreibung und ein optionales Bild auf der linken Seite des Textes.

|Eigenschaft           | Beschreibung                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Optional) Die URL des Bildes der Karte.                                                                           |
|`title`            | Der Titeltext für die Karte.                                                                                      |
|`cardDescription`  | Der Beschreibungstext für die Karte.                                                                                |
|`domain`           | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Es kann auf der Benutzeroberfläche der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz der klassischen Inhaltskarte (Textanzeige) finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Eine vollständige Referenz der klassischen Bildkarte (Kurznachrichten) finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Karten-Methoden

Mit diesen zusätzlichen Methoden können Sie einen angepassten Content-Card-Feed in Ihrer App erstellen:

| Methode                                   | Beschreibung                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Fordert die neuesten Inhaltskarten vom Braze SDK-Server an.                                           |
| `getContentCards()`                      | Ruft Inhaltskarten aus dem Braze SDK ab. Dies gibt die neueste Liste der Karten vom Server zurück. |
| `logContentCardClicked(cardId)`          | Protokolliert einen Klick für die angegebene Content Card ID. Diese Methode wird nur zu Analysezwecken verwendet.                    |
| `logContentCardImpression(cardId)`       | Protokolliert einen Abdruck für die angegebene Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Protokolliert eine Ausblendung für die angegebene Content-Card-ID.                                                        |
