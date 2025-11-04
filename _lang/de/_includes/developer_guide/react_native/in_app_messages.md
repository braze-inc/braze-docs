{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Nachrichtentypen

{% tabs %}
{% multi_lang_include developer_guide/_shared/push_notifications/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/push_notifications/message_types/swift.md %}
{% endtabs %}

## Datenmodell

Das Modell für In-App-Nachrichten ist im React Native SDK verfügbar. Braze verfügt über vier In-App-Nachrichtentypen, die dasselbe Datenmodell verwenden: **Slideup**, **Modal**, **Full** und **HTML Full**.

### Nachrichten

Das In-App-Nachricht-Modell bildet die Grundlage für alle In-App-Nachrichten.

|Eigenschaft          | Beschreibung                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | Die JSON-Darstellung der Nachricht.                                                                                |
|`message`         | Der Text der Nachricht.                                                                                                      |
|`header`          | Die Kopfzeile der Nachricht.                                                                                                    |
|`uri`             | Die URI, die mit dem Klick auf den Button verbunden ist.                                                                       |
|`imageUrl`        | Die URL des Bildes der Nachricht.                                                                                                 |
|`zippedAssetsUrl` | Die gezippten Assets, die für die Anzeige von HTML-Inhalten vorbereitet sind.                                                                    |
|`useWebView`      | Gibt an, ob der Klick auf den Button über eine Webansicht umgeleitet werden soll.                                            |
|`duration`        | Die Anzeigedauer der Nachrichten.                                                                                          |
|`clickAction`     | Der Aktionstyp für den Klick auf den Button. Die Typen sind: `URI`, und `NONE`.                                     |
|`dismissType`     | Die Art des Abschlusses der Nachricht. Die beiden Arten sind: `SWIPE` und `AUTO_DISMISS`.                                                 |
|`messageType`     | Der vom SDK unterstützte Typ der In-App-Nachricht. Die vier Typen sind: `SLIDEUP`, `MODAL`, `FULL` und `HTML_FULL`.          |
|`extras`          | Das Wörterbuch der Nachrichten-Extras. Standardwert: `[:]`.                                                                   |
|`buttons`         | Die Liste der Buttons in der In-App-Nachricht.                                                                             |
|`toString()`      | Die Nachricht als String-Darstellung.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz des In-App-Nachricht-Modells finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) und [für iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Buttons

In-App-Nachrichten können Buttons hinzugefügt werden, um Aktionen durchzuführen und Analytics zu protokollieren. Das Button-Modell bildet die Grundlage für alle In-App-Nachricht-Buttons.

|Eigenschaft          | Beschreibung                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | Der Text auf dem Button.                                                                                                     |
|`uri`             | Die URI, die mit dem Klick auf den Button verbunden ist.                                                                            |
|`useWebView`      | Gibt an, ob der Klick auf den Button über eine Webansicht umgeleitet werden soll.                                                 |
|`clickAction`     | Die Art der Klick-Aktion, die verarbeitet wird, wenn der Nutzer auf den Button klickt. Die Typen sind: `URI`, und `NONE`. |
|`id`              | Die ID des Buttons in der Nachricht.                                                                                               |
|`toString()`      | Der Button als String-Darstellung.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Eine vollständige Referenz des Button-Modells finden Sie in der Dokumentation [für Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).
