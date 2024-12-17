---
nav_title: OTT and TV Display
article_title: OTT and TV Display for Android and FireOS
page_order: 5
platform: 
  - Android
  - FireOS
description: "This reference article covers in-app messaging OTT display information for your Android or FireOS application."
channel:
  - in-app messages

---

# OTT and TV display

> The Braze Android SDK natively supports displaying in-app messages on OTT devices like Android TV or Fire Stick.

## Key differences

Some key differences exist in the display of standard in-app messages between native and OTT devices.

For OTT devices:

* In-app messages that require touch mode, such as slideup, are disabled on OTT.
* The currently selected or focused item, such as a button or close button, will be highlighted.
* Body clicks on the in-app message itself, such as not on a button, are not supported.

