---
nav_title: Refreshing the Feed
platform: iOS
page_order: 3
search_rank: 5
---

# Refreshing Content Cards

You can manually request Braze to refresh the user's Content Cards using the `requestContentCardsRefresh:` method on the `Appboy` interface. For example:

```objc
[[Appboy sharedInstance] requestContentCardsRefresh];
```

For more information see the [`Appboy.h` header file](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h).
