---
nav_title: Open in New Tab
article_title: Open In-App Message Link in New Tab for Web
platform: Web
channel: in-app messages
page_type: reference
description: "This article covers how to set your in-app message links to open in a new tab for your web application."

---

# Open a link a in new tab

> This article covers how to set your in-app message links to open in a new tab for your web application.

## Configuring links to open in a new tab

To set your in-app message links to open in a new tab, set the `openInAppMessagesInNewTab` option to `true` to force all links from in-app message clicks open in a new tab or window.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
