## About the Braze Vega SDK

The Braze Vega SDK lets you collect analytics and display rich in-app messages to your users. Most methods in the Braze Vega SDK are asynchronous and return promises that should be awaited or resolved.

## Integrating the Braze Vega SDK

### Step 1: Install the Braze library

Install the Braze Vega SDK using your preferred package manager.

{% tabs local %}
{% tab npm %}
If your project uses NPM, you can add the Braze Vega SDK as a dependency.

```bash
npm install @braze/vega-sdk --save
```

After installation, you can import the methods you need:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
If your project uses Yarn, you can add the Braze Vega SDK as a dependency.

```bash
yarn add @braze/vega-sdk
```

After installation, you can import the methods you need:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Step 2: Initialize the SDK

After the Braze Vega SDK is added to your project, initialize the library with the API key and [SDK endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) found in **Settings** > **App Settings** within your Braze dashboard.

{% alert important %}
You must await or resolve the `changeUser` promise before calling other Braze methods, or events and attributes may be set on the incorrect user.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```

{% alert important %}
Anonymous users may be counted towards your [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). As a result, you may want to conditionally load or initialize the SDK to exclude these users from your MAU count.
{% endalert %}

## Optional configurations

### Logging

You can enable SDK logging to help with debugging and troubleshooting. There are multiple ways to enable logging.

#### Enable logging during initialization

Pass `enableLogging: true` to `initialize()` to log debugging messages to the console:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Basic logs are visible to all users, so consider disabling logging before releasing your code to production.
{% endalert %}

#### Enable logging after initialization

Use `toggleLogging()` to enable or disable SDK logging after initialization:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Custom logging

Use `setLogger()` to provide a custom logger function for more control over how SDK logs are handled:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Configuration options

You can pass additional configuration options to `initialize()` to customize the SDK behavior:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Upgrading the SDK

When you reference the Braze Vega SDK from NPM or Yarn, you can upgrade to the latest version by updating your package dependency:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Testing your integration

To verify your SDK integration is working correctly:

1. Initialize the SDK with `enableLogging: true` to see debug messages in the console
2. Ensure you `await changeUser()` before calling other SDK methods
3. Call `await openSession()` to start a session
4. Check your Braze dashboard under **Overview** to verify that session data is being recorded
5. Test logging a custom event and verify it appears in your dashboard


