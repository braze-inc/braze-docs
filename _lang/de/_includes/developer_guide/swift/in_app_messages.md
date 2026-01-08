{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch In-App-Nachrichten aktivieren.

## Nachrichtentypen

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Aktivieren von In-App-Nachrichten

### Schritt 1: Erstellen Sie eine Implementierung von `BrazeInAppMessagePresenter`

Damit Braze In-App-Nachrichten anzeigen kann, erstellen Sie eine Implementierung des `BrazeInAppMessagePresenter` -Protokolls und weisen Sie es der optionalen `inAppMessagePresenter` auf Ihrer Braze-Instanz zu. Sie können auch den standardmäßigen UI-Presenter von Braze verwenden, indem Sie ein `BrazeInAppMessageUI`-Objekt instanziieren.

Beachten Sie, dass Sie die Bibliothek `BrazeUI` importieren müssen, um auf die Klasse `BrazeInAppMessageUI` zuzugreifen.

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

### Schritt 2: Behandeln Sie keine passenden Trigger

Implementieren Sie [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) innerhalb der entsprechenden `BrazeDelegate` Klasse. Wenn Braze keinen passenden Trigger für ein bestimmtes Ereignis findet, ruft es diese Methode automatisch auf.
