---
nav_title: "Nutzer:innen IDs festlegen"
article_title: "Nutzer:innen IDs für Windows Universal festlegen"
platform: Windows Universal
page_order: 1
description: "Dieser referenzierte Artikel beschreibt, wie Sie Nutzer:innen auf der Windows Universal-Plattform festlegen."
hidden: true
---

# Nutzer:innen IDs festlegen
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Sobald der Nutzer identifiziert ist (in der Regel nach dem Einloggen), sollten Sie den folgenden Aufruf tätigen, um die Nutzer-ID festzulegen:

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**Rufen Sie `changeUser()` nicht auf, wenn sich ein:e Nutzer abmeldet. `changeUser()` sollte nur aufgerufen werden, wenn sich der oder die Nutzer:in in die Anwendung einloggt.** Wenn Sie `changeUser()` auf einen statischen Standardwert setzen, werden ALLE Nutzeraktivitäten mit diesem Standardnutzer verknüpft, bis sich der oder die Nutzer:in sich erneut anmeldet.
{% endalert %}

Außerdem empfehlen wir, die ID nicht zu ändern, wenn sich ein Nutzer:innen abmeldet, da Sie dann den zuvor angemeldeten Nutzer:innen nicht mit erneuten Interaktionen ansprechen können. Wenn Sie mit mehreren Benutzern auf demselben Gerät rechnen, aber nur einen von ihnen ansprechen möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die Benutzer-ID, die Sie ansprechen möchten, während Sie abgemeldet sind, separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser Benutzer-ID zu wechseln.

## Vorgeschlagene Namenskonvention für Nutzer:in

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Best Practices und Hinweise zur Integration von Nutzer:in

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

