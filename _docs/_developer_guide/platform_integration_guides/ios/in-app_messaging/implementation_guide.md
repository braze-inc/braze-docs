---
nav_title: Implementation Guide
platform: iOS
page_order: 7
description: "This implementation guide covers In-App Message code considerations, three use cases built by our team, accompanying code snippets, and guidance on "
---

# In-App Messaging Implementation Guide

> This implementation guide covers Content Card code considerations, three use cases built by our team, accompanying code snippets, and guidance on logging impressions, clicks, and dismissals. Visit our Braze Demo Repository [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Please note that this implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.

## Code Considerations

### Import Statements and Helper Files

When building out Content Cards, you should integrate them using a single `import Appboy-iOS-SDK` statement and helper file. This approach limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code. An example helper file can be found [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze%20Demo/AppboyManager.swift).

### Content Cards as Custom Objects

Much like a rocketship adding a booster, your own custom objects can be extended to function as Content Cards. Limited API surfaces such as this, provide flexibility to work with different data backends interchangeably. This can be done by conforming to the `ContentCardable` protocol and implementing the initializer (as seen below) and through the use of the `ContentCardData` struct, allows you to access the `ABKContentCard` data.

The initializer also includes a `ContentCardClassType` enum. Through the use of key-value pairs within the Braze dashboard, you can set an explicit `class_type` key that will be used to determine what object to initialize. Once you have a solid understanding of these code considerations, check out our [use cases](#sample-use-cases) below to get started implementing your own custom objects.

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

There are three sample customer use cases provided. Each sample has video walkthroughs, code snippets, and a look into how Content Card variables may look and be used in the Braze dashboard:
- [Modifying IAM Slideup Point](#modifying-iam-slideup-point)
- [Custom Modal In-App Message](#custom-modal-in=app-message)
- [Custom Full In-App Message](#custom-full-in-app-message)

### Modifying IAM Slideup Point
INTRO TEXT

{% include video.html id="" align="center" %}
#### __Load Content Cards Alongside Existing Content__<br><br>

{% tabs %}
{% tab Swift %}
__Subclassing ABKInAppMessageSlideupViewController__<br>

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% endtab %}
{%Subclassing ABKInAppMessageSlideupViewController__<br> 

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
__Subclassing ABKInAppMessageSlideupViewController__<br>

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
__Subclassing ABKInAppMessageSlideupViewController__<br> 

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
__Subclassing ABKInAppMessageSlideupViewController__<br>

```swift
func setSlideConstraint() {
  guard let superview = view.superview else { return }
   
  slideConstraint?.constant = superview.safeAreaInsets.bottom + tabBarHeight
}
```
{% endtab %}
{% tab Objective-C %}
__Subclassing ABKInAppMessageSlideupViewController__<br> 

```objc
- (void)setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = self.view.superview.safeAreaInsets.bottom + self.tabBarHeight;
}
```
{% endtab %}
{% endtabs %}

### Custom Modal In-App Message
Content Cards can be used in a message center format where each message is its own card. Each card contains additional key-value pairs that power on-click UI/UX.
{% include video.html id="dmaT61p8kW8" align="center" %}

{% tabs %}
{% tab Swift %}
__Parsing "view_type"__<br>
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
__Subclassing ABKInAppMessageModalViewController__<br>
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
__Subclassing ABKInAppMessageModalViewController__<br>
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
__Subclassing ABKInAppMessageModalViewController__<br>
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
__Subclassing ABKInAppMessageModalViewController__<br>
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
__Subclassing ABKInAppMessageModalViewController__<br>
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
__Subclassing ABKInAppMessageModalViewController__<br>
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
INTRO TEXT

{% include video.html id="76ivkU6Zmdg" align="center" %}


