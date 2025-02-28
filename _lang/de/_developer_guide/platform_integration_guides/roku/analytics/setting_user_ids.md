---
nav_title: "Nutzer:innen einstellen"
article_title: "Nutzer:innen IDs für Roku festlegen"
platform: Roku
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt Methoden zur Identifizierung und Einrichtung von Nutzer für Roku sowie bewährte Verfahren und wichtige Überlegungen."
 
---

# Nutzer:innen IDs festlegen

> Dieser Referenzartikel behandelt Methoden zur Identifizierung und Einrichtung von Nutzer für Roku sowie bewährte Verfahren und wichtige Überlegungen.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Sobald der Nutzer identifiziert ist (in der Regel nach dem Einloggen), sollten Sie den folgenden Aufruf tätigen, um die ID des Nutzers festzulegen:

```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## Vorgeschlagene Namenskonvention für Nutzer:in

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Best Practices und Hinweise zur Integration von Nutzer:in

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

