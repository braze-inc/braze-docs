---
nav_title: Angepasste Stile
article_title: In-App-Nachricht Angepasster Stile für das Internet
platform: Web
channel: in-app messages
page_order: 1
page_type: reference
description: "Dieser Artikel behandelt das angepasste Stile von In-App-Nachricht für Ihre Internet-Anwendung."

---

# Angepasste Stile

> Die UI-Elemente von Braze sind standardmäßig so gestaltet, dass sie ein neutrales In-App-Nachricht-Erlebnis bieten und die Konsistenz mit anderen mobilen Plattformen von Braze gewährleisten. Die Standard-Stile von Braze sind in CSS im Braze SDK definiert. 

Indem Sie ausgewählte Stile in Ihrer Anwendung außer Kraft setzen, können Sie unsere standardmäßigen In-App-Nachrichtentypen mit Ihren eigenen Hintergrundbildern, Schriftfamilien, Stilen, Größen, Animationen und vielem mehr anpassen. 

Im Folgenden finden Sie ein Beispiel für eine Überschreibung, die bewirkt, dass die Kopfzeilen einer In-App-Nachricht kursiv dargestellt werden:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

In den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) finden Sie weitere Informationen.

## In-App-Nachricht Standard z-index

In-App-Nachrichten werden standardmäßig über `z-index: 9001` angezeigt. Dies lässt sich in `inAppMessageZIndex ` mit der Option [initialization](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) konfigurieren, falls Ihre Website Elemente mit höheren Werten als diesem stilisiert.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Diese Option wurde mit dem Internet SDK v3.3.0 eingeführt. Ältere SDKs müssen upgegradet werden, um diese Option nutzen zu können.
{% endalert %}

