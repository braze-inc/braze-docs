---
nav_title: AMP Support
article_title: AMP Support for Web
platform: Web
page_order: 5
page_type: reference
description: "This reference article describes how to integrate Braze on an AMP page."

---

# AMP support

{% alert note %}
This section is not necessary to integrate unless you're trying to integrate Braze on an AMP page.
{% endalert %}

Accelerated Mobile Pages (AMP) is a Google-backed project designed to improve page load time on mobile devices by enforcing certain standards, including restricting the usage of JavaScript. 

As a result, the Braze SDK cannot be loaded onto an AMP page. However, the AMP project does provide a component that supports Web push. The [following instructions](https://www.ampproject.org/docs/reference/components/amp-web-push) detail how to set up that component and reference the following documentation on the `amp-web-push` component.

## Step 1: Include AMP web push script

Add the following async script tag to your head:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## Step 2: Add a subscription and unsubscription widget

You'll need to add a widget that allows users to subscribe and unsubscribe from push. This should live inside the body of your HTML and can be styled however you see fit. 

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

## Step 3: Download helper iFrame and permission dialog

The AMP Web Push component works by creating a popup that handles the push subscription. As a result, you'll need to include a couple of helper files in your project. Download the [helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) file and [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) file and store them on your site. 

## Step 4: Create a service worker file

Create a `service-worker.js` file with the content below, and place it in the root directory of your website:

```js
self.importScripts('https://js.appboycdn.com/web-sdk/3.5/service-worker.js');
```

## Step 5: Configure the AMP web push HTML element

You'll now need to add the `amp-web-push` HTML element to your page. Drop the following HTML code into the body of your document:

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey=YOUR_API_KEY&baseUrl=YOUR_BASE_URL"
>
```

In particular, the `service-worker-URL` requires appending your `apiKey` and `baseUrl` (https://dev.appboy.com/api/v3) as query parameters.

You should now be configured for push subscription and unsubscription on your AMP page. 
