---
nav_title: Implementation Guide
platform: iOS
page_order: 4.1
description: "This implementation guide covers in-app message code considerations, three use cases built by our team, and accompanying code snippets."
---

# In-App Messaging Implementation Guide

> This implementation guide covers in-app message code consideration, three use cases built by our team, and accompanying code snippets. Visit out Braze Demo Repository [here]()! Please note that this implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.

## Code Considerations

### Understanding Subclassing

A subclass inherits its properties from its superclass and can be used to override them to refine or modify their behavior. In the example below, you can see that the superclass Mammal has a subclass of Cat and Dog, and Dog has a subclass of GermanShephard and Poodle. Because Poodle is a subclass of Dog that is a subclass of Mammal, Poodle has access to Mammal properties and methods like `getEyeColor()`. This same type of subclassing behavior can be used to our advantage when building out in-app messages. 

__In-App Messages can be Subclasses to Power Custom Views__<br>
Like riding a rollercoaster, pushing the limits to get the most out of in-app messages can be intimidating, but by leveraging subclasses you can have a safe, engaging, and enjoyable implementation experience.

### ABKInAppMessage Subclasses

The code snippet below is a UI delegate method from the Braze SDK that determines what subclass view you want to populate your in-app message with. Within this method are five subclasses. We will be covering a basic implementation and show how the full, slide up and modal subclasses can be implemented in captivating ways. Please note that if you want to set up your custom view controller, you must set up all other in-app message subclasses. Once you have a solid understanding of the concepts behind subclassing, check out our [use cases](#sample-use-cases) below to get started implementing In-App Messaging subclasses.

{% include video.html id="" align="center" %}

{% tabs %}
{% tab Swift %}
__ABKInAppMessage Subclasses__<br>

```swift
extension AppboyManager: ABKInAppMessageUIDelegate {
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return slideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return modalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return fullViewController(inAppMessage: inAppMessage)
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
    return [self slideupViewControllerWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage];
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

There are three sample customer use cases provided. Each sample has video walkthroughs, code snippets, and a look into how In-App Messaging variables may look and be used in the Braze dashboard:
- [In-App Message Slideup Customization](#in-app-messaging-slideup-customization)
- [Custom Modal In-App Message](#custom-modal-in-app-message)
- [Custom Full In-App Message](#custom-full-in-app-message)

### In-App Message Slideup Customization

While building out your slide-up in-app message, you may notice you aren't able to customize the placement of the message. While this option is not explicitly offered out-of-the-box, customization like this is made possible by subclassing the `ABKInAppMessageSlideupViewController` and overriding slide constraint settings to set your own custom constraint value.

{% include video.html id="" align="center" %}

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
__Adjust Constraint for Device Orientation__<br>
Adjust the constraint in `viewWillTransition()` so the in-app message positioning stays synced and displays correctly when changing device orientation. 

```swift
override func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator) {
  super.viewWillTransition(to: size, with: coordinator)
  coordinator.animate(alongsideTransition: { context in
    self.setSlideConstraint()
  }, completion: nil)
}
```
{% endtab %}
{% tab Objective-C %}
__Adjust Constraint for Device Orientation__<br> 
Adjust the constraint in the `viewWillTransition` so the in-app message positioning stays synced and displays correctly when changing device orientation. 
```objc
- (void)viewWillTransitionToSize:(CGSize)size withTransitionCoordinator:(id<UIViewControllerTransitionCoordinator>)coordinator {
  [super viewWillTransitionToSize:size withTransitionCoordinator:coordinator];
  [coordinator animateAlongsideTransition:^(id<UIViewControllerTransitionCoordinatorContext>  _Nonnull context) {
    [self setSlideConstraint:self.slideConstraint];
  } completion:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
__Update `slideConstraint` Variable__<br>
The `slideConstraint` public variable comes from the superclass `ABKInAppMessageSlideupViewController`. Here you must update the `slideConstraint` variable so it gets updated in the view controller superclass. 

```swift
func setSlideConstraint() {
  guard let superview = view.superview else { return }
   
  slideConstraint?.constant = superview.safeAreaInsets.bottom + tabBarHeight
}
```
{% endtab %}
{% tab Objective-C %}
__Update `slideConstraint` Variable__<br>
The `slideConstraint` public variable comes from the superclass `ABKInAppMessageSlideupViewController`. Here you must update the `slideConstraint` variable so it gets updated in the view controller superclass.  

```objc
- (void)setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = self.view.superview.safeAreaInsets.bottom + self.tabBarHeight;
}
```
{% endtab %}
{% endtabs %}

### Custom Modal In-App Message

The Custom Modal subclass can be used to create a `pickerView` that offers engaging ways to collect valuable user data. The example below shows how you can use Connected Content and the `pickerView` to capture custom attributes like Favorite Team from a dynamic list of items. 

{% include video.html id="dmaT61p8kW8" align="center" %}

{% tabs %}
{% tab Swift %}
__Parsing "view_type"__<br>
An in-app message has an `extras` dictionary that comes with the `ABKInAppMessage` modal. We are able to query that dictionary to find the `view_type` key (if any) and display the correct type of view.
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
An in-app message has an `extras` dictionary that comes with the `ABKInAppMessage` modal. We are able to query that dictionary to find the `view_type` key (if any) and display the correct type of view.
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
Override `loadview()` and set your own custom view to suit your needs.
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
Override `loadview()` and set your own custom view to suit your needs.
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
__Format Variables for PickerView__<br>
The `pickerView` requires that you format the in-app message message string response to an array of individual strings, seperated by a comma and a space. 
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
The `pickerView` requires that you format the in-app message message string response to an array of individual strings, seperated by a comma and a space. 
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
   
  if (self.selectedItem.length > 0 && [self.inAppMessage.extras objectForKey: key]) {
    [[AppboyManager shared] setCustomAttributeWithKey:self.inAppMessage.extras[key] andStringValue:self.selectedItem];
  }
}
```
{% endtab %}
{% endtabs %}

### Custom Full In-App Message

Use custom full in-app messages to create interactive, user-friendly prompts to collect valuable customer data. The example below shows an implementation of the custom full in-app message reimagined as an interactive push primer with notification preferences. 

{% include video.html id="" align="center" %}

#### Intercepting In-App Message Touches

Intercepting in-app message touches is crucial in making the custom full in-app message buttons function correctly. By default, the `ABKInAppMessageImmersive` adds a tap gesture recognizer onto the message so users are able to dismiss messages without buttons. While useful, this is not the desired behavior so you must add a `UISwitch` or list of switches to the table view to deal with the conflicting button behavior. Through the use of multiple UIswitches, the touches now get handled by our custom view. Thanks to Apple, we are able to give buttons and other controls precedence when working with gesture recognizers, making our custom full in-app message work as it should. 