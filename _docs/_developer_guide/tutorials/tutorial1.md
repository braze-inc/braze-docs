---
nav_title: Tutorial 1
article_title: Developer Tutorials
page_order: 1
layout: dev_guide
description: "Interactive, step-by-step coding tutorials using dynamic, scrollable code."
---
<style>

@media (min-width: 1200px) {
    #dev-main,#featured_main {
        max-width:unset;
        margin-left: auto;
        margin-right: auto
    }
}
</style>
# Setting Up Push Notifications

{% tabs %}
{% tab Web %}
{% scrolly %}

```js file=index.js
braze.initialize("XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", {
  baseUrl: "sondheim.braze.com",
  enableLogging: true,
  sessionTimeoutInSeconds: 10,
  serviceWorkerLocation: "/service-worker.js",
  allowUserSuppliedJavascript: true, //
  noCookies: true,
});

// Request Push Permission
const requestPushPermission = () => {
  braze.requestPushPermission(
    (endpoint, publicKey, userAuth) => {
      console.log("Push permission granted!");
      console.log("Endpoint:", endpoint);
      console.log("Public Key:", publicKey);
      console.log("User Auth:", userAuth);
    },
    (temporaryDenial) => {
      if (temporaryDenial) {
        console.warn("Push permission temporarily denied.");
      } else {
        console.error("Push permission permanently denied.");
      }
    }
  );
};

const requestPushPermission = () => {
  braze.requestPushPermission(
    (endpoint, publicKey, userAuth) => {
      console.log("Push permission granted!");
      console.log("Endpoint:", endpoint);
      console.log("Public Key:", publicKey);
      console.log("User Auth:", userAuth);
    },
    (temporaryDenial) => {
      if (temporaryDenial) {
        console.warn("Push permission temporarily denied.");
      } else {
        console.error("Push permission permanently denied.");
      }
    }
  );
};
```

```js file=service-worker.js
self.importScripts("https://js.appboycdn.com/web-sdk/5.6/service-worker.js");
```

!!step
lines-index.js=1-8

#### Initialize braze

Some instructions on what this `line` does, and how to use it.

- item 1
- item 2

!!step
lines-index.js=1-2,4,6-7

#### Set up basic settings

Some instructions on what these lines do, and how to use them.

!!step
lines-index.js=3

#### Enable logging

Some instructions on what these lines do, and how to use them.

!!step
lines-service-worker.js=1

#### Create your service-worker file

Add this line to the service worker file to allow for push notifications.

!!step
lines-index.js=5

#### Link your service-worker file

Some instructions on what these lines do, and how to use them.

!!step
lines-index.js=11-27

#### Request push permissions

Highlighting some more stuff

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

!!step
lines-delegate.swift=1
Some instructions on what this `line` does, and how to use it.

!!step
lines-delegate.swift=3-4
Some instructions on what these lines do, and how to use them.

!!step
lines-delegate.swift=6-9
Highlighting just the decision logic, lines 6–9.

!!step
lines-delegate.swift=10
No lines!

{% endscrolly %}

{% endtab %}

{% endtabs %}
