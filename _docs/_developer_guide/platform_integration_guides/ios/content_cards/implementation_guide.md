---
nav_title: Advanced Implementation (Optional)
platform: iOS
page_order: 7
description: "This advanced implementation guide covers Content Card code considerations, three use cases built by our team, accompanying code snippets, and guidance on logging impressions, clicks, and dismissals."
---

{% alert important %}
Looking for the out-of-the-box Content Card developer integration guide? Find it [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/).
{% endalert %}

# Content Card Implementation Guide

> This optional and advanced implementation guide covers Content Card code considerations, three custom use cases built by our team, accompanying code snippets, and guidance on logging impressions, clicks, and dismissals. Visit our Braze Demo Repository [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Please note that this implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.

## Code Considerations

### Import Statements and Helper Files

When building out Content Cards, it is recommended to integrate them using a single `import Appboy-iOS-SDK` statement with the use of a helper file. This approach limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code. An example helper file can be found [here](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

### Content Cards as Custom Objects

Much like a rocketship adding a booster, your own custom objects can be extended to function as Content Cards. Limited API surfaces such as this provide flexibility to work with different data backends interchangeably. This can be done by conforming to the `ContentCardable` protocol and implementing the initializer (as seen below) and, through the use of the `ContentCardData` struct, allows you to access the `ABKContentCard` data. The `ABKContentCard` payload will be used to initialize the `ContentCardData` struct and the custom object itself, all from a `Dictionary` type via the initializer the protocol comes with.

The initializer also includes a `ContentCardClassType` enum. This enum is used to decide which object to initialize. Through the use of key-value pairs within the Braze dashboard, you can set an explicit `class_type` key that will be used to determine what object to initialize. These key-value pairs for Content Cards come through in the `extras` variable on the `ABKContentCard`. Another core component of the initializer is the `metaData` dictionary parameter. The `metaData` includes everything from the `ABKContentCard` parsed out into a series of keys and values. Once the relevant cards are parsed and converted to your custom objects, the app is ready to begin working with them as if the objects were instantiated from JSON or any other source. 

Once you have a solid understanding of these code considerations, check out our [use cases](#sample-use-cases) below to get started implementing your own custom objects.

{% tabs %}
{% tab Swift %}
__No `ABKContentCard` Dependencies__<br>
`ContentCardData` represents the parsed out values of an `ABKContentCard`.

__ContentCardable Protocol__
```swift
protocol ContentCardable {
  var contentCardData: ContentCardData? { get }
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType)
}
 
extension ContentCardable {
  var isContentCard: Bool {
    return contentCardData != nil
  }
   
  func logContentCardClicked() {
    BrazeManager.shared.logContentCardClicked(idString: contentCardData?.contentCardId)
  }
   
  func logContentCardDismissed() {
    BrazeManager.shared.logContentCardDismissed(idString: contentCardData?.contentCardId)
  }
   
  func logContentCardImpression() {
    BrazeManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```
__Content Card Data Struct__
```swift
struct ContentCardData: Hashable {
  let contentCardId: String
  let contentCardClassType: ContentCardClassType
  let createdAt: Double
  let isDismissable: Bool
  ...
  // other Content Card properties such as expiresAt, pinned, etc.
}
 
extension ContentCardData: Equatable {
  static func ==(lhs: ContentCardData, rhs: ContentCardData) -> Bool {
    return lhs.contentCardId == rhs.contentCardId
  }
}
```
{% endtab %}
{% tab Objective-C %}

__No `ABKContentCard` Dependencies__<br>
`ContentCardData` represents the parsed out values of an `ABKContentCard`.

__ContentCardable Protocol__
```objc
@protocol ContentCardable <NSObject>
 
@property (nonatomic, strong) ContentCardData *contentCardData;
- (instancetype __nullable)initWithMetaData:(NSDictionary *)metaData
                                  classType:(enum ContentCardClassType)classType;
 
- (BOOL)isContentCard;
- (void)logContentCardImpression;
- (void)logContentCardClicked;
- (void)logContentCardDismissed;
 
@end
```
__Content Card Data Struct__
```objc
@interface ContentCardData : NSObject
 
+ (ContentCardClassType)contentCardClassTypeForString:(NSString *)rawValue;
 
- (instancetype)initWithIdString:(NSString *)idString
                       classType:(ContentCardClassType)classType
                       createdAt:(double)createdAt isDismissible:(BOOL)isDismissible;
 
@property (nonatomic, readonly) NSString *contentCardId;
@property (nonatomic) ContentCardClassType classType;
@property (nonatomic, readonly) double *createdAt;
@property (nonatomic, readonly) BOOL isDismissible;
...
// other Content Card properties such as expiresAt, pinned, etc.    
 
@end
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Custom Object Initializer__<br>
MetaData from an `ABKContentCard` is used to populate your object's variables. The key-value pairs set up in the Braze Dashboard are represented in the "extras" dictionary.

```swift
extension CustomObject: ContentCardable {
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType) {
    guard let idString = metaData[.idString] as? String,
      let createdAt = metaData[.created] as? Double,
      let isDismissable = metaData[.dismissable] as? Bool,
      let extras = metaData[.extras] as? [AnyHashable: Any],
      else { return nil }
 
    let contentCardData = ContentCardData(contentCardId: idString, contentCardClassType: contentCardClassType, createdAt: createdAt, isDismissable: isDismissable)
    let customObjectProperty = extras["YOUR-CUSTOM-OBJECT-PROPERTY"] as? String
           
    self.init(contentCardData: contentCardData, property: customObjectProperty)
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Custom Object Initializer__<br>
MetaData from an `ABKContentCard` is used to populate your object's variables. The key-value pairs set up in the Braze Dashboard are represented in the "extras" dictionary.

```objc
- (id _Nullable)initWithMetaData:(nonnull NSDictionary *)metaData classType:(enum ContentCardClassType)classType {
  self = [super init];
  if (self) {
    if ([metaData objectForKey:ContentCardKeyIdString] && [metaData objectForKey:ContentCardKeyCreated] && [metaData objectForKey:ContentCardKeyDismissible] && [metaData objectForKey:ContentCardKeyExtras]) {
      NSDictionary  *extras = metaData[ContentCardKeyExtras];
      NSString *idString = metaData[ContentCardKeyIdString];
      double createdAt = [metaData[ContentCardKeyCreated] doubleValue];
      BOOL isDismissible = metaData[ContentCardKeyDismissible];
 
      if ([extras objectForKey: @"YOUR-CUSTOM-PROPERTY")
        _customObjectProperty = extras[@"YOUR-CUSTOM-OBJECT-PROPERTY"];
 
      self.contentCardData = [[ContentCardData alloc] initWithIdString:idString classType:classType createdAt:createdAt isDismissible:isDismissible];
 
      return self;
    }
  }
  return nil;
}
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Identifying Types__<br>
The `ContentCardClassType` enum represents the `class_type` value in the Braze Dashboard. This value is also used as a filter identifier to display Content Cards in different places. 

```swift
enum ContentCardClassType: Hashable {
  case yourValue
  case yourOtherValue
  ...
  case none
 
  init(rawType: String?) {
    switch rawType?.lowercased() {
    case "your_value":
      self = .yourValue
    case "your_other_value":
      self = .yourOtherValue
    ...
    default:
      self = .none
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Identifying Types__<br>
The `ContentCardClassType` enum represents the `class_type` value in the Braze Dashboard. This value is also used as a filter identifier to display Content Cards in different places. 

```objc
typedef NS_ENUM(NSInteger, ContentCardClassType) {
  ContentCardClassTypeNone = 0,
  ContentCardClassTypeYourValue,
  ContentCardClassTypeYourOtherValue,
  ...
};
 
+ (NSArray *)contentCardClassTypeArray {
  return @[ @"", @"your_value", @"your_other_value" ];
}
 
+ (ContentCardClassType)contentCardClassTypeForString:(NSString*)rawValue {
  if ([[self contentCardClassTypeArray] indexOfObject:rawValue] == NSNotFound) {
    return ContentCardClassTypeNone;
  } else {
    NSInteger value = [[self contentCardClassTypeArray] indexOfObject:rawValue];
    return (ContentCardClassType) value;
  }
}
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Working with Content Cards__<br>

```swift
func handleContentCardsUpdated(_ notification: Notification, for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  guard let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool, updateIsSuccessful, let cards = contentCards else { return [] }
             
  return convertContentCards(cards, for: classTypes)
}
```
{% endtab %}
{% tab Objective-C %}
__Working with Content Cards__<br>

```objc
- (NSArray *)handleContentCardsUpdated:(NSNotification *)notification forClassType:(ContentCardClassType)classType {  
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    return [self convertContentCards:self.contentCards forClassType:classType];
  } else {
    return @[];
  }
}
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Working with Payload Data__<br>

```swift
func convertContentCards(_ cards: [ABKContentCard], for classTypes: [ContentCardClassType]) -> [ContentCardable] {
  var contentCardables: [ContentCardable] = []
    
  for card in cards {
    let classTypeString = card.extras?[ContentCardKey.classType.rawValue] as? String
    let classType = ContentCardClassType(rawType: classTypeString)
    guard classTypes.contains(classType) else { continue }
       
    var metaData: [ContentCardKey: Any] = [:]
    switch card {
    case let banner as ABKBannerContentCard:
      metaData[.image] = banner.image
    case let captioned as ABKCaptionedImageContentCard:
      metaData[.title] = captioned.title
      metaData[.cardDescription] = captioned.cardDescription
      metaData[.image] = captioned.image
    case let classic as ABKClassicContentCard:
      metaData[.title] = classic.title
      metaData[.cardDescription] = classic.cardDescription
    default:
      break
    }
 
    metaData[.idString] = card.idString
    metaData[.created] = card.created
    metaData[.dismissible] = card.dismissible
    metaData[.urlString] = card.urlString
    metaData[.extras] = card.extras
    ...
    // other Content Card properties such as expiresAt, pinned, etc.
      
    if let contentCardable = contentCardable(with: metaData, for: classType) {
      contentCardables.append(contentCardable)
    }
  }
  return contentCardables
}
```
{% endtab %}
{% tab Objective-C %}
__Working with Payload Data__<br>

```objc
- (NSArray *)convertContentCards:(NSArray<ABKContentCard*> *)cards forClassType:(ContentCardClassType)classType {
  NSMutableArray *contentCardables = [[NSMutableArray alloc] init];      for (ABKContentCard *card in cards) {
    NSString *classTypeString = [card.extras objectForKey:ContentCardKeyClassType];
    ContentCardClassType cardClassType = [ContentCardData contentCardClassTypeForString: classTypeString];
    if (cardClassType != classType) { continue; }
     
    NSMutableDictionary *metaData = [[NSMutableDictionary alloc] init];
    if ([card isKindOfClass:[ABKBannerContentCard class]]) {
      ABKBannerContentCard *banner = (ABKBannerContentCard *)card;
      metaData[ContentCardKeyImage] = banner.image;
    } else if ([card isKindOfClass:[ABKCaptionedImageContentCard class]]) {
      ABKCaptionedImageContentCard *captioned = (ABKCaptionedImageContentCard *)card;
      metaData[ContentCardKeyTitle] = captioned.title;
      metaData[ContentCardKeyCardDescription] = captioned.cardDescription;
      metaData[ContentCardKeyImage] = captioned.image;
    } else if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ABKClassicContentCard *classic = (ABKClassicContentCard *)card;
      metaData[ContentCardKeyCardDescription] = classic.title;
      metaData[ContentCardKeyImage] = classic.image;
    }
     
    metaData[ContentCardKeyIdString] = card.idString;
    metaData[ContentCardKeyCreated] = [NSNumber numberWithDouble:card.created];
    metaData[ContentCardKeyDismissible] = [NSNumber numberWithBool:card.dismissible];
    metaData[ContentCardKeyUrlString] = card.urlString;
    metaData[ContentCardKeyExtras] = card.extras;
    ...
    // other Content Card properties such as expiresAt, pinned, etc.   
 
    id<ContentCardable> contentCardable = [self contentCardableWithMetaData:metaData forClassType:classType];
    if (contentCardable) {
      [contentCardables addObject:contentCardable];
    }
  }
 
  return contentCardables;
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
__Initalizing your Custom Objects from Content Card Payload Data__<br>
```swift
func contentCardable(with metaData: [ContentCardKey: Any], for classType: ContentCardClassType) -> ContentCardable? {
  switch classType {
  case .yourValue:
    return CustomObject(metaData: metaData, classType: classType)
  case .yourOtherValue:
    return OtherCustomObject(metaData: metaData, classType: classType)
  ...
  default:
    return nil
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Initalizing your Custom Objects from Content Card Payload Data__<br>
```obj-c
- (id<ContentCardable>)contentCardableWithMetaData:(NSDictionary *)metaData forClassType:(ContentCardClassType)classType {
  switch (classType) {
    case ContentCardClassTypeYourValue:
      return [[CustomObject alloc] initWithMetaData:metaData classType:classType];
    case ContentCardClassTypeYourOtherValue:
      return nil;
    ...
    default:
      return nil;
  }
}
```
{% endtab %}
{% endtabs %}

## Sample Use Cases

There are three sample customer use cases provided. Each sample has video walkthroughs, code snippets, and a look into how Content Card variables may look and be used in the Braze dashboard:
- [Content Cards As Supplemental Content](#content-cards-as-supplemental-content)
- [Content Cards in a Message Center](#content-cards-in-a-message-center)
- [Interactive Content Cards](#interactive-content-cards)

### Content Cards as Supplemental Content

![Supplementary Content PNG][1]{: style="float:right;max-width:25%;margin-left:15px;border:0;"}

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

The example to the left shows a `UICollectionView` with a hybrid list of items - items that are populated via local data and also Content Cards powered by Braze. With this, Content Cards can be indistinguishable alongside existing content. Please visit our [repo](https://github.com/braze-inc/braze-growth-shares-ios-demo-app) to see examples of how to handle different types of Content Cards in the same feed.

#### Dashboard Configuration

This Content Card is delivered by an API triggered campaign with API triggered key-value pairs. This is ideal for campaigns where the card's values depend on external factors to determine what content to display to the user. Note that `class_type` should be known at set-up time, as seen here with the value of `class_type` set to `home_tile`, a variable that must remain consistent.

![Supplementary Content PNG][2]{: style="max-width:60%;"}

#### Backend Explanation

Because this use case includes data from different sources, data must be harmoniously fetched to display on screen without disrupting the user experience. This can be done with `OperationQueues`, where each operation is its own queue. As shown below, there is one queue for loading local data and one for loading Content Cards. There also exists a `BarrierBlock` that initiates the callback after both operations have been completed. 

Requesting Content Cards requires you to wait for the notification callback from the SDK. A semaphore has been implemented here to wait until the SDK posts the notification callback so the barrier block knows when the Content Card operation is completed. Note that custom objects will be returned and not Content Cards. Both the local data and the Content Card payload data are returned in the same array to be populated on-screen.

#### __Load Content Cards Alongside Existing Content__<br><br>

{% tabs %}
{% tab Swift %}
__Load the data simultaneously with OperationQueues__<br>
A `BarrierBlock` is used to synchronize the execution of the two tasks in the queue.
```swift
addOperation { [weak self] in
  guard let self = self else { return }
  self.loadTiles(self.tileCompletionHandler)
}

addOperation { [weak self] in
  guard let self = self else { return }
  self.loadContentCards()
  self.semaphore.wait()
}

addBarrierBlock {
  completion(tiles, ads)
}
```
{% endtab %}
{% tab Objective-C %}
__Load the data simultaneously with OperationQueues__<br>
A `BarrierBlock` is used to synchronize the execution of the two tasks in the queue.

```objc
HomeListOperationQueue * __weak weakSelf = self;

[self addOperationWithBlock:^{
  if (weakSelf) {
    [weakSelf loadLocalTilesWithCompletion:^(NSMutableArray * localTiles, NSError*) {
      [tiles addObjectsFromArray:localTiles];
    }];
  }
}];

[self addOperationWithBlock:^{
  if (weakSelf) {
    [weakSelf loadContentCards];
    dispatch_semaphore_wait(semaphore, DISPATCH_TIME_FOREVER);
  }
}];
    
[self addBarrierBlock:^{
  completion(tiles, ads);
}];
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Load Local Data Operation__<br>
The corresponding `[Tile]` array will be seamlessly blended with an array of Content Cards.

```swift
func loadTiles(_ completion: @escaping ([Tile]) -> ()) {
    switch result {
    case .success(let metaData):
      completion(metaData.tiles)
    case .failure:
      // handle error
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Load Local Data Operation__<br>
The corresponding `[Tile]` array will be seamlessly blended with an array of Content Cards.

```objc
- (void)loadTilesWithCompletion:(void (^)(NSMutableArray*, NSError *))completion {
  [localDataCoordinator loadTilesFromLocalDataWithCompletion:^(NSMutableArray *tiles, NSError *error) {
    if (error == nil) {
      completion(tiles, error);
    } else {
      // handle error
    }
  }];
}
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Load Content Card Operation__<br>
A semaphore is used to signal when the task is executed due to the notification callback from the Braze SDK. 

```swift
func loadContentCards() {
    BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
    BrazeManager.shared.requestContentCardsRefresh()
}
  
  @objc private func contentCardsUpdated(_ notification: Notification) {
    let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.item(.tile), .ad])
    contentCardCompletionHandler(contentCards)
    semaphore.signal()
  }
```
{% endtab %}
{% tab Objective-C %}
__Load Content Card Operation__<br>
A semaphore is used to signal when the task is executed due to the notification callback from the Braze SDK. 

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}

- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeHomeTile),@(ContentCardClassTypeAdBanner)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];
  contentCardCompletionHandler(contentCards);
  dispatch_semaphore_signal(semaphore);
}
```
{% endtab %}
{% endtabs %}

### Content Cards in a Message Center

Content Cards can be used in a message center format where each message is its own card. Each message in the message center is populated via a Content Card payload, and each card contains additional key-value pairs that power on-click UI/UX. In the example to the right, one message directs you to an arbitrary custom view, while another opens to a webview that displays custom HTML.

![Message Center PNG][3]{: style="border:0;"}

#### Dashboard Configuration

For the following message types, key-value pairs `class_type` and `message_header` should be added to your dashboard configuration. The names assigned here are arbitrary but should be distinguishable between class types. These key-value pairs are the key identifiers that the application looks at when deciding where to go when the user clicks on an abridged inbox message. 

| Arbitrary Custom View Message | Webview Message |
| ---- | ---- |
| <br>The key-value pairs for this use case include `message_header` set as `Full Page` and `class_type` set as `message_full_page`.<br><br><br>![Message Center JPG1][4]{: style="max-width:100%;"} | The key-value pairs for this use case include `message_header` set as `HTML`, `class_type` set as `message_webview`, and `message_title`.<br><br>This message also looks for an HTML key-value pair, but if you are working with a web domain, a URL key-value pair is also valid.<br><br>![Message Center JPG2][5] |
{: .reset-td-br-1 .reset-td-br-2}

#### Backend Explanation

The message center logic is driven by the `contentCardClassType` that is provided by the key-value pairs from Braze. Using the `addContentCardToView()` function, you are able to both filter and identify these class types.

{% tabs %}
{% tab Swift %}
__Using `class_type` for On Click Behavior__<br>
When a message is clicked, the `ContentCardClassType` handles how the next screen should be populated.
```swift
func addContentCardToView(with message: Message) {
    switch message.contentCardData?.contentCardClassType {
      case .message(.fullPage):
        loadContentCardFullPageView(with: message as! FullPageMessage)
      case .message(.webView):
        loadContentCardWebView(with: message as! WebViewMessage)
      default:
        break
    }
}
```
{% endtab %}
{% tab Objective-C %}
__Using `class_type` for On Click Behavior__<br>
When a message is clicked, the `ContentCardClassType` handles how the next screen should be populated.
```objc
- (void)addContentCardToView:(Message *)message {
  switch (message.contentCardData.classType) {
    case ContentCardClassTypeMessageFullPage:
      [self loadContentCardFullPageView:(FullPageMessage *)message];
      break;
    case ContentCardClassTypeMessageWebview:
      [self loadContentCardWebView:(WebViewMessage *)message];
      break;
    default:
      break;
  }
}
```
{% endtab %}
{% endtabs %}

### Interactive Content Cards

Content Cards can be leveraged to create interactive experiences for your users. In the example to the right, we have a Content Card pop-up appear at checkout providing users last-minute promotions. Well-placed cards like this are a great way to give users a "nudge" toward specific user actions.  

![Interactive Content PNG][6]{: style="border:0;"}

#### Dashboard Configuration

The dashboard configuration for interactive Content Cards is quick and straightforward. The key-value pairs for this use case include a `discount_percentage` set as the desired discount amount and `class_type` set as `coupon_code`. These key-value pairs are how type-specific Content Cards get filtered and displayed on the checkout screen.

![Interactive Content JPG][7]{: style="max-width:70%;"} 

#### Backend Explanation

The `loadContentCard()` method is used to request Content Cards, and the `contentCardsUpdated()` method is used to query an array of type-specific Content Cards set via the `class_type` filter in the dashboard key-value pairs. This will render the object into a view to display on-screen.

To display the object on screen, use the `configureView()` function and provide it a String type to render the image. Notice the view itself is source-independent, meaning the view can be configured with non-Braze types.

#### Interactable View<br><br>

{% tabs %}
{% tab Swift %}
__Requesting Content Cards__<br>
As long as the observer is still retained in memory, a notification callback from the Braze SDK can be expected. 

```swift
func loadContentCards() {
  BrazeManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
  BrazeManager.shared.requestContentCardsRefresh()
}
```
{% endtab %}
{% tab Objective-C %}
__Requesting Content Cards__<br>
As long as the observer is still retained in memory, a notification callback from the Braze SDK can be expected. 

```objc
- (void)loadContentCards {
  [[BrazeManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[BrazeManager shared] requestContentCardsRefresh];
}
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Getting Type-Specific Content Cards__<br>
The `class_type` is passed in as a filter to only return Content Cards that have a matching `class_type`.
```swift
@objc func contentCardsUpdated(_ notification: Notification) {
  guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.yourValue]) as? [CustomObject],!contentCards.isEmpty else { return }
 
 // do something with your array of custom objects
}
```
{% endtab %}
{% tab Objective-C %}
__Getting Type-Specific Content Cards__<br>
The `class_type` is passed in as a filter to only return Content Cards that have a matching `class_type`.
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeYourValue)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];
 
  // do something with your array of custom objects
}
```
{% endtab %}
{% endtabs %}

## Logging Impressions, Clicks, and Dismissals

After extending your own custom objects to function as Content Cards, logging valuable metrics like impressions, clicks, and dismissals is quick and simple. This can be done through the use of a `ContentCardable` protocol that references and provides data to a helper file to be logged by the Braze SDK.

#### Backend Explanation 

The `logContentCardImpression()` method can only be called from an `ABKContentCard`.To handle this, in the `ContentCardable` protocol, there exists a reference to the Content Card ID. The protocol has a `logContentCardImpression()` method that calls into the `BrazeManager.swift` helper file which only exposes an `idString` parameter. Once passed this off to the helper file, the Braze SDK has a public variable, `ContentCards`, that can be queried to get the Content Card from its own identifier that has been passed in. Once the Content Card has been obtained, impressions, click, and dismissals can be logged, all while successfully working with ABK objects only at the moment required.

#### __Implementation Components__<br><br>

{% tabs %}
{% tab Swift %}
__Logging Analytics__<br>
```swift
customObject.logContentCardImpression()
customObject.logContentCardClicked()
customObject.logContentCardDismissed()
```
{% endtab %}
{% tab Objective-C %}
__Logging Analytics__<br>
```objc
[customObject logContentCardImpression];
[customObject logContentCardClicked];
[customObject logContentCardDismissed];
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
__Custom Objects Call the Logging Methods__<br>
For objects that conform to the `ContentCardable` protocol, the analytics methods can be called directly from the objects. As seen in the snippet below, the object is referenced to log the impression.
```swift
func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
  let message = messages[indexPath.row]
  message.logContentCardImpression()
}
```
{% endtab %}
{% tab Objective-C %}
__Custom Objects Call the Logging Methods__<br>
For objects that conform to the `ContentCardable` protocol, the analytics methods can be called directly from the objects. As seen in the snippet below, the object is referenced to log the impression.
```objc
-(void)tableView:(UITableView *)tableView willDisplayCell:(UITableViewCell *)cell forRowAtIndexPath:(NSIndexPath *)indexPath {
  Message *message = self.messages[indexPath.row];
  [message logContentCardImpression];
}
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Retrieve the Content Card from the ContentCardId__<br>
The `ContentCardable` protocol handles the heavy lifting of calling the helper file and passing the unique identifier from the Content Card associated with the custom object.
```swift
protocol ContentCardable {
  func logContentCardImpression() {
    BrazeManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Retrieve the Content Card from the ContentCardId__<br>
The `ContentCardable` protocol handles the heavy lifting of calling the helper file and passing the unique identifier from the Content Card associated with the custom object.
```objc
- (void)logContentCardImpression {
  [[BrazeManager shared] logContentCardImpression:self.contentCardData.contentCardId];
}
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Retreive the `ABKContentCard`__<br>
The [helper file](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift#L171) can reference Braze SDK dependencies such as the `Appboy.sharedInstance()?.contentCardsController.contentCards` array to get the `ABKContentCard` to call our logging methods.
```swift
extension BrazeManager {
  func logContentCardImpression(idString: String?) {
    guard let contentCard = getContentCard(forString: idString) else { return }
 
    contentCard.logContentCardImpression()
  }
   
  private func getContentCard(forString idString: String?) -> ABKContentCard? {
    return contentCards?.first(where: { $0.idString == idString })
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Retreive the `ABKContentCard`__<br>
The [helper file](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift#L171) can reference Braze SDK dependencies such as the `Appboy.sharedInstance()?.contentCardsController.contentCards` array to get the `ABKContentCard` to call our logging methods.
```objc
- (void)logContentCardImpression:(NSString *)idString {
  ABKContentCard *contentCard = [self getContentCard:idString];
  [contentCard logContentCardImpression];
}
 
- (ABKContentCard *)getContentCard:(NSString *)idString {
  NSPredicate *predicate = [NSPredicate predicateWithFormat:@"self.idString == %@", idString];
  NSArray *filteredArray = [self.contentCards filteredArrayUsingPredicate:predicate];
 
  return filteredArray.firstObject;
}
```
{% endtab %}
{% endtabs %}

{% alert important %}
For a control variant Content Card, a custom object should still be instantiated, and UI logic should set the object's corresponding view as hidden. The object can then log an impression to inform our analytics of when a user would have seen the control card.
{% endalert %}

[1]: {% image_buster /assets/img/cc_implementation/supplementary.png %}
[2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %}
[3]: {% image_buster /assets/img/cc_implementation/message_center.png %}
[4]: {% image_buster /assets/img/cc_implementation/full_page.png %}
[5]: {% image_buster /assets/img/cc_implementation/html_webview.png %}
[6]: {% image_buster /assets/img/cc_implementation/discount2.png %}
[7]: {% image_buster /assets/img/cc_implementation/discount.png %}