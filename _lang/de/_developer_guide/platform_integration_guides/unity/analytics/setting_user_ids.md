---
nav_title: "Nutzer:innen einstellen"
article_title: "Benutzer:innen IDs für Unity festlegen"
platform: 
  - Unity
  - iOS
  - Android
page_order: 0
description: "Dieser Artikel referenziert das Einrichten von Nutzer-IDs auf der Unity-Plattform, einschließlich vorgeschlagener Benennungskonventionen und bewährter Verfahren."
 
---

# Nutzer:innen IDs festlegen

> Dieser Artikel referenziert das Einrichten von Nutzer-IDs auf der Unity-Plattform, einschließlich vorgeschlagener Benennungskonventionen und bewährter Verfahren.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Sobald der Nutzer identifiziert ist (in der Regel nach dem Einloggen), sollten Sie den folgenden Aufruf tätigen, um die ID des Nutzers festzulegen:

```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```

{% alert warning %}
**Rufen Sie `ChangeUser()` nicht auf, wenn sich ein:e Nutzer abmeldet. `ChangeUser()` sollte nur aufgerufen werden, wenn sich der oder die Nutzer:in in die Anwendung einloggt.** Wenn Sie `ChangeUser()` auf einen statischen Standardwert setzen, werden ALLE Nutzeraktivitäten mit diesem Standardnutzer verknüpft, bis sich der oder die Nutzer:in sich erneut anmeldet.
{% endalert %}

Außerdem empfehlen wir, die ID nicht zu ändern, wenn sich ein Nutzer:innen abmeldet, da Sie dann den zuvor angemeldeten Nutzer:innen nicht mit erneuten Interaktionen ansprechen können. Wenn Sie mit mehreren Nutzern auf demselben Gerät rechnen, aber nur einen von ihnen anvisieren möchten, wenn sich Ihre App im abgemeldeten Zustand befindet, empfehlen wir Ihnen, die Nutzer:innen-ID, die Sie anvisieren möchten, während Sie abgemeldet sind, separat zu verfolgen und im Rahmen des Abmeldevorgangs Ihrer App wieder zu dieser Nutzer:innen-ID zu wechseln.

## Vorgeschlagene Namenskonvention für Nutzer:in

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Best Practices und Hinweise zur Integration von Nutzer:in

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
