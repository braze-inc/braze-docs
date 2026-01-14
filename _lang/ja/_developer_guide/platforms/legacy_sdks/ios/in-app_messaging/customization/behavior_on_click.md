---
nav_title: クリック時のカスタム動作
article_title: iOS 用のアプリ内メッセージオンクリック動作のカスタマイズ
platform: iOS
page_order: 5
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングのカスタムクリック時動作について説明します。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# クリック時のアプリ内メッセージ動作のカスタマイズ

`ABKInAppMessage` の`inAppMessageClickActionType` プロパティは、アプリ内メッセージがクリックされた後の動作を定義します。このプロパティは読み取り専用です。アプリ内メッセージのクリック動作を変更する場合は、`ABKInAppMessage` で以下のメソッドを呼び出すことができます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

`inAppMessageClickActionType` は次のいずれかの値に設定できます。

| `ABKInAppMessageClickActionType` | クリック時動作 |
| -------------------------- | -------- |
| `ABKInAppMessageRedirectToURI` | メッセージがクリックされたときに指定された URIが表示され、メッセージは破棄されます。`uri` パラメータを nil にすることはできないことに注意してください。 |
| `ABKInAppMessageNoneClickAction` | クリックするとメッセージが却下されます。`uri` パラメータは無視され、`ABKInAppMessage` の `uri` プロパティは nil に設定されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージ `clickAction` も最終ペイロードに含まれます。
{% endalert %}

## アプリ内メッセージ本文クリック数のカスタマイズ

アプリ内メッセージがクリックされると、次の [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) デリゲートメソッドが呼び出されます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## アプリ内メッセージボタンクリックのカスタマイズ

アプリ内メッセージボタンや HTML アプリ内メッセージボタン (リンクなど) のクリックに対して、[`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)には次のデリゲートメソッドが含まれています。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

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
{% tab OBJECTIVE-C %}

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
{% tab swift %}

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

アプリ内メッセージにボタンがある場合、実行されるクリックアクションは `ABKInAppMessageButton` モデルのクリックアクションのみです。`ABKInAppMessage` モデルにデフォルトのクリックアクションが割り当てられている場合でも、アプリ内のメッセージ本文はクリックできません。

## メソッドの宣言

詳細については、次のヘッダー ファイルを参照してください。

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

