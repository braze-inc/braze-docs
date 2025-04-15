---
nav_title: Conditionally Display In-App Messages
guide_top_header: Conditionally Display In-App Messages
article_title: Conditionally Display In-App Messages
page_order: 1
layout: scrolly
description: "A tutorial on how to conditionally control whether or not to show a triggered in-app message"
---
# Conditionally Display In-App Messages

{% tabs %}
{% tab Web %}
{% scrolly %}
```js file=index.js
import * as braze from "@braze/web-sdk";
// remove any calls to `automaticallyShowInAppMessages()`
// REMOVE --> braze.automaticallyShowInAppMessages()

braze.subscribeToInAppMessage(function(message) {
  if (location.pathname === '/checkout' || document.getElementById('#checkout')) {
    // do not show the message
  } else {
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
lines-index.js=5,11

#### 2. Subscribe to the in-app message callback handler

Register a callback using [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage).

This method will be called whenever an in-app message has been triggered, with a `message` argument.

!!step
lines-index.js=6-10

#### 3. Check for any display condition

Apply your custom logic to control whether or not the message should be displayed.

In this example, we're checking if the URL contains "checkout" or if a `#checkout` element exists on the page.

!!step
lines-index.js=9

#### 4. Conditionally call the `showInAppMessage` method

If you want to display the message, call the [`showInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) method on the provided `message`

If you do not want to display the message, don't call `showInAppMessage`
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
