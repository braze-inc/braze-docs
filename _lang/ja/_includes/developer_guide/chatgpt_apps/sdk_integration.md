# ChatGPTアプリの統合

## 設定

### ステップ 1: Brazeの統合ファイルを取得する

[ChatGPTアプリ統合リポジトリ](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts)からファイルを`braze.js`プロジェクトにコピーせよ。このファイルには、必要なすべてのBraze SDK設定と補助関数が含まれている。

### ステップ 2:依存関係をインストールする

Brazeの最新機能を利用するには、当社のWeb SDKを導入せよ。

**クライアントサイド統合については：**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## 実装

BrazeをChatGPTアプリに統合する方法は、ユースケースに応じて2通りある：

### クライアントサイド統合（カスタムウィジェット）

{% alert tip %}
**推奨されるアプローチ：**この方法により、ChatGPTアプリウィジェット内でリッチなメッセージング体験とリアルタイムのユーザーインタラクショントラッキングが可能になる。
{% endalert %}

カスタムChatGPTアプリウィジェット内でBrazeメッセージングを表示し、ユーザーインタラクションをトラッキングするには、Web SDK統合を使用する。完全なメッセージングの例は[、こちらの](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox)サンプルリポジトリで見つけることができる。

#### ウィジェットのメタデータを設定する

MCPサーバーファイルに以下のメタデータを追加し、Brazeドメインを許可する。CDNドメインは[地域](https://www.braze.com/docs/developer_guide/platforms/web/content_security_policy)に応じて更新すること：

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

実際のBraze SDKエンドポイントで`YOUR-SDK-ENDPOINT`置き換える。

#### useBrazeフックを設定する

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

#### Brazeコンテンツカードを表示する

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

#### ウィジェットのイベントのトラッキング

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

### サーバーサイド統合（MCPサーバー）

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
MCPサーバー上でメッセージング機能のサーバーサイド統合も必要なら、に連絡せよ<span style="white-space:nowrap;">`mcp-product@braze.com`</span>。MCPサーバーからのイベントや購入のトラッキング, 追跡には、当社の[REST API]({{site.baseurl}}/api/home)を使用する。

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
