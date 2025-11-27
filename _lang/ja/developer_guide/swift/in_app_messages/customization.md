{% multi_lang_include developer_guide/prerequisites/swift.md %}

## UI デリゲートの設定(必須)

アプリ内メッセージの表示をカスタマイズし、さまざまなライフサイクルイベントに対応するには、[`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) を設定する必要があります。これは、トリガーのアプリ内メッセージ有料読み込むsの受信と処理、ディスプレイライフサイクルイベントの受信、およびディスプレイタイミングのコントロールに使用されるデリゲートプロトコルです。`BrazeInAppMessageUIDelegate` を使用するには、次の操作を行う必要があります。
- デフォルト[`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) インプリメンテーションを`inAppMessagePresenter` として使用します。 
- `BrazeUI` ライブラリーをプロジェクトに含めます。

### ステップ 1: `BrazeInAppMessageUIDelegate` プロトコルを実装する 

まず、`BrazeInAppMessageUIDelegate` プロトコルと、対応する必要なメソッドを実装します。以下の例では、このプロトコルをアプリケーションの `AppDelegate` クラスに実装しています。

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### ステップ 2: `delegate` オブジェクトを割り当てます 

`delegate` オブジェクトを`BrazeInAppMessageUI` インスタンスに割り当ててから、このアプリ内メッセージ UI を`inAppMessagePresenter` として割り当てます。

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
パラメータが言語ランタイムと互換性がないため、すべてのデリゲートメソッドを Objective-C で使用できるわけではありません。
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
アプリ内メッセージ UI デリゲートの段階的な実装については、この[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)を参照してください。
{% endalert %}

## オン・クリック動作

各`Braze.InAppMessage` オブジェクトには対応する [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction) が含まれ、これによってクリック時の動作が定義されます。 

### クリックアクションのタイプ

`Braze.InAppMessage` の`clickAction` プロパティは `.none` にデフォルト設定されていますが、次のうちいずれかの値に設定できます。

| `ClickAction` | クリック時動作 |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | 指定されたURLを外部ブラウザで開く。`useWebView` が`true` に設定されていれば、ウェブビューで開く。 |
| `.none` | クリックするとメッセージが却下されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージ `clickAction` も最終ペイロードに含まれます。
{% endalert %}

### クリック時の動作をカスタマイズする

この動作をカスタマイズするために、以下のサンプルを参照して `clickAction` プロパティを変更できます。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

`inAppMessage(_:prepareWith:)` メソッドは、Objective-C では利用できません。

{% endtab %}
{% endtabs %}

### カスタム動作の処理

アプリ内メッセージがクリックされると、次の [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) デリゲートメソッドが呼び出されます。アプリ内メッセージボタンと HTML アプリ内メッセージボタン（リンク）のクリックについては、ボタン ID がオプションのパラメータとして提供されます。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

このメソッドは、Braze がクリックアクションを実行し続けるかどうかを示すブール値を返します。

{% tabs %}
{% tab swift %}

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

## モーダル消去のカスタマイズ

外側のタップで閉じる操作を有効にするため、カスタマイズするアプリ内メッセージの種類の `Attributes` 構造体で `dismissOnBackgroundTap` プロパティを変更できます。 

たとえば、モーダル画像のアプリ内メッセージに対してこの機能を有効にする場合は、以下を設定します。

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

`Attributes` によるカスタマイズは Objective-C では使用できません。

{% endtab %}
{% endtabs %}

デフォルト値は `false` です。これにより、ユーザーがアプリ内メッセージの外側をタップしたときにモーダルアプリ内メッセージが閉じられるかどうかが決まります。

| `DismissModalOnOutsideTap` | 説明 |
|----------|-------------|
| `true`         | モーダルアプリ内メッセージは、外部タップで閉じられます。     |
| `false`        | デフォルトでは、モーダルアプリ内メッセージは外部タップをしても閉じられません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

アプリ内メッセージのカスタマイズの詳細については、こちらの[記事](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)を参照してください。

## メッセージの方向をカスタマイズする

アプリ内メッセージの向きをカスタマイズできます。すべてのメッセージに新しいデフォルトの向きを設定したり、1つのメッセージにカスタムの向きを設定したりできます。

{% tabs local %}
{% tab all messages %}
すべてのアプリ内メッセージ s のデフォルト方向を選択するには、[`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) メソッドを使用して、`preferredOrientation` プロパティを`PresentationContext` に設定します。 

たとえば、縦向きをデフォルト方向に設定するには:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab single message %}
単一のメッセージの方向を設定するには、`orientation` プロパティの`Braze.InAppMessage` を変更します。

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

アプリ内メッセージが表示された後、メッセージが表示されている間にデバイスの向きが変更されると、メッセージはデバイスと共に回転します(メッセージの`orientation` 設定でサポートされている場合)。

また、表示するためには、アプリ内メッセージの`orientation` プロパティで装置の向きをサポートする必要があります。また、`preferredOrientation` 設定が適用されるのは、Xcodeのターゲットの設定の [**導入情報**] セクションで、アプリケーションでサポートされているインターフェイスの向きにその向きが含まれている場合に限られます。

![Xcodeでサポートされているオリエンテーション]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})()

{% alert note %}
向きはメッセージの表示にのみ適用されます。デバイスの向きが変わると、メッセージビューでサポートされている向きのいずれかが採用されます。小型のデバイス (iPhone、iPod Touch) では、モーダルアプリ内メッセージやフルアプリ内メッセージを横向きに設定すると、コンテンツが切り捨てられることがあります。
{% endalert %}

## 表示タイミングのカスタマイズ 

利用可能なアプリ内メッセージをユーザーエクスペリエンスの特定のポイントで表示するかどうかをコントロールできます。全画面でのゲーム中や読み込み画面など、アプリ内メッセージを表示させたくない状況がある場合は、保留中のアプリ内メッセージを遅延させるか、破棄することができます。アプリ内メッセージのタイミングをコントロールするには、`inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)を使用して `BrazeInAppMessageUI.DisplayChoice` プロパティを設定します。 

{% tabs %}
{% tab swift %}

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

{% alert tip %}
`InAppMessageUI`のサンプルについては、[Swift Braze SDKリポジトリー](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI)と[Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)を確認してください。
{% endalert %}

## ステータス棒を非表示にする

`Full`、`FullImage`、および `HTML` アプリ内メッセージについて、SDK ではステータスバーがデフォルトで非表示になります。他の種類のアプリ内メッセージでは、ステータスバーは変更されません。この動作を設定するには、`inAppMessage(_:prepareWith:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)を使用して `PresentationContext` で `statusBarHideBehavior` プロパティを設定します。このフィールドの値は次のうちいずれかになります。

| ステータスバー非表示の動作            | 説明                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | メッセージ・ビューはステータス・バーの非表示状態を決定する。                                 |
| `.hidden`                           | ステータスバーは常に隠す。                                                           |
| `.visible`                          | 常にステータスバーを表示する。                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ダークモードを無効にする

ユーザーデバイスでダークモードが有効になっているときにアプリ内メッセージでダークモードスタイルが採用されないようにするには、`inAppMessage(_:prepareWith:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)を実装します。メソッドに渡される `PresentationContext` には、表示される `InAppMessage` オブジェクトの参照が含まれます。各 `InAppMessage` に、`dark` と `light` のモードテーマを含む `themes` プロパティがあります。`themes.dark` プロパティを `nil` に設定すると、Braze では自動的にライトテーマを使用してアプリ内メッセージが表示されます。

ボタンがあるアプリ内メッセージの種類では、`buttons` プロパティに追加の `themes` オブジェクトがあります。ボタンでダークモードのスタイルが採用されないようにするには、[`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) を使用して `dark` テーマがない `light` テーマのボタンの新しい配列を作成できます。

{% tabs %}
{% tab swift %}

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

## アプリストアレビュープロンプトのカスタマイズ

キャンペーンでアプリ内メッセージ s を使用して、ユーザー s にアプリストアの確認を依頼できます。

{% alert note %}
このプロンプトの例は Braze のデフォルト動作をオーバーライドするため、これが実装されるとインプレッションを自動的に追跡できません。自分の分析をロギングする必要があります。
{% endalert %}

### ステップ 1: アプリ内メッセージデリゲートの設定

まず、アプリで [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_setting-up-the-ui-delegate-required) を設定します。 

### ステップ 2:デフォルトの App Store レビューメッセージを無効にする

次に、`inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)を実装して、デフォルトの App Store レビューメッセージを無効にします。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### ステップ 3: ディープリンクの作成

ディープリンク処理コードで、次のコードを追加して `{YOUR-APP-SCHEME}:app-store-review` ディープリンクを処理します。`SKStoreReviewController` を使用するには `StoreKit` をインポートする必要があることに注意してください。

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### ステップ4: クリック時のカスタム動作の設定

次に、以下を使用してアプリ内メッセージングキャンペーンを作成します。

- キーと値のペア `"AppStore Review" : "true"`
- ディープリンク `{YOUR-APP-SCHEME}:app-store-review` を使用して、クリック時動作を [アプリにディープリンクする] に設定します。

{% endraw %}

{% alert tip %}
Appleは、App Store のレビュープロンプトをユーザーごとに年間最大3回に制限しているため、キャンペーンの[レート]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)はユーザーごとに年間3回に制限する必要があります。<br><br>ユーザーは、App Store のレビュープロンプトをオフにできます。そのため、カスタムレビュープロンプトでは、App Store のネイティブレビュープロンプトが表示されることを約束したり、直接のレビューを求めたりしないでください。
{% endalert %}
