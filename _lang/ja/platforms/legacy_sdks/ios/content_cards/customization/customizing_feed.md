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

また、サブクラス化戦略を使用すべきか、完全にカスタムのビューコントローラーを使用して、[データ更新を配信登録]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration/)すべきかを検討することも重要です。たとえば、`ABKContentCardsTableViewController` をサブクラス化する場合は、[`populateContentCards` メソッド](#overriding-populated-content-cards)を使用してカードのフィルター処理と順序付けを行うことができます (推奨)。ただし、ビューコントローラーを完全にカスタマイズすると、カルーセルでの表示やインタラクティブ要素の追加など、カードの動作をより詳細に制御できるようになりますが、順序付けとフィルター処理のロジックを実装するためにオブザーバーに頼らなければならなくなります。また、インプレッション数、却下イベント数、クリック数を適切に記録するには、それぞれの分析メソッドを実装する必要もあります。

## UI をカスタマイズする

次のコードスニペットは、SDK が提供するメソッドを使用して、UI のニーズに合わせてコンテンツカードのスタイル設定と変更を行う方法を示しています。これらの方法によって、カスタムフォント、カスタマイズされたカラーコンポーネント、カスタマイズされたテキストなど、コンテンツカード UI のあらゆる側面をカスタマイズすることができます。 

コンテンツカードの UI をカスタマイズする方法は 2 通りあります。 
- ダイナミックメソッド: カードごとの更新 カード UI
- スタティックメソッド: すべてのカードでUI を更新します

### 動的 UI

コンテンツカーの `applyCard` メソッドはカードオブジェクトを参照し、UI の更新に使用されるキーと値のペアを渡すことができます。

{% tabs %}
{% tab Objective-C %}
```objc
- (void)applyCard:(ABKCaptionedImageContentCard *)captionedImageCard {
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
override func apply(_ captionedImageCard: ABKCaptionedImageContentCard!) {
  super.apply(captionedImageCard)         
 
  if let backgroundColor = card.extras?[ContentCardKey.backgroundColor.rawValue] as? String,
     let backgroundColorValue = backgroundColor.colorValue() {
    rootView.backgroundColor = backgroundColorValue
  } else {
    rootView.backgroundColor = .lightGray
  }
}
```
{% endtab %}
{% endtabs %}

### 静的 UI

`setUpUI` メソッドは、すべてのカードで静的コンテンツカードコンポーネントに値を代入できます。

{% tabs %}
{% tab Objective-C %}
```objc
#import "CustomClassicContentCardCell.h"  
 
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
  titleLabel.font = .italicSystemFont(ofSize: 20)
}
```
{% endtab %}
{% endtabs %}

## カスタムインターフェイスを提供する

カスタムインターフェイスを提供するには、必要なカードタイプごとにカスタムクラスを登録します。 

![バナーコンテンツカード。バナーコンテンツカードでは、バナーの右側に「Braze Demoをダウンロードしていただきありがとうございます。」というテキストが付いた画像が表示されます。(]({% image_buster /assets/img/interface1.png %})){: style="max-width:35%;margin-left:15px;"}
![キャプション付き画像コンテンツカードキャプション付きコンテンツカードには、Braze の画像が表示され、「Braze Demo をダウンロードしていただきありがとうございます。」というキャプションが下部に重ねて表示されます。()]({% image_buster /assets/img/interface2.png %}){: style="max-width:25%;margin-left:15px;"}
![従来のコンテンツカード。従来のコンテンツカードでは、カードの中央に画像が表示され、その下に「Braze Demoをダウンロードしてくれてありがとう」という言葉が表示されます。()

Braze には、3 つのコンテンツカードテンプレート (バナー、キャプション付き画像、クラシック) が用意されています。または、独自のカスタムインターフェイスを提供する場合は、次のコードスニペットを参照してください。

{% tabs %}
{% tab Objective-C %}
```objc
- (void)registerTableViewCellClasses {
  [super registerTableViewCellClasses];
 
  // Replace the default class registrations with custom classes for these two types of cards
  [self.tableView registerClass:[CustomCaptionedImageContentCardCell class] forCellReuseIdentifier:@"ABKCaptionedImageContentCardCell"];
  [self.tableView registerClass:[CustomClassicContentCardCell class] forCellReuseIdentifier:@"ABKClassicCardCell"];
}
```
{% endtab %}
{% tab Swift %}
```swift
override func registerTableViewCellClasses() {
  super.registerTableViewCellClasses()
     
  // Replace the default class registrations with custom classes
  tableView.register(CustomCaptionedImageContentCardCell.self, forCellReuseIdentifier: "ABKCaptionedImageContentCardCell")
  tableView.register(CustomBannerContentCardCell.self, forCellReuseIdentifier: "ABKBannerContentCardCell")
  tableView.register(CustomClassicImageContentCardCell.self, forCellReuseIdentifier: "ABKClassicImageCardCell")
  tableView.register(CustomClassicContentCardCell.self, forCellReuseIdentifier: "ABKClassicCardCell")
}
```
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