---
nav_title: Modal Dismissal
article_title: In-App Message Modal Dismissal for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "This reference article covers in-app messaging customization options for your Android application."
channel:
  - in-app messages

---

# Dismiss modal on outside tap

The default and historical value is `false`, meaning clicks outside the modal will not close the modal. Setting this value to `true` will result in the modal in-app message being dismissed when the user taps outside of the in-app message. This behavior can be toggled on by calling:

```java
AppboyInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```
