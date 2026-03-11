{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## アプリ内メッセージを有効にする

{% alert note %}
このステップはiOS専用だ。Androidでは、アプリ内メッセージのデフォルト実装は既に設定済みだ。
{% endalert %}

iOSアプリ内メッセージのデフォルトプレゼンターを設定するには、プロトコ`BrazeInAppMessagePresenter`ルの実装を作成し、それをBrazeインスタンスの`inAppMessagePresenter`オプションに割り当てる。`BrazeInAppMessageUI` オブジェクトをインスタンス化することで、デフォルトの Braze UI プレゼンターを使用することもできます。

その`BrazeInAppMessageUI`クラスにアクセスするには、その`BrazeUI`ライブラリーをインポートしなければならない。

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

実装をさらにカスタマイズするには、[アプリ内メッセージデータのログ記録]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter)を参照せよ。
