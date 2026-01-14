---
nav_title: カスタムディスプレイの操作
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

[`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h) を設定すると、アプリ内メッセージが表示される前に次のデリゲートメソッドが呼び出されます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

[`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) を実装しただけの場合は、代わりに次の UI デリゲートメソッドが呼び出されます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

このデリゲートメソッドを実装し、`ABKInAppMessageDisplayChoice` に対して次のいずれかの値を返すことで、アプリ内メッセージ処理をカスタマイズできます。

| `ABKInAppMessageDisplayChoice` | 動作 |
| -------------------------- | -------- |
| OBJECTIVE-C： `ABKDisplayInAppMessageNow`<br>SWIFT： `displayInAppMessageNow` | メッセージはすぐに表示される。 |
| OBJECTIVE-C： `ABKDisplayInAppMessageLater`<br>SWIFT： `displayInAppMessageLater` | メッセージは表示されず、スタックの一番上に戻される。 |
| OBJECTIVE-C： `ABKDiscardInAppMessage`<br>SWIFT： `discardInAppMessage`| メッセージは破棄され、表示されない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

`beforeInAppMessageDisplayed:` delegate メソッドを使用して、アプリ内メッセージ表示ロジックを追加したり、Braze がそれらを表示する前にアプリ内メッセージをカスタマイズしたり、Braze in-app メッセージ表示ロジックおよびUI を完全にオプトアウトしたりできます。

実装例については、[サンプルアプリケーション](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m)をご覧ください。

## 表示前のアプリ内メッセージの上書き

アプリ内メッセージの表示動作を変更したい場合は、必要な表示ロジックを `beforeInAppMessageDisplayed:` デリゲートメソッドに追加する必要があります。たとえば、キーボードが現在表示されている場合は画面の上部からアプリ内メッセージを表示したり、アプリ内メッセージデータモデルをを取得してアプリ内メッセージを自分で表示したりできます。

セッションの開始時にアプリ内メッセージキャンペーンが表示されない場合は、必要な表示ロジックが `beforeInAppMessageDisplayed:` デリゲートメソッドに追加されていることを確認してください。これにより、キーボードが表示されている場合でも、アプリ内メッセージキャンペーンを画面の上部から表示できます。

## ダークモードを無効にする

ユーザーデバイスでダークモードが有効になっているときにアプリ内メッセージがダークモードスタイルを採用しないようにするには、[`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d) プロパティを使用します。`ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` または `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:`メソッドのいずれかから、メソッドの `inAppMessage` パラメーターの `enableDarkTheme` プロパティを `NO` に設定します。

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab swift %}

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
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

さらに、`ABKInAppMessageImmersive` のサブクラス (*i.e*、`Modal` と `Full` のアプリ内メッセージなど) のボタンクリック数を記録する必要があります。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## メソッド宣言

詳細については、次のヘッダー ファイルを参照してください。

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## 実装サンプル

[`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) アプリ内メッセージサンプルアプリを参照してください。



