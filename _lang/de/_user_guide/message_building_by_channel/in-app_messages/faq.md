---
nav_title: FAQ
article_title: In-App-Nachricht FAQ
page_order: 19
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu In-App-Nachrichten."
tool: in-app messages

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu In-App-Nachrichten.

### Was ist eine In-Browser-Nachricht und wie unterscheidet sie sich von einer In-App-Nachricht?

In-Browser-Nachrichten sind In-App-Nachrichten, die an Webbrowser gesendet werden. Um eine In-Browser-Nachricht zu erstellen, stellen Sie sicher, dass Sie bei der Erstellung Ihrer In-App-Nachrichtenkampagne oder Ihres Canvas unter dem Feld **Senden an die** Option **Webbrowser** wählen. 

### Wird eine In-App-Nachricht angezeigt, wenn ein Gerät offline ist?

Das kommt darauf an. Da In-App-Nachrichten beim Start der Sitzung zugestellt werden und das Gerät die Nutzdaten herunterladen kann, bevor es offline geht, kann die In-App-Nachricht auch dann angezeigt werden, wenn es offline ist. Wenn die Nutzdaten nicht heruntergeladen werden, wird die In-App-Nachricht nicht angezeigt.

### Wenn ein Benutzer bereits eine In-App-Nachricht auf seinem Gerät hat und das Ablaufdatum der Nachricht geändert wird, wird dann das Ablaufdatum auf seinem Gerät aktualisiert?

Wenn ein:e Nutzer:in eine Sitzung eintritt, prüft Braze, ob an den In-App-Nachrichten, für die sie:er berechtigt ist, Änderungen vorgenommen wurden und aktualisiert sie entsprechend. Wenn sich also das Ablaufdatum geändert hat und sie eine Sitzung anmelden, wird die In-App-Nachricht mit den aktualisierten Informationen an das Gerät gesendet.

### Wie richte ich Ruhezeiten für eine In-App-Nachricht-Kampagne ein?

Das Feature Ruhezeiten kann nicht mit In-App-Nachricht-Kampagnen verwendet werden. Mit dieser Funktion können Sie verhindern, dass Nachrichten zu bestimmten Zeiten an Ihre Benutzer gesendet werden. Bei In-App-Kampagnen erhalten Ihre Nutzer nur dann In-App-Nachrichten, wenn sie in der App aktiv sind. 

Um In-App-Nachrichten zu einem bestimmten Zeitpunkt zu versenden, verwenden Sie den folgenden Beispiel-Code von Liquid. Damit kann die Nachricht abgebrochen werden, wenn die In-App-Nachricht nach 19:59 Uhr oder vor 8 Uhr in der angegebenen Zeitzone angezeigt wird.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Wann wird die Berechtigung für eine In-App-Nachricht berechnet?

Die Anspruchsberechtigung für eine In-App-Nachricht wird zum Zeitpunkt der Zustellung berechnet. Wenn eine In-App-Nachricht für den Versand um 7 Uhr morgens vorgesehen ist, wird die Berechtigung für diese In-App-Nachricht um 7 Uhr morgens geprüft.

Sobald die In-App-Nachricht angezeigt wird, hängt die Anspruchsberechtigung davon ab, wann die In-App-Nachricht heruntergeladen und ausgelöst wird.

### Was sind vorgefertigte In-App-Nachrichten?

In-App-Nachrichten werden als Schablonen-In-App-Nachrichten zugestellt, wenn die Option **Kampagneneignung vor der Anzeige neu bewerten** ausgewählt wurde oder wenn eines der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- SMS-Variablen wie z.B. {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Das bedeutet, dass das Gerät beim Start der Sitzung den Trigger dieser In-App-Nachricht anstelle der gesamten Nachricht empfängt. Wenn die:der Nutzer:in die In-App-Nachricht triggert, wird ihr:sein Gerät eine Anfrage an das Netzwerk stellen, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Zugang zum Internet hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Liquid-Logik zu lange braucht, um sie aufzulösen.
{% endalert %}

### Warum liefert meine archivierte Messaging-Kampagne immer noch Impressionen von In-App-Nachrichten?

Dies kann bei Nutzer:innen vorkommen, die die Segmentierungskriterien erfüllt haben, als die In-App-Nachricht-Kampagne aktiv war.

Um dies zu verhindern, wählen Sie bei der Einrichtung Ihrer Kampagne die Option **Berechtigung der Kampagne neu bewerten, bevor sie angezeigt wird**. 

### Wie berechnet Braze den Ablauf einer In-App-Nachricht, die auf "nach 1 Tag(en)" eingestellt ist?

Braze berechnet eine Verfallszeit von einem Tag als 24 Stunden, nachdem Nutzer:innen berechtigt sind, eine Nachricht zu erhalten.