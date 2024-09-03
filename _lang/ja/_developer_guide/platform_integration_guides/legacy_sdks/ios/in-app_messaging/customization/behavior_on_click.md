---
nav_title: クリック時のカスタム動作
article_title: iOS 用アプリ内メッセージクリック時動作のカスタマイズ
platform: iOS
page_order: 5
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングのカスタムクリック時動作について説明します。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# クリック時のアプリ内メッセージ動作のカスタマイズ

{% alert note %}
この記事には、廃止予定のニュースフィードの情報が含まれています。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

`ABKInAppMessage` の`inAppMessageClickActionType` プロパティは、アプリ内メッセージがクリックされた後の動作を定義します。このプロパティは読み取り専用です。アプリ内メッセージのクリック動作を変更する場合は、`ABKInAppMessage` で以下のメソッドを呼び出すことができます。

{% tabs %}
{% tab 目標-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab 速い %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

`inAppMessageClickActionType` は次のいずれかの値に設定できます。

| `ABKInAppMessageClickActionType` | オン・クリックの行動 |
| -------------------------- | -------- |
| `ABKInAppMessageDisplayNewsFeed` | メッセージがクリックされるとニュースフィードが表示され、メッセージは解除される。なお、`uri` パラメーターは無視され、`ABKInAppMessage` の`uri` プロパティはnilに設定される。 |
| `ABKInAppMessageRedirectToURI` | メッセージがクリックされると、与えられたURIが表示され、メッセージが消える。なお、`uri` パラメーターはnilにはできない。 |
| `ABKInAppMessageNoneClickAction` | クリックするとメッセージが消える。なお、`uri` パラメーターは無視され、`ABKInAppMessage` の`uri` プロパティはnilに設定される。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージ `clickAction` も最終ペイロードに含まれます。
{% endalert %}

## アプリ内メッセージ本文クリック数のカスタマイズ

アプリ内メッセージがクリックされると、次の [`ABKInAppMessageUIDelegate`][34] デリゲートメソッドが呼び出されます。

{% tabs %}
{% tab 目標-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab 速い %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## アプリ内メッセージボタンクリックのカスタマイズ

アプリ内メッセージボタンや HTML アプリ内メッセージボタン (リンクなど) のクリックに対して、[`ABKInAppMessageUIDelegate`][34]には次のデリゲートメソッドが含まれています。

{% tabs %}
{% tab 目標-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab 速い %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

各メソッドは、Braze がクリックアクションを実行し続ける必要があるかどうかを示す `BOOL` 値を返します。

デリゲートメソッドでボタンのクリックアクションタイプにアクセスするには、次のコードを使用できます。

{% tabs %}
{% tab 目標-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab 速い %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

アプリ内メッセージにボタンがある場合、実行されるクリックアクションは `ABKInAppMessageButton` モデルのクリックアクションのみです。`ABKInAppMessage` モデルにデフォルトのクリックアクション (「ニュースフィード」) が割り当てられていても、アプリ内のメッセージ本文はクリックできません。

## メソッド宣言

詳細については、次のヘッダー ファイルを参照してください。

- [`ABKInAppMessage.h`][14]

[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h
