---
nav_title: Integration Overview
article_title: News Feed Integration Overview for iOS
platform: iOS
page_order: 1
description: "This article covers an overview of integrating the News Feed into your iOS application."
channel:
  - news feed

---

# News Feed integration overview

{% alert tip %}
Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel - it is more flexible, customizable, and reliable. It is also easier to find and use in the Braze product. Contact your Braze account manager for more information.
{% endalert %}

Integrating the view controller `ABKNewsFeedViewController` will display the Braze News Feed.

You have a great deal of flexibility in how you choose to display the view controllers. There are different versions of the view controllers to accommodate different navigation structures.

{% alert note %}
The News Feed that is called by the default behavior of an in-app message click will not respect any delegates you set for the News Feed. If you want to respect that, you must [set the delegate on `ABKInAppMessageUIController`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#setting-delegates) and implement the `ABKInAppMessageUIDelegate` delegate method [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#customizing-in-app-message-body-clicks).
{% endalert %}

## News Feed view controller integration

The News Feed can be integrated with two view controller contexts: navigation or modal.

### Navigation context - ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

To customize the navigation bar's `title`, set the title property of the `ABKNewsFeedTableViewController` instance's `navigationItem`.

### Modal context - ABKFeedViewControllerModalContext

This modal is used present the view controller in a modal view, with a navigation bar on top and a **Done** button on the right side of the bar. To customize the modal's title, set the `title` property of the `ABKNewsFeedTableViewController` instance's `navigationItem`. 

If a delegate **is NOT set**, the **Done** button will dismiss the modal view. If a delegate **is set**, the **Done** button will call the delegate, and the delegate itself will be responsible for dismissing the view.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

For view controller examples, check out our [News Feed sample app][3].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#setting-delegates
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#customizing-in-app-message-body-clicks
[3]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample
