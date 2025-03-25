---
nav_title: Wiederholungen verbundener Inhalte
article_title: Wiederholungen verbundener Inhalte
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Connected-Content-Wiederholungen umgehen können."

---

# Erneute Connected-Content-Versuche

> Da Connected-Content auf den Empfang von Daten aus APIs angewiesen ist, besteht die Möglichkeit, dass eine API zeitweise nicht verfügbar ist, während Braze den Aufruf durchführt. In diesem Fall unterstützt Braze die Wiederholungslogik, um die Anfrage mit exponentiellem Backoff erneut zu versuchen. 

Um Wiederholungen zu ermöglichen, fügen Sie `:retry` in den Aufruf von Connected-Content ein, wie im folgenden Code Snippet gezeigt:
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Wenn der API-Aufruf fehlschlägt und diese Funktion aktiviert ist, versucht Braze den Aufruf erneut, wobei das von Ihnen festgelegte [Ratenlimit][47] für jede erneute Übertragung eingehalten wird. Braze verschiebt alle fehlgeschlagenen Nachrichten an das Ende der Warteschlange und fügt gegebenenfalls zusätzliche Minuten zu den Gesamtminuten hinzu, die für den Versand Ihrer Nachricht erforderlich wären.

Wenn ein Wiederholungsversuch erfolgreich war, wird die Nachricht gesendet und es werden keine weiteren Wiederholungsversuche für diese Nachricht unternommen. Wenn der Aufruf von Connected-Content 5 Mal fehlschlägt, wird die Nachricht abgebrochen, ähnlich wie wenn ein [Tag für den Abbruch einer Nachricht][1] getriggert wurde.

{% alert note %}
Connected-Content `:retry` ist für In-App-Nachrichten nicht verfügbar.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
