---
nav_title: Protokollierung angepasster Event-Eigenschaften
article_title: Protokollierung angepasster Event-Eigenschaften
page_order: 3
page_type: solution
description: "Dieser Hilfeartikel führt Sie durch drei wichtige Prüfungen, um sicherzustellen, dass Ihre angepassten Events so protokolliert werden, wie Sie es erwarten."
tool: 
- Campaigns
- Canvas
---

# Protokollierung angepasster Event-Eigenschaften

Es gibt drei wichtige Prüfungen, die Sie durchführen müssen, um sicherzustellen, dass Ihre angepassten Events so protokolliert werden, wie Sie es erwarten:

* [Festlegen, welche Ereignisse protokolliert werden](#verify-events)
* [Protokoll überprüfen](#verify-log)
* [Werte überprüfen](#verify-values)

## Überprüfen Sie angepasste Event-Eigenschaften

[Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) sind Metadaten, die angepasste Events beschreiben. Bei der Protokollierung eines angepassten Events können mehrere Eigenschaften protokolliert werden.

### Ereignisse überprüfen

Erkundigen Sie sich bei Ihren Entwickler:in, welche Event-Eigenschaften getrackt werden. Beachten Sie, dass bei allen Event-Eigenschaften zwischen Groß- und Kleinschreibung unterschieden wird. Weitere Informationen zum Tracking angepasster Events finden Sie in diesen Artikeln, die auf Ihrer Plattform basieren:

* [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
* [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
* [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Protokoll überprüfen

Um zu bestätigen, dass die Event-Eigenschaften erfolgreich getrackt wurden, können Sie alle Event-Eigenschaften auf der Seite **Angepasste Events** einsehen.

1. Navigieren Sie zu **Dateneinstellungen** > **Angepasste Events**.
2. Suchen Sie Ihr angepasstes Event in der Liste.
3. Klicken Sie für Ihre Veranstaltung auf **Eigenschaften verwalten**. Dies zeigt Ihnen die Namen der Eigenschaften an, die mit einem Ereignis verbunden sind.

### Werte überprüfen

Nachdem Sie Ihren Nutzer:in als Testnutzer:in hinzugefügt haben, folgen Sie diesen Schritten, um Ihre Werte zu überprüfen: 

1. Führen Sie das angepasste Event innerhalb der App aus.
2. Warten Sie etwa 10 Sekunden, bis die Daten geleert sind.
3. Aktualisieren Sie das [Event-Benutzerprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), um das angepasste Event und den Wert der mit ihm übergebenen Eigenschaft anzuzeigen.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 10\. April 2023_

