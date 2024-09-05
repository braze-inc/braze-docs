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

> このリファレンス記事では、Unity プラットフォームのAndroid SDKインテグレーションについて説明します。以下の手順に従って、Unity アプリ ライケーションでBraze を実行します。

## ステップ1:Braze Unityの選択

Braze[`.unitypackage`][41] は、Android およびiOS プラットフォームs のネイティブバインディングをC# インターフェイスとともにバンドルします。

[ Braze Unityリリースページ][42] では、いくつかのBraze Unity パッケージを下位読み込むに使用できます。
 
- `Appboy.unitypackage`
    - このパッケージは、Braze Android およびiOS SDK s と[SDWebImage][unity-1] 依存関係をiOS のBraze in-アプリ メッセージング、およびコンテンツカード機能の適切な機能に必要なiOS SDKにバンドルします。SDWeb"画像フレームワークは、GIFを含む"画像のダウン読み込むと表示に使用されます。完全なBraze機能を使用する場合は、このパッケージを読み込むしてインポートします。
- `Appboy-nodeps.unitypackage`
    - このパッケージは、[SDOAImage][unity-1] フレームワークが存在しないことを除いて、`Appboy.unitypackage` と似ています。このパッケージは、SDOAImage フレームワークをiOS アプリに表示しない場合に便利です。

**iOS**:iOS プロジェクトに[SDWebImage][unity-1] の依存関係が必要かどうかを確認するには、\[iOS アプリ内メッセージ ドキュメント]\[unity-4]] を参照してください。<br>
**Android**:Unity 2.6.0 以降、バンドルされたBraze Android SDK アーティファクトには[AndroidX][unity-3] 依存関係が必要です。以前に`jetified unitypackage` を使用していた場合は、対応する`unitypackage` に安全に移行できます。

## ステップ2:パッケージをインポートする

Unityエディタで、**Assets > Import Package > Custom Package** に移動して、パッケージをUnity プロジェクトにインポートします。次に、**Import**をクリックします。

または、[ Unity アセットパッケージインポート][41] の手順に従って、カスタムUnityパッケージのインポートに関する詳細を確認してください。 

{% alert note %}
iOS またはAndroid プラグインのみをインポートする場合は、Braze`.unitypackage` をインポートするときに`Plugins/Android` または`Plugins/iOS` サブディレクトリの選択を解除します。
{% endalert %}

## ステップ3:アップデート AndroidManifest.xml

Android Unityのプロジェクトでは、アプリライケーションを実行するために、[`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)が存在する必要があります。さらに、Braze は[`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) にいくつか追加する必要があります。

### 設定 AndroidManifest.xml

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

> `AndroidManifest.xml` に登録されているすべてのアクティビティクラスは、Braze Android SDKと完全に統合されている必要があります。独自のアクティビティクラスを追加する場合は、[ Unity アクティビティ統合手順](#extending-braze-unity-player) に従って、分析が収集されるようにする必要があります。

{% alert note %}
最終的な`AndroidManifest.xml` には、`"android.intent.category.LAUNCHER"` が存在する単一のアクティビティのみを含める必要があります。
{% endalert %}

### AndroidManifest.xmlをパッケージ名で更新します

パッケージ名を確認するには、**File >Build Settings >Player Settings >Android Tab**を選択します。
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

`AndroidManifest.xml` では、`REPLACE_WITH_YOUR_PACKAGE_NAME` のすべてのインスタンスを前のステップの`Package Name` に置き換える必要があります。

## ステップ4: グレードル依存関係の追加 {#unity-android-gradle-configuration}

グラッドル依存関係をUnityプロジェクトに追加するには、まず、公開設定で\["カスタムメイングラッドテンプレート&クォート;]\[Unity-5]]を有効にします。これにより、プロジェクトで使用するテンプレートグラドルファイルが作成されます。グラッドルファイルは、設定依存関係や他のビルドタイムプロジェクト設定を処理します。詳細については、Braze Unityのサンプリングアプリの\[mainTemplate.gradle]\[Unity-6]] を参照してください。

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

## ステップ5:SDKの設定 {#unity-static-configuration}

Braze は、Unity Androidインテグレーションを自動化するためのネイティブUnity ソリューションを提供します。 

1. Unityエディタで、** Braze > Braze Configuration** に移動して、Braze 設定を開封します。
2. **Unity Androidインテグレーションの自動化**を確認してください。
3. **Braze API キー**フィールドで、**設定の管理**にあるアプリアプリケーションのAPI キーをBraze ダッシュボードから入力します。

{% alert note %}
この自動統合は、手動で作成された`braze.xml` ファイルでは使用しないでください。プロジェクトのビルド中に設定値が競合する可能性があるためです。手動の`braze.xml` が必要な場合は、自動統合を無効にします。
{% endalert %}

## 基本SDK一体化完了

Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。統合プッシュの詳細については、次の記事を参照してください。[Android][53]と[iOS][50]、[アプリ内メッセージs][34]、[コンテンツカード][40]。

高度なSDKインテグレーションオプションについては、[高度なインプリメンテーション][54]を参照してください。

[5]: #transitioning-from-manual-to-automated-integration
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[54]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#android-sdk-advanced
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
\[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/
\[unity-5]: https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing
\[unity-6]: https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle
