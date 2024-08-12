---
nav_title: フィードのカスタマイズ
article_title: iOS のコンテンツカードフィードをカスタマイズする
platform: iOS
page_order: 2
description: "この記事では、iOS アプリケーションのコンテンツカードフィードのカスタマイズオプションについて説明します。"
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# コンテンツカードフィードをカスタマイズする

`ABKContentCardsTableViewController` を拡張してすべての UI 要素とコンテンツカードの動作をカスタマイズすることで、独自のコンテンツカードインターフェイスを作成できます。コンテンツカードセルをサブクラス化してからプログラムで使用することも、新しいクラスを登録するカスタムストーリーボードを導入することによって使用することもできます。完全な例については、コンテンツカードの[サンプルアプリ](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp)をご確認ください。 

また、サブクラス化戦略を使用すべきか、完全にカスタムのビューコントローラーを使用して、[データ更新を配信登録]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/integration/)すべきかを検討することも重要です。たとえば、`ABKContentCardsTableViewController` をサブクラス化する場合は、[`populateContentCards` メソッド](#overriding-populated-content-cards)を使用してカードのフィルター処理と順序付けを行うことができます (推奨)。ただし、ビューコントローラーを完全にカスタマイズすると、カルーセルでの表示やインタラクティブ要素の追加など、カードの動作をより詳細に制御できるようになりますが、順序付けとフィルター処理のロジックを実装するためにオブザーバーに頼らなければならなくなります。また、インプレッション数、却下イベント数、クリック数が適切に記録されるように、それぞれの分析メソッドを実装する必要もあります。

## UI をカスタマイズする

次のコードスニペットは、SDK が提供するメソッドを使用して、UI のニーズに合わせてコンテンツカードのスタイル設定と変更を行う方法を示しています。これらの方法によって、カスタムフォント、カスタマイズされたカラーコンポーネント、カスタマイズされたテキストなど、コンテンツカード UI のあらゆる側面をカスタマイズすることができます。 

コンテンツカードの UI をカスタマイズする方法は 2 通りあります。
\- 動的な方法: カードごとにカード UI を更新する
\- 静的な方法: すべてのカードで UI を更新する

### 動的 UI

コンテンツカーの `applyCard` メソッドはカードオブジェクトを参照し、UI の更新に使用されるキーと値のペアを渡すことができます。

{% tabs %}
{% tab Objective-C %}
\`\`\`objc
\- (void)applyCard:(ABKCaptionedImageContentCard \*)captionedImageCard {
  [super applyCard:captionedImageCard];    
 
  if ([card.extras objectForKey:ContentCardKeyBackgroundColorValue]) {
NSString *backgroundColor = [card.extras objectForKey:ContentCardKeyBackgroundColor];
if ([backgroundColor colorValue]) {
self.rootView.backgroundColor = [backgroundColor colorValue];
} else {
    self.rootView.backgroundColor = [UIColor lightGray];
    }
      } else {
    self.rootView.backgroundColor = [UIColor lightGray];
      }  
    }
  ```
{% endtab %}
{% tab Swift %}
```swift
    override func apply(_ captionedImageCard:ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)         
 
  if let backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] as?String,
     let backgroundColorValue = backgroundColor.colorValue() {
    rootView.backgroundColor = backgroundColorValue
  } else {
    rootView.backgroundColor = .lightGray
  }
}
\`\`\`
{% endtab %}
{% endtabs %}

### 静的 UI

`setUpUI` メソッドは、すべてのカードで静的コンテンツカードコンポーネントに値を代入できます。

{% tabs %}
{% tab Objective-C %}
\`\`\`objc
\#import "CustomClassicContentCardCell.h"  
 
@implementation CustomClassicContentCardCell
 
- (void)setUpUI {
[super setUpUI];
self.rootView.backgroundColor = [UIColor lightGrayColor];
self.rootView.layer.borderColor = [UIColor purpleColor].CGColor;
self.unviewedLineView.backgroundColor = [UIColor redColor];
self.titleLabel.font = [UIFont italicSystemFontOfSize:20];
}
  ```
{% endtab %}
{% tab Swift %}
```swift
  override func setUpUI() {
  super.setUpUI()
     
  rootView.backgroundColor = .lightGray
  rootView.layer.borderColor = UIColor.purple.cgColor
  unviewedLineViewColor = .red
  titleLabel.font = .italicSystemFont(ofSize:20)
}
\`\`\`
{% endtab %}
{% endtabs %}

## カスタムインターフェイスを提供する

カスタムインターフェイスを提供するには、必要なカードタイプごとにカスタムクラスを登録します。 

![A banner Content Card. A banner Content Card shows an image to the right of the banner with the text "Thanks for downloading Braze Demo!".]({% image_buster /assets/img/interface1.png %}){: style="max-width:35%;margin-left:15px;"}
![A captioned image Content Card. A captioned Content Card shows a Braze image with the caption overlaid across the bottom "Thanks for downloading Braze Demo!". ]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![A classic Content Card. A classic Content Card shows an image in the center of the card with the words "Thanks for downloading Braze Demo" underneath.]({% image_buster /assets/img/interface3.png %}){: style="max-width:18%;margin-left:15px;"}

Braze には、3 つのコンテンツカードテンプレート (バナー、キャプション付き画像、クラシック) が用意されています。または、独自のカスタムインターフェイスを提供する場合は、次のコードスニペットを参照してください。

{% tabs %}
{% tab Objective-C %}
\`\`\`objc
\- (void)registerTableViewCellClasses {
  [super registerTableViewCellClasses];
 
  // これら 2 種類のカードのデフォルトのクラス登録をカスタムクラスに置き換えます
  [self.tableView registerClass:[CustomCaptionedImageContentCardCell class] forCellReuseIdentifier:@"ABKCaptionedImageContentCardCell"];
  [self.tableView registerClass:[CustomClassicContentCardCell class] forCellReuseIdentifier:@"ABKClassicCardCell"];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func registerTableViewCellClasses() {
  super.registerTableViewCellClasses()
     
  // デフォルトのクラス登録をカスタムクラスで置き換えます
  tableView.register(CustomCaptionedImageContentCardCell.self, forCellReuseIdentifier:"ABKCaptionedImageContentCardCell")
  tableView.register(CustomBannerContentCardCell.self, forCellReuseIdentifier:"ABKBannerContentCardCell")
  tableView.register(CustomClassicImageContentCardCell.self, forCellReuseIdentifier:"ABKClassicImageCardCell")
  tableView.register(CustomClassicContentCardCell.self, forCellReuseIdentifier:"ABKClassicCardCell")
}
\`\`\`
{% endtab %}
{% endtabs %}

## 値が挿入されたコンテンツカードをオーバーライドする

コンテンツカードをプログラムで変更するには、`populateContentCards` メソッドを使用します。

{% tabs %}
{% tab Objective-C %}
```objc
- (void)populateContentCards {
  NSMutableArray<ABKContentCard *> *cards = [NSMutableArray arrayWithArray:[Appboy.sharedInstance.contentCardsController getContentCards]];
  for (ABKContentCard *card in cards) {
    // Replaces the card description for all Classic Content Cards
    if ([card isKindOfClass:[ABKClassicContentCard class]]) {
      ((ABKClassicContentCard *)card).cardDescription = @"Custom Feed Override title [classic cards only]!";
    }
  }
  super.cards = cards;
}
```
{% endtab %}
{% tab Swift %}
```swift
override func populateContentCards() {
  guard let cards = Appboy.sharedInstance()?.contentCardsController.contentCards else { return }
  for card in cards {
    // Replaces the card description for all Classic Content Cards
    if let classicCard = card as? ABKClassicContentCard {
      classicCard.cardDescription = "Custom Feed Override title [classic cards only]!"
    }
  }
  super.cards = (cards as NSArray).mutableCopy() as? NSMutableArray
}
```
{% endtab %}
{% endtabs %}