---
nav_title: Customer Feedback
platform: iOS
page_order: 7

hidden: true
description: "This article covers the deprecated customer feedback module."

---
{% alert Update %}
Customer Feedback is no longer supported. [Learn more about this and other deprecated features here]({{site.baseurl}}/help/release_notes/deprecations/#feedback).
{% endalert %}

# Customer Feedback

The Braze feedback form allows users to submit feedback about your app that is immediately sent to your company's dashboard.

## Integration {#feedback-integration}

![iOS ActivityFeed+FeedBack]({% image_buster /assets/img_archive/iosfeed.png %} "News Feed and Feedback Form")

Integrating the ViewController `FeedbackViewController` will show a feedback form and allow users to post Feedback to Braze.

Our Feedback view controllers are open-source and available [here][4]. You have a great deal of flexibility in how you choose to display the view controllers. There are two different versions of the view controllers to accommodate different navigation structures.

### Modal Feedback View Controller

`ABKModalFeedbackViewController` presents the view controller in a modal view that includes a navigation bar, "Cancel," and "Send" buttons.
You can integrate it either programmatically or in your storyboard.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKModalFeedbackViewController *modalFeedback = [[ABKModalFeedbackViewController alloc] init];
[self presentViewController:modalFeedback animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
presentViewController(ABKModalFeedbackViewController.init(), animated:true, completion: nil)
```

{% endtab %}
{% endtabs %}

### Navigation Feedback View Controller

`ABKNavigationFeedbackViewController` can be used in a navigation stack as a child of a `UINavigationController`. This Feedback view controller includes a "Send" button.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKNavigationFeedbackViewController *navFeedback = [[ABKNavigationFeedbackViewController alloc] init];
[navigationController pushViewController:navFeedback animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
navigationController.pushViewController(ABKNavigationFeedbackViewController.init(), animated: true)
```

{% endtab %}
{% endtabs %}

### Storyboard Integration

The Braze view controllers can also be integrated using Storyboards. Check out the [Feedback Sample App][1] in the iOS SDK for an example.

### Sample Code {#feedback-sample-code}

`ABKNavigationFeedbackViewController` and `ABKModalFeedbackViewController` are utilized in the [Feedback Sample App][1]. For further details see the [`ABKFeedBackViewController` header files][11]

>  You should only implement the `ABKFeedbackViewController` using the contexts as outlined above. Never directly.

#### One Button Integration - Modal View

Below are examples of how to integrate the Braze view controllers into your app. We've included a one-button integration example so you can have one call to open the feedback view controller from within the News Feed view.

```objc
ABKNavigationFeedbackViewController *newsFeedModal = [[ABKNavigationFeedbackViewController alloc] init];
self.modalNavigationController = [[UINavigationController alloc] initWithRootViewController:newsFeedModal];
UIBarButtonItem *feedbackBarButtonItem = [[UIBarButtonItem alloc] initWithTitle:@"Feedback"
    style:UIBarButtonItemStyleBordered target:self action:@selector(openFeedbackFromModalFeed:)];
newsFeedModal.navigationItem.leftBarButtonItem = feedbackBarButtonItem;
UIBarButtonItem *closeButtonItem = [[UIBarButtonItem alloc] initWithTitle:@"Close"
    style:UIBarButtonItemStyleBordered target:self action:@selector(closeModalNaviagationView:)];
newsFeedModal.navigationItem.rightBarButtonItem = closeButtonItem;
[self presentModalViewController:self.modalNavigationController animated:YES];
```

## Customization {#feedback-customization}

To add customized behavior across the life cycle of a Feedback view controller, we recommend that you create a category or a subclass of the `FeedbackViewController` you are using and override the corresponding methods for different stages of the view controller.

The methods are:

| `- (ABKFeedback *)appboyFeedbackFromMessage:(NSString *)message email:(NSString *)email isBug:(BOOL)isBug;`|
|:------------------------ |
|  This method is for customizing the feedback object from user inputs. It replaces the old feedbackViewControllerBeforeFeedbackSent delegate method. |

| `- (void)feedbackSent:(ABKFeedbackSentResult)feedbackSentResult;`|
|:------------------------ |
|  This method is for custom handling after feedback is sent. It replaces the old feedbackViewControllerFeedbackSent delegate method. |

| `- (IBAction)issueButtonTapped:(UIButton *)sender;`|
|:------------------------ |
|  The touch up inside action for the issue button. The default behavior is to change the select state of the button. |

| `- (IBAction)sendButtonTapped:(UIBarButtonItem *)sender;`|
|:------------------------ |
|  The touch up inside action for the send button. The default behavior is to check the validation of the feedback object, show the spinner view, and send the feedback through the Braze SDK. |

## Manual Feedback Collection

The following method will allow you to pass Feedback to Braze from a form or field within your app. This is perfect for passing feedback from an existing UI element to Braze.

The SDK will call the completion handler after the feedback sends successfully or fails to send..

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)submitFeedback:(ABKFeedback *)feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: \(feedbackSentResult)")
    }
```

{% endtab %}
{% endtabs %}

When manually collecting feedback, you can also log when the form is displayed using `- (void) logFeedbackDisplayed;` in `Appboy.h`. For example:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logFeedbackDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logFeedbackDisplayed()
```

{% endtab %}
{% endtabs %}

## Third-Party Provider Integrations

Braze has easy integrations with both [Desk.com][13] and [Zendesk][14]. So long as you are collecting feedback through our ready-made UI or manually using the `submitFeedback` method, you can pass that feedback through to either third-party provider. This will afford you the benefit of having the entire user profile card available to the CSR handling the case, and allow you to segment based upon the number of feedback requests a user has submitted.

To take advantage of these integrations, please visit the ["Feedback" section within the "Settings" page][15].

[1]: https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/Feedback/AppboyFeedbackSample/AppboyFeedbackSample
[4]: https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKFeedbackViewController/FeedbackViewController
[11]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKFeedbackViewController/FeedbackViewController/ABKFeedbackViewController.h
[13]: http://www.desk.com
[14]: http://www.zendesk.com
[15]: https://dashboard-01.braze.com/app_settings/app_settings/feedback/
