---
nav_title: Android
article_title: ユニティ用 SDK アンドロイドインテグレーション
platform: 
  - Unity
  - Android
page_order: 0
description: "このリファレンス記事では、Unity プラットフォームの Android SDK インテグレーションについて説明しています。"
search_rank: .9
---

# SDK アンドロイド統合

> このリファレンス記事では、Unity プラットフォームの Android SDK インテグレーションについて説明しています。以下の手順に従って、お使いの Unity アプリケーションで Braze を実行してください。

## ステップ 1:Braze ユニティパッケージをお選びください

Brazeには、[`.unitypackage`][41]AndroidおよびiOSプラットフォーム用のネイティブバインディングとC＃インターフェイスがバンドルされています。

Braze Unity [のリリースページでは、いくつかの Braze Unity][42] パッケージをダウンロードできます。
 
- `Appboy.unitypackage`
    - このパッケージには、Braze Android SDK と iOS SDK と iOS SDK のほか、[Braze アプリ内メッセージングの適切な機能と iOS でのコンテンツカード機能の適切な機能に必要な iOS SDK の SDWebImage][unity-1] 依存関係がバンドルされています。SDWebImageフレームワークは、GIFを含む画像のダウンロードと表示に使用されます。Braze の全機能を利用したい場合は、このパッケージをダウンロードしてインポートしてください。
- `Appboy-nodeps.unitypackage`
    - このパッケージは、[SDWebImage `Appboy.unitypackage`][unity-1] フレームワークが存在しない点を除いてと似ています。このパッケージは、SDWebImage フレームワークを iOS アプリに表示したくない場合に便利です。

**iOS**:iOS プロジェクトに [SDWebImage][unity-1] 依存関係が必要かどうかを確認するには、[iOS アプリ内メッセージドキュメント] [unity-4] を参照してください。<br>
**Android**:[Unity 2.6.0 以降、バンドルされている Braze Android SDK アーティファクトには AndroidX の依存関係が必要です。][unity-3]以前にを使用していた場合は`jetified unitypackage`、対応するバージョンに安全に移行できます`unitypackage`。

## ステップ 2: パッケージをインポートする

Unity エディターで、「**アセット」>「パッケージのインポート」>「カスタムパッケージ」に移動して、パッケージを Unity プロジェクトにインポートします**。次に、[**インポート**] をクリックします。

または、[Unity アセットパッケージのインポート手順に従って][41]、カスタム Unity パッケージのインポートに関する詳細なガイドを参照してください。 

{% alert note %}
iOS または Android プラグインのみをインポートする場合は、Braze `Plugins/Android` `Plugins/iOS` をインポートするときにまたはサブディレクトリの選択を解除してください。`.unitypackage`
{% endalert %}

## ステップ 3: AndroidManifest.xml を更新中

Android Unity プロジェクトでは、アプリケーションを実行するにはが必要です。[`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)さらに、Brazeが機能するにはいくつかの追加機能が必要です。[`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)

### AndroidManifest.xml を設定する

アプリにがない場合は`AndroidManifest.xml`、以下をテンプレートとして使用できます。それ以外の場合は、すでにセクションがある場合は`AndroidManifest.xml`、次の欠落しているセクションのいずれかが既存のセクションに追加されていることを確認してください`AndroidManifest.xml`。

\`\`\`xml
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

> `AndroidManifest.xml``Assets/Plugins/Android/AndroidManifest.xml`お前は下に存在するはずだ詳細については、[Unity Androidマニフェストのドキュメントを参照してください](https://docs.unity3d.com/Manual/android-manifest.html)。

> `AndroidManifest.xml`ファイルに登録されているすべてのアクティビティクラスは、Braze Android SDKと完全に統合されている必要があります。独自の Activity クラスを追加する場合は、[Unity Activity の統合手順に従ってアナリティクスが収集されていることを確認する必要があります](#extending-braze-unity-player)。

{% alert note %}
決勝戦には、`AndroidManifest.xml``"android.intent.category.LAUNCHER"`プレゼント付きのアクティビティが1つだけ含まれている必要があります。
{% endalert %}

### AndroidManifest.xml をパッケージ名で更新してください

パッケージ名を確認するには、[**ファイル] > [ビルド設定] > [プレーヤー設定] > [Android] タブをクリックします**。
![\]({% image_buster /assets/img_archive/UnityPackageName.png %})

で`AndroidManifest.xml`、`REPLACE_WITH_YOUR_PACKAGE_NAME``Package Name`のすべてのインスタンスを前のステップで作成したインスタンスに置き換える必要があります。

## ステップ 4: グラドル依存関係の追加 {#unity-android-gradle-configuration}

以下の依存関係が必要です。

\`\`\`groovy
実装「org.jetbrains.kotlin: kotlin-stdlib: 1.5.21"
実装「org.jetbrains.kotlinx: kotlinx-coroutines-android: 1.5.2"

//Android でデフォルトのコンテンツカードアクティビティを使用する場合は両方が必要です
実装「layout:androidx.スワイプリフレッシュスワイプリフレッシュ+」layout:
実装「アンドロイドxリサイクルビュー：リサイクルビュー：+」
\`\`\`

Unity を使用してこれらの依存関係を追加する方法の例を以下に示します。 tools:

##### [カスタム Gradle テンプレート](https://docs.unity3d.com/Manual/android-gradle-overview.html)

```groovy
dependencies {
  implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"
  implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2"
}
```
##### [Unity の外部依存関係マネージャー](https://github.com/googlesamples/unity-jar-resolver)

```xml
<dependencies>
  <androidPackages>
    <androidPackage spec="org.jetbrains.kotlin:kotlin-stdlib:1.5.21" />
    <androidPackage spec="org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2" />
  </androidPackages>
</dependencies>
```

## ステップ 5: SDK を設定する {#unity-static-configuration}

Braze は Unity Android との統合を自動化するためのネイティブ Unity ソリューションを提供しています。 

1. Unity エディターで、Braze **> Braze 設定に移動して Braze** 設定を開きます。
2. 「**Unity Android インテグレーションの自動化**」ボックスをチェックしてください。
3. **Braze API キーフィールドに**、Braze ダッシュボードの **[設定の管理]** にあるアプリケーションの API キーを入力します。

{% alert note %}
この自動統合は、プロジェクトの構築中に設定値が競合する可能性があるため、`braze.xml`手動で作成したファイルでは使用しないでください。マニュアルが必要な場合は`braze.xml`、自動統合を無効にしてください。
{% endalert %}

## \## 基本的な SDK 統合の完了

これで、Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。統合プッシュについて詳しくは、以下の記事をご覧ください。[Android][53] と [iOS][50]、[アプリ内メッセージ][34]、[コンテンツカード][40]

高度な SDK 統合オプションについては、「[高度な実装][54]」をご覧ください。

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
[unity-4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/
