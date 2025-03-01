---
nav_title: Testen Sie Ihre Basis-Integration
article_title: Testen Sie Ihre Basis-Integration für Android und FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Dieser referenzierte Artikel beschreibt, wie Sie Ihre grundlegende Integration für Ihre Android- oder FireOS-Anwendung testen können."

---

# Testen Sie Ihre grundlegende Integration

> Dieser referenzierte Artikel beschreibt, wie Sie Ihre grundlegende Integration für Ihre Android- oder FireOS-Anwendung testen können.

## Bestätigen Sie, dass das Session-Tracking funktioniert

Jetzt sollte das Session-Tracking in Ihrer Braze Integration funktionieren. Um dies zu testen, gehen Sie zur **Übersicht**, wählen Sie Ihre Anwendung aus dem Dropdown-Menü für den Namen der ausgewählten App (standardmäßig "Alle Apps") und setzen Sie **Daten anzeigen für** auf "Heute". Öffnen Sie dann Ihre App und aktualisieren Sie die Seite - Ihre wichtigsten Metriken sollten sich alle um 1 erhöht haben.

![]({% image_buster /assets/img_archive/android_sessions.png %})

Sie sollten Ihre Integration weiter testen, indem Sie durch Ihre Anwendung navigieren und sicherstellen, dass nur eine Sitzung protokolliert wurde. Stellen Sie die App dann für mindestens 10 Sekunden in den Hintergrund und holen Sie sie wieder in den Vordergrund. Standardmäßig wird eine neue Sitzung erstellt, wenn die App in den Vordergrund geholt wird, nachdem sie länger als 10 Sekunden im Hintergrund war oder geschlossen wurde. Nachdem Sie dies getan haben, bestätigen Sie, dass eine weitere Sitzung protokolliert wurde.

## Debugging des Session-Tracking
Wenn sich das Session-Tracking unerwartet verhält, schalten Sie die [ausführliche Protokollierung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#enabling-logs) ein und beobachten Sie Ihre App, während Sie die Schritte zum Triggern der Sitzung nachvollziehen. Beobachten Sie die Braze-Anweisungen in logcat, um herauszufinden, wo Sie die Protokollierung von `openSession`- und `closeSession`-Aufrufen in Ihren Aktivitäten verpasst haben.

