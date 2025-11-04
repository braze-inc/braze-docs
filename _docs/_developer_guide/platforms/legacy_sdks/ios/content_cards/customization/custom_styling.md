---
nav_title: Custom styling
article_title: Custom Content Card Styling for iOS
platform: iOS
page_order: 1
description: "This article covers Content Card custom styling options for your iOS application."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Custom Styling

## Overriding default images

{% alert important %}
Integration of `SDWebImage` is required if you plan on using our Braze UI for displaying images within iOS in-app messages or Content Cards.
{% endalert %}

Braze allows clients to replace existing default images with their own custom images. To accomplish this, create a new `png` file with the custom image and add it to the app's image bundle. Then, rename the file with the image's name to override the default image in our library. Also, be sure to upload the `@2x` and `@3x` versions of the images to accommodate different phone sizes. Images available for override in Content Cards include:

- Placeholder image: `appboy_cc_noimage_lrg`
- Pinned icon image: `appboy_cc_icon_pinned`

Because Content Cards have a maximum size of 2 KB for content you enter in the dashboard (including message text, image URLs, links, and all key-value pairs), check the size before sending. Exceeding this amount will prevent the card from sending.

{% alert important %}
Overriding default images is currently not supported in our Xamarin iOS integration.
{% endalert %}

## Disabling Dark Mode

To prevent the Content Card UI from adopting dark theme styling when the user device has Dark Mode enabled, set the `ABKContentCardsTableViewController.enableDarkTheme` property. You can access the `enableDarkTheme` property directly on an `ABKContentCardsTableViewController` instance or via the `ABKContentCardsViewController.contentCardsViewController` property to best suit your own UI.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
- (IBAction)presentModalContentCards:(id)sender {
  ABKContentCardsViewController *contentCardsVC = [ABKContentCardsViewController new];
  contentCardsVC.contentCardsViewController.enableDarkTheme = NO;
  ...
  [self.navigationController presentViewController:contentCardsVC animated:YES completion:nil];
}

// Accessing enableDarkTheme directly.
- (IBAction)presentNavigationContentCards:(id)sender {
  ABKContentCardsTableViewController *contentCardsTableVC = [[ABKContentCardsTableViewController alloc] init];
  contentCardsTableVC.enableDarkTheme = NO;
  ...
  [self.navigationController pushViewController:contentCardsTableVC animated:YES];
}
```

{% endtab %}
{% tab swift %}

```swift
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
@IBAction func presentModalContentCards(_ sender: Any) {
  let contentCardsVC = ABKContentCardsViewController()
  contentCardsVC.contentCardsViewController.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsVC, animated: true, completion: nil)
}

// Accessing enableDarkTheme directly.
@IBAction func presentNavigationContentCards(_ sender: Any) {
  let contentCardsTableVC = ABKContentCardsTableViewController()
  contentCardsTableVC.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsTableVC, animated: true, completion: nil)
}
```

{% endtab %}
{% endtabs %}

