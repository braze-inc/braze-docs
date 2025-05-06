---
nav_title: Accessing Key-Value Pairs
guide_top_header: Accessing In-App Message Key-Value Pairs
article_title: Accessing Key-Value Pairs
page_order: 1
layout: scrolly
description: "A tutorial on how to access key-value pairs with in-app messages"
---
# Accessing Key-Value Pairs

{% tabs %}
{% tab Web %}
{% scrolly %}
```js file=index.js
import * as braze from "@braze/web-sdk";
// remove any calls to `automaticallyShowInAppMessages()`
// REMOVE --> braze.automaticallyShowInAppMessages()

braze.subscribeToInAppMessage(function(message) {
  const extras = message.extras;
  const customTemplateType = extras['custom-template'] || '';
  const customColor = extras['custom-color'] || '';
  const customMessageId = extras['message-id'] || '';

  if (customTemplateType) {
    // add your own custom code to render this message
  } else {
    // otherwise, use Braze built-in UI
    braze.showInAppMessage(message);
  }
});
```

!!step
lines-index.js=2-3

#### 1. Remove calls to `automaticallyShowInAppMessages()`

Be sure to remove any calls to [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages).

This method will show your messages regardless of any customized code you add later on.

!!step
lines-index.js=5,17

#### 2. Subscribe to the in-app message callback handler

Register a callback using [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage).

This method will be called whenever an in-app message has been triggered, with a `message` argument.

!!step
lines-index.js=6

#### 3. Access the `message.extras` property

Key-value pairs you have defined in the Braze dashboard will be available using the `extras` message property.

All values supplied will be typed as a string

!!step
lines-index.js=11-16

#### 4. Conditionally call the `showInAppMessage` method

If you want Braze to display the message, call the [`showInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) method on the provided `message`.

Otherwise you can use the custom properties as you wish!
{% endscrolly %}
{% endtab %}
{% tab iOS %}
{% scrolly %}
```swift file=delegate.swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endscrolly %}
{% endtab %}
{% endtabs %}
