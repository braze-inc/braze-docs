---
nav_title: Best Practices and Use Cases
platform: iOS
page_order: 7
description: "This developer article covers Content Card best practices, three use cases built by our team, accompanying code snippets, as well as an implementation walkthrough."
---

# Best Practices and Use Cases
{% include video.html id="e0G7IJfkMOI" align="right" %}

> This developer article covers Content Card best practices, three use cases built by our team, accompanying code snippets, as well as an implementation walkthrough. Included to the right is our full video walkthrough, with sections included and referenced throughout the rest of the article.

## Best Practices

### Code Considerations

When adding Content Cards to your codebase, it is a best practice to decouple your code. By keeping your code separate from the SDK code, it makes it easier to troubleshoot. For example, try to minimize your SDK imports down to a single "import Appboy-iOS-SDK" statement. This limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code.
- __Decoupled__ - Your data should be source-independent. Decoupled code allows you to easily track where your Content Card data is coming from and going to.
- __Flexibility__ - Offers type-agnostic extended functionality. You can extend your custom production code to handle Content Card data.
- __Easy to Debug__ - Errors can be traced to one place. Because of the minimization of SDK imports, your code now has a single source of data to check and follow along. 

## Sample Use Cases

There are 3 sample customer use cases provided. Each sample has video walkthroughs, code snippets for each demo application, and dashboard implementation examples:
- [Content Cards As Supplemental Content](#content-cards-as-supplemental-content)
- [Content Cards in a Message Center](#content-cards-in-a-message-center)
- [Interactive Content Cards](#interactive-content-cards)

### Content Cards as Supplemental Content

You can seamlessly blend Content Cards into an existing feed, allowing data from multiple feeds to load simultaneously. This creates a cohesive, harmonious experience with Braze Content Cards and existing feed content.

{% tabs %}
{% tab Video %}

{% include video.html id="wSo1I9nLqKU" align="center" %}

{% endtab %}
{% tab Swift - Demo Code Snippets %}
#### Load Content Cards Alongside Existing Content
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

#### Extending Course Functionality
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

#### ABKContentCard Dependencies
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

#### Campaign Key-Value Pairs From Braze Dashboard
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

#### Identifying Multiple Types
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
{% endtabs %}

### Content Cards in a Message Center
Content Cards can be used in a message center format where each message is its own card. Each one can contain additional key-value pairs that power on-click UI/UX.
{% tabs %}
{% tab Video %}

{% include video.html id="ZpXvjca9KyY" align="center" %}

{% endtab %}
{% tab Swift - Demo Code Snippets %}
#### Using Class_type for On Click Behavior
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
{% endtabs %}

### Interactive Content Cards
Content Cards can be leveraged to create interactive experiences for your users. In the demo below, we have a Content Card pop-up appear at checkout providing users last-minute promotions. Well-placed cards like this are a great way to give users a "nudge" toward specific user actions. 

{% tabs %}
{% tab Video %}

{% include video.html id="INDgFPIZrNQ" align="center" %}

{% endtab %}
{% tab Swift - Demo Code Snippets %}
#### Interactable View Steps

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
#### Coupon Configuration
The Content Card Key-Value Pair provides the imageUrl for the View
```swift
func configureView(_ imageUrl: String?, _ origin: CGPoint, _ animatePoint: CGFloat, _ direction: UISwipeGestureRecognizer.Direction, _ delegate: GestureViewEventDelegate? = nil) {
    swipeGesture.direction = direction
    frame.origin = origin
    self.delegate = delegate
    
    configureView(imageUrl)
    
    UIView.animate(withDuration: 1.0, animations: {
      self.frame.origin.x = animatePoint
    })
  }
```
{% endtab %}
{% endtabs %}

## Implementation Walkthrough

How do we log impressions, clicks, and dismissals while staying true to the code considerations mentioned above? We recommend storing your content cards as `idString` in order to log and reference them through a helper file. 

{% tabs %}
{% tab Video %}

{% include video.html id="INDVFUtv6Fc" align="center" %}

{% endtab %}
{% tab Swift - Demo Code Snippets %}
#### __Implementation Components__


__Update Content Card Dictionary__

Mapped through the Content Card idString
```swift
private var contentCardsDictionary: [String: ABKContentCard] = [:]

for card in cards {
      contentCardsDictionary[card.idString] = card
```


__Encapsulated ABK Methods__

Only exposing the idString as a parameter
```swift
switch rows[indexPath.row] {
    case .item(let course):
      guard course.isContentCard else { break }
      course.logContentCardImpression()
```


__Get Content Card from IDString__

Via Content Card Dictionary
```swift
protocol ContentCardable {
  func logContentCardImpression() {
    AppboyManager.shared.logContentCardImpression(idString: contentCardData?.contentCardId)
  }
}
```


__Call ABKCONTENTCARD Functions__

100% handled through AppboyManager.Swift
```swift
func logContentCardClicked(idString: String?) {
    guard let idString = idString, let contentCard = contentCardsDictionary[idString] else { return }
    
    contentCard.logContentCardClicked()
  }
```
{% endtab %}
{% endtabs %}
