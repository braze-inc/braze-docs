# ChatGPT 앱 통합

## 설정

### 1단계: Braze 통합 파일 받기

[ChatGPT 앱 통합 리포지토리에서](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) `braze.js` 파일을 프로젝트에 복사하세요. 이 파일에는 필요한 모든 Braze 소프트웨어 개발 키트 구성 및 도우미 기능이 포함되어 있습니다.

### 2단계: 설치 종속성

Braze의 최신 기능 세트를 위한 웹 소프트웨어 개발 키트를 설치하세요:

**클라이언트 측 통합용:**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Implementation

사용 사례에 따라 두 가지 방법으로 Braze를 ChatGPT 앱과 통합할 수 있습니다:

### 클라이언트 측 통합(커스텀 위젯)

{% alert tip %}
**권장 접근 방식:** 이 방법을 사용하면 ChatGPT 앱 위젯 내에서 풍부한 메시징 경험과 실시간 사용자 상호작용 추적이 가능합니다.
{% endalert %}

커스텀 ChatGPT 앱 위젯 내에서 Braze 메시징을 표시하고 사용자 상호작용을 추적하려면 웹 SDK 통합을 사용하세요. 전체 메시징 예제는 [여기에서](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox) 샘플 리포지토리에서 확인할 수 있습니다.

#### 위젯 메타데이터 구성

MCP 서버 파일에 다음 메타데이터를 추가하여 Braze 도메인을 허용하고 [지역에](https://www.braze.com/docs/developer_guide/platforms/web/content_security_policy) 따라 CDN 도메인을 업데이트하세요:

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

`YOUR-SDK-ENDPOINT` 을 실제 Braze SDK 엔드포인트로 바꿉니다.

#### 사용브레이즈 후크 설정

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

#### Braze 콘텐츠 카드 표시하기

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

#### 위젯 이벤트 추적

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

### 서버 측 통합(MCP 서버)

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
MCP 서버에서 이벤트 및 구매를 추적하려면 [REST API를](https://www.braze.com/docs/api/home) 사용하세요. MCP 서버에 메시징 기능도 필요한 경우 [지원 케이스로](https://support.braze.com/login) 문의하세요.

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
