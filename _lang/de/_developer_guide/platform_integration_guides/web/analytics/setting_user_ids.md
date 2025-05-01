---
nav_title: "Nutzer:innen einstellen"
article_title: "Benutzer:innen IDs für das Internet festlegen"
platform: Web
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie die IDs Ihrer Nutzer:innen festlegen, einschließlich bewährter Verfahren und wichtiger Punkte, die Sie beachten sollten, bevor Sie Änderungen vornehmen."
 
---

# Nutzer:innen IDs festlegen

> Dieser Artikel beschreibt, wie Sie die IDs Ihrer Nutzer:innen festlegen, einschließlich bewährter Verfahren und wichtiger Punkte, die Sie beachten sollten, bevor Sie Änderungen vornehmen.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Sobald der Nutzer identifiziert ist (in der Regel nach dem Einloggen), sollten Sie den folgenden Aufruf tätigen, um die Nutzer-ID festzulegen:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**Rufen Sie `changeUser()` nicht auf, wenn sich ein Nutzer abmeldet.** Wenn Sie `changeUser()` auf einen statischen Standardwert setzen, werden ALLE Nutzeraktivitäten mit diesem Standardnutzer verknüpft, bis sich der Nutzer erneut anmeldet.
{% endalert %}

Wir raten davon ab, die ID zu ändern, wenn sich ein Nutzer abmeldet, da Sie dann den zuvor angemeldeten Nutzer nicht mehr mit erneuten Interaktionen ansprechen können. Wenn Sie mit mehreren Benutzern auf demselben Gerät rechnen, aber nur einen von ihnen ansprechen möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die Benutzer-ID, die Sie ansprechen möchten, während Sie abgemeldet sind, separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser Benutzer-ID zu wechseln.

Weitere Informationen finden Sie in der [Dokumentation`changeUser()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "Javadocs").

## Vorgeschlagene Namenskonvention für Nutzer:in

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Best Practices und Hinweise zur Integration von Nutzer:in

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## User:innen Aliasing

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Web" %}

