---
nav_title: Abbrechen von Connected-Content
article_title: Abbrechen von Connected-Content
page_order: 2
description: "Dieser Referenzartikel behandelt einige Best Practices zum Abbrechen von Connected-Content."

---

# Abbrechen von Connected-Content {#aborting-connected-content}

> Mit Liquid-Templating haben Sie die Möglichkeit, Nachrichten mit bedingter Logik abzubrechen. 

Im folgenden Beispiel geben die Bedingungen `connected.recommendations.size < 5` und `connected.foo.bar == nil` Situationen an, die zum Abbruch der Nachricht führen würden.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

Sie können auch einen Grund für den Abbruch angeben, der im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) gespeichert wird. Dieser Abbruchgrund muss eine Zeichenkette sein und darf kein Liquid enthalten.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Abgebrochene Nachrichten werden von Braze nicht auf die Anzahl der gesendeten Nachrichten in Ihrem Braze-Konto oder in Currents angerechnet.
{% endalert %}
