---
nav_title: Verfolgen von benutzerdefinierten Ereignissen
article_title: Tracking von angepassten Events für das Internet
platform: Web
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie angepasste Events tracken und diesen Events Web-Eigenschaften hinzufügen können."

---

# Tracking von angepassten Events

> Sie können in Braze benutzerdefinierte Ereignisse aufzeichnen, um mehr über die Nutzungsmuster Ihrer App zu erfahren und Ihre Benutzer nach ihren Aktionen auf dem Dashboard zu segmentieren.

Sehen Sie sich vor der Implementierung unbedingt in unseren [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices) die Beispiele für die Segmentierungsoptionen von angepassten Events, angepassten Attributen und Kauf-Events an. Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) vertraut zu machen.

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

Siehe die Dokumentation zu [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) für weitere Informationen.

## Hinzufügen von Eigenschaften {#properties-events}

Sie können optional Metadaten über angepasste Events hinzufügen, indem Sie ein Objekt mit Eigenschaften mit Ihrem angepassten Event übergeben.

Eigenschaften werden als Schlüssel-Werte-Paare definiert. Die Schlüssel sind Strings und die Werte können `string`, `numeric`, `boolean`, oder [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) Objekte sein.

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

Weitere Informationen finden Sie in der [Dokumentation`logCustomEvent()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

