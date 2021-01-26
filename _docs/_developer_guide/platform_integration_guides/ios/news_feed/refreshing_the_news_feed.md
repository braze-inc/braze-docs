---
nav_title: Refreshing the News Feed
platform: iOS
page_order: 4

---

# Refreshing the News Feed

You can manually request Braze to refresh the user's News Feed in `Appboy.h` using `- (void) requestFeedRefresh;`. For example:
```objc
[[Appboy sharedInstance] requestFeedRefresh];
```

For more information see the [`Appboy.h` header file][15].


[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/headers/AppboyKitLibrary/Appboy.h "Appboy.h Header File"
