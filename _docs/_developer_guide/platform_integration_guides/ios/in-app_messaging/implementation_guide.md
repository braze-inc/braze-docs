---
nav_title: Advanced Implementation (Optional)
article_title: In-App Message Implementation Guide for iOS (Optional)
platform: iOS
page_order: 6
description: "This advanced implementation guide covers iOS in-app message code considerations, three use cases built by our team, and accompanying code snippets."
channel:
  - in-app messages
---

{% alert important %}
Looking for the out-of-the-box in-app message developer integration guide? Find it [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/).
{% endalert %}

# In-app messaging implementation guide

> This optional and advanced implementation guide covers in-app message code considerations, three custom use cases built by our team, and accompanying code snippets. Visit our Braze Demo repository [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Please note that this implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.  Looking for HTML implementations? Take a look at our [HTML template repository](https://github.com/braze-inc/in-app-message-templates)!

## Code considerations

The following guide offers an optional custom developer integration to use in addition to out-of-the-box in-app messages. Custom view controllers are included below with each use case, offering examples to extend functionality and natively customize the look and feel of your in-app messages.

### ABKInAppMessage subclasses

The code snippet below is a UI delegate method from the Braze SDK that determines what subclass view you want to populate your in-app message with. We cover a basic implementation in this guide and show how the full, slide up, and modal subclasses can be implemented in captivating ways. Please note that if you want to set up your custom view controller, you must set up all other in-app message subclasses. Once you have a solid understanding of the concepts behind subclassing, check out our [use cases](#sample-use-cases) below to get started implementing in-app messaging subclasses.

{% tabs %}
{% tab Swift %}
__ABKInAppMessage Subclasses__<br>

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
__ABKInAppMessage Subclasses__<br> 

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

## Sample use cases

There are three sample customer use cases provided.  Each use case offers a detailed explanation, relevant code snippets, and a look into how in-app messages may look and be used in the Braze dashboard:
- [Custom Slideup In-App Message](#custom-slideup-in-app-message)
- [Custom Modal In-App Message](#custom-modal-in-app-message)
- [Custom Full In-App Message](#custom-full-in-app-message)

### Custom slideup in-app message

![Slideup in-app message][2]{: style="float:right;max-width:45%;margin-left:15px;border:0;"}

While building out your slide-up in-app message, you may notice you aren't able to modify the placement of the message. While this option is not explicitly offered out-of-the-box, modification like this is made possible by subclassing the `ABKInAppMessageSlideupViewController` and overriding the `offset` variable with your own custom variable. The image to the right shows two examples of how this can be used to adjust both slide-up and slide-down in-app messages. 

Visit the [SlideFromBottomViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) to get started.

#### __Adding additional behavior to our default UI__<br><br>

{% tabs %}
{% tab Swift %}
__Update `offset` Variable__<br>
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
__Update `slideConstraint` Variable__<br>
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
Visit the Braze Demo repository for the [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17) function referenced above.
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
__Update `offset` Variable__<br>
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
__Update `slideConstraint` Variable__<br>
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
__Override and Set Custom Constraint__<br>
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
__Override and Set Custom Constraint__<br> 
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

__Adjust Constraint for Device Orientation__<br>
Adjust the respective value in `viewWillTransition()` because the subclass assumes responsibility for keeping the constraint synced during layout changes.

### Custom modal in-app message

![Modal in-app message][3]{: style="float:right;max-width:23%;margin-left:15px;border:0;"}

An `ABKInAppMessageModalViewController` can be subclassed to leverage a `UIPickerView` offering engaging ways to collect valuable user attributes. The custom modal in-app message allows you to use Connected Content or any available list to display and capture attributes from a dynamic list of items. 

You can interject your own views into subclassed in-app messages. This example showcases how a `UIPickerView` can be utilized to extend the functionality of an `ABKModalInAppMessageViewController`.

Visit the [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift) to get started.

#### Dashboard configuration

To set up a modal in-app message in the dashboard, you must provide a list of items formatted as a comma-seperated string. In our example, we use Connected Content to pull a JSON list of team names and format them accordingly.

![Modal dashboard][4]

In the key-value pairs, provide an `attribute_key`; this key, along with the user's selected value, will be saved to their user profile as a custom attribute. User attributes sent to Braze must be handled by your custom view logic.

The `extras` dictionary in the `ABKInAppMessage` object allows you to query for a `view_type` key (if any) that signals the correct view to display. It’s important to note that in-app messages are configured on a per-message basis, so custom and out-of-the-box modal views can work harmoniously.

![Modal dashboard key-value pairs][5]{: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
__Using `view_type` for UI Display Behavior__<br>
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
__Using `view_type` for UI Display Behavior__<br>
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
__Override and Provide Custom View__<br>
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
__Override and Provide Custom View__<br>
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
__Format Variables for a Dynamic List__<br>
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
__Format Variables for PickerView__<br>
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
__Assign Custom Attribute__<br>
Using the subclass, after a user presses submit, pass the attribute with its corresponding selected value to Braze.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
__Assign Custom Attribute__<br>
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

### Custom full in-app message

![Full screen in-app message][6]{: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Use custom full in-app messages to create interactive, user-friendly prompts to collect valuable customer data. The example to the right shows an implementation of the custom full in-app message reimagined as an interactive push primer with notification preferences. 

Visit the [FullListViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) to get started.

#### Dashboard configuration

To set up a custom full in-app message in the dashboard, you will need to provide a list of your tags formatted as a comma-seperated string. 

<!---
![Full dashboard][8]
--->

In the key-value pairs, provide an `attribute_key`; this key, along with the user's selected values, will be saved to their user profile as a custom attribute. User attributes sent to Braze must be handled by your custom view logic.

The `extras` dictionary in the `ABKInAppMessage` object allows you to query for a `view_type` key (if any) that signals the correct view to display. It’s important to note that in-app messages are configured on a per-message basis, so custom and out-of-the-box modal views can work harmoniously.

![Full screen dashboard key-value pairs][7]{: style="max-width:65%;"}

#### Intercepting in-app message touches
![Touches][1]{: style="float:right;max-width:30%;margin-left:10px;border:0"}
Intercepting in-app message touches is crucial in making the custom full in-app message buttons function correctly. By default, the `ABKInAppMessageImmersive` adds a tap gesture recognizer onto the message, so users can dismiss messages without buttons. By adding a `UISwitch` or button to the `UITableViewCell` view hierarchy, the touches now get handled by our custom view. As of iOS 6, buttons and other controls have precedence when working with gesture recognizers, making our custom full in-app message work as it should. 

[1]: {% image_buster /assets/img/iam_implementation_guide.png %}
[2]: {% image_buster /assets/img/iam_implementation/slideup.png %}
[3]: {% image_buster /assets/img/iam_implementation/modal.png %}
[4]: {% image_buster /assets/img/iam_implementation/dashboard1.png %}
[5]: {% image_buster /assets/img/iam_implementation/dashboard2.png %}
[6]: {% image_buster /assets/img/iam_implementation/fullscreen.png %}
[7]: {% image_buster /assets/img/iam_implementation/dashboard3.png %}
[8]: {% image_buster /assets/img/iam_implementation/dashboard4.png %}
