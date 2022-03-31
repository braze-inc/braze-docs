---
nav_title: Card Dismissal
article_title: Content Card Dismissal for Android and FireOS
page_order: 4.5
platform: 
  - Android
  - FireOS
description: "This article covers customization options for your Content Cards in your Android or FireOS application."
channel:
  - content cards

---

# Card dismissal

Disabling swipe-to-dismiss functionality is done on a per-card basis via the [`card.setIsDismissibleByUser()`][48] method. Cards can be intercepted before display using the [`ContentCardsFragment.setContentCardUpdateHandler()`][45] method.

[45]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[48]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.enums/-card-key/index.html#285743463%2FClasslikes%2F-1725759721
