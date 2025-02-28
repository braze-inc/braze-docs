---
nav_title: Ausblenden von Nachrichten
article_title: Ausblenden von In-App-Nachrichten für Web
platform: Web
channel: in-app messages
page_order: 2
page_type: reference
description: "Dieser Artikel behandelt die Kündigung von In-App-Nachrichten für Ihre Internet-Anwendung."

---

# Ausblenden von Nachrichten

> In diesem Artikel erfahren Sie, wie Sie In-App-Nachrichten für Ihre Internet-Anwendung ablehnen können.

Standardmäßig wird eine In-App-Nachricht durch Drücken des Escape-Buttons oder durch einen Klick auf den ausgegrauten Hintergrund der Seite verworfen, wenn sie angezeigt wird. Konfigurieren Sie die `requireExplicitInAppMessageDismissal` [-Initialisierungsoption](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) auf `true`, um dieses Verhalten zu verhindern und einen expliziten Klick auf einen Button zu verlangen, um Nachrichten zu schließen. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

