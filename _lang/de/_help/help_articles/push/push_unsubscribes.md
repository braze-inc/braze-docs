---
nav_title: Tracking von Push-Abmeldungen
article_title: Tracking von Push-Abmeldungen
page_type: solution
description: "Dieser Hilfeartikel enthält einige Tipps zum Tracking von Push-Abmeldungen."
channel: push
---

# Tracking von Push-Abmeldungen

Push-Abmeldungen hängen von Updates des Push-Status eines Nutzers:innen durch Anbieter wie Apple oder Google ab. Diese Updates können unregelmäßig und unvorhersehbar sein. Daher werden Push-Abmeldungen nicht als Metrik in den Analytics für Push-Kampagnen berücksichtigt. 

Dennoch kann das manuelle Tracking von Push-Abmeldungen wertvolle Insights über die Reaktionen der Nutzer:innen auf die Häufigkeit Ihrer Push-Benachrichtigungen und die Relevanz der Inhalte liefern. Hier sind zwei Optionen für das Tracking von Push-Abmeldungen.

## Option 1: Filter für Segmente verwenden

Als Abhilfe können Sie ein Segment erstellen, um Nutzer:innen zu identifizieren, die nicht über Push Enablement verfügen, d.h. die weder Abonnent:innen noch Opt-in sind und auch keinen [Push-Token im Vordergrund]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) haben. Um zum Beispiel die Anzahl der Abmeldungen in Ihrer Android App zu sehen, würden Sie die Kombination der folgenden Segmente verwenden: 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![Der Abschnitt Segment Builder mit dem Filter "Hintergrund oder Vordergrund Push Enablement für App" für die TEST (Android) App ist falsch, und der Filter "Hat deinstalliert" sind ausgewählt, um 2.393 erreichbare Nutzer:innen anzuzeigen.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Beachten Sie, dass die Filter für die Segmentierung nur ungefähr sind und nicht speziell an ein Datum und eine Kampagne gebunden werden können.

## Option 2: Verwenden Sie ein angepasstes Event

{% alert important %}
Beachten Sie, dass die Protokollierung eines angepassten Events für eine Aboänderung [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count) verbraucht. Verwenden Sie alternativ Segmentierungsfilter, um Nutzer:innen zu identifizieren und zu targetieren, die nicht Push-aktiviert sind.
{% endalert %}

Als weitere Abhilfe empfehlen wir, ein angepasstes Event für Push-Abmeldungen zu erstellen, das darauf basiert, ob der Push Enablement-Status eines Nutzers `true` oder `false` ist, um diese Metrik zu verfolgen.

_Zuletzt aktualisiert am 13\. Juni 2024_
