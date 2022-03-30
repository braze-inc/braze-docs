---
nav_title: Open Link in New Tab
article_title: Open In-App Message Link in New Tab for Web
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "This article covers how to set your in-app message links to open in a new tab for your web application."

---

# Open message link in new tab

To set your in-app message links to open in a new tab, set the `openInAppMessagesInNewTab` option to `true` to force all links from in-app message clicks open in a new tab or window.

```javascript
appboy.initialize('api-key', { openInAppMessagesInNewTab: true} );
```