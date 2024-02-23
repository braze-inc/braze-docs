---
nav_title: Other SDK customizations
article_title: Other SDK customizations for Web
platform: Web
page_order: 1
page_type: reference
description: "This reference article covers additional customization and configuration options for the Braze Web SDK such as logging."
---

# Other SDK customizations for Web

> This reference article covers additional customization and configuration options for the Braze Web SDK such as verbose logging.

## Prerequisites

To customize your Braze Web SDK, you'll need to [integrate the SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/web_sdk_integration/) first.

## Logging

To enable logging, you can use [`enableLogging`](#enablelogging) for basic logging, or [`setLogger`](#setlogger) for custom logging.

### enableLogging

Use `enableLogging` to log basic debugging messages to the javascript console.

```javascript
enableLogging: true
```

Your method should be similar to the following:

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'sdk.iad-03.braze.com',
    enableLogging: true
});
braze.openSession();
```

{% alert important %}
These logs will be visible to all users, so consider removing `enableLogging`, or switch to [`setLogger`](#setlogger), before releasing your code to production.
{% endalert %}

### setLogger

Use `setLogger` to log custom debugging messages to the javascript console.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Replace `STRING` with a single string parameter which will be used as your message. Your method should be similar to the following:

```javascript
braze.initialize('YOUR-API-KEY');
braze.setLogger(function(message) {
    // Custom log handling
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```
