---
nav_title: Personalisierung von Landing Pages
article_title: Personalisierung von Landing Pages
description: "In diesem Artikel erfahren Sie, wie Sie die Landing Pages von Braze mit dem Drag-and-Drop-Editor personalisieren können."
page_order: 4
---

# Personalisierung von Landing Pages

> Verwenden Sie Liquid Personalisierung auf Landing Pages, um den Inhalt dynamisch mit Nutzerprofil-Daten anzupassen. So können Sie beispielsweise Schlagzeilen auf der Grundlage verschiedener Nutzer:innen-Attribute personalisieren, ohne mehrere statische Landing Pages zu verwalten.

{% alert important %}
Die Liquid Personalisierung für Landing Pages ist nur auf der Pro-Stufe der Landing Pages verfügbar. [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) und [Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) werden bei der Personalisierung von Landing Pages in Liquid derzeit nicht unterstützt.
{% endalert %}

## Liquid einfüllen

Im Drag-and-Drop-Editor können Sie die Personalisierung von Liquid sowohl im Editor als auch in den Seiten- oder Blockeinstellungen im rechten Panel einfügen. Eine Anleitung zur Implementierung von Liquid finden Sie in unserer speziellen [Liquid Dokumentation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1).

\![Landing Page Editor mit Liquid Personalisierung hinzugefügt.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Vorschau und Test

Bei der Vorschau einer Landing Page im Editor können Sie die Seite als zufälliger Benutzer, als bestehender Nutzer:innen oder als angepasster Nutzer anzeigen.

Wenn Sie jedoch eine Vorschau der Landing Page über die Datentabelle oder die **Detailseite der Landing Page** anzeigen, können Sie sie nur als zufälliger Nutzer:innen sehen.

## Überlegungen zur Personalisierung

Um eine optimale Performance mit personalisierten Landing Pages zu gewährleisten, beachten Sie die folgenden Größenbeschränkungen:

- **Speichern Sie eine Landing Page:** Wenn die Größe 500 KB übersteigt, erhalten Sie möglicherweise eine Nachricht, die Sie darauf hinweist, dass die Seite unsere Größenbeschränkungen überschritten hat und daher nicht veröffentlicht werden kann.
- **Rendering mit Liquid Personalisierung:** Die Gesamtgröße darf 1 MB nicht überschreiten. Andernfalls wird die Seite möglicherweise automatisch von Braze nicht veröffentlicht.

### Vermeiden Sie die Veröffentlichung von Landing Pages

Wenn Ihre Seite diese Größenbeschränkungen überschreitet, erhalten Sie eine E-Mail, dass sie möglicherweise nicht mehr veröffentlicht wird, wenn sie das Limit weiterhin überschreitet. Wenn der Schwellenwert erreicht ist, wird die Seite automatisch unveröffentlicht, und Sie erhalten eine Benachrichtigung.

Um zu verhindern, dass Ihre Seite die Größenbeschränkungen überschreitet oder zu langsam lädt, sollten Sie die Personalisierung mit Liquid verwenden:

- Führt nicht ständig Schleifen durch oder referenziert große Datensätze.
- Verlassen Sie sich nicht auf umfangreiche mathematische oder bedingte Logik innerhalb des Liquid-Blocks.

## Fallback-Seiten

Wenn Ihre Nutzer:innen versuchen, auf eine Seite zuzugreifen, die nicht veröffentlicht wurde, wird eine Nachricht angezeigt, die besagt, dass die Seite derzeit nicht geladen werden kann. Gründe dafür, dass eine Seite nicht veröffentlicht wurde, können sein:

- Komplexes oder gebrochenes Liquid, das lange Renderzeiten verursachen kann
- Nutzer:innen Probleme mit dem Netzwerk
- Überschreitung der maximalen Größe der Landing Page
