{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## アプリ内メッセージを有効にする

{% alert note %}
このステップはiOS専用である。アプリ内メッセージのデフォルト実装は、Androidではすでに設定されている。
{% endalert %}

iOSのアプリ内メッセージのデフォルトプレゼンターを設定するには、`BrazeInAppMessagePresenter` プロトコルの実装を作成し、Brazeインスタンスのオプション`inAppMessagePresenter` に割り当てる。`BrazeInAppMessageUI` オブジェクトをインスタンス化することで、デフォルトの Braze UI プレゼンターを使用することもできます。

`BrazeInAppMessageUI` クラスにアクセスするには、`BrazeUI` ライブラリーをインポートする必要がある。

{% tabs %}
{% tab swift %}

```swift
import BrazeUI

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  ...

  let braze = BrazePlugin.initBraze(configuration)

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = BrazeInAppMessageUI()
  AppDelegate.braze = braze

  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  ...

  Braze *braze = [BrazePlugin initBraze:configuration];

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}
```
{% endtab %}
{% endtabs %}

実装をさらにカスタマイズするには、[アプリ内メッセージデータのログを]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter)参照すること。
