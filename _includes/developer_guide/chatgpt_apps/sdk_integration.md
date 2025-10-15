# ChatGPT App Integration

## Setup

### 1. Get the Braze Integration File

Copy the `braze.js` file from our [ChatGPT Apps integration repository](https://github.com/braze-inc/chatgpt-apps-braze-integration) to your project. This file contains all the necessary Braze SDK configuration and helper functions.

### 2. Install Dependencies

The Braze JavaScript SDK provides the core functionality for tracking user events and sending data to Braze. It's primarily designed for headless (server-side) environments, making it perfect for ChatGPT Apps integration. Note that this SDK is currently in [Beta](https://www.braze.com/company/legal/beta-terms).

```bash
npm install @braze/javascript-sdk
```

## Implementation

The following code snippets should be added to your MCP server file (typically `server.js` or `server.ts`) where you handle ChatGPT App requests and tool calls. These snippets show how to integrate Braze tracking into your existing server logic.

### Import the Braze Functions

```javascript
// Import the desired methods from wherever you saved the file
import { BrazeSessionInfo, logCustomEvent, logPurchase } from "./braze/braze.js";
```

### Set Up Session Information

```javascript
// Create session info for Braze
const brazeSessionInfo: BrazeSessionInfo = {
  userId: userId,
  sessionId: sessionId || "default-session"
};
```

### Track User Interactions

```javascript
// Log custom events for user interactions
await logCustomEvent(brazeSessionInfo, "chatgpt_app_interaction", {
  app_id: "your_chatgpt_app_id",
  tool_name: request.params.name,
  user_authenticated: userId !== "anonymous",
  timestamp: new Date().toISOString()
});
```

### Track Purchases and Transactions

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

<!-- ### Handle Authentication Context

```javascript
// Extract user info from authentication
const authHeader = req.headers.authorization;
const token = AuthService.extractTokenFromHeader(authHeader);
let userInfo = null;

if (token) {
  userInfo = AuthService.validateToken(token);
}

// Convert to Braze-compatible format
const serverUserInfo = userInfo ? {
  userId: userInfo.userId,
  userEmail: userInfo.email,
  userName: userInfo.name
} : undefined;
``` -->

### Track Conversation Events

```javascript
// When a user starts a conversation
await logCustomEvent(brazeSessionInfo, "conversation_started", {
  app_id: "your_chatgpt_app_id",
  user_input_length: userMessage.length,
  timestamp: new Date().toISOString()
});

// When AI provides a response
await logCustomEvent(brazeSessionInfo, "ai_response_generated", {
  response_length: aiResponse.length,
  response_time_ms: responseTime,
  model_used: "gpt-4"
});
```

{% alert tip %}
Use the [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to verify your integration and troubleshoot any issues.
{% endalert %}
