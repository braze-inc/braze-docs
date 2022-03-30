---
nav_title: Custom Styling
article_title: Content Card Custom Styling for Web
page_order: 1
platform: Web
channel: content cards
page_type: reference
description: "This article covers Content Cards custom styling options for your web application."

---

# Content Card customization

## Customizing the default UI

Braze UI elements come with a default look and feel that matches the composers within the Braze dashboard and aims for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK.

By overriding selected styles in your application, it is possible to customize our standard feed with your own background images, font families, styles, sizes, animations, and more. 

For instance, the following is an example override that will cause Content Cards to appear 800px wide:

``` css
body .ab-feed {
  width: 800px;
}
```