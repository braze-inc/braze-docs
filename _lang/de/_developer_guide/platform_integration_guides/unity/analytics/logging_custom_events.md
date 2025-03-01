---
nav_title: Verfolgen von benutzerdefinierten Ereignissen
article_title: Tracking von angepassten Events für Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Events auf der Unity-Plattform protokollieren können."

---

# Tracking von angepassten Events

> Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen auf dem Dashboard zu segmentieren.

Sehen Sie sich vor der Implementierung unbedingt in unseren [Best Practices][4] die Beispiele für die Segmentierungsoptionen von angepassten Events, angepassten Attributen und Kauf-Events an. Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

```csharp
AppboyBinding.LogCustomEvent("event name");
```

Braze unterstützt auch das Hinzufügen von Metadaten über angepasste Events durch Übergabe eines `Dictionary` von Event-Eigenschaften:

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## REST API

Sie können auch unsere REST API verwenden, um Events aufzuzeichnen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer][5].

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
