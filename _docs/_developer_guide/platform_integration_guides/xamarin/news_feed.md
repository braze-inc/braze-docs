---
nav_title: News Feed
article_title: News Feed for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 3
description: "This article covers iOS, Android, and FireOS News Feed integration for the Xamarin platform."
channel: news feed 
---

# News Feed

## Android

See the [Android integration instructions][1] for information on how to integrate the News Feed into your Xamarin Android app.  Furthermore, you can look at the [sample application][2] implementation samples.

## iOS 

See the [iOS integration instructions][11] for information on how to integrate the News Feed into your Xamarin iOS app.  Furthermore, you can look at the [sample application][12] implementation samples.

Of all the implementation options, the quickest to implement is the Modal, which can be added by doing the following in your ViewController:

```csharp
// C#
ABKFeedViewControllerModalContext m = new ABKFeedViewControllerModalContext ();
this.PresentViewController (m, true, null);
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/#news-feed
[2]: https://github.com/Appboy/appboy-xamarin-bindings
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[12]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples
