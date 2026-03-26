{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## アプリ内メッセージを有効にする

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Braze Flutter SDK は、Android と iOS の両方でデフォルトのアプリ内メッセージプレゼンターを自動的に設定します。アプリ内メッセージは、追加の設定なしで表示され、Dart レイヤーに転送されます。

### iOS でのアプリ内メッセージプレゼンターのカスタマイズ

iOS でデフォルトのアプリ内メッセージプレゼンターをオーバーライドするには、`BrazePlugin.configure(_:postInitialization:)` の `postInitialization` クロージャを使用します。カスタムプレゼンターは、アプリ内メッセージデータを Dart レイヤーに転送するために `BrazePlugin.processInAppMessage(message)` を呼び出す必要があります。

```swift
import BrazeUI

BrazePlugin.configure(
  { configuration in
    // Set non-API-key configurations here.
  },
  postInitialization: { braze in
    let customPresenter = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = customPresenter
  }
)
```

カスタムプレゼンタークラスでは、`BrazePlugin.processInAppMessage(message)` と `super.present(message: message)` を呼び出して、データを Dart に転送し、デフォルトの UI を表示します。

```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    BrazePlugin.processInAppMessage(message)
    super.present(message: message)
  }
}
```

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

{% alert note %}
このステップは iOS 専用です。Android では、アプリ内メッセージのデフォルト実装は既に設定済みです。
{% endalert %}

iOS でアプリ内メッセージのデフォルトプレゼンターを設定するには、`BrazeInAppMessagePresenter` プロトコルの実装を作成し、それを Braze インスタンスのオプションの `inAppMessagePresenter` に割り当てます。`BrazeInAppMessageUI` オブジェクトをインスタンス化することで、デフォルトの Braze UI プレゼンターを使用することもできます。

`BrazeInAppMessageUI` クラスにアクセスするには、`BrazeUI` ライブラリーをインポートする必要があります。

{% subtabs %}
{% subtab swift %}

```swift
import BrazeUI

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  ...

  let braze = BrazePlugin.initBraze(configuration)

  braze.inAppMessagePresenter = BrazeInAppMessageUI()
  AppDelegate.braze = braze

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  ...

  Braze *braze = [BrazePlugin initBraze:configuration];

  braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

アプリ内メッセージデータへのアクセスの詳細については、[アプリ内メッセージデータのログ記録]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter)を参照してください。