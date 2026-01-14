---
nav_title: Erneute Connected-Content-Versuche
article_title: Wiederholungen verbundener Inhalte
page_order: 5
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Connected-Content-Wiederholungen umgehen können."

---

# Wiederholungslogik für Connected-Content verwenden

> Auf dieser Seite erfahren Sie, wie Sie Ihren Connected-Content-Aufrufen Wiederholungsversuche hinzufügen können.

## Wie Wiederholungen funktionieren 

Da Connected-Content auf den Empfang von Daten aus APIs angewiesen ist, kann eine API zeitweise nicht verfügbar sein, während Braze den Aufruf durchführt. In diesem Fall unterstützt Braze die Wiederholungslogik, um die Anfrage mit exponentiellem Backoff erneut zu versuchen.

{% alert note %}
Connected-Content `:retry` ist für In-App-Nachrichten nicht verfügbar.
{% endalert %}

## Wiederholungslogik verwenden

Um die Wiederholungslogik zu verwenden, fügen Sie den Tag `:retry` zum Aufruf von Connected-Content hinzu, wie im folgenden Code-Snippet gezeigt:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Wenn ein `:retry` Tag im Connected-Content-Aufruf enthalten ist, wird Braze versuchen, den Aufruf bis zu fünf Mal zu wiederholen.

### Ergebnisse der Wiederholungsversuche

#### Wenn ein Wiederholungsversuch erfolgreich ist

Wenn ein Wiederholungsversuch erfolgreich ist, wird die Nachricht gesendet und es werden keine weiteren Wiederholungsversuche für diese Nachricht unternommen.

#### Wenn der API-Aufruf fehlschlägt und Wiederholungsversuche aktiviert sind

Wenn der API-Aufruf fehlschlägt und diese Funktion aktiviert ist, versucht Braze den Aufruf erneut, wobei das von Ihnen festgelegte [Ratenlimit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) für jede erneute Übertragung eingehalten wird. Braze verschiebt alle fehlgeschlagenen Nachrichten an das Ende der Warteschlange und fügt gegebenenfalls zusätzliche Minuten zu den Gesamtminuten hinzu, die für den Versand Ihrer Nachricht erforderlich wären.

Wenn der Aufruf von Connected-Content mehr als fünf Mal fehlschlägt, wird die Nachricht abgebrochen, ähnlich wie ein [Tag für den Abbruch einer Nachricht]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) getriggert wird.