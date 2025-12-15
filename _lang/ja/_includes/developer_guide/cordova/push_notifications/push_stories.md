{% multi_lang_include developer_guide/prerequisites/cordova.md %} [プッシュ通知の設定も]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova)必要だ。

## プッシュストーリーの設定

### ステップ 1: 通知コンテンツ拡張機能を作成する

Xcode プロジェクトで、通知コンテンツ拡張機能を作成します。完全なウォークスルーについては、「[iOS プッシュ通知ストーリーのチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/)」を参照してください。

### ステップ 2:プッシュ通知アプ​​リグループを構成する

プロジェクトの `config.xml` ファイルで、[先ほど作成した](#cordova_step-1-create-a-notification-content-extension)プッシュ通知アプリグループを構成します。

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

`PUSH_APP_GROUP` をプッシュ通知アプ​​リグループの名前で置き換えます。`config.xml` は次のようになります。

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### ステップ 3:新しいターゲットを追加する

Podfile を開き、[先に作成した](#cordova_step-1-create-a-notification-content-extension)通知コンテンツ拡張機能のターゲットに `BrazePushStory` を追加します。シンボルの重複エラーを防ぐため、静的リンクを使用します。

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

`NOTIFICATION_CONTENT_EXTENSION` を通知コンテンツ拡張機能の名前で置き換えます。Podfile は次のようになります。

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

### ステップ 4:CocoaPods の依存関係を再インストールする

ターミナルで、iOS ディレクトリに移動し、CocoaPod の依存関係を再インストールします。

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
