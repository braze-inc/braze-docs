---
nav_title: 読み取り&amp;アンプ;未読インジケータ
article_title: iOS 用コンテンツカード既読 / 未読インジケーター
platform: iOS
page_order: 4
description: "このリファレンス記事では、iOS の既読 / 未読インジケーターと、それをコンテンツカードに実装する方法について説明します。"
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 既読 / 未読インジケーター

## 未閲覧インジケーターを無効にする

![2つのコンテンツカードが並んで表示されます。左側のカードの下に青い線が表示され、表示されていないことを示します。右側のカードには、すでに表示されていることを示す青い線が表示されません。]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

カードが閲覧されたかどうかを示すカード下部の青い線を無効にするには、`ABKContentCardsTableViewController` の `disableUnviewedIndicator` プロパティを `YES` に設定します。

## 未閲覧インジケーターをカスタマイズする

未閲覧インジケーターには、`ABKBaseContentCardCell` クラスの `unviewedLineView` プロパティを使用してアクセスできます。`UITableViewCell` の実装を使用する場合は、セルが描画される前にプロパティにアクセスする必要があります。

たとえば、未閲覧インジケーターの色を赤に設定するには、次のようにします。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab swift %}

```swift
(card as? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}
