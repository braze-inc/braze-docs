---
nav_title: アプリ内メッセージ UI デリゲート
article_title: iOS のアプリ内メッセージ UI デリゲート
platform: Swift
page_order: 2
description: "このリファレンス記事では、Swift SDK の iOS アプリ内メッセージングデリゲートの設定について説明しています。"
channel:
  - in-app messages

---

# アプリ内メッセージ UI デリゲート

> オプションの [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) を使用してアプリ内メッセージの表示をカスタマイズし、さまざまなライフサイクルイベントに対応します。このデリゲートプロトコルを使用すると、トリガーされたアプリ内メッセージペイロードを受信して​​さらに処理したり、表示ライフサイクルイベントを受信したり、表示タイミングを制御したりできます。 

## 前提条件

`BrazeInAppMessageUIDelegate` を使用するには:
* デフォルトの [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) 実装を `inAppMessagePresenter` として使用する必要があります。 
* `BrazeUI` ライブラリーをプロジェクトに含める必要があります。

## アプリ内メッセージデリゲートの設定

次のサンプルコードに従って、Braze インスタンスで [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) デリゲートオブジェクトを設定します。

{% tabs %}
{% tab SWIFT %}

まず、`BrazeInAppMessageUIDelegate` プロトコルと、対応する必要なメソッドを実装します。以下の例では、このプロトコルをアプリケーションの `AppDelegate` クラスに実装しています。

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

次に、このアプリ内メッセージ UI を `inAppMessagePresenter` として割り当てる前に、`BrazeInAppMessageUI` インスタンスで `delegate` オブジェクトを割り当てます。

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab OBJECTIVE-C %}

まず、`BrazeInAppMessageUIDelegate` プロトコルと、対応する必要なメソッドを実装します。以下の例では、このプロトコルをアプリケーションの `AppDelegate` クラスに実装しています。

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

次に、このアプリ内メッセージ UI を `inAppMessagePresenter` として割り当てる前に、`BrazeInAppMessageUI` インスタンスで `delegate` オブジェクトを割り当てます。

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

パラメータが言語ランタイムと互換性がないため、すべてのデリゲートメソッドを Objective-C で使用できるわけではありません。

{% endtab %}
{% endtabs %}

### ステップバイステップガイド

アプリ内メッセージ UI デリゲートの段階的な実装については、この[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)を参照してください。

## iOS のアプリ内メッセージの向きのカスタマイズ

### 好みの向きの設定

すべてのアプリ内メッセージは、デバイスの向きに関係なく特定の向きで表示されるように設定できます。好みの向きを設定するには、`inAppMessage(_:prepareWith:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)を使用して `PresentationContext` で `preferredOrientation` プロパティを設定します。 

{% tabs %}
{% tab SWIFT %}

たとえば、好みの向きとして縦を作成するには以下を設定します。

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endtab %}
{% endtabs %}

アプリ内メッセージが表示された後、メッセージが表示されている間にデバイスの向きが変わった場合、メッセージの `orientation` 設定でサポートされていれば、メッセージがデバイスに合わせて回転します。

メッセージを表示するには、デバイスの向きがアプリ内メッセージの `orientation` プロパティでもサポートされている必要があることに注意してください。また、`preferredOrientation` 設定が適用されるのは、Xcodeのターゲットの設定の [**導入情報**] セクションで、アプリケーションでサポートされているインターフェイスの向きにその向きが含まれている場合に限られます。

![Xcodeでサポートされているオリエンテーション]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
向きはメッセージの表示にのみ適用されます。デバイスの向きが変わると、メッセージビューでサポートされている向きのいずれかが採用されます。小型のデバイス (iPhone、iPod Touch) では、モーダルアプリ内メッセージやフルアプリ内メッセージを横向きに設定すると、コンテンツが切り捨てられることがあります。
{% endalert %}

### メッセージの向きの変更

向きをメッセージごとに設定することもできます。このプロパティでは、各メッセージに使用可能なすべての方向タイプが定義されます。そのためには、該当する `Braze.InAppMessage` で `orientation` プロパティを設定します。

{% tabs %}
{% tab SWIFT %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

## ダークモードを無効にする

ユーザーデバイスでダークモードが有効になっているときにアプリ内メッセージでダークモードスタイルが採用されないようにするには、`inAppMessage(_:prepareWith:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)を実装します。メソッドに渡される `PresentationContext` には、表示される `InAppMessage` オブジェクトの参照が含まれます。各 `InAppMessage` に、`dark` と `light` のモードテーマを含む `themes` プロパティがあります。`themes.dark` プロパティを `nil` に設定すると、Braze では自動的にライトテーマを使用してアプリ内メッセージが表示されます。

ボタンがあるアプリ内メッセージの種類では、`buttons` プロパティに追加の `themes` オブジェクトがあります。ボタンでダークモードのスタイルが採用されないようにするには、[`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) を使用して `dark` テーマがない `light` テーマのボタンの新しい配列を作成できます。

{% tabs %}
{% tab SWIFT %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup
    
    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal
    
    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage
    
    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full
    
    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage
    
    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## ボタンクリックのカスタマイズ

アプリ内メッセージのボタン情報にアクセスするか、クリック動作をオーバーライドするには、[`BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-122yi) を実装します。`true` を返して Braze にクリックアクションの処理を許可するか、`false` を返して動作をオーバーライドします。
{% tabs %}
{% tab SWIFT %}

```swift
  func inAppMessage(
    _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
    buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
  ) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }
    
    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}


## 表示中にステータスバーを非表示にする

`Full`、`FullImage`、および `HTML` アプリ内メッセージについて、SDK ではステータスバーがデフォルトで非表示になります。他の種類のアプリ内メッセージでは、ステータスバーは変更されません。この動作を設定するには、`inAppMessage(_:prepareWith:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)を使用して `PresentationContext` で `statusBarHideBehavior` プロパティを設定します。このフィールドの値は次のうちいずれかになります。

| ステータスバー非表示の動作            | 説明                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | メッセージ・ビューはステータス・バーの非表示状態を決定する。                                 |
| `.hidden`                           | ステータスバーは常に隠す。                                                           |
| `.visible`                          | 常にステータスバーを表示する。                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 表示タイミングのカスタマイズ 

利用可能なアプリ内メッセージをユーザーエクスペリエンスの特定のポイントで表示するかどうかをコントロールできます。全画面でのゲーム中や読み込み画面など、アプリ内メッセージを表示させたくない状況がある場合は、保留中のアプリ内メッセージを遅延させるか、破棄することができます。アプリ内メッセージのタイミングをコントロールするには、`inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)を使用して `BrazeInAppMessageUI.DisplayChoice` プロパティを設定します。 

{% tabs %}
{% tab SWIFT %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

次のうちいずれかの値を返すよう `BrazeInAppMessageUI.DisplayChoice` を設定します。

| ディスプレイの選択                      | 動作                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | メッセージはすぐに表示される。これはデフォルト値です。                                                       |
| `.reenqueue`                        | メッセージは表示されず、スタックの一番上に戻される。                                       |
| `.later`                            | メッセージは表示されず、スタックの一番上に戻される。(非推奨、`.reenqueue` を使用してください) |
| `.discard`                          | メッセージは破棄され、表示されない。                                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 実装サンプル

[Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) と [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI) のサンプルについては、[例] フォルダーで `InAppMessageUI` を参照してください。

