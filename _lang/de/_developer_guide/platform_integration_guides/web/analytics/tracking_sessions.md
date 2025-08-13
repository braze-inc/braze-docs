---
nav_title: Tracking von Sitzungen
article_title: Tracking-Sitzungen für das Internet
platform: Web
page_order: 0
description: "In diesem Referenzartikel erfahren Sie, wie Sie Tracking-Sitzungen im Internet durchführen können."

---

# Tracking von Sitzungen

> Das Braze SDK meldet Sitzungsdaten, die vom Braze Dashboard verwendet werden, um das Benutzerengagement und andere Analysen zu berechnen, die für das Verständnis Ihrer Benutzer wichtig sind. Das SDK generiert Datenpunkte für "start session" und "close session", die die Sitzungsdauer und die Anzahl der Sitzungen berücksichtigen und im Braze-Dashboard auf der Grundlage der folgenden Sitzungssemantik angezeigt werden.

## Lebenszyklus einer Sitzung

Standardmäßig beginnen die Sitzungen, wenn `braze.openSession()` zum ersten Mal aufgerufen wird, und bleiben bis zu einer Inaktivität von mindestens 30 Minuten geöffnet. Das bedeutet, dass die Sitzung fortgesetzt wird, wenn Nutzer die Seite verlassen und innerhalb 30 Minuten wieder zurückkehren. Wenn sie erst nach Ablauf der 30 Minuten zurückkehren, wird automatisch ein Datenpunkt "close session" für die Zeit ihrer Abwesenheit erzeugt, und eine neue Sitzung wird geöffnet.

{% alert note %}
Wenn Sie eine neue Sitzung erzwingen müssen, können Sie dies tun, indem Sie den Nutzer wechseln.
{% endalert %}

## Anpassen des Sitzungs-Timeouts

Um das Sitzungs-Timeout anzupassen, übergeben Sie die Option `sessionTimeoutInSeconds` an Ihre [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)-Funktion. Der Mindestwert für `sessionTimeoutInSeconds` ist 1 Sekunde.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

Wenn Sie ein Timeout für die Sitzung festgelegt haben, erstreckt sich die Sitzungssemantik auf dieses angepasste Timeout.

## Testen des Sitzungs-Trackings

Um Sitzungen über Ihren Benutzer zu erkennen, suchen Sie Ihren Benutzer im Dashboard und navigieren Sie im Benutzerprofil zu **App-Nutzung**. Sie können sich vergewissern, dass das Sitzungs-Tracking funktioniert, indem Sie überprüfen, ob die Sitzungsmetrik wie erwartet ansteigt.

![Eine Komponente des Nutzerprofils, die anzeigt, wie viele Sitzungen stattgefunden haben, wann die App zum ersten Mal benutzt wurde und wann sie zuletzt benutzt wurde.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%"}

