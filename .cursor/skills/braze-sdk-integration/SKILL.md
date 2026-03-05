---
name: braze-sdk-integration
description: Supports initial Braze SDK setup and baseline configuration across Web, React Native, iOS, and Android. Use when you need help finding setup credentials, validating endpoint format, and creating starter configuration files.
---

# Braze SDK setup skill

Use this skill when helping users complete initial Braze SDK setup and baseline configuration.
For deeper implementation and production debugging, use the Braze Docs MCP server. For setup steps, see [Building with an LLM](https://www.braze.com/docs/developer_guide/getting_started/build_with_llm).

## When to use

Trigger this skill when the user mentions or asks about:

- **Braze SDK setup** across Web, React Native, iOS, or Android
- **Setup credentials** (finding the API key and SDK endpoint)
- **Endpoint format validation** (for example, `sdk.iad-01.braze.com`)
- **Starter configuration files** (`res/values/braze.xml` or `BrazeConfig.ts`)
- **First-run setup checks** (initialization order and session start basics)

## Instructions

### Initial setup checklist

1. **Discover API key and endpoint**
   - In the Braze dashboard, go to **Settings** > **App Settings** (or **Manage Settings**).
   - Copy the **API Key** (sometimes labeled "App Identifier" or "SDK Key") for the correct app.
   - Copy the **SDK Endpoint** from the same page or from [Braze SDK endpoints](https://www.braze.com/docs/user_guide/administrative/access_braze/sdk_endpoints/). Format is `sdk.<cluster>.braze.com` (e.g. `sdk.iad-01.braze.com`). Do **not** include `https://`.
   - Logging in at [dashboard.braze.com](https://dashboard.braze.com) routes to the correct cluster.

2. **Install the SDK** for the target platform (package manager, CocoaPods/SPM, Gradle, etc.) per the [Integrate the Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/) docs.

3. **Configure the SDK** with the API key and endpoint using the platform-specific blocks below.

4. **Lifecycle and session**
   - Call session/open-session logic after configuration (e.g. `braze.openSession()` on Web, or rely on automatic session handling on mobile).
   - For in-app messages to show automatically (Web), call `braze.automaticallyShowInAppMessages()` before `openSession()`.

5. **Optional**: Run the `scripts/validate_setup.py` utility (see [Utility scripts](#utility-scripts)) to validate the endpoint format and generate a boilerplate config file.

### Utility scripts

**validate_setup.py**: Validates SDK endpoint format and generates a starter config file. Detects Android (Gradle) or Web (package.json) and writes `res/values/braze.xml` or `BrazeConfig.ts` accordingly. Run from the app project root:

```bash
python3 .cursor/skills/braze-sdk-integration/scripts/validate_setup.py
```

The agent may run this script when helping with initial setup. The script prompts for API key and endpoint interactively.

### Platform-specific configuration

**Web** (`braze.initialize`):

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",  // e.g. sdk.iad-01.braze.com
  enableLogging: false,
  allowUserSuppliedJavascript: false,  // set true for HTML in-app messages
});

braze.automaticallyShowInAppMessages();
if (isLoggedIn) braze.changeUser(userIdentifier);
braze.openSession();
```

**Android** (`res/values/braze.xml`):

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_SDK_ENDPOINT</string>
</resources>
```

**iOS (Swift)** (`Braze.Configuration`):

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-SDK-ENDPOINT"
)
let braze = Braze(configuration: configuration)
```

### Standard analytics

Use this section as a handoff checklist after setup. For full implementation details, use platform-specific documentation.

- **Identify user (when ID changes only)**: `changeUser(userId)` (Web: `braze.changeUser(userId)`; iOS/Android equivalent per platform docs). Call only when the logged-in user or anonymous→identified transition happens; do not call on every launch with the same ID.
- **Custom events**: `logCustomEvent(eventName, eventProperties)` (property keys/values per platform).
- **Purchases**: `logPurchase(productId, currency, price, quantity, properties?)`. **Mandatory fields**: `productId` (string), `currency` (e.g. `"USD"`), `price` (number). Quantity is typically 1 if omitted; optional properties object for metadata. Empty `productId` will not log the purchase.

### Setup troubleshooting

Use this section for setup blockers only. For runtime behavior issues after setup, use the platform-specific troubleshooting guides.

- **SDK Debugger**: Use the [Braze SDK Debugger](https://www.braze.com/docs/developer_guide/sdk_integration/debugging/) (Braze dashboard → **Settings** → **Setup and Testing** → **SDK Debugger**) to inspect sessions, events, and user state without enabling verbose logging in the app.
- **Verbose logging**: For deeper investigation, enable [verbose logging](https://www.braze.com/docs/developer_guide/sdk_integration/verbose_logging/) in the SDK (e.g. Web: `enableLogging: true`; iOS: `configuration.logger.level = .debug`; Android: per-doc logging level). Use sparingly in production.
- **Common issues**: Wrong endpoint format (no `https://`), missing `openSession()` or equivalent, calling `changeUser` too often, or missing required purchase fields (`productId`, `currency`, `price`).

## Best practices

1. **`changeUser`**
   - Call only when the user identity actually changes (e.g. login, or switching accounts). Do not call on every app launch with the same ID; this can create duplicate or orphaned profiles and affect MAU.

2. **Critical events**
   - After logging high-value or time-sensitive events (e.g. purchase, signup), call `requestImmediateDataFlush()` (or platform equivalent) so data is sent to Braze immediately instead of waiting for the next batch.

3. **HTML in-app messages (Web)**
   - To support HTML in-app messages that can execute JavaScript, set `allowUserSuppliedJavascript: true` in `braze.initialize()` options. Enable only if you need HTML/JS messages; Braze requires this opt-in for security.

4. **Lifecycle**
   - Initialize once, then use the same Braze instance. Call session/open methods after `changeUser` and in-app message setup (e.g. on Web, call `openSession()` last).

5. **References**
   - Official integration guide: [Integrate the Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/)
   - SDK endpoints: [API and SDK endpoints](https://www.braze.com/docs/user_guide/administrative/access_braze/sdk_endpoints/)
   - User lifecycle: [User profile lifecycle](https://www.braze.com/docs/user_guide/data/unification/user_data/user_profile_lifecycle/)
