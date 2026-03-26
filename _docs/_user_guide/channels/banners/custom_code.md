---
nav_title: Custom code and JavaScript bridge
article_title: Custom code and JavaScript bridge for Banners
page_order: 2
page_type: reference
description: "Learn how to use custom HTML in Banners and the JavaScript bridge to log clicks and trigger Braze actions."
channel:
  - banners
---

# Custom code and JavaScript bridge for Banners

> When you use the **Custom Code** editor block in the Banner composer, you must call `brazeBridge.logClick()` from within your custom HTML to log clicks. Banners use the same JavaScript bridge as HTML in-app messages, so the same methods and patterns apply.

If you use custom HTML in your Banner design, the Braze SDK cannot automatically attach click listeners to elements inside your custom code. You must explicitly call `brazeBridge.logClick()` for any clickable elements (links, buttons, and similar) that you want to track in campaign analytics.

For example, to log a click when a user taps a button in your custom HTML:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

For the full JavaScript bridge reference, including all available methods and click tracking options, see the section below.

## JavaScript bridge {#javascript-bridge}

{% include javascript_bridge/reference.md %}
