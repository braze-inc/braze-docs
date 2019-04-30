---
nav_title: Customization
platform: iOS
page_order: 1
search_rank: 5
---

## Content Cards View Controller Integration

Content Cards can be integrated with two view controller contexts: Navigation or Modal.

### Navigation Context

Set the instance's title and navigation items before pushing it into a navigation controller:

```objc
ABKContentCardsTableViewController *contentCards = [ABKContentCardsTableViewController getNavigationFeedViewController];
[self.navigationController pushViewController:contentCards animated:YES];
```

### Modal Context

This modal is used to present the view controller in a modal view, with a navigation bar on top and a Done button on the right side of the bar.

Set the modal's title via the `navigationBarTitle` property:

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```
For examples of these view controllers, check out the [Stopwatch Sample Project](https://github.com/Appboy/appboy-ios-sdk/tree/master/Example/Stopwatch).

## Customizing the Content Cards Feed

You can create your own Content Cards interface by extending `ABKContentCardsTableViewController`. You can customize all UI elements and Content Cards behavior in this way. Or you can create a completely custom view controller and subscribe for data updates. In this case you would need to log all view and dismissed events and clicks manually.
