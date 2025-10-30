# Integration der ChatGPT App

## Einrichtung

### Schritt 1: Holen Sie sich die Braze-Integrationsdatei

Kopieren Sie die Datei `braze.js` aus unserem [Repository für die Integration von ChatGPT Apps](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) in Ihr Projekt. Diese Datei enthält alle notwendigen Konfigurations- und Hilfsfunktionen des Braze SDK.

### Schritt 2: Abhängigkeiten installieren

Installieren Sie unser Web SDK, um die aktuellsten Features von Braze zu nutzen:

**Für die Client-seitige Integration:**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Implementierung

Es gibt zwei Möglichkeiten, Braze in Ihre ChatGPT App zu integrieren, abhängig von Ihrem Anwendungsfall:

### Client-seitige Integration (angepasste Widgets)

{% alert tip %}
**Empfohlene Vorgehensweise:** Diese Methode ermöglicht reichhaltige Messaging-Erlebnisse und Realtime Tracking der Nutzer:innen-Interaktion innerhalb Ihrer ChatGPT App-Widgets.
{% endalert %}

Für die Anzeige von Braze Messaging und das Tracking von Nutzer:innen innerhalb Ihrer angepassten ChatGPT App-Widgets verwenden Sie die Web SDK-Integration. Ein vollständiges Beispiel für Messaging finden Sie in unserem Beispiel-Repository [hier](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox).

#### Widget-Metadaten konfigurieren

Fügen Sie die folgenden Metadaten zu Ihrer MCP Server-Datei hinzu, um Braze Domains zuzulassen, und stellen Sie sicher, dass Sie die CDN Domain entsprechend Ihrer [Region](https://www.braze.com/docs/developer_guide/platforms/web/content_security_policy) aktualisieren:

```javascript
"openai/widgetCSP": {
  connect_domains: ["https://YOUR-SDK-ENDPOINT"],
  resource_domains: [
    "https://appboy-images.com",
    "https://braze-images.com",
    "https://cdn.braze.eu",
    "https://use.fontawesome.com"
  ],
}
```

Ersetzen Sie `YOUR-SDK-ENDPOINT` durch Ihren tatsächlichen Braze SDK-Endpunkt.

#### Richten Sie den useBraze-Haken ein

```javascript
import { useBraze } from "./utils/braze";

function YourWidget() {
  const braze = useBraze({
    apiKey: "your-braze-api-key",
    baseUrl: "your-braze-endpoint.braze.com",
  });

  useEffect(() => {
    if (!braze.isInitialized) {
      return;
    }

    // Set user identity
    braze.changeUser("user-id-123");
    
    // Log widget interactions
    braze.logCustomEvent("viewed_pizzaz_list");
  }, [braze.isInitialized]);

  return (
    // Your widget JSX
  );
}
```

#### Braze Content-Cards anzeigen

```javascript
const [cards, setCards] = useState([]);

useEffect(() => {
  // Get cached content cards
  setCards(braze.getCachedContentCards()?.cards ?? []);

  // Subscribe to content card updates
  braze.subscribeToContentCardsUpdates((contentCards) => {
    setCards(contentCards.cards);
  });

  // Open session
  braze.openSession();

  return () => {
    braze.removeAllSubscriptions();
  }
}, []);
```

#### Tracking von Widget-Ereignissen

```javascript
// Track user interactions within your widget
const handleButtonClick = () => {
  braze.logCustomEvent("widget_button_clicked", {
    button_type: "save_list",
    widget_name: "pizza_list"
  });
};

const handleItemInteraction = (itemId) => {
  braze.logCustomEvent("item_interacted", {
    item_id: itemId,
    interaction_type: "view_details"
  });
};
```

### Server-seitige Integration (MCP Server)

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
Für das Tracking von Ereignissen und Käufen auf Ihrem MCP Server verwenden Sie unsere [REST API](https://www.braze.com/docs/api/home). Wenn Sie auf Ihrem MCP Server auch Messaging-Funktionen benötigen, wenden Sie sich bitte mit einem [Support-Fall](https://support.braze.com/login) an uns.

<!-- #### Import the Braze functions

```javascript
// Import the desired methods from wherever you saved the file
import { BrazeSessionInfo, logCustomEvent, logPurchase } from "./braze/braze.js";
```

#### Set up session information

```javascript
// Create session info for Braze
const brazeSessionInfo: BrazeSessionInfo = {
  userId: userId,
  sessionId: sessionId || "default-session"
};
```

#### Track user interactions

```javascript
// Log custom events for user interactions
await logCustomEvent(brazeSessionInfo, "chatgpt_app_interaction", {
  app_id: "your_chatgpt_app_id",
  tool_name: request.params.name,
  user_authenticated: userId !== "anonymous",
  timestamp: new Date().toISOString()
});
```

#### Track purchases and transactions

```javascript
// Calculate order details for purchases
const totalPrice = examplePriceMethod(args.size, args.quantity);
const orderId = `ORDER-${Date.now()}`;

// Define the purchase properties you'd like to use
const purchaseProperties = {
  orderId,
  customerName: args.customerName,
  size: args.size,
  quantity: args.quantity,
  deliveryAddress: args.deliveryAddress,
  specialInstructions: args.specialInstructions,
  estimatedTime,
  totalPrice
};

// Log the purchase to Braze
await logPurchase(
  brazeSessionInfo, 
  "pizza", 
  totalPrice, 
  "USD", 
  args.quantity, 
  purchaseProperties
);
```

{% alert tip %}
Use the [SDK debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to verify your integration and troubleshoot any issues.
{% endalert %} -->
