{% multi_lang_include developer_guide/prerequisites/cordova.md %} [プッシュ通知の設定も]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova)必要だ。

## リッチプッシュ通知の設定

### ステップ 1: 通知サービス拡張機能を作成する

Xcode プロジェクトで、通知サービス拡張機能を作成します。完全なウォークスルーについては、「[iOS リッチプッシュ通知チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)」を参照してください。

### ステップ 2:新しいターゲットを追加する

Podfile を開き、[先ほど作成した](#cordova_step-1-create-a-notification-service-extension)通知サービス拡張機能のターゲットに `BrazeNotificationService` を追加します。`BrazeNotificationService` がすでにターゲットに追加されている場合は、続行する前に削除してください。シンボルの重複エラーを防ぐため、静的リンクを使用します。

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

`NOTIFICATION_SERVICE_EXTENSION` を通知サービス拡張機能の名前で置き換えます。Podfile は次のようになります。

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

### ステップ 3:CocoaPods の依存関係を再インストールする

ターミナルで、プロジェクトの iOS ディレクトリに移動し、CocoaPod の依存関係を再インストールします。

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
