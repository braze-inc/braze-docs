---
nav_title: Tracking von Sitzungen
article_title: Tracking-Sitzungen für Windows Universal
platform: Windows Universal
page_order: 0
description: "Dieser Artikel referenziert, wie Sie Sitzungen auf der Windows Universal-Plattform tracken können."
hidden: true
---

# Analytics
{% multi_lang_include archive/windows_deprecation.md %}

## Session-Tracking

Das Braze SDK meldet Sitzungsdaten, die vom Braze-Dashboard verwendet werden, um das Engagement der Nutzer:innen und andere Analysen zu berechnen, die für das Verständnis Ihrer Nutzer:innen unerlässlich sind. Basierend auf der folgenden Sitzungssemantik generiert unser SDK Datenpunkte für "Sitzungsbeginn" und "Sitzungsende", die die Sitzungsdauer und die Anzahl der Sitzungen berücksichtigen, die im Braze-Dashboard angezeigt werden.

### Lebenszyklus einer Sitzung

Unsere Windows Integration protokolliert die Öffnung der Sitzung, wenn die App gestartet wird, und schließt die Sitzung, wenn die Anwendung geschlossen wird. Der Mindestwert für `sessionTimeoutInSeconds` ist 1 Sekunde. Wenn Sie eine neue Sitzung erzwingen müssen, können Sie dies tun, indem Sie den Nutzer wechseln.

### Testen des Sitzungs-Trackings

Um Sitzungen über Ihren Nutzer:innen zu erkennen, suchen Sie Ihren Nutzer auf dem Dashboard und navigieren Sie im Nutzerprofil zu "App-Nutzung". Sie können sich vergewissern, dass das Session Tracking funktioniert, indem Sie überprüfen, ob die Metrik "Sessions" in dem Maße ansteigt, wie Sie es erwarten.

![Ein Nutzerprofil, das die App-Nutzung mit 25 Sitzungen anzeigt, die letzte Nutzung vor zwei Stunden und die erste Nutzung vor zwanzig Tagen]({% image_buster /assets/img_archive/test_session.png %})


