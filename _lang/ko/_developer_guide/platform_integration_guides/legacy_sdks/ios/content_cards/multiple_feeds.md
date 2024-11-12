---
nav_title: 다중 피드
article_title: iOS용 다중 콘텐츠 카드 피드 사용
platform: iOS
page_order: 6
description: "이 참조 문서에서는 iOS 애플리케이션에서 여러 콘텐츠 카드 피드를 구현하는 방법을 다룹니다."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 여러 콘텐츠 카드 피드 사용

콘텐츠 카드는 앱에서 특정 카드만 표시하도록 필터링할 수 있으므로 다양한 사용 사례(예: 트랜잭션 피드와 마케팅 피드)별로 여러 콘텐츠 카드 피드를 지원할 수 있습니다.

다음 설명서에서는 특정 통합에 맞게 변경할 수 있는 예제 구현을 보여줍니다.

## 1단계: 카드에 키-값 쌍 설정

콘텐츠 카드 캠페인을 생성할 때 각 카드에 키-값 페어 데이터를 설정할 수 있습니다. 우리의 필터링 로직은 이 키-값 페어 데이터를 사용하여 카드를 분류할 것입니다.

이 예제에서는 `feed_type` 키와 함께 키-값 페어를 설정하여 카드를 표시해야 하는 콘텐츠 카드 피드를 지정합니다. 값은 `Transactional`, `Marketing` 등에서와 같이 커스텀 피드에 따라 달라집니다.

## 2단계: 콘텐츠 카드 리스너 설정

다음 코드 스니펫을 사용하여 콘텐츠 카드 업데이트에 대해 수신 대기할 관찰자를 추가합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                           selector:@selector(contentCardsUpdatedNotificationReceived:)
                                               name:ABKContentCardsProcessedNotification
                                             object:nil];
```

{% endtab %}
{% tab SWIFT %}

```swift
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

{% endtab %}
{% endtabs %}

다음 메서드를 추가하여 관찰자의 업데이트에 응답하고 반환된 카드를 유형별로 필터링합니다.

첫 번째 메서드, `contentCardsUpdatedNotificationReceived:`에서는 관찰자의 업데이트를 처리합니다. 그리고 두 번째 메서드, `getCardsForFeedType:`을 원하는 피드 유형(이 경우 `Transactional`)과 함께 호출합니다.

{% tabs %}
{% tab 목표-C %}

```objc
- (void)contentCardsUpdatedNotificationReceived:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // Get an array containing only cards that have the "Transactional" feed type set in their extras.
    NSArray<ABKContentCard *> *filteredArray = [self getCardsForFeedType:@"Transactional"];
    NSLog(@"Got filtered array of length: %lu", [filteredArray count]);

    // Pass filteredArray to your UI layer for display.
  }
}

- (NSArray<ABKContentCard *> *)getCardsForFeedType:(NSString *)type {
  NSArray<ABKContentCard *> *cards = [Appboy.sharedInstance.contentCardsController getContentCards];

  NSArray<ABKContentCard *> *filteredArray = [cards filteredArrayUsingPredicate:[NSPredicate predicateWithBlock:^BOOL(ABKContentCard * card, NSDictionary *bindings) {
    NSDictionary *extras = [card extras];
    if (extras != nil && [extras objectForKey:@"feed_type"] != nil && [[extras objectForKey:@"feed_type"] isEqualToString:type]) {
      NSLog(@"Got card: %@ ", card.idString);
      return YES;
    }
    return NO;
  }]];

  return filteredArray;
}
```

{% endtab %}
{% tab SWIFT %}

```swift
@objc private func contentCardsUpdatedNotificationReceived(notification: NSNotification) {
    guard let updateSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool else { return }
    if updateSuccessful {
        // Get an array containing only cards that have the "Transactional" feed type set in their extras.
        let filteredArray = getCards(forFeedType: "Transactional")
        NSLog("Got filtered array of length: %@",filteredArray?.count ?? 0)

        // Pass filteredArray to your UI layer for display.
    }
}

func getCards(forFeedType type: String) -> [ABKContentCard]? {
    guard let allCards = Appboy.sharedInstance()?.contentCardsController.contentCards as? [ABKContentCard] else { return nil }
    // return filtered cards
    return allCards.filter {
        if $0.extras?["feed_type"] as? String == type {
            NSLog("%@","Got card: \($0.idString)")
            return true
        } else {
            return false
        }
    }
}
```

{% endtab %}
{% endtabs %}
