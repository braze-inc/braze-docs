---
nav_title: Disabling Swipe to Dismiss
article_title: Disabling Content Card Swipe to Dismiss for Android and FireOS
page_order: 4.5
platform: 
  - Android
  - FireOS
description: "This article covers customization options for your Content Cards in your Android application."
channel:
  - content cards

---

# Disabling swipe to dismiss

Disabling swipe-to-dismiss functionality is done on a per-card basis via the [`card.setIsDismissibleByUser()`][48] method. Cards can be intercepted before display using the [`ContentCardsFragment.setContentCardUpdateHandler()`][45] method.

[45]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[48]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/set-is-dismissible-by-user.html
