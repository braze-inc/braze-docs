---
nav_title: Schlüssel-Werte-Paare
article_title: In-App Nachrichten Schlüssel-Wert-Paare für das Internet
platform: Web
channel: in-app messages
page_order: 9
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie In-App-Nachricht-Schlüssel-Wert-Paare nutzen können, um Informationen für Ihre Internet-Anwendung anzuzeigen."

---

# Schlüssel-Wert-Paare

> In diesem Artikel erfahren Sie, wie Sie In-App-Nachricht-Schlüssel-Wert-Paare nutzen können, um Informationen für Ihre Internet-Anwendung anzuzeigen.

In-App-Nachricht-Objekte können Schlüssel-Wert-Paare als `extras`-Eigenschaft enthalten. Sie werden auf dem Dashboard unter **Einstellungen** festgelegt, wenn Sie eine In-App-Nachricht-Kampagne erstellen. Diese können verwendet werden, um Daten mit einer In-App-Nachricht zur weiteren Bearbeitung durch Ihre Website zu senden. Zum Beispiel:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
