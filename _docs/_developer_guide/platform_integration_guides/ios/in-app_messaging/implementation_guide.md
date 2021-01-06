---
nav_title: Implementation Guide
platform: iOS
page_order: 4.1
description: "This implementation guide covers in-app message code considerations, three use cases built by our team, and accompanying code snippets."
---

# In-App Messaging Implementation Guide

> This implementation guide covers in-app message code consideration, three use cases built by our team, and accompanying code snippets. Visit out Braze Demo Repository [here]()! Please note that this implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.
 
## Code Considerations

### ABKInAppMessage Subclasses

The code snippet below is a UI delegate method from the Braze SDK that determines what subclass view you want to populate your in-app message with. We cover a basic implementation in this guide and show how the full, slide up and modal subclasses can be implemented in captivating ways. Please note that if you want to set up your custom view controller, you must set up all other in-app message subclasses. Once you have a solid understanding of the concepts behind subclassing, check out our [use cases](#sample-use-cases) below to get started implementing in-app messaging subclasses.

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
    case is ABKInAppMessageImmersive:
      return ABKInAppMessageImmersiveViewController(inAppMessage: inAppMessage)
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
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
    return [[ABKInAppMessageImmersiveViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## Sample Use Cases

There are three sample customer use cases provided. Each sample has video walkthroughs, code snippets, and a look into how in-app messaging variables may look and be used in the Braze dashboard:
- [In-App Message Slideup Modification](#in-app-messaging-slideup-customization)
- [Custom Modal In-App Message](#custom-modal-in-app-message)
- [Custom Full In-App Message](#custom-full-in-app-message)

### In-App Message Slideup Modification

While building out your slide-up in-app message, you may notice you aren't able to modify the placement of the message. While this option is not explicitly offered out-of-the-box, customization like this is made possible by subclassing the `ABKInAppMessageSlideupViewController` and overriding slide constraint settings to set your own custom constraint value.

{% include video.html id="xfTtkZGjpxQ" align="center" %}

#### __Subclassing the ABKInAppMessageSlideupViewController__<br><br>

{% tabs %}
{% tab Swift %}
__Override and Set Custom Constraint__<br>
Override `beforeMoveInAppMessageViewOnScreen()` and set your own custom constraint value to suit your needs. The original value is set in the superclass.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% endtab %}
{% tab Objective-C %}
__Override and Set Custom Constraint__<br> 
Override `beforeMoveInAppMessageViewOnScreen()` and set your own custom constraint value to suit your needs. The original value is set in the superclass.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
__Update `slideConstraint` Variable__<br>
The `slideConstraint` public variable comes from the superclass `ABKInAppMessageSlideupViewController`. Here, you can update the `slideConstraint` so it gets updated in the view controller superclass. 

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
{% endtab %}
{% tab Objective-C %}
__Update `slideConstraint` Variable__<br>
The `slideConstraint` public variable comes from the superclass `ABKInAppMessageSlideupViewController`. Here, you can update the `slideConstraint` so it gets updated in the view controller superclass.  

```objc
- (void)setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = self.view.superview.safeAreaInsets.bottom + self.tabBarHeight;
}
```
{% endtab %}
{% endtabs %}

__Adjust Constraint for Device Orientation__<br>
Adjust the constraint in `viewWillTransition()` because the subclass assumes responsibility of keeping the constraint synced during layout changes.

### Custom Modal In-App Message

An `ABKInAppMessageModalViewController` can be subclassed to leverage a `UIPickerView` offering engaging ways to collect valuable user data. The example below shows how you can use Connected Content to capture custom attributes from a dynamic list of items. 

{% include video.html id="hOPUB5fn0F0" align="center" %}

{% tabs %}
{% tab Swift %}
__Parsing "view_type"__<br>
An in-app message has an `extras` dictionary that comes with the `ABKInAppMessage` modal. We are able to query that dictionary to find the `view_type` key (if any) and display the correct type of view. It’s important to to note that in-app messages are configured on a per-message basis, so custom and out-of-the-box modal views can work harmoniously.

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
__Parsing "view_type"__<br>
An in-app message has an `extras` dictionary that comes with the `ABKInAppMessage` modal. We are able to query that dictionary to find the `view_type` key (if any) and display the correct type of view. It’s important to to note that in-app messages are configured on a per-message basis, so custom and out-of-the-box modal views can work harmoniously.

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
Before reloading the `UIPickerView` components, the `inAppMessage` message variable is output as a _String_. This message must be formatted as an array of items to be displayed correctly. As an example, this can be achieved using [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc).
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
Using the subclass, after a user presses submit, pass the item to Braze with the custom `attributeKey` from the in-app message.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
__Assign Custom Attribute__<br>
Using the subclass, after a user presses submit, pass the item to Braze with the custom `attributeKey` from the in-app message.
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

### Custom Full In-App Message

Use custom full in-app messages to create interactive, user-friendly prompts to collect valuable customer data. The example below shows an implementation of the custom full in-app message reimagined as an interactive push primer with notification preferences. 

{% include video.html id="X2HsHIeNo4I" align="center" %}

#### Intercepting In-App Message Touches
![Touches][1]{: style="float:right;max-width:30%;margin-left:10px;border:0"}
Intercepting in-app message touches is crucial in making the custom full in-app message buttons function correctly. By default, the `ABKInAppMessageImmersive` adds a tap gesture recognizer onto the message so users are able to dismiss messages without buttons. While useful, this is not always the desired behavior, so you have the option to add a `UISwitch` or list of switches to the table view to work with the existing button behavior. Through the use of multiple switches, the touches now get handled by our custom view. As of iOS 6, buttons and other controls have precedence when working with gesture recognizers, making our custom full in-app message work as it should. 

[1]: {% image_buster /assets/img/iam_implementation_guide.png %}
