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

To enable logging, you can use [`enableLogging`](#enablelogging) which provides basic logging, or [`setLogger`](#setlogger) which provides custom logging.

### enableLogging

`enableLogging` is used to enable basic logging for the Braze Web SDK. When enabled, Braze will log to the javascript console which is visible to all users. Consider removing `enableLogging` from your code or switch to using [`setLogger`](#setlogger) before releasing to production.

#### Usage

, and accepts the boolean values `true` or `false`.

```javascript

```

#### Example

```javascript

```

### setLogger

`setLogger` is used to create custom log messages.

`setLogger` accepts any string, and, by default, outputs this string to the browser console.

By default, Braze logs to the browser console. Call this method to set a custom log action and enable debug-level log statements.

#### Usage

```javascript
setLogger(loggerFunction: (message: string) => void): void
```

#### Example

```javascript
setLogger(function(message) {
    // Custom log handling
    console.log("Custom Logger: " + message);
});
```
