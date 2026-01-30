# Integração do app ChatGPT

## Configuração

### Etapa 1: Obtenha o arquivo de integração do Braze

Copie o arquivo `braze.js` do nosso [repositório de integração de apps ChatGPT](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) para o seu projeto. Esse arquivo contém todas as funções auxiliares e de configuração do Braze SDK necessárias.

### Etapa 2: Instalar dependências

Instale nosso Web SDK para obter o conjunto mais atualizado de recursos do Braze:

**Para integração lado a lado com o cliente:**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Implementação

Há duas maneiras de integrar o Braze ao seu app ChatGPT, dependendo do seu caso de uso:

### Integração lado a lado com o cliente (widgets personalizados)

{% alert tip %}
**Abordagem recomendada:** Esse método ativa experiências ricas de mensagens e rastreamento da interação do usuário em tempo real nos widgets do seu app ChatGPT.
{% endalert %}

Para exibir as mensagens do Braze e rastrear as interações dos usuários nos widgets personalizados do seu app ChatGPT, use a integração do SDK da Web. Um exemplo completo de envio de mensagens pode ser encontrado em nosso repositório de amostras [aqui](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox).

#### Configurar metadados do widget

Adicione os seguintes metadados ao arquivo do servidor MCP para permitir domínios do Braze, certificando-se de atualizar o domínio CDN com base em [sua região](https://www.braze.com/docs/developer_guide/platforms/web/content_security_policy):

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

Substitua `YOUR-SDK-ENDPOINT` por seu endpoint real do SDK do Braze.

#### Configurar o gancho useBraze

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

#### Exibir cartões de conteúdo do Braze

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

#### Rastreamento de eventos do widget

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

### Integração lado a lado com o servidor (servidor MCP)

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
Se também precisar de uma integração lado a lado do servidor para a funcionalidade de envio de mensagens no seu servidor MCP, entre em contato com <span style="white-space:nowrap;">`mcp-product@braze.com`</span>. Para rastreamento de eventos e compras de seu servidor MCP, use nossa [API REST]({{site.baseurl}}/api/home).

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
