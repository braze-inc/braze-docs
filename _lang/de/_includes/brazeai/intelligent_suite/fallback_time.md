Sie können eine der folgenden Optionen wählen:

- **Beliebt:** Dies ist die Zeit, in der Ihre App von allen Nutzer:innen am häufigsten verwendet wird.
- **Anpassen:** Dies ist ein angepasster Fallback Ihrer Wahl. Die Nachricht wird basierend auf der Ortszeit jedes einzelnen Nutzers:innen zugestellt.

{% subtabs local %}
{% subtab most popular %}
Die beliebteste App-Zeit wird durch die durchschnittliche Sitzungsstartzeit für Ihren Workspace (in Ortszeit) bestimmt. Diese Zeit wird im Chart der Vorschau in rot angezeigt.

Für den unwahrscheinlichen Fall, dass Ihre App nicht über genügend Sitzungsdaten verfügt, um zu berechnen, wann die App am meisten genutzt wird (eine völlig neue App ohne Daten), wird die Nachricht um 17 Uhr in der Ortszeit des Nutzers gesendet. Wenn die Ortszeit der Nutzerin oder des Nutzers nicht bekannt ist, wird sie um 17 Uhr in der Zeitzone Ihres Unternehmens gesendet.

Es ist wichtig, dass Sie sich der Einschränkungen bewusst sind, die der Einsatz von Intelligent Timing zu einem frühen Zeitpunkt im Lebenszyklus eines Nutzers mit sich bringt, wenn nur wenige Daten verfügbar sind. Sie kann dennoch wertvoll sein, denn selbst Nutzer mit wenigen aufgezeichneten Sitzungen können Einblicke in ihr Verhalten geben. Braze kann jedoch den optimalen Sendezeitpunkt später im Lebenszyklus einer Nutzerin oder eines Nutzers besser berechnen.

{% if include.type == "campaigns" %}
{% alert note %}
Wenn Sie für Kampagnen ein [Zeitfenster für die Zustellung](#sending-within-specific-hours) angegeben haben und die beliebteste Zeit für die Nutzung Ihrer App außerhalb dieses Zeitfensters liegt, wird die Nachricht so nah wie möglich an den Rand des Zeitfensters gesendet. Wenn Ihr Zustellungsfenster beispielsweise zwischen 13 und 20 Uhr liegt und die beliebteste App-Zeit 22 Uhr ist, wird die Nachricht um 20 Uhr gesendet.
{% endalert %}
{% endif %}
{% endsubtab %}

{% subtab custom %}
Verwenden Sie die angepasste Fallback-Zeit, um eine andere Zeit für den Versand der Nachricht zu wählen. Ähnlich wie bei der beliebtesten App-Zeit wird die Nachricht zur Ausweichzeit in der lokalen Zeitzone des Benutzers gesendet. Wenn die lokale Zeitzone des Benutzers unbekannt ist, wird sie in der Zeitzone Ihres Unternehmens gesendet.

Wenn Sie bei Kampagnen mit einer benutzerdefinierten Ausweichzeit die Kampagne innerhalb von 24 Stunden nach dem Versanddatum starten, erhalten Benutzer, deren optimale Zeit bereits verstrichen ist, die Kampagne zur benutzerdefinierten Ausweichzeit. Wenn die benutzerdefinierte Ausweichzeit in ihrer Zeitzone bereits abgelaufen ist, wird die Nachricht sofort gesendet.
{% endsubtab %}
{% endsubtabs %}