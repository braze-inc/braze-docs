---
nav_title: Prüfen von Standortdaten
article_title: Prüfen von Standortdaten
page_order: 1
page_type: solution
description: "Dieser Hilfe-Artikel führt Sie durch schnelle Überprüfungen, die Ihnen helfen können, wenn keine Benutzer verfügbare Standorte haben."
tool: Location
---

# Überprüfung der Standortdaten

Braze erfasst über sein SDK standardmäßig den letzten Standort eines Benutzers. Das bedeutet in der Regel, dass der "letzte Standort" der Standort ist, von dem aus Ihr Nutzer Ihre App zuletzt genutzt hat. Wenn Sie Braze Standortdaten im Hintergrund senden, stehen Ihnen möglicherweise detailliertere Daten zur Verfügung.

Wenn keine Benutzer über verfügbare Standorte verfügen, können Sie die Datenerfassung und die Datumsübertragung mit zwei schnellen Prüfungen bestätigen.

## Datenerfassung

Bestätigen Sie, dass Ihre App Standortdaten sammelt:

- Für iOS bedeutet dies, dass die Nutzer an einem bestimmten Punkt der User Journey über eine Abfrage zustimmen, ihre Standortdaten zu teilen. 
- Bei Android stellen Sie sicher, dass Ihre App bei der Installation um die Erlaubnis für einen guten oder groben Standort bittet.

Um zu sehen, ob Standortdaten des Benutzers an Braze gesendet werden, verwenden Sie den Filter **Standort verfügbar**. Mit diesem Filter können Sie den Prozentsatz der Nutzer mit einem "letzten Standort" sehen.

![][25]

## Datenübertragung

Bestätigen Sie, dass Ihre Entwickler Standortdaten an Braze weitergeben. Normalerweise wird die Weitergabe von Standortdaten automatisch vom SDK vorgenommen, nachdem der Benutzer die entsprechenden Berechtigungen erteilt hat, aber möglicherweise haben Ihre Entwickler die Standortverfolgung in Braze deaktiviert. Weitere Informationen zur Standortverfolgung finden Sie unter:
- [Android][26]
- [iOS][27]
- [Web][28]

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 16\. November 2022_

[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
