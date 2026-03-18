# Intégration de l'application ChatGPT

## Configuration

### Étape 1 : Obtenir le fichier d'intégration Braze

Veuillez copier le`braze.js`fichier depuis notre [référentiel d'intégration des applications ChatGPT](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) vers votre projet. Ce fichier contient toutes les configurations et fonctions d'aide nécessaires au SDK Braze.

### Étape 2 : Veuillez installer les dépendances.

Veuillez installer notre SDK Web pour bénéficier des fonctionnalités les plus récentes de Braze :

**Pour l'intégration côté client :**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Mise en œuvre

Il existe deux méthodes pour réaliser l'intégration de Braze à votre application ChatGPT, en fonction de votre cas d'utilisation :

### Intégration côté client (widgets personnalisés)

{% alert tip %}
**Approche recommandée :** Cette méthode permet de bénéficier d'une expérience de communication enrichie et d'un suivi en temps réel des interactions des utilisateurs au sein des widgets de votre application ChatGPT.
{% endalert %}

Pour afficher les messages Braze et suivre les interactions des utilisateurs dans les widgets personnalisés de votre application ChatGPT, veuillez utiliser l'intégration SDK. Un exemple complet d'envoi de messages est disponible dans notre référentiel d'exemples [ici](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox).

#### Configurer les métadonnées du widget

Veuillez ajouter les métadonnées suivantes à votre fichier serveur MCP afin d'autoriser les domaines Braze, en veillant à mettre à jour le domaine du réseau de diffusion de contenu en fonction de [votre région](https://www.braze.com/docs/developer_guide/platforms/web/content_security_policy) :

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

Veuillez remplacer`YOUR-SDK-ENDPOINT`par votre endpoint SDK Braze réel.

#### Configurer le hook useBraze

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

#### Afficher les cartes de contenu Braze

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

#### Suivre les événements du widget

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

### Intégration côté serveur (serveur MCP)

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
Si vous avez également besoin d'une intégration côté serveur pour l'envoi de messages sur votre serveur MCP, veuillez contacter <span style="white-space:nowrap;">`mcp-product@braze.com`</span>. Pour suivre les événements et les achats depuis votre serveur MCP, veuillez utiliser notre [API REST]({{site.baseurl}}/api/home).

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
