---
nav_title: Advanced implementation (optional)
article_title: In-App Message Implementation Guide for iOS (Optional)
platform: iOS
page_order: 6
description: "This advanced implementation guide covers iOS in-app message code considerations, three use cases built by our team, and accompanying code snippets."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Looking for the basic in-app message developer integration guide? Find it [here]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/overview/).
{% endalert %}

# In-app messaging implementation guide

> This optional and advanced implementation guide covers in-app message code considerations, three custom use cases built by our team, and accompanying code snippets. Visit our Braze Demo repository [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! This implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested. Looking for HTML implementations? Take a look at our [HTML template repository](https://github.com/braze-inc/in-app-message-templates)!

## Code considerations

The following guide offers an optional custom developer integration to use in addition to default in-app messages. Custom view controllers are included with each use case, offering examples to extend functionality and natively customize the look and feel of your in-app messages.

### ABKInAppMessage subclasses

The following code snippet is a UI delegate method from the Braze SDK that determines what subclass view you want to populate your in-app message with. We cover a basic implementation in this guide and show how the full, slide up, and modal subclasses can be implemented in captivating ways. Note that if you want to set up your custom view controller, you must set up all other in-app message subclasses. After you have a solid understanding of the concepts behind subclassing, check out our [use cases](#sample-use-cases) to start implementing in-app messaging subclasses.

{% tabs %}
{% tab Swift %}
**ABKInAppMessage subclasses**<br>

```swift
extension AppboyManager: ABKInAppMessageUIDelegate {
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return slideupViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageModal: 
      return modalViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageFull:
      return fullViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
**ABKInAppMessage subclasses**<br> 

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [self slideupViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## Use cases

We've provided three use cases below. Each use case offers a detailed explanation, relevant code snippets, and a look into how in-app messages may look and be used in the Braze dashboard:
- [Custom slide-up in-app message](#custom-slide-up-in-app-message)
- [Custom modal in-app message](#custom-modal-in-app-message)
- [Custom full in-app message](#custom-full-in-app-message)

### Custom slide-up in-app message

![Two iPhone side-by-side. The first iPhone has the slide-up message touching the bottom of the phone screen. The second iPhone has the slide-up message sitting higher on the screen allowing you to see the displayed app navigation button.]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

While building out your slide-up in-app message, you may notice you aren't able to modify the placement of the message using default methods. Modification like this is made possible by subclassing the `ABKInAppMessageSlideupViewController` and overriding the `offset` variable with your own custom variable. The image to the right shows an example of how this can be used to adjust your slide-up in-app messages. 

Visit the [`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) to get started.

#### Adding additional behavior to our default UI<br><br>

{% tabs %}
{% tab Swift %}
**Update `offset` variable**<br>
Update the `offset` variable and set your own offset to suit your needs.
```swift
func setSlideConstraint() {
  offset = 0
}
```

```swift
override var offset: CGFloat {
  get {
    return super.offset
  }
  set {
    super.offset = newValue + adjustedOffset
  }
}
```

{% details Version 3.34.0 or earlier  %}
**Update `slideConstraint` variable**<br>
The `slideConstraint` public variable comes from the superclass `ABKInAppMessageSlideupViewController`. 

```swift
func setSlideConstraint() {
    slideConstraint?.constant = bottomSpacing
}
```

```swift
private var bottomSpacing: CGFloat {
    return AppboyManager.shared.activeApplicationViewController.topMostViewController().view.safeAreaInsets.bottom
}
``` 
Visit the Braze Demo repository for the [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17) function.
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
**Update `offset` variable**<br>
Update the `offset` variable and set your own offset to suit your needs.
```objc
- (void)setOffset {
  self.offset = 0;
}
```

```objc
- (CGFloat)offset {
  return [super offset];
}
 
- (void)setOffset:(CGFloat)offset {
  [super setOffset:offset + [self adjustedOffset]];
}
```
{% details Version 3.34.0 or earlier  %}
**Update `slideConstraint` variable**<br>
The `slideConstraint` public variable comes from the superclass `ABKInAppMessageSlideupViewController`. 

```objc
- (void)self.setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = bottomSpacing;
}
```

```objc
- (CGFloat)bottomSpacing {
  return [AppboyManager shared].activeApplicationViewController.topMostViewController.view.safeAreaInsets.bottom;
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Override and set custom constraint**<br>
Override `beforeMoveInAppMessageViewOnScreen()` and set your own custom constraint value to suit your needs. The original value is set in the superclass.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Version 3.34.0 or earlier %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective-C %}
**Override and set custom constraint**<br> 
Override `beforeMoveInAppMessageViewOnScreen()` and set your own custom constraint value to suit your needs. The original value is set in the superclass.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Version 3.34.0 or earlier  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**Adjust constraint for device orientation**<br>
Adjust the respective value in `viewWillTransition()` because the subclass assumes responsibility for keeping the constraint synced during layout changes.

### Custom modal in-app message

![An iPhone showing a modal in-app message that allows you to cycle through a list of sports teams and select your favorite one. At the bottom of this in-app message, there is a large blue submit button.]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

An `ABKInAppMessageModalViewController` can be subclassed to leverage a `UIPickerView` offering engaging ways to collect valuable user attributes. The custom modal in-app message allows you to use Connected Content or any available list to display and capture attributes from a dynamic list of items. 

You can interject your own views into subclassed in-app messages. This example showcases how a `UIPickerView` can be utilized to extend the functionality of an `ABKModalInAppMessageViewController`.

Visit the [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift) to get started.

#### Dashboard configuration

To set up a modal in-app message in the dashboard, you must provide a list of items formatted as a comma-separated string. In our example, we use Connected Content to pull a JSON list of team names and format them accordingly.

![The in-app message composer shows a preview of what the in-app message will look like but instead displays the list of items you supplied to Braze. As the Braze UI does not display your custom in-app message UI unless sent to a phone, the preview is not indicative of what your message will look like, so we recommend you test before sending.]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

In the key-value pairs, provide an `attribute_key`; this key, along with the user's selected value, will be saved to their user profile as a custom attribute. Your custom view logic must handle user attributes sent to Braze.

The `extras` dictionary in the `ABKInAppMessage` object allows you to query for a `view_type` key (if any) that signals the correct view to display. It's important to note that in-app messages are configured on a per-message basis, so custom and default modal views can work harmoniously.

![Two key-value pairs found in the message composer. The first key-value pair has "attribute_key" set as "Favorite Team", and the second has "view_type" set as "picker".]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**Using `view_type` for UI display behavior**<br>
Query the `extras` dictionary for your `view_type` to load the desired subclassed view controller.

```swift
func modalViewController(inAppMessage: ABKInAppMessage) -> ABKInAppMessageModalViewController {
  switch inAppMessage.extras?[InAppMessageKey.viewType.rawValue] as? String {
  case InAppMessageViewType.picker.rawValue:
    return ModalPickerViewController(inAppMessage: inAppMessage)
  default:
    return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Using `view_type` for UI display behavior**<br>
Query the `extras` dictionary for your `view_type` to load the desired subclassed view controller.

```objc
- (ABKInAppMessageModalViewController *)modalViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyViewType];
  NSString *viewType = [inAppMessageData rawValueForInAppMessageViewType:InAppMessageViewTypePicker];
   
  if ([inAppMessage.extras objectForKey:key] && [inAppMessage.extras[key] isEqualToString:viewType]) {
    return [[ModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Override and provide custom view**<br>
Override `loadView()` and set your own custom view to suit your needs.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objective-C %}
**Override and provide custom view**<br>
Override `loadView()` and set your own custom view to suit your needs.
```objc
- (void)loadView {
  NSString *nibName = @"ModalPickerViewController";
  [[NSBundle mainBundle] loadNibNamed:nibName owner:self options:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Format variables for a dynamic list**<br>
Before reloading the `UIPickerView` components, the `inAppMessage` message variable is output as a _String_. This message must be formatted as an array of items to be displayed correctly. As an example, this can be achieved using [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components).
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
**Format variables for PickerView**<br>
Before reloading the `UIPickerView` components, the `inAppMessage` message variable is output as a _String_. This message must be formatted as an array of items to be displayed correctly. For example, this can be achieved using [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc).
```objc
- (void)viewDidLoad {
  [super viewDidLoad];
   
  self.items = [[NSArray alloc] initWithArray:[self.inAppMessage.message componentsSeparatedByString:@", "]];
  [self.pickerView reloadAllComponents];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Assign custom attribute**<br>
Using the subclass, after a user presses submit, pass the attribute with its corresponding selected value to Braze.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
**Assign custom attribute**<br>
Using the subclass, after a user presses submit, pass the attribute with its corresponding selected value to Braze.
```objc
- (IBAction)primaryButtonTapped:(id)sender {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyAttributeKey];
   
  if (self.selectedItem.length > 0 && [self.inAppMessage.extras objectForKey:key]) {
    [[AppboyManager shared] setCustomAttributeWithKey:self.inAppMessage.extras[key] andStringValue:self.selectedItem];
  }
}
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Interesting in leveraging our custom modal in-app messages to share videos across FaceTime? Check out our SharePlay in-app message [implementation guide]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide/shareplay/).
{% endalert%}

### Custom full in-app message

![An in-app message that displays a list of configuration options with toggles beside each option. At the bottom of the message, there is a large blue submit button.]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Use custom full in-app messages to create interactive, user-friendly prompts to collect valuable customer data. The example to the right shows an implementation of the custom full in-app message reimagined as an interactive push primer with notification preferences. 

Visit the [`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) to get started.

#### Dashboard configuration

To set up a custom full in-app message in the dashboard, you must provide a list of your tags formatted as a comma-separated string. 

In the key-value pairs, provide an `attribute_key`; this key, along with the user's selected values, will be saved to their user profile as a custom attribute. Your custom view logic must handle user attributes sent to Braze.

![Three key-value pairs found in the message composer. The first key-value pair "attribute_key" is set as "Push Tags", the second "subtitle_text" is set as "Enabling notifications will also...", and the third "view_type" is set as "table_list".]({% image_buster /assets/img/iam_implementation/dashboard3.png %}){: style="max-width:65%;"}

#### Intercepting in-app message touches
![An Apple device displaying rows of settings and toggles. The custom view handles the buttons, and any touches outside of the button controls are handled by the in-app message and will dismiss it.]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
Intercepting in-app message touches is crucial in making the custom full in-app message buttons function correctly. By default, the `ABKInAppMessageImmersive` adds a tap gesture recognizer onto the message, so users can dismiss messages without buttons. By adding a `UISwitch` or button to the `UITableViewCell` view hierarchy, the touches now get handled by our custom view. As of iOS 6, buttons and other controls have precedence when working with gesture recognizers, making our custom full in-app message work as it should. 

