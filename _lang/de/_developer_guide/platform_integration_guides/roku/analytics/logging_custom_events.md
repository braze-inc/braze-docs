---
nav_title: Verfolgen von benutzerdefinierten Ereignissen
article_title: Tracking von angepassten Events für Roku
platform: Roku
page_order: 2
page_type: reference
description: "Diese Seite beschreibt die Methoden zur Aufzeichnung angepasster Events für Roku über das Braze SDK."

---

# Tracking von angepassten Events

> Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen auf dem Dashboard zu segmentieren. Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

## Hinzufügen eines angepassten Events

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```

### Hinzufügen von Eigenschaften

Sie können Metadaten zu angepassten Events hinzufügen, indem Sie ein mit Eigenschaften-Wörterbuch mit Ihrem angepassten Event übergeben.

Eigenschaften werden als Schlüssel-Werte-Paare definiert.  Die Schlüssel sind Objekte des Typs `String` und die Werte können ein `String` oder `Integer` sein.

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
