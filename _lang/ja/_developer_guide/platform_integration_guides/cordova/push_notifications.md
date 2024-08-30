---
nav_title: プッシュ通知
article_title: Cordova Braze SDK のプッシュ通知
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "この記事では、Cordova でのプッシュ通知の実装について説明します。"
channel: push
---

# プッシュ通知の統合

> Cordova Braze SDKのプッシュ通知を統合する方法を学びます。

{% multi_lang_include cordova/prerequisites.md %}

## 基本的なプッシュ機能

デフォルトで、基本的なプッシュ通知機能はBraze Cordovaプラグインで有効になっています。これらの機能は、[XML構成をカスタマイズする]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/#customization-options)ことで無効にできます。より詳細なネイティブプッシュ通知機能については、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)および[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)プッシュ通知ガイドを参照してください。

## 拡張プッシュ機能

{% alert important %}
Cordova プラグインを追加、削除、または更新すると、Cordova は Xcode プロジェクトの Podfile を上書きします。つまり、Cordova プラグインを変更するたびに、このプロセスを繰り返す必要があります。
{% endalert %}

### リッチプッシュ通知

#### ステップ 1:通知サービス拡張機能を作成する

Xcode プロジェクトで、通知サービス拡張機能を作成します。完全なウォークスルーについては、「[iOS リッチプッシュ通知チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)」を参照してください。

#### ステップ 2:新しいターゲットを追加する

Podfile を開き、[先ほど作成した](#step-1-create-a-notification-service-extension)通知サービス拡張機能のターゲットに `BrazeNotificationService` を追加します。`BrazeNotificationService` がすでにターゲットに追加されている場合は、続行する前に削除してください。シンボルの重複エラーを防ぐため、静的リンクを使用します。

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

#### ステップ 3:CocoaPods の依存関係を再インストールする

ターミナルで、プロジェクトの iOS ディレクトリに移動し、CocoaPod の依存関係を再インストールします。

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

### プッシュ通知ストーリー

#### ステップ 1:通知コンテンツ拡張機能を作成する

Xcode プロジェクトで、通知コンテンツ拡張機能を作成します。完全なウォークスルーについては、「[iOS プッシュ通知ストーリーのチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/)」を参照してください。

#### ステップ 2:プッシュ通知アプ​​リグループを構成する

プロジェクトの `config.xml` ファイルで、[先ほど作成した](#step-1-create-a-notification-content-extension)プッシュ通知アプリグループを構成します。

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

`PUSH_APP_GROUP` をプッシュ通知アプ​​リグループの名前で置き換えます。`config.xml` は次のようになります。

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

#### ステップ 3:新しいターゲットを追加する

Podfile を開き、[先に作成した](#step-1-create-a-notification-content-extension)通知コンテンツ拡張機能のターゲットに `BrazePushStory` を追加します。シンボルの重複エラーを防ぐため、静的リンクを使用します。

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

#### ステップ 4:CocoaPods の依存関係を再インストールする

ターミナルで、iOS ディレクトリに移動し、CocoaPod の依存関係を再インストールします。

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
