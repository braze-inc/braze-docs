---
nav_title: Verfolgung von Push-Abmeldungen
article_title: Verfolgung von Push-Abmeldungen
page_type: solution
description: "In diesem Hilfe-Artikel finden Sie einige Tipps zum Verfolgen von Push-Abmeldungen."
channel: push
---

# Verfolgung von Push-Abbestellungen

Push-Abmeldungen hängen von Aktualisierungen des Push-Status eines Benutzers durch Anbieter wie Apple oder Google ab. Diese Aktualisierungen können unregelmäßig und unvorhersehbar sein. Daher werden Push-Abmeldungen nicht als Metrik in die Analyse von Push-Kampagnen aufgenommen. 

Die manuelle Nachverfolgung von Push-Abmeldungen kann jedoch wertvolle Einblicke in die Reaktionen der Nutzer auf die Häufigkeit Ihrer Benachrichtigungen und die Relevanz der Inhalte liefern. Hier sind zwei Optionen für die Verfolgung von Push-Abmeldungen.

## Option 1: Segmentfilter verwenden

Als Abhilfe können Sie ein Segment erstellen, um Benutzer zu identifizieren, die nicht Push-fähig sind, d.h. die nicht abonniert oder angemeldet sind und kein [Push-Token für den Vordergrund]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) haben. Um zum Beispiel die Anzahl der Abmeldungen in Ihrer Android-App zu sehen, würden Sie die Kombination der folgenden Segmente verwenden: 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![Der Abschnitt Segment Builder mit dem Filter "Background or Foreground Push Enabled for App" für die App TEST (Android) ist falsch, und der Filter "Has Uninstalled" ist ausgewählt, um 2.393 erreichbare Benutzer anzuzeigen.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Beachten Sie, dass die Segmentierungsfilter nur ungefähr sind und nicht spezifisch an ein Datum und eine Kampagne gebunden werden können.

## Option 2: Verwenden Sie ein benutzerdefiniertes Ereignis

{% alert important %}
Beachten Sie, dass die Protokollierung eines benutzerdefinierten Ereignisses für eine Abonnementänderung [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count) verbraucht. Alternativ können Sie auch Segmentfilter verwenden, um Nutzer zu identifizieren und anzusprechen, die nicht Push-fähig sind.
{% endalert %}

Als weitere Abhilfe empfehlen wir, ein benutzerdefiniertes Ereignis für Push-Abmeldungen zu erstellen, das darauf basiert, ob der Push-Status eines Benutzers `true` oder `false` ist, um diese Kennzahl zu verfolgen.

_Zuletzt aktualisiert am 13\. Juni 2024_
