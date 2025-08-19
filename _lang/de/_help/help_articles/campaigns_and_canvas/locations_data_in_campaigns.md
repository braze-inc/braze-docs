---
nav_title: Prüfen von Standort Daten
article_title: Prüfen von Standort Daten
page_order: 1
page_type: solution
description: "Dieser Hilfeartikel führt Sie durch Schnellprüfungen, die Ihnen helfen können, wenn keine Nutzer:innen über Standorte verfügen."
tool: Location
---

# Prüfen von Standort-Daten

Braze erfasst den letzten Standort eines Nutzers:innen standardmäßig über sein SDK. Das bedeutet in der Regel, dass der "letzte Standort" der Standort ist, von dem aus Ihr Nutzer:innen Ihre App zuletzt genutzt hat. Wenn Sie Braze Standortdaten im Hintergrund senden, stehen Ihnen möglicherweise detailliertere Daten zur Verfügung.

Wenn keine Nutzer:innen über Standorte verfügen, können Sie die Datenerfassung und die Datumsübertragung mit zwei schnellen Prüfungen bestätigen.

## Datenerfassung

Bestätigen Sie, dass Ihre App Standortdaten sammelt:

- Für iOS bedeutet dies, dass Nutzer:innen an einem bestimmten Punkt der User Journey über eine Abfrage die Freigabe ihrer Standortdaten bestätigen. 
- Für Android stellen Sie sicher, dass Ihre App bei der Installation nach den Berechtigungen für feine oder grobe Standorte fragt.

Um zu sehen, ob Nutzer:innen Standortdaten an Braze gesendet werden, verwenden Sie den Filter **Standort verfügbar**. Mit diesem Filter können Sie den Prozentsatz der Nutzer:innen mit "jüngstem Standort" sehen.

![]({% image_buster /assets/img_archive/trouble7.png %})

## Übertragung von Daten

Bestätigen Sie, dass Ihre Entwickler:in Standortdaten an Braze weitergeben. Normalerweise erfolgt die Weitergabe von Standort-Daten automatisch durch das SDK, nachdem der Nutzer die entsprechenden Berechtigungen erteilt hat. Möglicherweise haben Ihre Entwickler:in jedoch das Standort-Tracking in Braze deaktiviert. Weitere Informationen zum Standort-Tracking finden Sie unter:
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 16\. November 2022_

