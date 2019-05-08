---
nav_title: Customization
platform: iOS
page_order: 1
search_rank: 5
---

## Content Cards View Controller Integration

Content Cards can be integrated with two view controller contexts: Navigation or Modal.

### Navigation Context

Example of pushing a `ABKContentCardsTableViewController` instance into a navigation controller:

```objc
ABKContentCardsTableViewController *contentCards = [ABKContentCardsTableViewController getNavigationFeedViewController];
[self.navigationController pushViewController:contentCards animated:YES];
```

{{site.data.alerts.note}} To customize the navigation bar's title, set the title property of the `ABKContentCardsTableViewController` instance's `navigationItem`. {{site.data.alerts.end}}

### Modal Context

This modal is used to present the view controller in a modal view, with a navigation bar on top and a Done button on the right side of the bar.

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```
For examples of these view controllers, check out our [Content Cards sample app](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{{site.data.alerts.note}} To customize the header, set the title property of the `navigationItem` belonging to the `ABKContentCardsTableViewController` instance embedded in the parent `ABKContentCardsViewController` instance. {{site.data.alerts.end}}

## Customizing the Content Cards Feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController` to customize all UI elements and Content Cards behavior. Alternatively, you can create a completely custom view controller and subscribe for data updates. In the latter case, you would need to log all view events, dismissed events, and clicks manually.
