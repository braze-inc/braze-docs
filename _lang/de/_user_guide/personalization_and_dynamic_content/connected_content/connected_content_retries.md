---
nav_title: Wiederholungen verbundener Inhalte
article_title: Wiederholungen verbundener Inhalte
page_order: 5
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Connected-Content-Wiederholungen umgehen können."

---

# 

> Auf dieser Seite erfahren Sie, wie Sie Ihren Connected-Content-Aufrufen Wiederholungsversuche hinzufügen können.

##  

 In diesem Fall unterstützt Braze die Wiederholungslogik, um die Anfrage mit exponentiellem Backoff erneut zu versuchen.

{% alert note %}
Connected-Content `:retry` ist für In-App-Nachrichten nicht verfügbar.
{% endalert %}

## 




```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}



### Ergebnisse der Wiederholungsversuche

#### Wenn ein Wiederholungsversuch erfolgreich ist



#### Wenn der API-Aufruf fehlschlägt und Wiederholungsversuche aktiviert sind

 Braze verschiebt alle fehlgeschlagenen Nachrichten an das Ende der Warteschlange und fügt gegebenenfalls zusätzliche Minuten zu den Gesamtminuten hinzu, die für den Versand Ihrer Nachricht erforderlich wären.

