---
nav_title: Best Practices and Use Cases
platform: iOS
page_order: 7
description: "This developer walkthrough covers Content Card code considerations, three use cases built by our team, accompanying code snippets, as well as an implementation walkthrough."
---

# Code Considerations and Use Cases

> This developer walkthrough covers Content Card code considerations, three use cases built by our team, accompanying code snippets, as well as an implementation walkthrough. Visit our Content Card Repository [here]()! Please note that the use case videos provided are centered around a Swift implementation, Objective-C code snippets have been included here for the sake of parity. 

## Code Considerations

### Import Statements and Helper Files

When building out Content Cards, you should integrate them using a single "import Appboy-iOS-SDK" statement. At the same time, you should also represent your Content Cards as custom objects in addition to handling all of the necessary Braze dependencies in a helper file. This limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code. An example helper file can be found [here]().

### Content Cards as Custom Objects

{% include video.html id="wSo1I9nLqKU" align="right" %}

This section covers how custom objects can be extended to function as content cards in a way that does not depend on the Braze SDK. This can be done by implementing the ContentCardable protocol and initializer described below, and through the use of the Contentcardable struct, allows you to access the ABKContentCardData. 

Included in this initializer is a ContentCardClassType enum parameter, this enum is used to decide which object to initialize. Through the use of key-value pairs within the Braze dashboard, you are then able to pass Braze a `class_type` object and value that pulls and displays the appropriate content card.

This can be accomplished by converting Cards to custom objects by passing the ABKcontentCard variables into a dictionary of content card payload data (optional) to be passed in with the initializer. This initializer then parses and converts these cards to work with your custom code. 

{% tabs %}
{% tab Swift %}
__Extending Functionality__<br>
Populating Course Object with the `Content Card` Payload

```swift
// MARK: - Course
struct Course: ContentCardable, Purchasable, Codable, Hashable {
  private(set) var contentCardData: ContentCardData?
  let id: Int
  let title: String
  let price: Decimal
  let imageUrl: String
    
  private enum CodingKeys: String, CodingKey {
    case id
    case title
    case price
    case imageUrl = "image"
  }
}
```
__ABKContentCard Dependencies__<br>
The Only Dependencies on `ABKContentCard` are its Primitive Types

```swift
protocol ContentCardable {
  var contentCardData: ContentCardData? { get }
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType)
}

extension ContentCardable {
  var isContentCard: Bool {
    return contentCardData != nil
  }

// MARK: - ContentCardData
struct ContentCardData: Hashable {
  let contentCardId: String
  let contentCardClassType: ContentCardClassType
  let createdAt: Double
  let isDismissable: Bool
}
```
__Key-Value Pairs__

```swift
// MARK: - Content Card Initalizer
extension Course {
  init?(metaData: [ContentCardKey: Any], classType contentCardClassType: ContentCardClassType) {
    guard let idString = metaData[.idString] as? String,
      let createdAt = metaData[.created] as? Double,
      let isDismissable = metaData[.dismissable] as? Bool,
      let extras = metaData[.extras] as? [AnyHashable: Any],
      let title  = extras["course_title"] as? String,
      let detail = extras["course_detail"] as? String,
      let priceString = extras["course_price"] as? String,
      let price = Decimal(string: priceString),
      let imageUrl = extras["course_image"] as? String
      else { return nil }
```
__Identifying Types__

```swift
init(rawType: String?) {
    switch rawType?.lowercased() {
    case "ad":
      self = .ad
    case "coupon_code":
      self = .coupon
    case "course_recommendation":
      self = .item(.course)
    case "message_classic":
      self = .message(.fullPage)
    case "message_webview":
      self = .message(.webView)
    default:
      self = .none
    }
  }
```
{% endtab %}
{% tab Objective-C %}

__ABKContentCard Dependencies__<br>
The Only Dependencies on `ABKContentCard` are its Primitive Types

```objc
@interface ContentCardData : NSObject

+ (ContentCardClassType)contentCardClassTypeForString:(NSString*)rawValue;

- (instancetype)initWithIdString:(NSString *)idString classType:(ContentCardClassType)classType createdAt:(double)createdAt isDismissable:(BOOL)isDismissable;

@property (nonatomic, readonly) NSString *contentCardId;
@property (nonatomic) ContentCardClassType classType;
@property (nonatomic, readonly) double *createdAt;
@property (nonatomic, readonly) BOOL isDismissable;

@end


@protocol ContentCardable <NSObject>

@property (nonatomic, strong) ContentCardData *contentCardData;
- (instancetype __nullable)initWithMetaData:(NSDictionary *)metaData classType:(enum ContentCardClassType)classType;

- (BOOL)isContentCard;
- (void)logContentCardImpression:(NSString * __nullable)idString;
- (void)logContentCardClick:(NSString * __nullable)idString;
- (void)logContentCardDismissal:(NSString * __nullable)idString;

@end
```
__Key-Value Pairs__

```objc
- (id _Nullable)initWithMetaData:(nonnull NSDictionary *)metaData classType:(enum ContentCardClassType)classType {
  self = [super init];
  
  if (self) {
    if (metaData[@"idString"] != nil && metaData[@"created"] != nil && metaData[@"dismissable"] != nil && metaData[@"extras"] != nil) {
    
      NSDictionary  *extras = metaData[@"extras"];
      NSString *idString = metaData[@"idString"];
      double createdAt = [metaData[@"createdAt"] doubleValue];
      BOOL isDismissable = metaData[@"isDimissable"];
      
      if (extras[@"tile_title"] != nil && extras[@"tile_price"] != nil && extras[@"tile_image"] !=  nil) {
        NSString *tagsString = extras[@"tile_tags"];

        _idString = idString;
        _title = extras[@"tile_title"];
        _tags = [tagsString separatedByCommaSpaceValue];
        _imageUrl = extras[@"tile_image"];
        
        self.price = [NSDecimalNumber decimalNumberWithString:extras[@"tile_price"]];
        
        self.contentCardData = [[ContentCardData alloc] initWithIdString:idString classType:classType createdAt: createdAt isDismissable:isDismissable];
        
        return self;
      }
    }
```
__Identifying Types__

```objc
typedef NS_ENUM(NSInteger, ContentCardClassType) {
  ContentCardClassTypeNone = 0,
  ContentCardClassTypeAdBanner,
  ContentCardClassTypeCoupon,
  ContentCardClassTypeHomeTile,
  ContentCardClassTypeMessageFullPage,
  ContentCardClassTypeMessageWebview,
};
#define kContentCardClassTypeArray @"", @"ad_banner", @"coupon_code", @"home_tile", @"message_full_page", @"message_webview", nil

+ (ContentCardClassType)contentCardClassTypeForString:(NSString*)rawValue {
  NSArray *contentCardClassTypeArray = [[NSArray alloc] initWithObjects:kContentCardClassTypeArray];
  if ([contentCardClassTypeArray indexOfObject:rawValue] == NSNotFound) {
    return ContentCardClassTypeNone;
  } else {
    NSInteger value = [contentCardClassTypeArray indexOfObject:rawValue];
    return (ContentCardClassType) value;
  }
}
```
{% endtab %}
{% endtabs %}

## Sample Use Cases

There are 3 sample customer use cases provided. Each sample has video walkthroughs, code snippets for each demo application, and a look into how content card variables may look and be used in the Braze dashboard:
- [Content Cards As Supplemental Content](#content-cards-as-supplemental-content)
- [Content Cards in a Message Center](#content-cards-in-a-message-center)
- [Interactive Content Cards](#interactive-content-cards)

### Content Cards as Supplemental Content

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

{% tabs %}
{% tab Swift %}
#### __Load Content Cards Alongside Existing Content__

Get the data simultaneously through Operation Queues
```swift
addOperation { [weak self] in
      guard let self = self else { return }
      self.loadCourses(self.courseCompletionHandler)
    }
    
addOperation { [weak self] in
      guard let self = self else { return }
      self.loadContentCards()
      self.semaphore.wait()
    }
```
Course Operation
```swift
func loadCourses(_ completion: @escaping ([Course]) -> ()) {
      switch result {
      case .success(let metaData):
        completion(metaData.courses)
      case .failure:
        cancelAllOperations()
    }
  }
```
Content Card Operation
```swift
func loadContentCards() {
    AppboyManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
    AppboyManager.shared.requestContentCardsRefresh()
  }

@objc private func contentCardsUpdated(_ notification: Notification) {
    let contentCards = AppboyManager.shared.handleContentCardsUpdated(notification, for: [.item(.course), .ad])
    contentCardCompletionHandler(contentCards)
    semaphore.signal()
  }
```
{% endtab %}
{% tab Objective-C %}
#### __Load Content Cards Alongside Existing Content__

Get the data simultaneously through Operation Queues
```objc
HomeListOperationQueue * __weak weakSelf = self;

[self addOperationWithBlock:^{
      if (weakSelf) {
        [weakSelf loadContentCards];
        dispatch_semaphore_wait(semaphore, DISPATCH_TIME_FOREVER);
      }
    }];
    
  [self addOperationWithBlock:^{
    if (weakSelf) {
      [weakSelf loadLocalCoursesWithCompletion:^(NSMutableArray * localCourses, NSError*) {
        [courses addObjectsFromArray:localCourses];
      }];
    }
  }];
    
    [self addBarrierBlock:^{
      completion(courses, ads);
    }];
```
Course Operation
```objc
- (void)loadCoursesWithCompletion:(void (^)(NSMutableArray*, NSError *))completion {
  [localDataCoordinator loadCoursesFromLocalDataWithCompletion:^(NSMutableArray *courses, NSError *error) {
    if (error == nil) {
      completion(courses, error);
    } else {
      // handle error
    }
  }];
}
```
Content Card Operation
```objc
- (void)loadContentCards {
  [[AppboyManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[AppboyManager shared] requestContentCardsRefresh];
}


- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeHomeTile),@(ContentCardClassTypeAdBanner)];
  NSArray *contentCards = [[AppboyManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];
contentCardCompletionHandler(contentCards);
dispatch_semaphore_signal(semaphore);
}
```
{% endtab %}
{% endtabs %}

### Content Cards in a Message Center
Content Cards can be used in a message center format where each message is its own card. Each one can contain additional key-value pairs that power on-click UI/UX.
{% include video.html id="ZpXvjca9KyY" align="right" %}

{% tabs %}
{% tab Swift %}
__Using 'class_type' for On Click Behavior__<br>
How to Filter and Identify Various Class Types
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
__Using 'class_type' for On Click Behavior__<br>
How to Filter and Identify Various Class Types
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

{% include video.html id="INDgFPIZrNQ" align="right" %}

{% tabs %}
{% tab Swift %}
#### __Interactable View__

Requesting Content Cards
```swift
func loadContentCards() {
    AppboyManager.shared.addObserverForContentCards(observer: self, selector: #selector(contentCardsUpdated))
    AppboyManager.shared.requestContentCardsRefresh()
  }
```

Getting Type-Specific Content Cards
```swift
  @objc func contentCardsUpdated(_ notification: Notification) {
    guard let contentCards = AppboyManager.shared.handleContentCardsUpdated(notification, for: [.coupon]) as? [Coupon], !contentCards.isEmpty else { return }
}
```
{% endtab %}
{% tab Objective-C %}
#### __Interactable View__

Requesting Content Cards
```objc
- (void)loadContentCards {
  [[AppboyManager shared] addObserverForContentCards:self selector:@selector(contentCardsUpdated:)];
  [[AppboyManager shared] requestContentCardsRefresh];
}
```

Getting Type-Specific Content Cards
```objc
- (void)contentCardsUpdated:(NSNotification *)notification {
  NSArray *classTypes = @[@(ContentCardClassTypeCouponCode)];
  NSArray *contentCards = [[AppboyManager shared] handleContentCardsUpdated:notification forClassTypes:classTypes];
}
```
{% endtab %}
{% endtabs %}

## Logging Impressions, Clicks, and Dismissals

How do we log impressions, clicks, and dismissals while staying true to the code considerations mentioned above? This can be done through the use of the ContentCardable protocol. This protocol has a method that calls into the helper file, only exposing an idString parameter. After this parameter gets passed to the helper file, the Braze SDK can query the Content Card from the identifier. Once the Content Card has been received, we are able to log impressions, click, and dismissals.

{% include video.html id="INDVFUtv6Fc" align="right" %}

{% tabs %}
{% tab Swift %}
#### __Implementation Components__

__Update Content Card Dictionary__<br>
Mapped through the Content Card idString
```swift
private var contentCardsDictionary: [String: ABKContentCard] = [:]

for card in cards {
      contentCardsDictionary[card.idString] = card
```

{% alert note %}
Note that the use of a ContentCardsDictionary is not required, but may be used here as a faster way to access the Content Card than querying the ContentCards array provided by the Braze SDK.
{% endalert %}


__Encapsulated ABK Methods__<br>
Only exposing the idString as a parameter
```swift
switch rows[indexPath.row] {
    case .item(let course):
      guard course.isContentCard else { break }
      course.logContentCardImpression()
```

__Get Content Card from IDString__<br>
Via Content Card Dictionary
```swift
protocol ContentCardable {
  func logContentCardImpression() {
    AppboyManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```

__Call ABKCONTENTCARD Functions__<br>
100% handled through AppboyManager.Swift
```swift
func logContentCardClicked(idString: String?) {
    guard let idString = idString, let contentCard = contentCardsDictionary[idString] else { return }
    
    contentCard.logContentCardClicked()
  }
```
{% endtab %}
{% tab Objective-C %}
#### __Implementation Components__


__Encapsulated ABK Methods__<br>
Only exposing the idString as a parameter
```objc
[message logContentCardImpression];
```

__Get Content Card from IDString__<br>
Via Content Card Dictionary
```objc
- (void)logContentCardImpression {
  [[AppboyManager shared] logContentCardImpression:self.contentCardData.contentCardId];
}
```

__Call ABKCONTENTCARD Functions__<br>
100% handled through AppboyManager.Swift
```objc
- (void)logContentCardImpression:(NSString * __nullable)idString {
  NSPredicate *predicate = [NSPredicate predicateWithFormat:@"self.idString == %@", idString];
  NSArray *filteredArray = [self.contentCards filteredArrayUsingPredicate:predicate];
  ABKContentCard *contentCard = filteredArray.firstObject;
  [contentCard logContentCardImpression];
}
```
{% endtab %}
{% endtabs %}