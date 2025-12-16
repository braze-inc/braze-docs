---
nav_title: 複数のフィード
article_title: iOS で複数のコンテンツカードフィードを使う
platform: iOS
page_order: 6
description: "この参考記事では、iOS アプリケーションに複数のコンテンツカードフィードを実装する方法について説明します。"
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 複数のコンテンツカードフィードを使用する

コンテンツカードは、アプリ上で特定のカードだけを表示するようにフィルタリングすることができ、異なるユースケース (トランザクション用フィードとマーケティング用フィードを使用する場合のように) に対して複数のコンテンツカードフィードを持つことが可能となります。

以下のドキュメントは、特定の統合に合わせて変更可能な実装例を示しています。

## ステップ1:カードにキーと値のペアを設定する

コンテンツカードキャンペーンを作成する際、各カードにキーと値のペアのデータを設定できます。フィルタリングロジックは、このキーと値のペアデータを使ってカードを分類します。

この例では、どのコンテンツカードフィードにカードを表示するかを指定する `feed_type` キーでキーと値のペアを設定します。この値は、`Transactional`、`Marketing` などのように、カスタムフィードの値になります。

## ステップ2:コンテンツカードのリスナーを設定する

次のコードスニペットを使って、コンテンツカードの更新をリッスンするオブザーバーを追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

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

オブザーバーからの更新に応答し、返されたカードをタイプ別にフィルターするために、以下のメソッドを追加します。

最初のメソッド `contentCardsUpdatedNotificationReceived:` は、オブザーバーからの更新を処理します。2番目のメソッド `getCardsForFeedType:` を希望するフィードタイプ (この場合、`Transactional`) で呼び出します。

{% tabs %}
{% tab OBJECTIVE-C %}

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
