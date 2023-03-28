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

> This article covers how to set up a iOS, Android, and FireOS News Feed for the Xamarin platform.

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

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
[2]: https://github.com/braze-inc/braze-xamarin-sdk
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[12]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples
