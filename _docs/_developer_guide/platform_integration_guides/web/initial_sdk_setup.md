---
nav_title: Initial SDK Setup
article_title: Initial setup for the Braze Web SDK
platform: Web
page_order: 0
page_type: reference
---

# Initial SDK setup for web

> This reference article covers how to install the Braze Web SDK. The Braze Web SDK lets you collect analytics and display rich in-app messages, push, and Content Card messages to your web users. See our [JavaScript Documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html "JSDocs") for a complete technical reference.

{% multi_lang_include archive/web-v4-rename.md %}

## Step 1: Install the Braze library

You can install the Braze library using one of the following methods. If your website uses a `Content-Security-Policy`, refer to our [Content security policy headers guide]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_security_policy/) before installing the library.

{% alert important %}
While most ad blockers will not block the Braze Web SDK, some more restrictive ad blockers are known to cause issues.
{% endalert %}

{% tabs local %}
{% tab package manager %}
If your site uses NPM or Yarn package managers, you can add the [Braze NPM package](https://www.npmjs.com/package/@braze/web-sdk) as a dependency.

Typescript definitions are now included as of v3.0.0. For notes on upgrading from 2.x to 3.x, see our [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Once installed, you can `import` or `require` the library in the typical fashion:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endtab %}

{% tab google tag manager %}
The Braze Web SDK can be installed from the Google Tag Manager Template Library. Two tags are supported:

1. Initialization tag: loads the Web SDK onto your website and optionally sets the External User ID.
2. Actions tag: used to trigger custom events, purchases, change user IDs, or toggle SDK tracking.

Visit the [Google Tag Manager integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager/) for more information.
{% endtab %}

{% tab braze cdn %}
Add the Braze Web SDK directly to your HTML by referencing our CDN-hosted script, which loads the library asynchronously.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>
{% endtab %}
{% endtabs %}

## Step 2: Initialize the SDK

Once the Braze Web SDK is added to your website, initialize the library with the API key and [SDK endpoint URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) found in **Settings** > **App Settings** within your Braze dashboard.

{% alert note %}
If you've configured your Braze initialization options in a Tag Manager, you can skip this step.
{% endalert %}

For a complete list of options for `braze.initialize()`, along with our other JavaScript methods, see our [JavaScript documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
});

// optionally show all in-app messages without custom handling
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
Anonymous users on mobile or web devices may be counted towards your [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). As a result, you may want to conditionally load or initialize the SDK to exclude these users from your MAU count.
{% endalert %}

## Step 3: Set up push notifications (optional)

To set up push notifications for the Braze Web SDK, additional set up is required. For a full walkthrough, see [Push notifications for web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/).

## Logging

To quickly enable logging, you can add `?brazeLogging=true` as a parameter to your website URL. Alternatively, you can enable [basic](#basic-logging) or [custom](#custom-logging) logging.

### Basic logging

{% tabs local %}
{% tab before initialization %}
Use `enableLogging` to log basic debugging messages to the javascript console before the SDK is initialized.

```javascript
enableLogging: true
```

Your method should be similar to the following:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab after initialization %}
Use `braze.toggleLogging()` to log basic debugging messages to the javascript console after the SDK is initialized. Your method should be similar to the following:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
Basic logs are visible to all users, so consider disabling, or switch to [`setLogger`](#custom-logging), before releasing your code to production.
{% endalert %}

### Custom logging

Use `setLogger` to log custom debugging messages to the javascript console. Unlike basic logs, these logs are not visible to users.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Replace `STRING` with your message as a single string parameter. Your method should be similar to the following:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Upgrading the SDK

{% multi_lang_include archive/web-v4-rename.md %}

When you reference the Braze Web SDK from our content delivery network, for example, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (as recommended by our default integration instructions), your users will receive minor updates (bug fixes and backward compatible features, versions `a.a.a` through `a.a.z` in the above examples) automatically when they refresh your site.

However, when we release major changes, we require you to upgrade the Braze Web SDK manually to ensure that nothing in your integration will be impacted by any breaking changes. Additionally, if you download our SDK and host it yourself, you won't receive any version updates automatically and should upgrade manually to receive the latest features and bug fixes.

You can keep up-to-date with our latest release [following our release feed](https://github.com/braze-inc/braze-web-sdk/tags.atom) with the RSS Reader or service of your choice, and see [our changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) for a full accounting of our Web SDK release history. To upgrade the Braze Web SDK:

- Update the Braze library version by changing the version number of `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`, or in your package manager's dependencies.
- If you have web push integrated, update the service worker file on your site - by default, this is located at `/service-worker.js` at your site's root directory, but the location may be customized in some integrations. You must access the root directory to host a service worker file.

These two files must be updated in coordination with each other for proper functionality.

## Alternative integration methods

### Server-side rendering frameworks {#ssr}

If you use a server-side rendering framework such as Next.js, you may encounter errors because the SDK is meant to be run in a browser environment. You can resolve these issues by dynamically importing the SDK.

You can retain the benefits of tree-shaking when doing so by exporting the parts of the SDK that you need in a separate file and then dynamically importing that file into your component.

```javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

Alternatively, if you're using webpack to bundle your app, you can take advantage of its magic comments to dynamically import only the parts of the SDK that you need.

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Vite support {#vite}

If you use Vite and see a warning around circular dependencies or `Uncaught TypeError: Class extends value undefined is not a constructor or null`, you may need to exclude the Braze SDK from its [dependency discovery](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Electron support {#electron}

Electron does not officially support web push notifications (see: this [GitHub issue](https://github.com/electron/electron/issues/6697)). There are other [open source workarounds](https://github.com/MatthieuLemoine/electron-push-receiver) you may try that have not been tested by Braze.

### AMD module loader

If you use RequireJS or other AMD module-loaders we recommend self-hosting a copy of our library and referencing it as you would with other resources:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```
### Alternative No AMD installation

If your site uses RequireJS or another AMD module-loader, but you prefer to load the Braze Web SDK through one of the other options above, you can load a version of the library that does not include AMD support. This version of the library can be loaded from the following CDN location:

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Tealium iQ
Tealium iQ offers a basic turnkey Braze integration. To configure the integration, search for Braze in the Tealium Tag Management interface, and provide the Web SDK API key from your dashboard.

For more details or in-depth Tealium configuration support, check out our [integration documentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) or reach out to your Tealium account manager.

### Other tag managers
Braze may also be compatible with other tag management solutions by following our integration instructions within a custom HTML tag. Reach out to a Braze representative if you need help evaluating these solutions.

### Jest framework troubleshooting {#jest}

When using Jest, you may see an error similar to `SyntaxError: Unexpected token 'export'`. To fix this, adjust your configuration in `package.json` to ignore the Braze SDK:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

