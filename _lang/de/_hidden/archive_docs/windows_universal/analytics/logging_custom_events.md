---
nav_title: Tracking angepasster Events
article_title: Tracking angepasster Events für Windows Universal
platform: Windows Universal
page_order: 2
description: "Dieser referenzierte Artikel beschreibt, wie Sie angepasste Events auf der Windows Universal Plattform tracken können."
hidden: true
---

# Tracking angepasster Events
{% multi_lang_include archive/windows_deprecation.md %}

Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen auf dem Dashboard zu segmentieren. Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/) vertraut zu machen.

Alle Ereignisse werden mit Hilfe der Eigenschaft `EventLogger` protokolliert, die in IAppboy enthalten ist. Um einen Verweis auf `EventLogger` zu erhalten, rufen Sie `Appboy.SharedInstance.EventLogger` auf. Sie können die folgenden Methoden verwenden, um wichtige Nutzer:innen-Aktionen und angepasste Events zu verfolgen:

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
