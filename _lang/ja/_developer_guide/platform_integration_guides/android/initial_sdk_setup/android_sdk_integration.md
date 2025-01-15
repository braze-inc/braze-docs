---
nav_title: Android SDK 統合
article_title: Android と FireOS の Android SDK 統合
page_order: 0
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、Android SDK を Android または FireOS アプリケーションに統合する方法について説明します。"
search_rank: 4
---

# Android SDK 統合

> このリファレンス記事では、Android SDK を Android または FireOS アプリケーションに統合する方法について説明します。Braze SDK をインストールすると、基本的な分析機能と、ユーザーエンゲージメントのためのアプリ内メッセージが提供されます。

{% alert note %}
Android 12 で最適なパフォーマンスを得るには、できるだけ早く [Braze Android SDK v13.1.2 以降](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312)にアップグレードすることをお勧めします。詳細については、[Android 12 アップグレード ガイド]({{site.baseurl}}/android_12/)を参照してください。
{% endalert %}

## ステップ1:Braze ライブラリーを統合する

Braze Android SDK は、オプションで UI コンポーネントなしで統合できます。ただし、独自のデザインのみの UI にカスタムデータを渡さない限り、コンテンツカードとアプリ内メッセージングは​​操作できなくなります。さらに、プッシュ処理コードが UI ライブラリーにあるため、プッシュ通知は機能しません。これらの UI 要素は完全にカスタマイズ可能であることに注意してください。これらの機能を統合することを強くお勧めします。各チャネルまたはツールを使用する利点のリストについては、[コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/#advantages-of-using-content-cards)と[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)に関するドキュメントを参照してください。

### 基本的な統合

Braze メッセージング機能にアクセスするには、UI ライブラリーを統合する必要があります。IDE に応じて UI ライブラリーを統合するには、次の Android Studio の手順を参照してください。

#### Braze 依存関係を追加する

`android-sdk-ui` の依存関係をアプリの `build.gradle` に追加します。 

位置情報や Braze ジオフェンス機能を使用している場合は、`android-sdk-location` もアプリの `build.gradle` に含めてください。

{% alert important %}
非ネイティブ Android SDK (Flutter、Cordova、Unity など) を使用している場合、その SDK には正しいバージョンの Android SDK の `android-sdk-ui` 依存関係がすでに含まれています。そのバージョンを手動で更新しないでください。
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

次の例は、依存関係行を配置する `build.gradle` 内の場所を示しています。なお、例で使用しているバージョンは古いバージョンです。Braze Android SDK の最新バージョンについては、[[Braze Android SDK リリース](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)] にアクセスしてください。

!["build.gradle" を表示するAndroid studio。ファイルの末尾に依存コードが追加されます。]({% image_buster /assets/img_archive/androidstudio2.png %})

#### Gradle 同期を実行する

Gradle 同期を実行してプロジェクトをビルドし、[依存関係の追加](#add-braze-dependency)を組み込んでください。

![Android Studio のバナーで、次のように記述されています。「前回のプロジェクトの同期以降、Gradle ファイルが変更されました。IDE が適切に動作するためにプロジェクトの同期が必要となる場合があります。今すぐ同期。"]({% image_buster /assets/img_archive/androidstudio3.png %})

## ステップ 2:braze.xmlでBraze SDKを構成する

{% alert note %}
2019 年 12 月をもって、カスタムエンドポイントは提供されなくなりました。既存のカスタムエンドポイントがある場合は、それを引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a>を参照してください。
{% endalert %}

ライブラリーが統合されたので、次に `braze.xml` ファイルをプロジェクトの `res/values` フォルダーに作成する必要があります。特定のデータクラスターを使用している場合、または既存のカスタムエンドポイントがある場合は、`braze.xml` ファイルでもエンドポイントを指定する必要があります。 

ファイルの内容は、次のコードスニペットのようになります。Braze ダッシュボードの [**設定の管理**] ページにある識別子で `YOUR_APP_IDENTIFIER_API_KEY` を置き換えてください。[dashboard.braze.com](https://dashboard.braze.com)にログインして、[クラスターアドレス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)を見つけてください。 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## ステップ3:AndroidManifest.xml に必要な権限を追加する
API キーを追加したので、次の権限を `AndroidManifest.xml` に追加する必要があります。

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android M のリリースにより、Android はインストール時権限モデルから実行時権限モデルに切り替わりました。ただし、これらの権限はどちらも通常の権限であり、アプリのマニフェストにリストされている場合は自動的に付与されます。詳細については、Android の[権限に関するドキュメント](https://developer.android.com/training/permissions/index.html)を参照してください。
{% endalert %}

## ステップ 4:Android でユーザーセッションを追跡する

### アクティビティライフサイクルコールバックの統合

`openSession()`、`closeSession()`、[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)、および `InAppMessageManager` 登録の呼び出しは、オプションで自動的に処理されます。

#### アクティビティライフサイクルコールバックを登録する

`onCreate()` クラスの `Application` メソッドに次のコードを追加します。

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

{% endtab %}
{% endtabs %}

[[`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)] で使用できるパラメーターの詳細については、SDK リファレンスドキュメントを参照してください。

## ステップ5: 位置情報の追跡を有効にする

Braze の位置情報収集機能を有効にする場合は、`com_braze_enable_location_collection` を含むように `braze.xml` ファイルを更新し、その値が `true` に設定されていることを確認します。

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK バージョン3.6.0 以降、Braze の位置情報収集機能はデフォルトで無効になっています。
{% endalert %}

## SDK 統合の完了

Braze は[アプリケーションから指定されたデータ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/)を収集できるようになり、基本的な統合が完了しました。

[カスタムイベントトラッキング]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)、[プッシュメッセージング]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)、[コンテンツカード]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/)、および Braze 機能の完全なスイートを有効にするには、次の記事にアクセスしてください。

