---
nav_title: Multiple Feeds
platform: iOS
page_order: 6
search_rank: 5
---

# Using Multiple Content Card Feeds

Content Cards can be filtered on the app to only display specific cards, which enables you to have multiple Content Card feeds for different use cases (as in having a "Transactional" feed versus a "Marketing" feed).

{% alert important %}
On iOS, this feature is currently only available for fully customized UIs. Contact your Customer Support Manager if you would like to display multiple Content Card feeds using our default UI.
{% endalert %}

The following documentation demonstrates an example implementation that can be changed to fit your specific integration.

## Step 1: Setting Key-Value Pairs on Cards

When creating a Content Card campaign, key-value pair data can be set on each Card. Our filtering logic will use this key-value pair data to categorize cards.

For the purposes of this example, we'll set a key-value pair with the key `feed_type` that will designate which Content Card feed the card should be displayed in. The value will be whatever your custom feeds will be, as in `Transactional`, `Marketing`, and more.

## Step 2: Set Up a Content Card Listener

Use the following code snippet to add an observer to listen for Content Card updates.

```
[[NSNotificationCenter defaultCenter] addObserver:self
                                           selector:@selector(contentCardsUpdatedNotificationReceived:)
                                               name:ABKContentCardsProcessedNotification
                                             object:nil];
```

Add the following methods to respond to updates from the observer and filter the returned cards by type. 

The first method, `contentCardsUpdatedNotificationReceived:`, handles updates from the observer. It the calls the second method, `getCardsForFeedType:`, with the desired feed type, in this case `Transactional`.

```
- (void)contentCardsUpdatedNotificationReceived:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // Get an array containing only cards that have the "Transactional" feed type set in their extras.
    NSMutableArray<ABKContentCard *> *filteredArray = [self getCardsForFeedType:@"Transactional"];
    NSLog(@"Got filtered array of length: %lu", [filteredArray count]);

    // Pass filteredArray to your UI layer for display.
  }
}

- (NSMutableArray<ABKContentCard *> *)getCardsForFeedType:(NSString *)type {
  NSMutableArray<ABKContentCard *> *cards = [NSMutableArray arrayWithArray:[Appboy.sharedInstance.contentCardsController getContentCards]];

  NSMutableArray<ABKContentCard *> *filteredArray = [NSMutableArray arrayWithArray:[cards filteredArrayUsingPredicate:[NSPredicate predicateWithBlock:^BOOL(ABKContentCard * card, NSDictionary *bindings) {
    NSDictionary *extras = [card extras];
      if (extras != nil && [extras objectForKey:@"feed_type"] != nil && [[extras objectForKey:@"feed_type"] isEqualToString:type]) {
        NSLog(@"Got card: %@ ", card.idString);
        return YES;
      }
    return NO;
  }]]];

  return filteredArray;
}
```
