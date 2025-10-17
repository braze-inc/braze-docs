# ChatGPT App Integration

## Setup

### 1. Get the Braze Integration File

Copy the `braze.js` file from our [ChatGPT Apps integration repository](https://github.com/braze-inc/chatgpt-apps-braze-integration) to your project. This file contains all the necessary Braze SDK configuration and helper functions.

### 2. Install Dependencies

The SDK you need depends on your integration approach:

**For Client-Side Integration (Recommended):**
```bash
npm install @braze/web-sdk
```

**For Server-Side Integration:**
```bash
npm install @braze/javascript-sdk
```

The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [Beta](https://www.braze.com/company/legal/beta-terms).

## Implementation

There are two ways to integrate Braze with your ChatGPT App depending on your use case:

### Client-Side Integration (Custom Widgets) - Recommended

{% alert tip %}
**Recommended Approach**: This method enables rich messaging experiences and real-time user interaction tracking within your ChatGPT App widgets.
{% endalert %}

For displaying Braze messaging and tracking user interactions within your custom ChatGPT App widgets, use the Web SDK integration.

#### Configure Widget Metadata

Add the following metadata to your MCP server file to allow Braze domains:

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

Replace `YOUR-SDK-ENDPOINT` with your actual Braze SDK endpoint.

#### Set Up the useBraze Hook

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

#### Display Braze Content Cards

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

#### Track Widget Events

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

### Server-Side Integration (MCP Server)

For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT App requests and tool calls.

#### Import the Braze Functions

```javascript
// Import the desired methods from wherever you saved the file
import { BrazeSessionInfo, logCustomEvent, logPurchase } from "./braze/braze.js";
```

#### Set Up Session Information

```javascript
// Create session info for Braze
const brazeSessionInfo: BrazeSessionInfo = {
  userId: userId,
  sessionId: sessionId || "default-session"
};
```

#### Track User Interactions

```javascript
// Log custom events for user interactions
await logCustomEvent(brazeSessionInfo, "chatgpt_app_interaction", {
  app_id: "your_chatgpt_app_id",
  tool_name: request.params.name,
  user_authenticated: userId !== "anonymous",
  timestamp: new Date().toISOString()
});
```

#### Track Purchases and Transactions

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
Use the [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to verify your integration and troubleshoot any issues.
{% endalert %}
