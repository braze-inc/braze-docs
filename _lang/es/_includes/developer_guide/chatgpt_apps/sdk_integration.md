# Integración de la aplicación ChatGPT

## Configurar

### Paso 1: Obtén el archivo de integración Braze

Copia el archivo `braze.js` de nuestro [repositorio de integración de aplicaciones ChatGPT](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) a tu proyecto. Este archivo contiene todas las funciones de configuración y ayuda necesarias del SDK de Braze.

### Paso 2: Instalar dependencias

Instala nuestro SDK Web para obtener el conjunto de características más actualizadas de Braze:

**Para la integración en paralelo con el cliente:**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Aplicación

Hay dos formas de integrar Braze con tu aplicación ChatGPT dependiendo de tu caso de uso:

### Integración del lado del cliente (widgets personalizados)

{% alert tip %}
**Enfoque recomendado:** Este método habilita experiencias de mensajería enriquecidas y seguimiento de la interacción del usuario en tiempo real dentro de los widgets de tu aplicación ChatGPT.
{% endalert %}

Para mostrar mensajes Braze y hacer un seguimiento de las interacciones de los usuarios dentro de los widgets personalizados de tu aplicación ChatGPT, utiliza la integración de SDK Web. Puedes encontrar un ejemplo completo de mensajería en nuestro repositorio de muestras [aquí](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox).

#### Configurar los metadatos del widget

Añade los siguientes metadatos al archivo de tu servidor MCP para permitir dominios Braze, asegurándote de actualizar el dominio CDN en función de [tu región](https://www.braze.com/docs/developer_guide/platforms/web/content_security_policy):

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

Sustituye `YOUR-SDK-ENDPOINT` por tu punto final SDK de Braze real.

#### Configura el gancho useBraze

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

#### Mostrar tarjetas de contenido Braze

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

#### Seguimiento de los eventos del widget

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

### Integración en paralelo con el servidor (servidor MCP)

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
Para el seguimiento de eventos y compras desde tu servidor MCP, utiliza nuestra [API REST](https://www.braze.com/docs/api/home). Si también necesitas funcionalidad de mensajería en tu servidor MCP, ponte en contacto con nosotros con un [caso de soporte](https://support.braze.com/login).

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
