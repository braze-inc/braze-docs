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

Much like a rocketship adding a booster, your own custom objects can be extended to function as Content Cards. Limited API surfaces such as this provide flexibility to work with different data backends interchangeably. This can be done by conforming to the `ContentCardable` protocol and implementing the initializer (as seen below) and, through the use of the `ContentCardData` struct, allows you to access the `ABKContentCard` data.

The initializer also includes a `ContentCardClassType` enum. Through the use of key-value pairs within the Braze dashboard, you can set an explicit `class_type` key that will be used to determine what object to initialize. Once you have a solid understanding of these code considerations, check out our [use cases](#sample-use-cases) below to get started implementing your own custom objects.

{% include video.html id="55KTZqYAl7Y" align="center" %}

{% tabs %}
{% tab Swift %}
__No `ABKContentCard` Dependencies__<br>
`ContentCardData` represents the parsed out values of an `ABKContentCard`.

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

struct ContentCardData: Hashable {
  let contentCardId: String
  let contentCardClassType: ContentCardClassType
  let createdAt: Double
  let isDismissable: Bool
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

```objc
// Header File
@interface ContentCardData : NSObject

+ (ContentCardClassType)contentCardClassTypeForString:(NSString *)rawValue;

- (instancetype)initWithIdString:(NSString *)idString 
                       classType:(ContentCardClassType)classType
                       createdAt:(double)createdAt isDismissable:(BOOL)isDismissable;

@property (nonatomic, readonly) NSString *contentCardId;
@property (nonatomic) ContentCardClassType classType;
@property (nonatomic, readonly) double *createdAt;
@property (nonatomic, readonly) BOOL isDismissable;

@end

@protocol ContentCardable <NSObject>

@property (nonatomic, strong) ContentCardData *contentCardData;
- (instancetype __nullable)initWithMetaData:(NSDictionary *)metaData 
                                  classType:(enum ContentCardClassType)classType;

- (BOOL)isContentCard;
- (void)logContentCardImpression;
- (void)logContentCardClick;
- (void)logContentCardDismissal;

@end
```
{% endtab %}
{% endtabs %}
{% tabs %}
{% tab Swift %}
__Custom Object Initializer__<br>
MetaData from an `ABKContentCard` is used to populate your object's variables. The key-value pairs set up in the Braze Dashboard are represented in the "extras" dictionary.

```swift
extension Tile: ContentCardable {
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType) {
    guard let idString = metaData[.idString] as? String,
      let createdAt = metaData[.created] as? Double,
      let isDismissable = metaData[.dismissable] as? Bool,
      let extras = metaData[.extras] as? [AnyHashable: Any],
      let tileIdString = extras["tile_id"] as? String,
      let tileId = Int(tilleIdString),  
      let title  = extras["tile_title"] as? String,
      let priceString = extras["tile_price"] as? String,
      let price = Decimal(string: priceString),
      let imageUrl = extras["tile_image"] as? String
      else { return nil }
    
    let tags = extras[ContentCardKey.tags.rawValue] as? String ?? ""
    let contentCardData = ContentCardData(contentCardId: idString, contentCardClassType: contentCardClassType, createdAt: createdAt, isDismissable: isDismissable)
    
    self.init(contentCardData: contentCardData, id: tileId, title: title, price: price, tags: tags.separatedByCommaSpaceValue, imageUrl: imageUrl)
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
    if (metaData[@"idString"] != nil && metaData[@"created"] != nil && metaData[@"dismissable"] != nil && metaData[@"extras"] != nil) {
      NSDictionary  *extras = metaData[@"extras"];
      NSString *idString = metaData[@"idString"];
      double createdAt = [metaData[@"createdAt"] doubleValue];
      BOOL isDismissable = metaData[@"isDimissable"];
      if (extras[@"tile_id"] != nil && extras[@"tile_title"] != nil && extras[@"tile_price"] != nil && extras[@"tile_image"] !=  nil) {
        NSString *tagsString = extras[@"tile_tags"];
        _idString = [extras[@"tile_id"] integerValue];
        _title = extras[@"tile_title"];
        _tags = [tagsString componentsSeparatedByString:@", "];
        _imageUrl = extras[@"tile_image"];
        self.price = [NSDecimalNumber decimalNumberWithString:extras[@"tile_price"]];
        self.contentCardData = [[ContentCardData alloc] initWithIdString:idString classType:classType createdAt:createdAt isDismissable:isDismissable];
        return self;
      }
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
The `ContentCardClassType` enum represents the `class_type` value in the Braze Dashboard.

```swift
enum ContentCardClassType: Hashable {
  case ad
  case coupon
  case item(ItemType)
  case message(MessageCenterViewType)
  case none
  
  enum ItemType {
    case tile
  }
  
  enum MessageCenterViewType {
    case fullPage
    case webView
  }

  init(rawType: String?) {
    switch rawType?.lowercased() {
    case "coupon_code":
      self = .coupon
    case "home_tile":
      self = .item(.tile)
    case "message_full_page":
      self = .message(.fullPage)
    case "message_webview":
      self = .message(.webView)
    case "ad_banner":
      self = .ad
    default:
      self = .none
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
__Identifying Types__<br>
The `ContentCardClassType` enum represents the `class_type` value in the Braze Dashboard.

```objc
typedef NS_ENUM(NSInteger, ContentCardClassType) {
  ContentCardClassTypeNone = 0,
  ContentCardClassTypeAdBanner,
  ContentCardClassTypeCoupon,
  ContentCardClassTypeHomeTile,
  ContentCardClassTypeMessageFullPage,
  ContentCardClassTypeMessageWebview,
};

+ (NSArray *)contentCardClassTypeArray {
  return @[ @"", @"ad_banner", @"coupon_code", @"home_tile", @"message_full_page", @"message_webview" ];
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

## Sample Use Cases

There are three sample customer use cases provided. Each sample has video walkthroughs, code snippets, and a look into how Content Card variables may look and be used in the Braze dashboard:
- [Content Cards As Supplemental Content](#content-cards-as-supplemental-content)
- [Content Cards in a Message Center](#content-cards-in-a-message-center)
- [Interactive Content Cards](#interactive-content-cards)

### Content Cards as Supplemental Content

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

The example to the left shows a `UICollectionView` with a hybrid list of items - items that are populated via local data and also Content Cards powered by Braze. With this, Content Cards can be indistinguishable alongside existing content. Please visit our [repo](https://github.com/braze-inc/braze-growth-shares-ios-demo-app) to see examples of how to handle different types of Content Cards in the same feed.

#### Dashboard Configuration

This Content Card is delivered by an API triggered campaign with API triggered key-value pairs. This is ideal for campaigns where the card's values depend on external factors to determine what content to display to what user. Note that `class_type` should be known at set-up time, as seen here with the value of `class_type` set to `home_card.` These other key-value pairs are optional and can highlight custom values but the `class_type` must remain consistent.

#### Backend Explanation

Because we are working with data from different sources, data must be harmoniously fetched to display on screen without disrupting the user experience. This can be done with `OperationQueues`, where each operation is its own queue. Shown below, we have one queue for loading local data and one for loading content cards. We also have a `BarrierBlock` that initiates the callback after both operations have been completed. 

Because we are requesting Content Cards, we have to wait for the notification callback from the SDK. A semaphore has been implemented to wait until the SDK posts the notification callback, so the barrier block knows when the content card operation is completed. Note that we are returning custom objects and not Content Cards. Both the local data and the Content Card payload data are returned in the same array to be populated on-screen.

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
Content Cards can be used in a message center format where each message is its own card. Each message in the message center is populated via a content card payload, and each card contains additional key-value pairs that power on-click UI/UX. In the example to the right, one message directs you to an arbitrary custom view, while another opens to a webview that is displaying custom HTML.

#### Dashboard Configuration

For the following message types, key-value pairs exist denoting the `class_type` and `message_header`. The names assigned here are arbitrary but should be distinguishable between class types. These key-value pairs are the key identifiers that the application looks at when deciding where to go when the user clicks on an abridged inbox message. 

__Arbitrary Custom View Message__<br>
The key-value pairs for this use case include `message_header` set as `Full Page` and `class_type` set as `message_full_page`.

__Webview Message__<br>
The key-value pairs for this use case include `message_header` set as `HTML`, `class_type` set as `message_webview`, and `message_title`. This message also looks for an HTML key-value pair, but if you are working with a web domain, a URL key-value pair is also valid.

#### Backend Explanation

The message center logic is driven by the `contentCardClassType` that is provided by the key-value pairs from Braze. Using the `addContentCardToView()` function, we are able to both filter and identify these class types.

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
Content Cards can be leveraged to create interactive experiences for your users. In the demo below, we have a Content Card pop-up appear at checkout providing users last-minute promotions. Well-placed cards like this are a great way to give users a "nudge" toward specific user actions.  

#### Dashboard Configuration

The dashboard configuration for interactive Content Cards is straightforward. The key-value pairs for this use case include a `discount_percentage` set as the desired discount amount and `class_type` set as `coupon_code`. These key-value pairs are how we filter for this specific type of Content Card on the checkout screen. 

#### Backend Explanation

In the code, we use the `loadContentCard()` function to request Content Cards, and the `contentCardsUpdated()` function to query an array of type-specific Content Cards set via the `class_type` filter in the dashboard key-value pairs. This will render the object into a view to display on-screen.

Next, to display the object on screen, we use the `configureView()` function and provide it a String type used to render the image. Notice the view itself is source-independent, meaning we are able to configure the view with non-Braze types.

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
    guard let contentCards = BrazeManager.shared.handleContentCardsUpdated(notification, for: [.coupon]) as? [Coupon], !contentCards.isEmpty else { return }
}
```
{% endtab %}
{% tab Objective-C %}
__Getting Type-Specific Content Cards__<br>
The `class_type` is passed in as a filter to only return Content Cards that have a matching `class_type`.
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeCouponCode)];
  NSArray *contentCards = [[BrazeManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];
}
```
{% endtab %}
{% endtabs %}

## Logging Impressions, Clicks, and Dismissals

After extending your own custom objects to function as Content Cards, logging valuable metrics like impressions, clicks, and dismissals is quick and simple. This can be done through the use of a `ContentCardable` protocol that references and provides data to a helper file to be logged by the Braze SDK.

#### Backend Explanation 

The `logContentCardImpression()` method can only be called from an `ABKContentCard`, so this needs to be handled if we are working with our own custom objects. In the `ContentCardable` protocol, there exists a reference to the Content Card ID. The protocol has a `logContentCardImpression()` method that calls into the `BrazeManager.swift` helper file which only exposes an `idString` parameter. Once we pass this off to the helper file, the Braze SDK has a public variable, `ContentCards`, that we can query to get the Content Card from its own identifier that we have passed in. Once we get the Content Card, we can log impressions, click, and dismissals, successfully working with ABK objects only at the moment we need to.

#### __Implementation Components__<br><br>

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
__Call `ABKContentCard` Functions__<br>
The [helper file](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift#L171) can reference Braze SDK dependencies such as the `Appboy.sharedInstance()?.contentCardsController.contentCards` array to get the `ABKContentCard` to call our logging methods.
```swift
func logContentCardImpression(idString: String?) {
  guard let contentCard = getContentCard(forString: idString) else { return }

  contentCard.logContentCardImpression()
}
  
private func getContentCard(forString idString: String?) -> ABKContentCard? {
  return contentCards?.first(where: { $0.idString == idString })
}
```
{% endtab %}
{% tab Objective-C %}
__Call `ABKContentCard` Functions__<br>
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
