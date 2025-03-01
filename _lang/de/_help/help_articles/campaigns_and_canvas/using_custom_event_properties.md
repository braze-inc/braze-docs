---
nav_title: Benutzerdefinierte Ereigniseigenschaften protokollieren
article_title: Benutzerdefinierte Ereigniseigenschaften protokollieren
page_order: 3
page_type: solution
description: "Dieser Hilfeartikel führt Sie durch drei wichtige Prüfungen, um sicherzustellen, dass Ihre benutzerdefinierten Ereignisse so protokolliert werden, wie Sie es erwarten."
tool: 
- Campaigns
- Canvas
---

# Protokollierung benutzerdefinierter Ereigniseigenschaften

Es gibt drei wichtige Prüfungen, die Sie durchführen müssen, um sicherzustellen, dass Ihre benutzerdefinierten Ereignisse so protokolliert werden, wie Sie es erwarten:

* [Festlegen, welche Ereignisse protokolliert werden](#verify-events)
* [Protokoll überprüfen](#verify-log)
* [Werte überprüfen](#verify-values)

## Überprüfen Sie benutzerdefinierte Ereigniseigenschaften

[Benutzerdefinierte Ereigniseigenschaften][22] sind Metadaten, die benutzerdefinierte Ereignisse beschreiben. Bei jeder Protokollierung eines benutzerdefinierten Ereignisses können mehrere Eigenschaften protokolliert werden.

### Ereignisse überprüfen

Erkundigen Sie sich bei Ihren Entwicklern, welche Ereigniseigenschaften verfolgt werden. Beachten Sie, dass bei allen Ereigniseigenschaften zwischen Groß- und Kleinschreibung unterschieden wird. Weitere Informationen zur Verfolgung von benutzerdefinierten Ereignissen finden Sie in diesen Artikeln, die sich auf Ihre Plattform beziehen:

* [Android][51]
* [iOS][23]
* [Web][52]

### Protokoll überprüfen

Um sich zu vergewissern, dass die Ereigniseigenschaften erfolgreich nachverfolgt wurden, können Sie alle Ereigniseigenschaften auf der Seite **Benutzerdefinierte Ereignisse** anzeigen.

1. Navigieren Sie zu **Dateneinstellungen** > **Benutzerdefinierte Ereignisse**.
2. Suchen Sie Ihr benutzerdefiniertes Ereignis in der Liste.
3. Klicken Sie für Ihr Ereignis auf **Eigenschaften verwalten**. Dies zeigt Ihnen die Namen der Eigenschaften an, die mit einem Ereignis verbunden sind.

### Werte überprüfen

Nachdem Sie Ihren Benutzer als Testbenutzer hinzugefügt haben, folgen Sie diesen Schritten, um Ihre Werte zu überprüfen: 

1. Führen Sie das benutzerdefinierte Ereignis innerhalb der App aus.
2. Warten Sie etwa 10 Sekunden, bis die Daten geleert wurden.
3. Aktualisieren Sie das [Ereignisbenutzerprotokoll][24], um das benutzerdefinierte Ereignis und den Wert der Ereigniseigenschaft, die mit ihm übergeben wurde, anzuzeigen.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 10\. April 2023_

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/ 
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
