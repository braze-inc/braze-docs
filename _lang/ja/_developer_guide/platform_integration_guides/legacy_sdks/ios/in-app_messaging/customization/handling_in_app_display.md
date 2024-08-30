---
nav_title: カスタムディスプレイ処理
article_title: iOS のアプリ内メッセージ表示処理のカスタマイズ
platform: iOS
page_order: 4
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングのカスタム表示処理について説明します。"
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アプリ内メッセージ表示のカスタム処理

[`ABKInAppMessageControllerDelegate`][16] を設定すると、アプリ内メッセージが表示される前に次のデリゲートメソッドが呼び出されます。

{% tabs %}
{% tab 目標-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab 速い %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

[`ABKInAppMessageUIDelegate`][34] を実装しただけの場合は、代わりに次の UI デリゲートメソッドが呼び出されます。

{% tabs %}
{% tab 目標-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab 速い %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

このデリゲートメソッドを実装し、`ABKInAppMessageDisplayChoice` に対して次のいずれかの値を返すことで、アプリ内メッセージ処理をカスタマイズできます。

| `ABKInAppMessageDisplayChoice` | 動作 |
| -------------------------- | -------- |
| Objective-Cである： `ABKDisplayInAppMessageNow`<br>スウィフトだ： `displayInAppMessageNow` | メッセージはすぐに表示される。 |
| Objective-Cである： `ABKDisplayInAppMessageLater`<br>スウィフトだ： `displayInAppMessageLater` | メッセージは表示されず、スタックの一番上に戻される。 |
| Objective-Cである： `ABKDiscardInAppMessage`<br>スウィフトだ： `discardInAppMessage`| メッセージは破棄され、表示されない。 |
{: .reset-td-br-1 .reset-td-br-2}

`beforeInAppMessageDisplayed:` デリゲートメソッドを使用して、アプリ内メッセージ表示ロジックを追加したり、Braze によって表示される前にアプリ内メッセージをカスタマイズしたり、Braze のアプリ内メッセージ表示ロジックと UI を完全にオプトアウトしたりできます。

実装例については、[サンプルアプリケーション][36]をご覧ください。

## 表示前のアプリ内メッセージの上書き

アプリ内メッセージの表示動作を変更したい場合は、必要な表示ロジックを `beforeInAppMessageDisplayed:` デリゲートメソッドに追加する必要があります。たとえば、キーボードが現在表示されている場合は画面の上部からアプリ内メッセージを表示したり、アプリ内メッセージデータモデルをを取得してアプリ内メッセージを自分で表示したりできます。

セッションの開始時にアプリ内メッセージキャンペーンが表示されない場合は、必要な表示ロジックが `beforeInAppMessageDisplayed:` デリゲートメソッドに追加されていることを確認してください。これにより、キーボードが表示されている場合でも、アプリ内メッセージキャンペーンを画面の上部から表示できます。

## ダークモードを無効にする

ユーザーデバイスでダークモードが有効になっているときにアプリ内メッセージがダークモードスタイルを採用しないようにするには、[`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d) プロパティを使用します。`ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` または `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:`メソッドのいずれかから、メソッドの `inAppMessage` パラメーターの `enableDarkTheme` プロパティを `NO` に設定します。

{% tabs %}
{% tab 目標-C %}

```objc
// ABKInAppMessageControllerDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}

// ABKInAppMessageUIDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMesssageDisplayed:(ABKInAppMessage *)inAppMessage
                                            withKeyboardIsUp:(BOOL)keyboardIsUp {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}
```

{% endtab %}
{% tab 速い %}

```swift
// ABKInAppMessageControllerDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}

// ABKInAppMessageUIDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}
```

{% endtab %}
{% endtabs %}

## 表示中にステータスバーを非表示にする

`Full` および `HTML` のアプリ内メッセージの場合、SDK はデフォルトでメッセージをステータスバーの上に配置しようとします。ただし、場合によっては、ステータスバーがアプリ内メッセージの上に表示されたままになることがあります。iOS SDK のバージョン [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) 以降では、`startWithApiKey:` に渡された `appboyOptions` 内で `ABKInAppMessageHideStatusBarKey` を `YES` に設定することで、`Full` および `HTML` のアプリ内メッセージを表示するときにステータスバーを強制的に非表示にできます。

## インプレッション数とクリック数を記録する

完全なカスタム処理を実装している場合 (たとえば、`beforeInAppMessageDisplayed:` で `ABKDiscardInAppMessage` を返すことで、Braze のアプリ内メッセージ表示を回避します)、アプリ内メッセージのインプレッション数とクリック数のログへの記録は自動的には行われません。アプリ内メッセージモデルを使用して独自のUIを実装する場合は、`ABKInAppMessage` クラスで次のメソッドを使用して分析をログに記録する必要があります。

{% tabs %}
{% tab 目標-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab 速い %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

さらに、`ABKInAppMessageImmersive` のサブクラス（ .*i.e*.、`Modal` 、`Full` のアプリ内メッセージ)：

{% tabs %}
{% tab 目標-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab 速い %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## メソッド宣言

詳細については、次のヘッダー ファイルを参照してください。

- [`ABKInAppMessage.h`][14]
- [`ABKInAppMessageControllerDelegate.h`][16]

## 実装サンプル

[`AppDelegate.m`][36] アプリ内メッセージサンプルアプリを参照してください。


[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h

