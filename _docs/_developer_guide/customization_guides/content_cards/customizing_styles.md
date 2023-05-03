---
nav_title: Customizing Card Styles
article_title: Customizing Content Card Styles
page_order: 1
description: "This article covers custom styling options for your Content Cards."
channel:
  - content cards
---

# Customizing Content Card styles

> Braze Content Cards come with a default look and feel. This article covers custom styling options for your Content Cards.

## Customizing styling
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

The default Content Cards UI can be integrated from the `BrazeUI` library of the Swift SDK. If you wish to intercept and react to the Content Card UI lifecycle, implement [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) as the delegate for your `BrazeContentCardUI.ViewController`.

> A view controller is the "glue" between the overall application and the screen. It controls the views that it owns according to the logic of your application. Every app has one, some have more than one. For more information about iOS view controller options, refer to the [Apple developer documentation](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).

The `BrazeUI` library of the Swift SDK provides two default view controller contexts: navigation or modal. This means you can integrate Content Cards in these contexts by adding a few lines of code to your app or site. You can also create a custom Content Card view controller instead of using the standard Braze one for even more customization options. 

{% subtabs %}
{% subtab Swift %}

<b>Navigation context</b>

A navigation controller is a view controller that manages one or more child view controllers in a navigation interface. Here is an example of pushing a `BrazeContentCardUI.ViewController` instance into a navigation controller:

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
```

<b>Modal context</b>

Use modal presentations to create temporary interruptions in your app’s workflow, such as prompting the user for important information. This model view has a navigation bar on top and a **Done** button on the side of the bar. Here is an example of pushing a `BrazeContentCard.ViewController` instance into a modal controller:

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endsubtab %}
{% subtab Objective-C %}

<b>Navigation context</b>

A navigation controller is a view controller that manages one or more child view controllers in a navigation interface. Here is an example of pushing a `BrazeContentCardUI.ViewController` instance into a navigation controller:

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

<b>Modal context</b>

Use modal presentations to create temporary interruptions in your app’s workflow, such as prompting the user for important information. This model view has a navigation bar on top and a **Done** button on the side of the bar. Here is an example of pushing a `BrazeContentCard.ViewController` instance into a modal controller:

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endsubtab %}
{% endsubtabs %}

For example usage of BrazeUI view controllers, check out the corresponding Content Cards UI samples in our [Examples app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% endtab %}
{% tab Web %}

Web content

{% endtab %}
{% endtabs %}



## Custom font
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

{% subtabs %}
{% subtab Swift %}

Swift content

{% endsubtab %}
{% subtab Objective-C %}

Objective-C content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Web content

{% endtab %}
{% endtabs %}

## Custom pinned icons
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.



{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

{% subtabs %}
{% subtab Swift %}

Swift content

{% endsubtab %}
{% subtab Objective-C %}

Objective-C content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Web content

{% endtab %}
{% endtabs %}

## Custom card rendering
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

{% subtabs %}
{% subtab Swift %}

Swift content

{% endsubtab %}
{% subtab Objective-C %}

Objective-C content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Web content

{% endtab %}
{% endtabs %}

## Dark theme customization 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam convallis velit eget bibendum vulputate. Praesent sed mauris nec turpis faucibus bibendum vel et enim. Suspendisse potenti. Donec eleifend, arcu non molestie laoreet, mauris mauris sodales nunc, vitae euismod augue metus eu justo. Vivamus eleifend interdum ipsum, vitae hendrerit libero auctor sit amet. Fusce sodales ipsum sit amet risus venenatis ultricies. Etiam elementum risus vel lorem tincidunt varius. Sed euismod elit vel enim volutpat, quis dapibus mauris convallis. Sed nec quam a est tempor imperdiet id id ante. Sed in tortor vel libero placerat tincidunt.

{% tabs %}
{% tab Android %}

Android content

{% subtabs %}
{% subtab Java %}

Java content

{% endsubtab %}
{% subtab Kotlin %}

Kotlin content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

iOS content

{% subtabs %}
{% subtab Swift %}

Swift content

{% endsubtab %}
{% subtab Objective-C %}

Objective-C content

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Web content

{% endtab %}
{% endtabs %}