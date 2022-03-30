---
nav_title: Disabling Web SDK Tracking
article_title: Disabling Web SDK Tracking
platform: Web
page_order: 6
page_type: reference
description: "This article covers disabling Web SDK tracking, including why, how, and the implications of doing so."

---

# Disable Web SDK tracking

{% include archive/web-v4-rename.md %}

To comply with data privacy regulations, data tracking activity on the Web SDK can be stopped entirely using the method [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/module-braze.html#.disableSDK). This method will sync data logged before when `disableSDK()` was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored. If you wish to resume data collection at a later point in time, you can use the [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/module-braze.html#.enableSDK) method in the future to resume data collection.

If you wish to provide users with the option to stop tracking, we recommend building a simple page with two links or buttons, one that calls `disableSDK()` when clicked, and another that calls `enableSDK()` to allow users to opt back in. You can use these controls to start or stop tracking via other data sub-processors as well.

Note that the Braze SDK does not need to be initialized to call `disableSDK()`, allowing you to disable tracking for fully anonymous users. Conversely,`enableSDK()` does not initialize the Braze SDK so you must also call `initialize()` afterward to enable tracking.
