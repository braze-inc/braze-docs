---
nav_title: "Nutzer:innen einstellen"
article_title: "Nutzer:innen IDs für iOS einstellen"
platform: Swift
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie Nutzer:innen IDs in Ihrer iOS App einrichten, welche Namenskonventionen für Nutzer:innen vorgeschlagen werden und wie Sie am besten vorgehen."
 
---

# Nutzer:innen IDs festlegen

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Vorgeschlagene Namenskonvention für Nutzer:in

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Zuweisung einer Nutzer:in ID

Sobald der Nutzer identifiziert ist (in der Regel nach dem Einloggen), sollten Sie den folgenden Aufruf tätigen, um die Nutzer-ID festzulegen:

{% tabs %}
{% tab schnell %}

```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**Rufen Sie `changeUser()` nicht auf, wenn sich ein Nutzer abmeldet. `changeUser()` darf nur beim Anmelden aufgerufen werden.** Wenn Sie [`changeUser()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser%28userid%3Asdkauthsignature%3Afileid%3Aline%3A%29) auf einen statischen Standardwert setzen, werden ALLE Benutzeraktivitäten mit diesem "Standardnutzer" verknüpft, bis eine erneute Anmeldung erfolgt.
{% endalert %}

Außerdem empfehlen wir, die ID nicht zu ändern, wenn sich ein Nutzer:innen abmeldet, da Sie dann den zuvor angemeldeten Nutzer:innen nicht mit erneuten Interaktionen ansprechen können. Wenn Sie mit mehreren Nutzern auf demselben Gerät rechnen, aber nur einen von ihnen ansprechen möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die ID des Nutzers, den Sie ansprechen möchten, während Sie abgemeldet sind, separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser ID zu wechseln.

## Best Practices und Hinweise zur Integration von Nutzer:in

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## User:innen Aliasing

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Swift" %}

