{% multi_lang_include developer_guide/prerequisites/web.md %}

## Angepasste Stile

Die UI-Elemente von Braze sind standardmäßig so gestaltet, dass sie ein neutrales In-App-Nachricht-Erlebnis bieten und die Konsistenz mit anderen mobilen Plattformen von Braze gewährleisten. Die Standard Stile von Braze sind in CSS im Braze SDK definiert. 

### Einstellen eines Standard-Stils

Indem Sie ausgewählte Stile in Ihrer Anwendung außer Kraft setzen, können Sie unsere standardmäßigen In-App-Nachrichtentypen mit Ihren eigenen Hintergrundbildern, Schriftfamilien, Stilen, Größen, Animationen und vielem mehr anpassen. 

Im Folgenden finden Sie ein Beispiel für eine Überschreibung, die bewirkt, dass die Kopfzeilen einer In-App-Nachricht kursiv dargestellt werden:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

In den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) finden Sie weitere Informationen.

### Anpassen des Z-Index

In-App-Nachrichten werden standardmäßig über `z-index: 9001` angezeigt. Dies lässt sich in `inAppMessageZIndex ` mit der Option [initialization](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) konfigurieren, falls Ihre Website Elemente mit höheren Werten als diesem stilisiert.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Dieses Feature ist nur für Internet Braze SDK v3.3.0 und höher verfügbar.
{% endalert %}

## Anpassen von Nachrichtenabweisungen

Standardmäßig wird eine In-App-Nachricht durch Drücken des Escape-Buttons oder durch einen Klick auf den ausgegrauten Hintergrund der Seite verworfen, wenn sie angezeigt wird. Konfigurieren Sie die `requireExplicitInAppMessageDismissal` [-Initialisierungsoption](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) auf `true`, um dieses Verhalten zu verhindern und einen expliziten Klick auf einen Button zu verlangen, um Nachrichten zu schließen. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Öffnen von Links in einem neuen Tab

Um festzulegen, dass Ihre In-App-Nachricht-Links in einem neuen Tab geöffnet werden, setzen Sie die Option `openInAppMessagesInNewTab` auf `true`, um zu erzwingen, dass alle Links von In-App-Nachrichten-Klicks in einem neuen Tab oder Fenster geöffnet werden.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
