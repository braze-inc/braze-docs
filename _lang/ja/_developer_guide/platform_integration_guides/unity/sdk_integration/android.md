---
nav_title: Android
article_title: Unity向けSDK Androidインテグレーション
platform: 
  - Unity
  - Android
page_order: 0
description: "このリファレンス記事では、Unity プラットフォームのAndroid SDKインテグレーションについて説明します。"
search_rank: .9
---

# SDK Androidインテグレーション

> このリファレンス記事では、Unity プラットフォームのAndroid SDKインテグレーションについて説明します。Braze を Unity アプリケーションで実行するには、以下の指示に従ってください。

## ステップ1:Braze Unity パッケージの選択

Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) は、Android プラットフォームと iOS プラットフォーム向けのネイティブバインディングを C# インターフェイスとともにバンドルします。

[Braze Unity リリースページ](https://github.com/Appboy/appboy-unity-sdk/releases)でいくつかの Braze Unity パッケージをダウンロードできます。
 
- `Appboy.unitypackage`
    - このパッケージは、Braze Android および iOS SDK と、iOS SDK の [SDWebImage](https://github.com/SDWebImage/SDWebImage) 依存関係をバンドルします。これは、Braze アプリ内メッセージングと、iOS 上のコンテンツカード機能を適切に機能させるために必要です。SDWebImage フレームワークは、GIF を含む画像のダウンロードと表示に使用されます。完全なBraze機能を使用する場合は、このパッケージを読み込むしてインポートします。
- `Appboy-nodeps.unitypackage`
    - このパッケージは `Appboy.unitypackage` に似ていますが、[SDWebImage](https://github.com/SDWebImage/SDWebImage) フレームワークが存在しない点が異なります。このパッケージは、iOS アプリに SDWebImage フレームワークが存在しないようにする場合に便利です。

**iOS**:iOS プロジェクトに [SDWebImage](https://github.com/SDWebImage/SDWebImage) の依存関係が必要かどうかを確認するには、[iOS アプリ内メッセージドキュメント]を参照してください。({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/).] <br>
**Android**:Unity 2.6.0 以降、バンドルされた Braze Android SDK アーティファクトには [AndroidX](https://developer.android.com/jetpack/androidx) 依存関係が必要です。以前に`jetified unitypackage` を使用していた場合は、対応する`unitypackage` に安全に移行できます。

## ステップ2:パッケージをインポートする

Unity エディターで Unity プロジェクトにパッケージをインポートするには、**[アセット] > [パッケージをインポート] > [カスタムパッケージ]** の順に移動します。次に、**Import**をクリックします。

または、カスタム Unity パッケージのインポートに関して詳しくは、[Unity アセットパッケージのインポート](https://docs.unity3d.com/Manual/AssetPackages.html)の説明を参照してください。 

{% alert note %}
iOS またはAndroid プラグインのみをインポートする場合は、Braze`.unitypackage` をインポートするときに`Plugins/Android` または`Plugins/iOS` サブディレクトリの選択を解除します。
{% endalert %}

## ステップ3:AndroidManifest.xml を更新する

Android Unity プロジェクトでは、アプリケーションを実行するために [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) が必要です。さらに、Braze が機能するには、[`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) にいくつかの追加が必要です。

### AndroidManifest.xml の設定

アプリに`AndroidManifest.xml` がない場合は、以下をテンプレートとして使用できます。それ以外の場合、すでに`AndroidManifest.xml` がある場合は、次のいずれかの欠落セクションが既存の`AndroidManifest.xml` に追加されていることを確認します。

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

> `AndroidManifest.xml` は`Assets/Plugins/Android/AndroidManifest.xml` の下に存在する必要があります。詳細については、[Unity OMAnifest ドキュメント](https://docs.unity3d.com/Manual/android-manifest.html)を参照してください。

> `AndroidManifest.xml` に登録されているすべてのアクティビティクラスは、Braze Android SDK と完全に統合されている必要があります。独自のアクティビティクラスを追加する場合は、[Unity アクティビティ統合手順](#extending-braze-unity-player)に従って、分析が収集されるようにする必要があります。

{% alert note %}
最終的な`AndroidManifest.xml` には、`"android.intent.category.LAUNCHER"` が存在する単一のアクティビティのみを含める必要があります。
{% endalert %}

### AndroidManifest.xmlをパッケージ名で更新します

パッケージ名を確認するには、**[ファイル] > [ビルド設定] > [プレーヤー設定] > [Android タブ]**を選択します。
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

`AndroidManifest.xml` では、`REPLACE_WITH_YOUR_PACKAGE_NAME` のすべてのインスタンスを前のステップの `Package Name` に置き換える必要があります。

## ステップ4: グレードル依存関係の追加 {#unity-android-gradle-configuration}

Unity プロジェクトに gradle の依存関係を追加するには、まず公開設定で [[Custom Main Gradle テンプレート]](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) を有効にします。これにより、プロジェクトで使用するテンプレートグラドルファイルが作成されます。gradle ファイルは、依存関係の設定やその他のビルド時のプロジェクト設定を処理します。詳細については、Braze Unity サンプルアプリの[mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle) を参照してください。

次の依存関係が必要です。

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

これらの依存関係は、[External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver)を使用して設定することもできます。

## ステップ5:SDK の設定 {#unity-static-configuration}

Braze は、Unity Android 統合を自動化するためのネイティブ Unity ソリューションを提供しています。 

1. Unity エディターで **[Braze] > [Braze 構成]** の順に移動して、[Braze 構成設定] を開きます。
2. [**Unity Android 統合の自動化**] ボックスにチェックマークを入れます。
3. **Braze API キー**フィールドで、**設定の管理**にあるアプリアプリケーションのAPI キーをBraze ダッシュボードから入力します。

{% alert note %}
手動で作成した `braze.xml` ファイルでは、プロジェクトのビルド中に設定値が競合する可能性があるため、この自動統合は使用しないでください。手動の`braze.xml` が必要な場合は、自動統合を無効にします。
{% endalert %}

## 基本的な SDK 統合の完了

Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。プッシュ統合の詳細については、次の記事を参照してください。[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/)と[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/)、[アプリ内メッセージs]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/)、[コンテンツカード]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/)。

高度なSDKインテグレーションオプションについては、[高度なインプリメンテーション]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#android-sdk-advanced)を参照してください。

